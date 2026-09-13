# Recovery and handoff

Read the selected task's plan and the latest progress entry, then open only findings needed by the next decision. Confirm the workspace, branch when relevant, and any changed user constraints. Compare recorded work with the actual diff/artifact/service state. An earlier "tests passed" applies only to the tested revision and environment.

If several candidate plans exist, use the task ID or matching objective. If that cannot be determined, report the ambiguity instead of guessing by modification time. Existing root-level plans remain valid; pass their containing directory to the helper.

A useful handoff contains: objective; approved scope; current state; verified results and commands or artifact pointers; remaining checks; blockers; worker ownership; next action. Keep credentials, raw private logs, and unnecessary history out. Do not ask another agent to reconstruct facts from an unexplained conclusion.

The helper recognizes `### Phase ...` sections containing exactly one `- **Status:** value` (the leading dash is optional) and checks for unchecked Markdown task items inside those sections. It ignores fenced code examples. Other plan formats can be maintained manually. The old shell/PowerShell hooks, automatic session-log crawler, shared active-plan pointer, and hash-attestation workflow have been retired from this Codex-focused version; no background execution is implied.
