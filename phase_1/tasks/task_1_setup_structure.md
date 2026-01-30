# Task 1: Setup Project Structure

## Description
Establish the foundational directory structure for the project to separate core logic, tests, and logs.

## Steps
1.  Check if `core/` directory exists; if not, create it.
2.  Check if `tests/` directory exists; if not, create it.
3.  Check if `logs/` directory exists; if not, create it.
4.  Ensure `__init__.py` exists in `core/` to make it a package.

## Input
- None (File system operations).

## Output
- Directories: `core/`, `tests/`, `logs/`.
- Files: `core/__init__.py`.

## Test
- Run `ls -R` to verify the structure matches:
    ```
    ./
    ├── core/
    │   └── __init__.py
    ├── tests/
    └── logs/
    ```
