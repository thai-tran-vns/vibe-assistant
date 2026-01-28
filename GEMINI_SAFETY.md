# Gemini Safety Protocol

## CRITICAL RULES - READ BEFORE ACTION

1.  **NO UNAUTHORIZED WRITES:** Do not overwrite configuration files like `.gitignore` unless explicitly instructed by the user to "overwrite" or "reset" it. If modifying, use `replace` or append, never full overwrite unless confirmed.
2.  **NO UNAUTHORIZED INSTALLATIONS:** Do not run `pip install`, `npm install`, or create virtual environments without asking the user for permission first.
3.  **NO SNEAKY STATE CHANGES:** Do not modify the system state (files, folders, env vars) during the "Planning" or "Thinking" phase. All side effects must be explicit tool calls after a plan is agreed upon.
4.  **CHECK FIRST:** Before running `write_file` or `run_shell_command` on sensitive files or for installations, refer to these rules.
