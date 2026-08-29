---
name: code-quality
description: >
  Discipline for writing minimal, correct, clean code and reviewing changes, in two
  invokable parts. Guidelines — surgical edits, prefer less code that works and reads
  well, TDD when behaviour is new, ~120 lines soft limit per file with documented
  exceptions, reject 2026 LLM anti-patterns (speculative abstractions, hallucinated
  APIs, dead code). Review — defect-first P0–P3 findings on a diff or commit, blast
  radius, test gaps, security-relevant issues. Invoke a part by name. Triggers include
  code review, PR review, write code carefully, TDD, refactor, clean code, меньше кода,
  ревью, проверь изменения.
version: 1.1.0
last_updated: 2026-08-29
---

# Code Quality — write carefully, review honestly

Two parts, one concern: code a senior engineer would trust, without surplus.

| Part | File | Invoke for |
|---|---|---|
| `guidelines` | `references/01-guidelines.md` | While writing or editing — minimal, working, clean |
| `review` | `references/02-review.md` | Defect-first review of a change / PR-style |

## How to invoke

- User names a part or asks for review → load that part.
- Writing code with no review asked → still apply `guidelines` silently.
- Review findings use `[P1] title — path:line` format; `No findings.` is valid.
