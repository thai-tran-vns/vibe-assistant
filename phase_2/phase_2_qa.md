# Phase 2 Questions

1. **REPL Await Handling:**
   - *Question:* Does the current `PythonREPL` support top-level `await`? If not, do we need to implement a wrapper to execute async tool calls (since file I/O will be async)?
   - *Answer:* Yes, we need to implement support for top-level `await`. The current `exec` implementation does not support it natively, so we will need to wrap async code or use `ast` transformations.

2. **Data Store Format:**
   - *Question:* Should `data/store.json` be a single file or a folder of JSONs? A single file is simpler (KISS) but risky for concurrency.
   - *Answer:* It should be a folder of JSON files. A naming pattern will be designed for efficiency (likely UUID-based).

3. **Tool namespace:**
   - *Question:* Should tools be global functions (e.g., `add_note()`) or namespaced (e.g., `tools.add_note()`)?
   - *Answer:* Tools should be local and MCP (Model Context Protocol) friendly. This implies a structured approach where tools expose their schemas and are potentially grouped (e.g., `tools.add_note`), rather than polluting the global namespace.
