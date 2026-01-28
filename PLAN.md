# Vibe Assistant Implementation Plan

## Project Goal
Build a proactive CLI assistant that handles user interactions and performs autonomous background tasks (planning, refining notes) when idle.

## Core Principles
*   **KISS (Keep It Simple Stupid):** Start with the absolute minimum to prove concurrency.
*   **Domain-First:** Define the entities (Notes, Tasks) before the implementation details.
*   **Async/Non-blocking:** Use Python's `asyncio` to handle user input and background tasks simultaneously.

## Architecture
*   **Language:** Python 3.
*   **Concurrency:** `asyncio` event loop.
*   **Input:** `aioconsole` for non-blocking standard input.
*   **Logging:** `loguru` for clean, thread-safe logging.
*   **Storage:** Local JSON files (initially).

---

## Implementation Phases

### Phase 1: The Async Skeleton (Current Focus)
**Goal:** Establish the concurrent runtime where a user can type commands while a background process is active.
1.  **Project Setup:** Initialize git, virtualenv, and dependencies (`loguru`, `aioconsole`).
2.  **Core Loop:** Create `main.py` with an `asyncio` event loop.
3.  **Components:**
    *   `user_loop()`: Awaits user input non-blockingly.
    *   `agent_loop()`: Runs indefinitely, simulating background activity (heartbeat).
4.  **Verification:** User can type `hello` and get a response while the agent logs "Checking notes..." in the background.

### Phase 2: Domain & State (The "Brain")
**Goal:** Introduce actual logic for Notes and Tasks.
1.  **Domain Models:** Create `Note` and `Task` dataclasses.
2.  **State Management:** Implement `NoteManager` and `TaskManager`.
3.  **Persistence:** Save/Load state to `data/notes.json` and `data/tasks.json`.
4.  **Logic:**
    *   User command `add note <text>` saves a note.
    *   Background agent reads notes and marks them as "processed".

### Phase 3: The "TUI" & Planning
**Goal:** Advanced visualization and task execution workflow.
1.  **UI Upgrade:** Transition to `rich` or `Textual` for a split-screen interface (Input vs. Status).
2.  **Task Planning:** Implement the flow: Request -> Plan -> Estimate -> Confirm -> Execute.
3.  **Proactivity:** Agent looks for "todo" keywords in notes and proposes tasks.
