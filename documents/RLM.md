To help you master this **Workflow Agent** codebase, I have designed a structured learning path organized by increasing complexity. This repository implements an agent that plans and executes tasks by generating Python code, using a library of "Skills" and "MCP Tools".

### Core Concept Analogy

Think of this system as a **Master Chef (The Agent)** in a high-end kitchen.

* **The Skills (`skills_v2/`)** are the **Recipe Books**. They tell the Chef *how* to prepare a specific dish (workflow) like "Onboarding" or "Performance Review".
* **The Tools (`tools/mcp_tools/`)** are the **Kitchen Appliances** (Oven, Blender, Knife). The Chef uses these to actually do the work (e.g., `bamboo_hr.py`, `slack.py`).
* **The Memory (`memory/`)** is the **Order Ticket & Notes**. It keeps track of what the customer asked for and what steps have already been completed.

---

### Level 1: The Blueprint (Architecture & Capabilities)

**Goal:** Understand what the agent can do and how it is organized.

**1. The Workspace Structure**
Start by exploring the high-level directories to understand the separation of concerns.

* **`agent_workspace/`**: The root module.
* **`workflow_agent/`**: The "Brain." Contains the logic for planning and executing code.


* **`skills_v2/`**: The "Knowledge." Contains Markdown definitions of business workflows (HR, Recruitment, Procurement).


* **`tools/mcp_tools/`**: The "Hands." Python implementations of external services (BambooHR, Jira, Slack).



**2. The Skill System**
The agent relies on "Skills" to decide *how* to solve a problem.

* **Definition:** Skills are defined in Markdown files within scope directories (e.g., `HR-scopes`). They provide a "Logic Flow" that the agent mimics.


* 
**Example:** Review `onboarding_new_hires.md`. Note how it lists **Dependencies** (tools) and **Action Steps** (logic).


* 
**Decision Making:** Read `skills_v2/Readme.md` to see how the planner decides between using a pre-written **Skill** vs. a **Custom Script**.



**3. The Tools (MCP)**

* **Implementation:** Look at `tools/mcp_tools/bamboo_hr.py`. You will see it loads mock data from JSON files in `data/`.


* **Documentation:** The agent doesn't read the Python code directly; it reads "MCP Docs" (Markdown files) located in `tools/mcp_docs/`. For example, `bamboo_hr/server.json` defines the available functions.



---

### Level 2: The Engine (The Execution Loop)

**Goal:** Trace how a user request becomes executed code.

**1. The Main Loop (`WorkflowAgent.run`)**
Open `workflow_agent/agent.py`. This is the orchestrator.

* 
**Phase 1: Planning.** The agent calls `self._planner.plan()` to analyze the user's intent and select a skill.


* 
**Phase 2: Execution.** It calls `execute_multi_turn_workflow`, which handles code generation and running the code.


* 
**Phase 3: Response.** Finally, `_workflow_executor.respond()` summarizes the results back to the user.



**2. Planning Logic**
Navigate to `workflow_agent/sub_agents/planner.py`.

* The planner reads the `skills_readme` and uses an LLM (via `baml_bridge`) to output a `Plan` object.


* The plan determines if the action is `chat`, `execute_skill`, or `custom_script`.



**3. Code Generation & Execution**
Navigate to `workflow_agent/sub_agents/executor.py`.

* 
**CodeGen:** The agent generates Python code based on the selected Skill MD and Tool Contracts.


* 
**Sandbox:** The `PythonCodeExecutor` (`code_executor.py`) runs this code in a temporary directory, injecting the necessary tool paths. It captures `stdout` and `stderr` to determine success or failure.



---

### Level 3: Advanced Concepts (Memory & Multi-Turn)

**Goal:** Understand how the agent handles complex, stateful interactions.

**1. Session Memory**
Explore `memory/session_memory.py` and `memory/chainlit_data_layer.py`.

* **Unified Storage:** The system uses YAML files to store threads. A single file contains both the conversation ("Messages") and the internal artifacts ("Working Steps" like plans and code).


* 
**Fact Extraction:** The `fact_extractor.py` uses regex to pull entities like names and dates from messages to keep context.



**2. Multi-Turn Workflows**
The agent can "pause" execution to ask for more info or wait for a long task.

* 
**Lookahead:** If a plan has `requires_lookahead: true`, the agent expects the code to output specific signals.


* 
**Signals:** Look for `CONTINUE_FACT` (to save data) or `CONTINUE_WORKFLOW` (to verify a checkpoint) in the execution output.


* 
**State Tracking:** The `WorkflowState` object in `agent.py` tracks the current step and collected facts across multiple turns.



### Recommended Next Step

Would you like me to walk you through the **`onboarding_new_hires.md`** skill file to explain exactly how the planner translates that Markdown into the executable Python code found in the tools directory?