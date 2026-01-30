# Phase 1: The Kitchen (Infrastructure & REPL) - Kanban Board

## 📋 To Do

### Infrastructure
- [x] **Setup Project Structure**: Ensure `core/`, `tests/`, `logs/` directories exist.
- [x] **Dependency Management**: Update `requirements.txt` with `aioconsole`, `loguru`.
- [x] **Async Entry Point (`main.py`)**:
    - [x] Implement `user_loop` using `aioconsole.ainput`.
    - [x] Implement `supervisor_loop` (placeholder for now).
    - [x] Setup `loguru` to write to `logs/app.log` (sink).
    - [x] Ensure graceful shutdown (SIGINT handling).

### Core Components
- [x] **Python REPL Engine (`core/repl.py`)**:
    - [x] Create `PythonREPL` class.
    - [x] Implement `execute(code: str) -> Any` method.
    - [x] **Context Management**: Ensure `locals()` dictionary persists between calls.
    - [x] **Output Capture**: Capture `stdout`/`stderr` from executed code.
    - [x] **Basic Safety**: Block usage of `exit()`, `quit()` inside the REPL to prevent killing the host.

### Testing & Verification
- [x] **Test Concurrency**: Verify `user_loop` is not blocked by `supervisor_loop`.
- [x] **Test REPL State**: Unit test to verify variable persistence.
- [x] **Test Logging**: Verify logs appear in file and not on console.

## 🏗️ In Progress
*Phase 1 Complete. Ready for Phase 2.*

## ✅ Done
- [x] **Plan Review**: Reviewed and finalized architectural approach (`plans.md`, `suggestions.md`).
