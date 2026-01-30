This analysis breaks down the codebase for **Recursive Language Models (RLMs)** (arXiv:2512.24601) into its core architectural components and provides structured learning paths to master the system.

### **Codebase Overview**

The RLM codebase implements an inference strategy that treats large contexts (e.g., 10M+ tokens) not as prompt input, but as an **external environment** (specifically, a Python REPL). The LLM writes code to inspect, slice, and recursively process this environment rather than reading the text linearly.

**Core Repository:** `alexzhang13/rlm` (Official)
**Key Concept:** `Context as a Variable` + `Recursive Self-Calls`

---

### **Part 1: Architectural Analysis**

The codebase is organized around three pillars: the **Agent (RLM)**, the **Environment (REPL)**, and the **Recursive Interface**.

#### **1. The Core Agent (`rlm/rlm_repl.py`)**

This is the "brain" of the system. Unlike standard agents that just "think" and "act," this agent's primary action is writing code to manage its own context.

* **The Loop:** It runs a continuous loop: `Observation -> Code Generation -> Execution -> Observation`.
* **Termination:** It listens for a specific signal (e.g., a variable `answer['ready'] = True` or a `FINAL()` function call) to stop the recursion and return the result.
* **Prompting:** It uses specialized system prompts (found in `rlm/utils/prompts.py`) that instruct the model *how* to use the Python environment to inspect data.

#### **2. The Execution Environment (`rlm/repl.py`)**

This is the sandbox where the "context" lives.

* **Persistence:** It maintains state across the agent's steps. If the agent defines `x = 5` in step 1, `x` is still 5 in step 2.
* **Context Loading:** Large documents are loaded here as string variables (e.g., `corpus`). The LLM never sees `corpus` directly; it sees `len(corpus)` or `corpus[:100]`.
* **Safety:** It executes generated code using standard Python `exec()` calls, often wrapped to capture `stdout` and `stderr`.

#### **3. The Recursive Primitive (`llm_query`)**

This is the defining feature of RLMs.

* **The Function:** The environment exposes a function, typically named `llm_query(prompt, context_snippet)`, to the Python REPL.
* **The Recursion:** When the main LLM executes `sub_result = llm_query("Summarize this", corpus[0:5000])`, it spawns a *new* LLM instance (a sub-call) to handle that specific chunk. This allows the model to "conquer" a large problem by "dividing" it programmatically.

---

### **Part 2: Structured Learning Paths**

These paths are designed to take you from basic understanding to advanced customization of the RLM architecture.

#### **Path A: The Mechanic (Understanding the Control Flow)**

*Goal: Understand how the LLM interacts with the Python REPL without recursion.*

1. **Entry Point:** Start with `rlm/repl.py`.
* **Focus:** Look at how the `exec_code()` function works. Note how it captures `stdout` to feed back to the LLM.
* **Task:** Manually instantiate the `REPL` class in a script, load a string variable into it, and execute a Python string that prints a slice of that variable.


2. **The Loop:** Move to `rlm/rlm_repl.py` (specifically the `completion` or `run` method).
* **Focus:** Trace the `while` loop. Identify where the model's output is parsed (extracting code blocks) and where it is sent to the REPL.
* **Key Insight:** Notice that the "Prompt" sent to the LLM grows with the *history of interactions* (code written + execution output), effectively creating a trajectory.



#### **Path B: The Recursionist (Mastering `llm_query`)**

*Goal: Learn how the model spawns sub-agents to solve sub-problems.*

1. **The Interface:** Examine how functions are registered in the REPL. Look for where `llm_query` or `submit_task` is defined.
2. **The Recursive Step:** Trace a call to `llm_query`.
* **Focus:** Does it call the *same* model class? Does it use a smaller model (e.g., GPT-4o-mini) for sub-tasks?
* **Task:** Create a dummy RLM that has a context of "123456...". Force it to write code that splits this string into two halves and calls `llm_query` on each half.


3. **State Management:** Observe how the "Answer" propagates back up. When a sub-LLM finishes, its text output becomes a *string variable* in the parent's REPL environment.

#### **Path C: The Architect (Customization & Scaling)**

*Goal: Apply RLM to custom data types or add new tools.*

1. **Prompt Engineering:** Analyze `rlm/utils/prompts.py`.
* **Focus:** The system prompt is critical. It explicitly forbids the model from asking for the full text and forces it to use Python slicing.
* **Experiment:** Try modifying the prompt to encourage "Binary Search" (looking at the middle of the file) vs. "Linear Scan".


2. **Tool Augmentation:**
* **Concept:** Since the environment is just Python, you can import *any* library.
* **Task:** Modify the `REPL` initialization to import `pandas`. Load a CSV file into the environment. Now the RLM can write pandas code to analyze data instead of just string manipulation.



### **Summary of Key Files**

| File | Role | Learning Focus |
| --- | --- | --- |
| `rlm_repl.py` | Main Agent Loop | How the model observes execution outputs. |
| `repl.py` | Python Sandbox | How context is stored as a variable (hidden from the prompt). |
| `utils/prompts.py` | Instruction Set | How the model is taught to *write code* instead of *answer directly*. |
| `utils/llm.py` | API Wrapper | How the recursion (sub-calls) is technically handled. |