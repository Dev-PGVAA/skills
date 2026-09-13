---
name: product
description: Evaluate product ideas, design validation experiments, plan delivery, or turn requirements into working software. Use the requested stage—evaluate, plan, spec-to-code, or file-planning—without forcing discovery or approval steps the task does not need.
---

# Product — Idea to working software

Enter at the stage the user actually requested. An evaluation is not authorization to build; an implementation request is not a request to restart market discovery. Preserve prior decisions, established architecture, approved scope, and explicit planning-before-implementation boundaries.

| Part | Reference | Use when |
|---|---|---|
| `evaluate` | [Evaluate](references/01-evaluate.md) | Assess demand, feasibility, economics, risks, variants, and experiments |
| `plan` | [Plan](references/02-plan.md) | Convert a chosen direction into milestones and evidence-based decisions |
| `spec-to-code` | [Spec to code](references/03-spec-to-code.md) | Resolve material requirements and implement the authorized scope |
| `file-planning` | [File planning](references/04-file-planning.md) | Persist decisions and progress for substantial work |

Read only relevant parts. Use the entire pipeline only when requested or genuinely necessary to deliver the authorized outcome. Small clear changes can go directly to code with brief acceptance criteria; long projects may use durable specs and tickets.

Quality bar: claims have evidence or explicit assumptions; commercial and noncommercial goals are evaluated on their own terms; experiments test the decisive uncertainty; implementation has observable acceptance evidence. Suggest stronger variants without silently replacing the user's product.

## Subagents

Use independent agents only when a stage has separable work and delegation is supported and permitted. The stage references define suitable roles. The parent assigns narrow questions or file ownership, provides constraints and required evidence, works on a useful complementary task, and integrates one result. Do not parallelize shared-file edits or dependent decisions. Default to no recursive delegation and use sequential specialist passes when tools or scope do not justify agents.
