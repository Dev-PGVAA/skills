---
name: code-quality
description: Write focused, verifiable code changes or perform a defect-first review of a diff, commit, or pull request. Use for implementation discipline, refactoring, and code review; choose review mode only when requested.
---

# Code Quality

Make the requested behavior correct with a focused change; review defects using concrete evidence. Respect repository instructions, existing architecture, user edits, and the requested read/write scope.

## Select the mode

- **Implement / refactor:** read [guidelines](references/01-guidelines.md). Define observable acceptance criteria and use the repository's actual tooling.
- **Review:** read [review](references/02-review.md). Remain read-only unless fixes are also requested. Confirm the comparison before drawing conclusions.
- A small edit needs a small workflow. Do not create plans, abstractions, tests, or extra files solely to satisfy this skill.

## Useful delegation

Use available subagents for independent work that materially reduces uncertainty. Skip delegation when context transfer costs more than the task; use the same roles sequentially if agents are unavailable.

- **Implementation:** a contract scout reads callers, interfaces, and existing tests while the parent implements; a verifier exercises the changed behavior after a stable patch. Split implementation only across genuinely independent files, with one owner per file and the parent owning integration files.
- **Review:** partition by risk, such as authorization/data handling and state/concurrency, or disjoint modules. Give every reviewer the same base/head and required user behavior. The parent traces cross-module paths, checks each proposed finding, removes duplicates, and assigns final severity.
- A delegated task names the objective, allowed paths, read/write scope, assumptions, stop point, and evidence expected. Return changed files or `path:line` findings, an actual reproducer/test result, and unresolved questions. Do not recursively delegate without a useful bounded reason.

## Completion

Report behavior changed or actionable findings, checks actually run, and material limitations. “No findings” is valid; passing typecheck is not proof of runtime behavior or deployment.
