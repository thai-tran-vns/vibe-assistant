# Task 2: Dependency Management

## Description
Update project dependencies to include libraries for asynchronous console I/O and logging.

## Steps
1.  Open `requirements.txt`.
2.  Add `aioconsole` (for async user input).
3.  Add `loguru` (for simplified logging).
4.  Ensure versions are pinned or compatible.

## Input
- Current `requirements.txt`.

## Output
- Updated `requirements.txt` with:
    - `aioconsole`
    - `loguru`

## Test
- Run `pip install -r requirements.txt` to ensure packages install without conflict.
- Run `pip list` to verify `aioconsole` and `loguru` are present.
