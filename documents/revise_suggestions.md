# Architectural Suggestions (Incorporated into Plan v2)

## 1. The Supervisor-Worker Architecture
*   **Supervisor Agent (`System`):** The "Head Chef". Monitors `Memory`, checks `Triggers`, delegates to `Sub-Agents`.
*   **Sub-Agents (`Workers`):** The "Line Cooks". Execute specific `Skills`.
    *   *Examples:* `TaskAgent`, `ChatAgent`.

## 2. Memory Architecture ("The Blackboard")
*   **The Shared Workspace:** A central `MemoryManager`.
*   **Structure:**
    *   `SessionMemory`: Recent user inputs, active context (Short-term).
    *   `Archive`: Stored notes, completed tasks (Long-term/Files).
    *   `WorkingMemory`: The current "Plan" being executed.

## 3. Capability System (Tools & Skills)
Decouple "Atomic Actions" from "Workflows".
*   **Tools (The "Appliances"):** Atomic, side-effect producing Python functions (e.g., `write_file`, `get_time`).
*   **Skills (The "Recipes"):** Workflows that chain Tools together (e.g., `SaveNoteSkill`, `DailyReviewSkill`).
    *   *Future Goal:* Define Skills in Markdown (RLM style).
*   **Registry:** Dynamic loader to register Skills/Tools by name.

## 4. Implementation Strategy (Pythonic)
*   **Protocol Classes:** Use `typing.Protocol` to define `Agent`, `Tool`, and `Skill` interfaces.
*   **Event Bus:** Consider a simple in-memory event bus (`user_input_received` -> `supervisor_wakes_up`).

## 5. Technology Stack Recommendations
*   **Pydantic:** For strict schema validation.
*   **LiteLLM:** (If AI is used) For unified LLM access.
*   **Loguru:** For structured logging.