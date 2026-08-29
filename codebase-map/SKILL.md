---
name: codebase-map
description: >
  Build and maintain a living orientation map of a repository so the agent does
  not re-scan the whole tree every session, plus optional evidence-based diagrams
  for humans. Two parts: orient — write/update docs/architecture/ (and a short
  AGENTS.md pointer) with entry points, layers, modules, “where to look for X”,
  dependencies; diagram — emit neat .drawio and/or Mermaid from the map or from
  code evidence only. Use when onboarding to a repo, starting a multi-file task,
  asking “where does X live”, architecture overview, or “draw the system”.
  Triggers: codebase map, repo map, architecture map, AGENTS.md, where is,
  draw.io, architecture diagram, orient the agent.
version: 1.0.0
last_updated: 2026-08-29
---

# Codebase Map

One skill, two parts. Goal: **persistent orientation** for the agent + **clear diagram** for the human, without token bloat.

| Part | File | Invoke for |
|---|---|---|
| `orient` | `references/01-orient.md` | Scan repo; write/update living map under `docs/architecture/` + short AGENTS.md pointer |
| `diagram` | `references/02-diagram.md` | Produce evidence-based `.drawio` and/or Mermaid from the map or code |

## How to invoke

- New or unknown repo / “where is auth” / multi-file task → `orient` first (or both in order).
- User wants a visual → `diagram` (prefer existing map if present).
- Do not dump the whole map into every reply. Point to files; load only the relevant section.

## Token discipline

- Map files live on disk; agent reads the index + one section, not the entire tree.
- Diagrams are artifacts the user opens; do not paste huge XML into chat unless asked.
- Prefer updating an existing map over full regeneration.
