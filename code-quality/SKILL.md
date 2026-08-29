---
name: code-quality
description: Discipline for writing and reviewing code, in two invokable parts. Guidelines — behavioral rules against common LLM coding mistakes (state assumptions, ask when unclear, minimum code that solves the problem, no speculative abstractions, surgical changes that touch only what the task requires, verifiable success criteria with a plan-check loop). Review — read-only defect-first review of a specific change (uncommitted diff, base-branch diff, or a commit) that returns every actionable finding as P0–P3 entries the author would actually fix, plus overall assessment and test gaps; flags only real, demonstrable, change-introduced issues. Invoke a part by name. Triggers include code review, PR review, review my diff, refactoring discipline, write code carefully.
---

# Code Quality — write carefully, review honestly

Two parts, one concern: code that a senior engineer would trust. Load the part that matches the task.

## Parts

| Part | File | Invoke for |
|---|---|---|
| `guidelines` | `references/01-guidelines.md` | While writing, refactoring, or editing code — keep changes surgical and simple |
| `review` | `references/02-review.md` | Defect-first review of a change — uncommitted work, base-branch diff, or a commit |

## How to invoke

- User names a part (or asks for a review of the change) → load that part's file and follow it exactly.
- Writing code with no review requested → still apply `guidelines` silently.
- Review findings use the `review` part's format only — `[P1] title — path:line` plus a short paragraph; `No findings.` is a valid result.

House rule both parts share: never invent results, never claim a check ran unless it did, every changed line traces to the task.
