# Revised Project Plan: The Supervisor Architecture (v2)

## Overview
Transform `vibe-assistant` into a **Supervisor-Worker Agent System** inspired by the `RLM` "Master Chef" model. The goal is a highly modular, autonomous CLI assistant.

*   **Supervisor (System):** The "Head Chef" who orchestrates.
*   **Sub-Agents (Workers):** The "Line Cooks" who execute specialized tasks.
*   **Skills:** The "Recipes" (workflows/logic) that Agents follow.
*   **Tools:** The "Kitchen Appliances" (atomic functions) used by Skills.
*   **Memory:** The "Orders & Notes" (shared context).

---

## Phase 1: The Foundation
**Focus:** Infrastructure, Event Loop, and basic "Supervisor" Skeleton.

### Tasks
1.  **Refine `main.py`:**
    *   Rename `agent_loop` to `supervisor_loop`.
    *   Ensure strict separation between "User Interface" (Input/Output) and "Agent Brain" (Logic).
2.  **Define Core Interfaces (`core.py`):**
    *   `Agent`: Protocol defining `run()`, `shutdown()`.
    *   `Memory`: Protocol for data access.
    *   `Tool`: Protocol for atomic executable actions.
3.  **Implement Basic Supervisor:**
    *   A simple state machine that logs "Watching..." and can react to a "ping" from the user.

---

## Phase 2: The "RLM" Core (Memory, Tools, Skills)
**Focus:** The Brain (Memory) and Hands (Tools/Skills).

### Tasks
1.  **Memory System (`memory/`):**
    *   **Concept:** Distinguish between "Session Memory" (Active context, short-term) and "Archive" (Long-term persistence).
    *   **Structure:** Create `MemoryManager`.
    *   **Persistence:** Implement atomic save/load to `data/memory.json` (or YAML as per RLM preference).
2.  **Tool System (`tools/`):**
    *   **Concept:** Atomic, side-effect producing Python functions (The "Appliances").
    *   **Initial Tools:**
        *   `FileTool`: Read/Write files.
        *   `TimeTool`: Get current time.
3.  **Skill System (`skills/`):**
    *   **Concept:** Workflows that chain Tools together (The "Recipes").
    *   **Implementation:**
        *   Define `BaseSkill` with `name`, `description`, `execute()`.
        *   Design to eventually support Markdown-defined logic (RLM style), but start with Python classes for simplicity.
        *   *Example Skill:* `SaveNoteSkill` (uses `FileTool` + formatting logic).

---

## Phase 3: The Sub-Agent Hierarchy
**Focus:** Specialization and Delegation.

### Tasks
1.  **Sub-Agent Framework:**
    *   Create `BaseAgent` class implementing the Phase 1 interface.
    *   Agents are assigned specific **Skills** and access to **Memory**.
2.  **The "Supervisor" Logic:**
    *   Implement routing logic (The "Dispatcher"):
        *   *If input implies action -> Delegate to `TaskAgent`.*
        *   *If input is chat -> Delegate to `ChatAgent`.*
3.  **Implement `TaskAgent`:**
    *   Equipped with `SaveNoteSkill`, `ListNotesSkill`.
4.  **Implement `ChatAgent`:**
    *   Equipped with basic conversation logic (echo or LLM integration).

---

## Phase 4: Autonomy & "Vibe"
**Focus:** Proactivity and TUI.

### Tasks
1.  **TUI Integration:**
    *   Move to `textual` or `rich` for a split-screen interface.
    *   Visualize Supervisor state (Idle, Delegating, Waiting).
2.  **Proactive Routines:**
    *   Give Supervisor a `Cron` trigger (e.g., "Every 5 mins check for stale tasks").
    *   Supervisor wakes up `HousekeeperAgent` to clean up memory.

---

## Verification Plan
*   **Unit Tests:** Test `Memory` read/write, `Tool` execution, and `Supervisor` routing logic.
*   **Integration Tests:** Simulate a user "Add Note" command -> Supervisor -> TaskAgent -> SaveNoteSkill -> FileTool -> Disk.