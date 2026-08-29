---
name: product
description: One skill for the full path from raw idea to working code, in four invokable parts. Evaluate — validate any business or product idea (problem, demand, market, economics, tech feasibility, moat, distribution) and get a verdict BUILD / TEST FIRST / REWORK / PIVOT / DROP plus aggressive contrarian/red-team, a stronger version, MVP and experiment plan. Plan — turn a validated idea into executable action with milestones, success metrics, kill criteria and build-measure-decide loops, no fake productivity. Spec-to-code — disciplined pipeline interview → SPEC.md → small dependency-aware tickets in TICKETS.md → safe implementation of one ticket at a time. File-planning — run long multi-step tasks through task_plan / findings / progress files (Manus-style working memory on disk). Invoke a part by name or run the whole pipeline. Triggers include idea validation, should I build this, MVP, roadmap, action plan, spec, requirements, tickets, implement a feature.
---

# Product — Idea → Plan → Spec → Code

One skill, four parts. Each part lives in `references/`, is self-contained, and matches one stage of taking an idea to shipped code. The output of one stage feeds the next, but every part works alone.

## Parts

| Part | File | Invoke for |
|---|---|---|
| `evaluate` | `references/01-evaluate.md` | Validate an idea, run contrarian/red-team, get a verdict and MVP/experiments |
| `plan` | `references/02-plan.md` | Action plan, roadmap, milestones with metrics and kill criteria |
| `spec-to-code` | `references/03-spec-to-code.md` | Interview → SPEC.md → tickets → implement one ticket |
| `file-planning` | `references/04-file-planning.md` | Organize a long multi-step task through plan/findings/progress files |

## How to invoke

- User names a part → load ONLY that part's file and apply it.
- Idea without a plan → run parts in order 01 → 02 → 03; `file-planning` is optional scaffolding for long sessions (its full templates and scripts live in `references/planning-with-files/`).
- Natural entry points: an idea → `evaluate`; a BUILD verdict → `spec-to-code` stage 2; a ready spec → `spec-to-code` stage 3.

Quality bar inherited by every part: no invented facts, confidence levels on conclusions, cheapest test first, smallest viable scope.
