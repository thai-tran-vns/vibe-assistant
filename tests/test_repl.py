import pytest
from core.repl import PythonREPL

def test_repl_variable_persistence():
    repl = PythonREPL()
    repl.execute("x = 10")
    result = repl.execute("print(x)")
    assert result.strip() == "10"

def test_repl_error_handling():
    repl = PythonREPL()
    result = repl.execute("print(non_existent_var)")
    assert "NameError" in result
    assert "non_existent_var" in result

def test_repl_safety_exit():
    repl = PythonREPL()
    # verify exit does not kill the process and prints the message
    result = repl.execute("exit()")
    assert "exit() and quit() are disabled" in result

def test_repl_safety_quit():
    repl = PythonREPL()
    result = repl.execute("quit()")
    assert "exit() and quit() are disabled" in result

def test_repl_multiple_lines():
    repl = PythonREPL()
    code = """
a = 5
b = 6
print(a + b)
"""
    result = repl.execute(code)
    assert result.strip() == "11"

def test_repl_function_scope():
    repl = PythonREPL()
    code = """
x = 10
def get_x():
    return x
print(get_x())
"""
    result = repl.execute(code)
    assert "10" in result
