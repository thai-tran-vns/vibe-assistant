# Phase 2 Suggestions

1. **Use `aiofiles`:**
   - Since the entire app is async (`aioconsole` loop), using standard `open()` in `MemoryManager` would block the event loop. We should use `aiofiles` to ensure the "Kitchen" stays responsive while the "Appliance" is working.

2. **Rich Output:**
   - Even though full TUI is Phase 4, we can use `rich.print` in `main.py` immediately to make the REPL output (stdout vs stderr) visually distinct.

3. **"Magic" Commands:**
   - Implement simple slash commands in `main.py` (e.g., `/clear`, `/reset`) that are intercepted before reaching the Python REPL. This keeps the Python environment clean.
