# Architectural Suggestions: The "Recursive Chef"

## 1. The Hybrid Architecture
Merge the **Supervisor** (State Machine) with the **REPL** (Execution Engine).
*   **Supervisor:** Manages the high-level loop (User Input -> Agent Wakeup -> Sleep).
*   **REPL:** The "Hands" of the agent. The Supervisor passes text commands to the Agent, which generates code to execute in the REPL.

## 2. Directory Structure (Aligned with `RLM.md`)
```text
vibe-assistant/
├── core/
│   ├── repl.py          # The Python Execution Sandbox
│   ├── loop.py          # The Supervisor/Async Logic
│   └── llm.py           # LLM Interface (and llm_query)
├── tools/               # The "Appliances"
│   ├── system.py        # File I/O, Time
│   └── memory.py        # Note/Task Managers (exposed to REPL)
├── skills/              # The "Recipes"
│   ├── basic.py         # Simple workflows
│   └── complex.md       # Future: Markdown-defined workflows
├── memory/              # The "Order Ticket"
│   ├── manager.py       # Persistence Logic
│   └── store.json       # The Data
└── ui/
    └── tui.py           # Rich/Textual Interface
```

## 3. Interaction Pattern: "Code as Action"
Instead of standard JSON Function Calling, use **Python Code Generation**.
*   *Standard:* Agent returns `{"function": "add_note", "args": {"text": "hi"}}`.
*   *Vibe RLM:* Agent writes `tools.memory.add_note("hi")`.
*   *Benefit:* The agent can compose tools naturally (e.g., `if tools.time.hour() > 17: tools.memory.add_note("Go home")`).

## 4. Proactivity via Cron
The Supervisor should have a simple scheduler that injects "Time Events" into the Agent's context.
*   *Trigger:* "It is now 9:00 AM."
*   *Agent Reaction:* Checks `skills.daily_review` and executes it if necessary.

