# Task 5: Testing & Verification

## Description
Verify the integrated system ensures concurrency, state persistence, and proper logging.

## Steps
1.  **Test Concurrency**:
    - Create a test (manual or automated) that runs the `main.py` loop.
    - Ensure the log file continues to grow (supervisor heartbeats) while the prompt is waiting for user input.

2.  **Test REPL State**:
    - Create a unit test `tests/test_repl.py`.
    - Test variable persistence:
        ```python
        repl = PythonREPL()
        repl.execute("a = 5")
        output = repl.execute("print(a)")
        assert output.strip() == "5"
        ```

3.  **Test Logging**:
    - Verify `logs/app.log` is created.
    - Verify console output does *not* contain log messages (only print output).

## Input
- `pytest` execution.
- Manual running of `main.py`.

## Output
- Test pass/fail reports.
- Verified behavior of the running application.

## Test
- Run `pytest`.
- Run `python main.py` and perform manual verification steps.
