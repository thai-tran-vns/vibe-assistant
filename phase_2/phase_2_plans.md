# Phase 2: The Appliances (Domain & Tools)

**Goal:** Build the "Hands" of the system (Tools) and the data layer (Memory), and integrate the REPL so the "Kitchen" is fully functional for manual cooking.

## 1. REPL Integration (Immediate Priority)
*Current State:* `main.py` echoes text. `core/repl.py` exists but is unused.
*Action:* Connect them.
- **Update `main.py`:**
    - Instantiate `PythonREPL` in `main`.
    - In `user_loop`, pass input to `repl.execute(code)`.
    - Print stdout/stderr result.
    - Handle `await` keywords if the REPL supports top-level await (or wrap it).

## 2. Domain Models (`models/`)
*Action:* Define the fundamental data structures using Pydantic (for easy JSON serialization).
- **`models/note.py`:**
    - `Note(id: UUID, content: str, tags: List[str], created_at: datetime)`
- **`models/task.py`:**
    - `Task(id: UUID, description: str, status: Enum['TODO', 'DONE'], due_date: Optional[datetime])`

## 3. Memory System (`memory/`)
*Action:* Create the persistent storage ("The Order Ticket").
- **`memory/storage.py`:**
    - Handle reading/writing to `data/store.json`.
    - Use `aiofiles` for async I/O to avoid blocking the `supervisor_loop`.
- **`memory/manager.py`:**
    - `MemoryManager` class.
    - Methods: `add_note`, `get_note`, `list_notes`, `add_task`, `complete_task`.
    - Manages the in-memory state and syncs to disk.

## 4. Tool Registry (`tools/`)
*Action:* Expose the Memory System as "Appliances" to the REPL.
- **`tools/base.py`:** Define a simple pattern/protocol for Tools.
- **`tools/memory.py`:**
    - Instantiate `MemoryManager`.
    - Create functions that map to `MemoryManager` methods.
    - **Crucial:** These functions must be injected into the `PythonREPL` locals.
    - *Example Usage in REPL:* `await tools.add_note("Buy milk")`

## Verification
- **Manual Test:** Run `main.py`, type `tools.add_note("Test")`, then check `data/store.json`.
- **Unit Tests:** Test `MemoryManager` persistence and Model validation.
