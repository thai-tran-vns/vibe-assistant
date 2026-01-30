# Q&A: The Consolidated "Recursive Chef" Plan

## Core Concepts

### Q: Are we building the "Master Chef" or the "Recursive REPL"?
**A:** Both. "Master Chef" is the **Metaphor** (Organization of Skills/Tools). "Recursive REPL" is the **Mechanism** (How the Chef works).
The Chef doesn't just push buttons (Function Calling); they write recipes on the fly (Python Code in REPL).

### Q: Why use a REPL for a simple Task Manager?
**A:** Flexibility. Standard agents are limited by their defined tools. A REPL-based agent can:
1.  Filter notes: `[n for n in notes if "urgent" in n.text]`
2.  Format output: `print(f"Items: {len(notes)}")`
3.  Combine data: `tools.email(tools.summarize(notes))`
All without us writing specific "FilterTool" or "FormatTool" classes.

### Q: How does this fit the `PLAN.md` async goal?
**A:** The `REPL` runs inside the Agent's event loop. It is just a component. The `main.py` still manages the `asyncio` concurrency to keep the UI responsive while the Agent (Chef) is "cooking" (executing code/thinking) in the background.

## Implementation Details

### Q: What is `llm_query` used for in this context?
**A:** Handling large data or complex logic. If a user asks "Summarize all 500 notes", the Agent shouldn't load them all into context. It should write code to batch them and use `llm_query` to summarize each batch recursively.

### Q: Is `tools/` just for external APIs?
**A:** No. In this architecture, `tools/` contains the "Appliances" - our own internal classes (`NoteManager`, `MemoryManager`) exposed to the REPL so the agent can control the application state.

