# Implementation guidelines

## Establish the local contract

Inspect status/diff, applicable repository instructions, manifests, relevant entrypoints, callers, and existing tests. Reuse the project's runtime and package manager. Identify the visible behavior, failure behavior, and compatibility constraints before editing. Clarify only a decision that changes the result and cannot be inferred safely.

Keep uncommitted user work intact. Do not revert, reformat, or remove unrelated code. When a requested change depends on a pre-existing failure, distinguish it from a regression introduced by the patch.

## Choose the smallest coherent change

- Reuse existing helpers and conventions when they fit. Add an abstraction when it removes real duplication or isolates a needed boundary; fewer lines alone is not the goal.
- Split modules by responsibilities and dependencies, not an arbitrary line count. Keep a cohesive algorithm together. Avoid wrapping a single expression in layers of forwarding functions.
- Preserve established dependency direction, server/client boundaries, and public interfaces. Do not impose a universal folder layout or architectural pattern.
- Handle errors at the boundary that can respond meaningfully. Preserve concrete causes; avoid swallowing failures, broad fallback-to-success, retry storms, and accidental secret logging.
- Use real APIs from installed versions or authoritative documentation. Verify flags before depending on them. Keep dependencies and feature flags tied to current requirements.
- Remove obsolete code caused by this change; leave independent cleanup outside the patch.

## Verify the behavior, not the implementation's shape

Prefer a failing behavioral regression test before fixing a bug. For new risky logic, use red → green → refactor where the harness makes that productive. Do not block a reversible copy/style change on new tests or create tests that merely repeat constants or private implementation details.

Select checks by the failure mode:

| Change | Useful evidence |
|---|---|
| Pure logic | Independent expected results; boundaries and invalid inputs |
| API/auth/data | Public contract, unauthorized cases, persistence, transaction rollback |
| Concurrent/async work | Duplicate requests, cancellation, ordering, retry idempotency |
| UI | User flow and relevant viewport/state; visual inspection when layout matters |
| Migration/config/build | Real migration/build or config parse in a disposable environment; recovery path where relevant |
| External integration | Mock proves local contract; provider response or user-visible result proves the live path |

Run focused checks first and required repository checks next. Broaden after a failure or uncovered risk. Do not run unrelated expensive suites merely to increase the count. Never run destructive tests against an unidentified database or stop a process without knowing its owner.

## Integrate and finish

Review the final diff for scope, accidental files, stale imports, changed contracts, and sensitive data. If workers edited disjoint files, inspect their diffs and run checks at shared boundaries; their summaries are not verification. Explain what changed, why it solves the problem, and what was actually checked. Report blocked or unavailable checks with the concrete reason.
