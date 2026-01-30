# Vibe Assistant - Consolidated Implementation Plan

## Project Goal
Build a proactive CLI assistant that utilizes concurrency to handle user interactions while performing autonomous background tasks (planning, refining notes).

## Core Principles
*   **Domain-First:** Define entities (Notes, Tasks) and logic before implementation details.
*   **Safety & Reliability:** Ensure data integrity (atomic writes) and graceful process termination.
*   **Test-Driven:** Logic must be testable independent of the async runtime.
*   **Progressive Complexity:** Skeleton -> Logic -> UI.

---

## Phase 1: The Robust Async Skeleton
**Objective:** Establish a stable concurrent runtime that handles user input and background tasks simultaneously, with safe shutdown and logging controls.

### Detailed Steps
1.  **Project Infrastructure:**
    *   Initialize git and virtual environment.
    *   Install core dependencies: `aioconsole` (async input), `loguru` (logging).
    *   Create `tests/` directory and configure `pytest`.
2.  **Async Core Loop:**
    *   Create `main.py` entry point.
    *   Implement `user_loop()`: Awaits user input via `aioconsole.ainput`.
    *   Implement `agent_loop()`: Runs a heartbeat that logs periodic status updates.
    *   **Mitigation:** Configure `loguru` to write verbose logs to a file (`app.log`) and only critical info to `stderr` to minimize prompt interference.
3.  **Graceful Shutdown:**
    *   Implement signal handlers (`SIGINT`, `SIGTERM`) in the `asyncio` loop.
    *   Ensure pending tasks are cancelled and awaited upon exit to prevent "hanging" processes.

### Testing & Evaluation
*   **Automated Tests:** None for this phase (mostly integration).
*   **Manual Verification:**
    *   *Concurrency:* Run app, type "hello", ensure immediate response while background logs appear.
    *   *Shutdown:* Press `Ctrl+C`. Verify the application exits immediately and cleans up without stack traces.
    *   *Log Check:* Verify `app.log` contains the background heartbeat messages.

---

## Phase 2: Domain Logic, Persistence & Testing
**Objective:** Implement the "Brain" of the assistant with robust state management and data integrity.

### Detailed Steps
1.  **Domain Models:**
    *   Create `models.py`: Define `Note` and `Task` using Python `dataclasses` or `pydantic`.
2.  **State Management (The Logic):**
    *   Create `managers.py`: Implement `NoteManager` and `TaskManager`.
    *   **Separation of Concerns:** Managers return data objects, they do *not* print to stdout.
3.  **Atomic Persistence:**
    *   Implement `save()` method using the "Write to Temp -> Rename" pattern to prevent data corruption on crash.
    *   Store data in `data/notes.json`.
4.  **CLI Integration:**
    *   Update `user_loop` to handle commands: `add <note>`, `list`.
    *   Update `agent_loop` to monitor the note count or status.

### Testing & Evaluation
*   **Automated Tests (Pytest):**
    *   `test_models.py`: Verify model instantiation and validation.
    *   `test_managers.py`: specific tests for `add_note`, `list_notes`, and persistence loading/saving.
*   **Manual Verification:**
    *   *Persistence:* Add a note, exit, restart. Verify note exists.
    *   *Crash Safety:* Kill process (`kill -9`) during a write operation (simulated). Verify JSON is valid.
    *   *Data Integrity:* check `data/notes.json` format manually.

---

## Phase 3: The TUI & Proactive Agent
**Objective:** Upgrade the user experience to a split-screen TUI and enable actual agent autonomy.

### Detailed Steps
1.  **UI Upgrade:**
    *   Introduce `rich` or `textual` library.
    *   Create a split layout: Bottom/Side for User Input, Main/Top for Logs & Status.
    *   Eliminate the "log garbling prompt" issue completely.
2.  **Agent Logic:**
    *   Implement "Proactive Scan": Agent reads new notes and identifies potential tasks.
    *   Implement logic: `Request -> Plan -> Execute`.
3.  **Refinement:**
    *   Add visual indicators for agent status (Idle, Thinking, Working).

### Testing & Evaluation
*   **Automated Tests:**
    *   Unit tests for the planning algorithm/heuristics.
*   **Manual Verification:**
    *   *UX:* Verify typing is never interrupted by background updates.
    *   *Workflow:* Create a note with a "todo". Verify agent eventually highlights it or proposes a task.