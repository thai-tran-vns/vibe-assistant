# Task 4: Python REPL Engine (`core/repl.py`)

## Description
Create a persistent Python Read-Eval-Print Loop (REPL) engine that can execute code, maintain state (variables), and capture output.

## Steps
1.  Create `core/repl.py`.
2.  Define class `PythonREPL`.
3.  **Constructor**:
    - Initialize a dictionary `self.locals` to hold the context (variables).
4.  **Execute Method**:
    - Define `def execute(self, code: str) -> str`:
        - Use `io.StringIO` to capture `sys.stdout` and `sys.stderr`.
        - Use `contextlib.redirect_stdout` and `redirect_stderr`.
        - Use `exec(code, {}, self.locals)` to execute the code.
        - Return the captured string output.
        - Handle exceptions (try/except) and return the traceback/error message as a string.
5.  **Safety**:
    - Shadow `exit` and `quit` in `self.locals` to prevent the user from accidentally killing the main process.

## Input
- `code` (str): Python code to execute.

## Output
- `result` (str): The captured stdout/stderr or error message.

## Test
- Create a test script (or use the REPL from `main.py` if integrated):
    - Instatiate `PythonREPL`.
    - `repl.execute("x = 10")`
    - `repl.execute("print(x)")` -> Should return "10\n".
    - `repl.execute("print(y)")` -> Should return error (NameError).
    - `repl.execute("exit()")` -> Should NOT exit the process.

