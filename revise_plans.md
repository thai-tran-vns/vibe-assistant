# Revised Project Plan: The Supervisor Architecture

## Overview
Transform `vibe-assistant` from a simple concurrent loop into a robust **Supervisor-Worker Agent System**. The goal is a highly modular, autonomous CLI assistant where a central "Supervisor" orchestrates specialized "Sub-agents" to handle tasks, utilizing a shared "Memory" and "Skill" system.

---

## Phase 1: The Foundation (Revised)
**Focus:** Infrastructure, Event Loop, and basic "Supervisor" Skeleton.
*Status: Partially Complete (Async loop exists).*

### Tasks
1.  **Refine `main.py`:**
    *   Rename `agent_loop` to `supervisor_loop`.
    *   Ensure strict separation between "User Interface" (Input/Output) and "Agent Brain" (Logic).
2.  **Define Core Interfaces (`core.py`):**
    *   `Agent`: Protocol defining `run()`, `shutdown()`.
    *   `Memory`: Protocol for data access.
    *   `Skill`: Protocol for executable actions.
3.  **Implement Basic Supervisor:**
    *   A simple state machine that logs "Watching..." and can react to a "ping" from the user.

---

## Phase 2: Memory & Skills System
**Focus:** The "Brain" and "Hands" of the system.

### Tasks
1.  **Memory System (`memory/`):**
    *   **Structure:** Create `MemoryManager` class.
    *   **Components:**
        *   `Inbox`: For incoming user messages.
        *   `Archive`: For persistent storage (JSON/SQLite).
    *   **Persistence:** Implement atomic save/load to `data/memory.json`.
2.  **Skill Registry (`skills/`):**
    *   **Base Class:** `BaseSkill` with `name`, `description`, `execute()`.
    *   **Initial Skills:**
        *   `SaveNoteSkill`: Saves text to memory.
        *   `ListNotesSkill`: Retrieves text.
    *   **Registry:** A dynamic loader to register skills by name.

---

## Phase 3: The Sub-Agent Hierarchy
**Focus:** Specialization and Delegation.

### Tasks
1.  **Sub-Agent Framework:**
    *   Create `BaseAgent` class implementing the Phase 1 interface.
    *   Give Agents access to specific `Skills` and `Memory` slices.
2.  **The "Supervisor" Logic:**
    *   Implement routing logic:
        *   *If input starts with "todo" -> Delegate to `TaskAgent`.*
        *   *If input is chat -> Delegate to `ChatAgent`.*
        *   *Else -> Log "Unknown command".*
3.  **Implement `TaskAgent`:**
    *   A specialized sub-agent that uses `SaveNoteSkill` to parse and store tasks.
4.  **Implement `ChatAgent`:**
    *   A specialized sub-agent that simply echoes or (later) calls an LLM.

---

## Phase 4: Autonomy & "Vibe"
**Focus:** Proactivity and TUI.

### Tasks
1.  **TUI Integration:**
    *   Move to `textual` or `rich` for a split-screen interface.
    *   Visualizing the "Supervisor" state (Idle, Delegating, Waiting).
2.  **Proactive Routines:**
    *   Give Supervisor a `Cron` trigger (e.g., "Every 5 mins check for stale tasks").
    *   Supervisor wakes up `HousekeeperAgent` to clean up memory.

---

## Verification Plan
*   **Unit Tests:** Test `Memory` read/write, `Skill` execution, and `Supervisor` routing logic in isolation.
*   **Integration Tests:** Simulate a user "Add Note" command and verify the full chain: User -> Supervisor -> TaskAgent -> Skill -> Memory -> Disk.
