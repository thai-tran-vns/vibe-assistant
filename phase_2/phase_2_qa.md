# Phase 2 Questions

1. **REPL Await Handling:**
   - *Question:* Does the current `PythonREPL` support top-level `await`? If not, do we need to implement a wrapper to execute async tool calls (since file I/O will be async)?
   - *Answer:* (Leave empty for now)

2. **Data Store Format:**
   - *Question:* Should `data/store.json` be a single file or a folder of JSONs? A single file is simpler (KISS) but risky for concurrency.
   - *Answer:* (Leave empty for now)

3. **Tool namespace:**
   - *Question:* Should tools be global functions (e.g., `add_note()`) or namespaced (e.g., `tools.add_note()`)?
   - *Answer:* (Leave empty for now)
