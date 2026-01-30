# Phase 1: The Robust Async Skeleton

**Objective:** Establish a stable concurrent runtime that handles user input and background tasks simultaneously, with safe shutdown and logging controls.

## 1. Project Infrastructure

### Tasks
- Initialize version control.
- Set up Python virtual environment.
- Install core dependencies.
- Configure testing framework.

### Step-by-Step Implementation
1.  **Initialize Git:**
    Already done
2.  **Virtual Environment:**
    - Create environment: Already Done
    - Activate environment: `source .venv/bin/activate`
3.  **Dependencies:**
    - Create `requirements.txt`:
        ```text
        aioconsole
        loguru
        pytest
        pytest-asyncio
        ```
    - For each dependency, run `uv add <name>`
4.  **Test Setup:**
    - Create `tests/` directory.
    - Create `tests/conftest.py` (empty for now).
    - Create `pytest.ini` for configuration if needed.

### Testing Strategy
- **Verification:** Run `pytest`. It should return "no tests collected" but exit successfully (exit code 5) or with no errors, confirming the harness works. Verify `import loguru` works in a python shell.

### Inputs & Outputs
- **Input:** `requirements.txt`
- **Output:** Installed packages in `.venv`.

### Dependencies
- `aioconsole`: For non-blocking standard input.
- `loguru`: For thread-safe, flexible logging.
- `pytest`, `pytest-asyncio`: For future testing.

---

## 2. Async Core Loop

### Tasks
- Create entry point `main.py`.
- Implement concurrent `user_loop` and `agent_loop`.
- Configure logging strategies (File vs. Console).

### Step-by-Step Implementation
1.  **Logging Configuration:**
    - In `main.py`, configure `loguru`.
    - **Rule:** Write verbose logs to `app.log`.
    - **Rule:** Write only `WARNING` or higher to `stderr` to avoid cluttering the CLI interface where the user types.
2.  **User Loop (`user_loop`):**
    - Define an `async` function.
    - Use `while True` loop.
    - Use `await aioconsole.ainput("You: ")` to capture input non-blockingly.
    - For now, just echo the input back or log it.
3.  **Agent Loop (`agent_loop`):**
    - Define an `async` function.
    - Use `while True` loop.
    - Perform a "heartbeat" log `logger.info("Agent heartbeat...")`.
    - `await asyncio.sleep(5)` to simulate background work.
4.  **Main Entry:**
    - Define `async def main()`.
    - Use `asyncio.gather(user_loop(), agent_loop())` to run them concurrently.
    - Add standard `if __name__ == "__main__": asyncio.run(main())` block.

### Testing Strategy
- **Manual Verification (Concurrency):**
    - Run `python main.py`.
    - Type "hello" and hit enter.
    - **Success Criteria:** The system echoes "hello" *immediately*.
    - **Success Criteria:** `app.log` file populates with "Agent heartbeat..." messages in the background, proving the user input didn't block the agent.

### Inputs & Outputs
- **Input:** User typing in terminal.
- **Output:** `app.log` file updates, console echoes user text.

### Dependencies
- `asyncio` (Standard Lib)
- `aioconsole`
- `loguru`

---

## 3. Graceful Shutdown

### Tasks
- Handle `SIGINT` (Ctrl+C) and `SIGTERM`.
- Ensure async tasks are cancelled and cleaned up properly.

### Step-by-Step Implementation
1.  **Signal Handling:**
    - In `main.py`, imports `signal` and `sys`.
    - Capture `KeyboardInterrupt` in the main execution block or attach a signal handler to the loop (though simple try/except in `run()` is often easiest for simple CLI apps).
2.  **Cleanup Logic:**
    - Wrap the `gather` or main loop in a `try...except asyncio.CancelledError` or `finally` block.
    - Iterate over `asyncio.all_tasks()`, cancel them, and `await` them (handling potential cancellation errors) to ensure clean exit.
    - Log "Shutdown complete".

### Testing Strategy
- **Manual Verification (Shutdown):**
    - Run the app. Let it run for 10 seconds.
    - Press `Ctrl+C`.
    - **Success Criteria:** The application exits *immediately* (no long hang).
    - **Success Criteria:** No "Traceback (most recent call last)" printed to the screen.
    - **Success Criteria:** `app.log` shows a clean "Shutdown initiated" -> "Shutdown complete" sequence.

### Inputs & Outputs
- **Input:** OS Signals (`SIGINT`).
- **Output:** Process exit code 0, clean log tail.

### Dependencies
- `signal` (Standard Lib)
- `sys` (Standard Lib)

---

## Resources for Review
- **Asyncio Event Loop:** [Python Docs](https://docs.python.org/3/library/asyncio-eventloop.html) - Understanding how `gather` and `run` work.
- **Loguru Sinks:** [Loguru Docs](https://loguru.readthedocs.io/en/stable/api/logger.html#sink) - Configuring separate sinks for file vs. stderr.
