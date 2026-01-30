import pytest
import asyncio
import os
from unittest.mock import patch
from main import main
from loguru import logger

@pytest.mark.asyncio
async def test_concurrency_and_logging(capsys):
    # 1. Setup: Clear log file if it exists
    log_file = "logs/app.log"
    if os.path.exists(log_file):
        os.remove(log_file)
    
    # Ensure logs directory exists (main does this, but for safety in test)
    os.makedirs("logs", exist_ok=True)

    # 2. Mock aioconsole.ainput
    # We want it to sleep longer than the supervisor heartbeat interval (1s)
    async def mocked_input(prompt):
        await asyncio.sleep(1.2)
        return "exit"

    with patch("aioconsole.ainput", side_effect=mocked_input):
        # We need to ensure loguru is re-configured as in main, 
        # or we rely on main calling it. 
        # main() calls logger.remove() and logger.add(...).
        # However, loguru is global. 
        
        await main()

    # 3. Verify Logging
    assert os.path.exists(log_file), "Log file should be created"
    
    with open(log_file, "r") as f:
        log_content = f.read()
    
    # Check for supervisor activity
    assert "Supervisor heartbeat..." in log_content, "Supervisor should run in background"
    
    # Check for user loop activity
    assert "User requested exit" in log_content
    
    # Check for clean exit
    assert "Shutdown complete" in log_content

    # 4. Verify Console Output (should NOT contain logs)
    captured = capsys.readouterr()
    stdout = captured.out
    stderr = captured.err
    
    # main.py prints "Exiting..." and echoes input, but logs go to file.
    # loguru default is stderr. We removed it in main.
    
    assert "Supervisor heartbeat" not in stdout
    assert "Supervisor heartbeat" not in stderr
    assert "Exiting..." in stdout
