# Questions & Clarifications (Resolved)

## Critical Items
1.  **Missing `RLM.md`**:
    *   *Status*: Found (`documents/RLM.md`).
    *   *Resolution*: The "Refinement/Learning/Memory" concepts (Master Chef analogy, Skill/Tool separation) have been incorporated into `revise_plans.md` (Phase 2).

2.  **Agent Nature**:
    *   *Question*: Are Agents LLM-driven?
    *   *Answer*: **Yes**.
    *   *Resolution*: Plan assumes `ChatAgent` and others will eventually use LLMs.

3.  **Memory Scope**:
    *   *Question*: Simple file or Vector Store?
    *   *Answer*: **Simple file** (preference RLM.md).
    *   *Resolution*: Plan specifies `MemoryManager` with Session/Archive separation (JSON/YAML).

4.  **Skill Scope**:
    *   *Question*: Python functions or Learned Behaviors?
    *   *Answer*: **Preference RLM.md first** (Declarative/Markdown).
    *   *Resolution*: Plan distinguishes between **Tools** (Python functions) and **Skills** (Workflows), with a roadmap to move Skills to Markdown definitions.