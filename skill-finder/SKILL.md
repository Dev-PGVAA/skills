---
name: skill-finder
description: List available skills, choose the best skill or mode for a task, and resolve overlapping skill triggers. Use for inventory and routing questions or genuine selection ambiguity; not a mandatory preflight for ordinary work.
---

# Skill finder

Use the current session's available-skills catalog as the authority for callable skills and exact paths. The map below describes this bundle, not a guarantee that every item is installed. For a fresh filesystem audit inspect the configured personal, repository, system, and plugin locations relevant to the user; distinguish discovered files from skills actually exposed in the session. Do not scan unrelated repositories or claim an unsupported precedence rule for duplicates.

## Bundle map

| Requested outcome | Primary skill / mode |
|---|---|
| Visual direction, UI, typography, accessibility, visual review | design / relevant part |
| Validate a product idea | product / evaluate |
| Plan an already chosen product | product / plan |
| Specification or authorized implementation | product / spec-to-code |
| External evidence, comparison, fact checking | deep-research |
| Substantial analytical report | research-report |
| Faithful condensation of supplied material | summary |
| More natural prose preserving facts and voice | humanizer |
| Rewrite/debug a prompt as the deliverable | prompt-enhancer |
| Learn or practice a subject | teach |
| Russian language norms or exam tasks | russian-master |
| Code changes and implementation discipline | code-quality / guidelines |
| Read-only review of a diff/commit | code-quality / review |
| Repository orientation or architecture diagram | codebase-map / orient or diagram |
| Current library documentation through Context7 | context7-cli |
| AI-system security audit or SOPS/age secrets workflow | security / audit or secrets |
| Persistent state for long or parallel work | planning-with-files |
| Note-vault links and duplicate candidates | graph-surgeon |
| Skill inventory and routing | skill-finder |

## Resolve overlap

Prefer an explicitly named skill, then the requested deliverable and stage. Choose one primary skill; add a supporting skill only for a concrete capability. Summary uses supplied material; research answers questions requiring external evidence. Humanizer changes voice; Russian editing checks norms. Codebase-map covers source architecture; graph-surgeon covers note links. Planning-with-files tracks execution state and does not replace product planning.

Existing plugin skills may be a better match for actual Word/PDF/slides/spreadsheets/site work. Inspect their descriptions instead of overriding them with this bundle. For duplicate names compare exact source paths, versions, and content; report ambiguity without claiming the loader merges or prioritizes them. Install/remove actions require the user's requested scope, not a routing decision.

An illustrative pipeline is a possible combination, not authorization to advance stages. An audit does not automatically start secrets migration; research does not automatically become a long report. Respect explicit plan-only and review-only requests, and carry through implementation when already requested.

## Delegation and output

Routing itself is usually local. For a requested large library audit, workers may inspect disjoint sets and return paths, capabilities, trigger collisions, and evidence; the parent deduplicates and reports coverage. Never spawn one agent per available skill simply to choose one, and do not invent separate agent findings without tools.

For "what do I have", group current available skills by purpose and identify duplicates or availability limits. For "which one", state the best fit and why; mention an alternative only if materially useful. For an action request, select and proceed instead of stopping at a recommendation. Read just the chosen entrypoint and required references.
