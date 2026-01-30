# Questions & Clarifications

## Critical Items
1.  **Missing `RLM.md`**: You mentioned "Read `RLM.md` file and learn from it", but this file is not present in the current directory or its subdirectories.
    *   *Action*: I have proceeded with standard "Supervisor-Worker" and "Memory/Skill" architectural patterns.
    *   *Request*: Please provide the content of `RLM.md` or summarize its specific "Refinement/Learning/Memory" concepts if they differ from standard patterns.
    *   *Answer*: [File is in vibe-assistant/documents/RML.md]

2.  **Agent Nature**:
    *   *Question*: Are the `Supervisor` and `Sub-agents` intended to be LLM-driven (using OpenAI/Anthropic/Gemini APIs) or deterministic state-machines?
    *   *Context*: The current "vibe-assistant" plan implies a local CLI tool. Adding "Agents" usually implies AI.
    *   *Answer*: [yes]

3.  **Memory Scope**:
    *   *Question*: Should "Memory" be simple file persistence (JSON/SQLite) or a semantic vector store (Chroma/FAISS) for retrieval-augmented generation?
    *   *Answer*: [Simple file (may preference RLM.md)]

4.  **Skill Scope**:
    *   *Question*: Do "Skills" refer to Python functions available to the agents (Tool use) or learned behaviors?
    *   *Answer*: [preference RLM.md first]
