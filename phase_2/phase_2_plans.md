# Phase 2: The Appliances (Domain & Tools)

**Goal:** Build the "Hands" of the system (Tools) and the data layer (Memory), and integrate the REPL so the "Kitchen" is fully functional for manual cooking.

## 1. REPL Integration (Immediate Priority)
*Current State:* `main.py` echoes text. `core/repl.py` exists but uses `exec()` which doesn't support `await`.
*Action:* Connect them and upgrade capabilities.
- **Update `core/repl.py`:**
    - Detect `await` keyword in input.
    - If present, wrap code in `async def _runner(): ...` and run with `await _runner()`.
    - Ensure local variables are preserved across executions.
- **Update `main.py`:**
    - Instantiate `PythonREPL` in `main`.
    - In `user_loop`, pass input to `repl.execute(code)`.
    - Print stdout/stderr result.

## 2. Domain Models (`models/`)
*Action:* Define the fundamental data structures using Pydantic (for easy JSON serialization/schema generation).
- **`models/note.py`:**
    - `Note(id: UUID, content: str, tags: List[str], created_at: datetime)`
- **`models/task.py`:**
    - `Task(id: UUID, description: str, status: Enum['TODO', 'DONE'], due_date: Optional[datetime])`

## 3. Memory System (`memory/`)
*Action:* Create the persistent storage ("The Order Ticket").
- **Strategy:** Folder of JSON files.
- **Naming Pattern:** `data/storage/{uuid}.json`.
    - *Efficiency:* Direct access by ID. No parsing of a massive list file.
    - *Concurrency:* Lower risk of write conflicts compared to a single file.
- **`memory/storage.py`:**
    - `save_item(item: BaseModel)`: Writes to `data/storage/{item.id}.json`.
    - `load_item(id: UUID)`: Reads specific file.
    - `list_items(type: Type)`: Scans directory (glob) and filters by type (checking JSON content or name if we prefix). *Decision: Keep it simple, read all JSONs or index them in memory if performance hits.*
- **`memory/manager.py`:**
    - `MemoryManager` class.
    - Methods: `add_note`, `get_note`, `list_notes`, `add_task`, `complete_task`.
    - Manages the in-memory state (optional cache) and syncs to disk via `storage.py`.

## 4. Tool Registry (`tools/`)
*Action:* Expose the Memory System as "Appliances" to the REPL, following MCP principles.
- **`tools/base.py`:**
    - Define `Tool` protocol/abstract class.
    - Method `get_schema()`: Returns JSON schema of the tool (for future LLM use).
    - Method `__call__`: The execution logic.
- **`tools/memory.py`:**
    - Wrap `MemoryManager` methods into Tool classes/functions.
    - **Namespace:** Inject a `tools` object into the REPL.
    - *Example Usage:* `await tools.notes.add("Buy milk")` or `await tools.add_note("Buy milk")`.
- **Injection:**
    - Update `main.py` or `repl.py` to inject these tools into `self.locals`.

## Verification
- **Manual Test:**
    1. Run `main.py`.
    2. Type `await tools.add_note("Test Note")`.
    3. Check `data/storage/` for a new JSON file.
    4. Type `tools.list_notes()`.
- **Unit Tests:** Test `MemoryManager` persistence (file creation) and Model validation.