import sys
import io
import contextlib
import traceback
from loguru import logger

class PythonREPL:
    def __init__(self):
        self.locals = {}
        # Shadow exit and quit to prevent accidental process termination
        self.locals["exit"] = self._exit_shadow
        self.locals["quit"] = self._exit_shadow

    def _exit_shadow(self, *args, **kwargs):
        print("exit() and quit() are disabled for safety.")

    def execute(self, code: str) -> str:
        logger.debug(f"Executing code:\n{code}")
        output_capture = io.StringIO()
        
        try:
            with contextlib.redirect_stdout(output_capture), contextlib.redirect_stderr(output_capture):
                # Using self.locals for both globals and locals ensures that functions 
                # defined in the REPL can access variables defined in the REPL.
                exec(code, self.locals, self.locals)
        except Exception:
            # Capture the traceback if an exception occurs
            traceback.print_exc(file=output_capture)
        
        result = output_capture.getvalue()
        # Log the result, but maybe truncate if it's too long? For now, debug log it.
        logger.debug(f"Execution result:\n{result}")
        return result
