# Task 3: Async Entry Point (`main.py`)

## Description
Implement the main application entry point using `asyncio`. This setup will manage two concurrent loops: one for user input and one for background supervision (supervisor). It also sets up logging to a file.

## Steps
1.  **Logging Setup**:
    - Import `loguru`.
    - Configure logger to remove the default handler.
    - Add a new sink to write logs to `logs/app.log`.
    - Ensure logs do *not* output to stdout/stderr (to keep the console clean for the REPL).

2.  **Async Loops**:
    - Define `async def user_loop()`:
        - Use `aioconsole.ainput` to read user commands asynchronously.
        - Print a prompt (e.g., `>>> `).
        - For now, just echo the input back or log it.
        - Handle `exit` or `quit` command to break the loop.
    - Define `async def supervisor_loop()`:
        - Create a loop that sleeps for a short interval (e.g., 1 second).
        - Log a "heartbeat" message to `logs/app.log` every few seconds to prove it's running concurrently.

3.  **Main Execution**:
    - Use `asyncio.gather` or `asyncio.create_task` to run `user_loop` and `supervisor_loop` concurrently.
    - Handle `KeyboardInterrupt` (SIGINT) gracefully to cancel tasks and exit.

## Input
- User keystrokes via `stdin`.

## Output
- `stdout`: User prompt `>>> ` and echo (if applicable).
- `logs/app.log`: Application logs and heartbeat messages.

## Test
- Run `python main.py`.
- Verify prompt `>>> ` appears.
- Type commands; verify responsiveness.
- Check `logs/app.log` and confirm "heartbeat" messages appear while waiting for user input (proving concurrency).
- Press `Ctrl+C` and verify the app shuts down without stack traces.
