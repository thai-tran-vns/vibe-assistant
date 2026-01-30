# Architectural Suggestions

## 1. The Supervisor-Worker Architecture
Instead of a single monolithic loop, we structure the application as a hierarchy:
*   **Supervisor Agent (`System`):** The "Main Loop". It never sleeps (conceptually). It monitors the `Memory`, checks `Triggers`, and decides which `Sub-Agent` to wake up.
*   **Sub-Agents (`Workers`):** Specialized units. They come alive, perform a specific task, return a result to `Memory`, and shut down/sleep.
    *   *Examples:* `NoteTaker`, `TaskPlanner`, `Summarizer`, `Housekeeper`.

## 2. Memory Architecture ("The Blackboard")
We should move away from direct file manipulation by agents.
*   **The Shared Workspace:** A central `MemoryStore` object.
*   **Structure:**
    *   `ShortTerm`: Recent user inputs, active context.
    *   `LongTerm`: Stored notes, completed tasks (Database/Files).
    *   `WorkingMemory`: The current "Plan" being executed.
*   **Pattern:** Agents read from Memory -> Think -> Write to Memory.

## 3. Skill Registry
Decouple "Capabilities" from "Agents".
*   **Skills:** Atomic, executable Python functions (e.g., `write_file`, `search_notes`, `send_notification`).
*   **Registry:** A dictionary mapping `skill_name` -> `callable`.
*   **Usage:** The Supervisor grants specific subsets of skills to specific sub-agents.

## 4. Implementation Strategy (Pythonic)
*   **Protocol Classes:** Use `typing.Protocol` to define `Agent` and `Skill` interfaces strictly.
*   **Event Bus:** Consider a simple in-memory event bus (`user_input_received` -> `supervisor_wakes_up`) to decouple the loop from the logic.

## 5. Technology Stack Recommendations
*   **Pydantic:** For strict schema validation of Agent inputs/outputs.
*   **LiteLLM:** (If AI is used) For unified API access to various LLMs.
*   **ChromaDB:** (Optional) For semantic search over long-term memory if the corpus grows large.
