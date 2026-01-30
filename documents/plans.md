# Revised Project Plan: The "Recursive Chef" Architecture (v4)

## Overview
This plan consolidates the original **CLI Assistant** scope with the **"Master Chef"** organizational model (`RLM.md`) and the **Recursive REPL** interaction mechanism (`RLM_paper.md`).

**The Concept:**
*   **The Kitchen (Environment):** An async Python REPL where the agent "lives".
*   **The Appliances (Tools):** Atomic functions (NoteManager, FileSystem) exposed to the REPL.
*   **The Recipes (Skills):** High-level workflows defined in Markdown/Code that the agent follows.
*   **The Chef (Agent):** The logic that observes the kitchen, plans using recipes, and executes via code generation.

---

## Phase 1: The Kitchen (Infrastructure & REPL)
**Goal:** Establish the `asyncio` runtime and the Python Execution Environment.

### Tasks
1.  **Async Core (`main.py`):**
    *   Implement the `user_loop` (Input) and `supervisor_loop` (Background) using `aioconsole`.
    *   Setup `loguru` for file-based logging (avoid stdout pollution).
2.  **The REPL (`core/repl.py`):
    *   Implement a `PythonREPL` class.
    *   **Context Persistence:** Maintain a `locals()` dictionary across turns.
    *   **Safety:** Basic restrictions on dangerous imports.
    *   *Connection to RLM Paper:* The agent interacts with the world *only* by writing code to this REPL.

---

## Phase 2: The Appliances (Domain & Tools)
**Goal:** Build the "Hands" of the system and the data layer.

### Tasks
1.  **Domain Models (`models/`):
    *   Define `Note`, `Task` (Pydantic/Dataclasses).
2.  **Memory System (`memory/`):
    *   **Session Memory:** Short-term context (recent REPL outputs).
    *   **Long-Term Memory:** The "Order Ticket". A `MemoryManager` that persists notes/tasks to `data/store.json` (Atomic writes).
3.  **Tool Registry (`tools/`):
    *   Create `Tool` protocol.
    *   Expose `MemoryManager` methods as tools (e.g., `tools.add_note`, `tools.list_notes`).
    *   *Key Distinction:* These are *deterministic Python functions* (The Appliances).

---

## Phase 3: The Chef (Agent Logic & Skills)
**Goal:** Implement the "Brain" that uses the Tools.

### Tasks
1.  **The Agent Loop (`agent/`):
    *   **Observation:** Read REPL output / Memory state.
    *   **Thought:** LLM decides what to do.
    *   **Action:** Generate Python code -> Execute in REPL.
2.  **Recursive "Sub-Chefs" (`llm_query`):
    *   Implement the `llm_query` primitive for the REPL.
    *   *Use Case:* If a note is too long, the Agent writes code to slice it and calls `llm_query` to summarize the slice.
3.  **Skills (`skills/`):
    *   Define "Recipes" (e.g., `ReviewDailyTasks`).
    *   Initially implement as Python functions that the Agent can call.
    *   *Evolution:* Move to Markdown-defined recipes that the Agent reads and interprets.

---

## Phase 4: The Service (UI & Proactivity)
**Goal:** A beautiful, proactive user experience.

### Tasks
1.  **TUI (`ui/`):
    *   Integrate `rich` (or `textual`) for a split-screen view.
    *   **Top Pane:** Agent Status / Logs (The "Kitchen Window").
    *   **Bottom Pane:** User Input.
2.  **Proactivity:**
    *   The `supervisor_loop` periodically injects a "Trigger" into the REPL (e.g., `check_schedule()`).
    *   The Agent wakes up, runs the code, and notifies the user if needed.

---

## Verification Plan
*   **Phase 1:** Test REPL variable persistence and async loop concurrency.
*   **Phase 2:** Test `MemoryManager` atomic saves and Tool exposure.
*   **Phase 3:** Integration test: "Agent, create a note about apples." -> Agent writes `tools.add_note("Apples")` -> Verify JSON.
*   **Phase 4:** User Acceptance: Verify TUI responsiveness while Agent works in background.
