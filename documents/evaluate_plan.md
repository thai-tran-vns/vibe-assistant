# Plan Evaluation

This document evaluates the proposed architecture and process for the Vibe Assistant, based on `PLAN.md`.

## 1. Process Evaluation

### Strengths
*   **Risk-First:** Phase 1 addresses the hardest technical challenge: running a background loop alongside blocking user input.
*   **Iterative:** Moving from a skeleton -> domain logic -> UI polish prevents over-engineering early on.
*   **Simple Stack:** Sticking to JSON and standard async libraries keeps overhead low.

### Weaknesses
*   **Output Conflict:** In a basic CLI (Phase 1/2), background logs printing to `stdout` will inevitably garble the user's input prompt. This makes the prototype frustrating to use before Phase 3 (TUI) arrives.
*   **Missing Testing Strategy:** There is no mention of unit tests for the Domain Logic (Phase 2). Logic should be tested independently of the async runtime.

## 2. Reliability & Risks

*   **The "Output" Race:** `loguru` printing asynchronously while the user types via `aioconsole` will break the visual prompt line.
    *   *Mitigation:* Use a dedicated logging area or silence non-critical background logs during input mode until the TUI is ready.
*   **Graceful Shutdown:** Async loops are notorious for hanging on exit if tasks aren't cancelled properly.
    *   *Risk:* `Ctrl+C` might leave the JSON file corrupted or the process hanging.
*   **JSON Corruption:** If the app crashes while writing to `notes.json`, data is lost.
    *   *Mitigation:* Write to a temporary file and atomic rename.

## 3. Improvements

*   **Add "Graceful Shutdown" to Phase 1:** Explicitly plan for a signal handler (SIGINT) to cancel pending tasks and close the loop cleanly.
*   **Atomic Writes in Phase 2:** Ensure the `save` method writes to `temp.json` and renames it to `notes.json` to prevent partial writes.
*   **Separate "View" from "Logic" early:** Even in Phase 2, ensure the `NoteManager` returns data rather than printing it directly. This makes the Phase 3 transition to a TUI much easier.

## 4. What to Validate Manually

*   **Input Interruption:** Type a long sentence while the background agent is logging. Does the cursor jump? Does the text get mixed with log lines?
*   **Crash Recovery:** Kill the process (`kill -9`) while it's "processing" a note. Check if `notes.json` is valid JSON afterwards.
*   **State Persistence:** Add a note, exit normally, and restart. Verify the note is still there.
