# Komplekt (compact improved)

**15 agent skills.** No bloat. Progressive disclosure keeps token cost near the previous set.

All instructional text is **English** (better model following), except `russian-master` (RU by design).

## Install

Copy each skill folder into `~/.agents/skills/<name>/` (Claude Code, Codex, Cursor, OpenCode, Grok, …).

## Contents

| Skill | Role |
|---|---|
| design | Full visual stack, 10 parts + deep layer (anti-slop 2026, WCAG 2.2, design-to-code) |
| product | Idea → plan → spec → code |
| deep-research | Evidence A–E + falsification + pre-research contract |
| research-report | 30+ page report with provenance gate |
| summary | Compress long text |
| humanizer | Natural prose and UI microcopy |
| teach | Learning plan |
| code-quality | Minimal clean code + TDD bias + defect-first / PR-oriented review |
| context7-cli | Current library docs |
| security | Agent audit (OWASP LLM 2026 + ASI01–ASI10 checklists) + secrets |
| planning-with-files | On-disk working memory (tie to product / research) |
| russian-master | Russian norms and EGE |
| skill-finder | Library routing |
| graph-surgeon | Note graph hygiene |
| **codebase-map** | Living repo orientation + evidence-based draw.io/Mermaid |

## Pipelines

```
product:     evaluate → plan → spec-to-code
research:    deep-research → research-report
security:    audit → secrets
design:      direction → tokens → … → anti-slop → a11y → review
code:        codebase-map/orient → code-quality (guidelines | review) → tests
orientation: codebase-map/orient  (then diagram if human needs visual)
```

## Token discipline

- Skills load **only when triggered**; SKILL.md stays short; details live in `references/`.
- `codebase-map` writes disk files — agent reads INDEX + one section, not the whole repo every turn.
- Do not install overlapping third-party “mega packs”; this set is intentionally closed.

## MCP / freshness notes (not separate skills)

- **NotebookLM / Gemini Notebook MCP** (if you already run it): use as grounded project memory — sources + cited answers. Pair with `deep-research` for open-web facts and NotebookLM for *your* docs/RFCs.
- Prefer live search for pricing, APIs, laws, CVE, model cards (same as deep-research recency rules). Other models benefit when you force tool use + dated sources the same way.

## Changelog focus (this build)

- security: ASI01–ASI10 + Excessive Agency checklists
- research-report: provenance gate + A–E linkage
- code-quality: less-code / ~120 LOC soft limit / TDD / LLM anti-patterns / PR blast-radius
- design: distributional convergence anti-slop, WCAG 2.2, design-to-code note
- **new** codebase-map (orient + diagram) — replaces the need for several architecture-only skills
