# Phase 1: The Kitchen (Infrastructure & REPL) - Kanban Board

## 📋 To Do

### Infrastructure
- [ ] **Setup Project Structure**: Ensure `core/`, `tests/`, `logs/` directories exist.
- [ ] **Dependency Management**: Update `requirements.txt` with `aioconsole`, `loguru`.
- [ ] **Async Entry Point (`main.py`)**:
    - [ ] Implement `user_loop` using `aioconsole.ainput`.
    - [ ] Implement `supervisor_loop` (placeholder for now).
    - [ ] Setup `loguru` to write to `logs/app.log` (sink).
    - [ ] Ensure graceful shutdown (SIGINT handling).

### Core Components
- [ ] **Python REPL Engine (`core/repl.py`)**:
    - [ ] Create `PythonREPL` class.
    - [ ] Implement `execute(code: str) -> Any` method.
    - [ ] **Context Management**: Ensure `locals()` dictionary persists between calls.
    - [ ] **Output Capture**: Capture `stdout`/`stderr` from executed code.
    - [ ] **Basic Safety**: Block usage of `exit()`, `quit()` inside the REPL to prevent killing the host.

### Testing & Verification
- [ ] **Test Concurrency**: Verify `user_loop` is not blocked by `supervisor_loop`.
- [ ] **Test REPL State**: Unit test to verify variable persistence.
- [ ] **Test Logging**: Verify logs appear in file and not on console.

## 🏗️ In Progress
*No tasks currently in progress.*

## ✅ Done
- [x] **Plan Review**: Reviewed and finalized architectural approach (`plans.md`, `suggestions.md`).
