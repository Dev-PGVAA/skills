---
name: skill-finder
description: >
  Lightweight skill dispatcher and inventory. Answers "какие скиллы у меня
  есть", "what skills do I have", "чем это сделать", routes a task to the right
  skill or skill part, and resolves conflicts between overlapping skills. Also
  consult this map when starting a substantial multi-step task and unsure which
  skill fits, or when two skills seem to match. Unlike forced pre-response
  scanning, this adds zero overhead to simple replies.
---

# Skill Finder

Two jobs: tell the user what their library contains, and pick the right skill
for a task. Keep it cheap — this is a map, not a ritual.

## When to consult this map

- The user asks what skills exist or which skill to use.
- A substantial multi-step task starts and the right skill is unclear.
- Two or more skills seem to match the same request.

Do NOT force a lookup before every reply. Simple questions, one-liners and
trivial edits skip this entirely.

## Routing map (August 2026 — 15 skills)

**Дизайн и сайты**
- любой дизайн: направление, типографика, сетки, цвет, анти-AI-slop,
  UI-компоненты, моушн, доступность, ревью → `design`
  (части: direction, tokens, typography, layout, components, motion,
  anti-slop, copy, a11y, review + deep-слой с таблицами)

**Идеи и продукт** → `product`
- валидация идеи, вердикт BUILD/PIVOT/DROP, red-team, MVP → часть `evaluate`
- план с фазами и kill-критериями → часть `plan`
- спека → тикеты → реализация тикета → часть `spec-to-code`
- длинные задачи через task_plan/findings/progress → часть `file-planning`

**Ресёрч и отчёты**
- глубокий ресёрч с уровнями доказательств A–E + фальсификация → `deep-research`
- большой отчёт 30+ страниц → `research-report`
- сжатие длинного текста/транскрипта → `summary`

**Текст и обучение**
- «очеловечить» прозу / UI microcopy → `humanizer`
- обучить теме, учебный план → `teach`

**Код**
- дисциплина кодинга, хирургические правки → `code-quality` (часть `guidelines`)
- ревью диффа/коммита → `code-quality` (часть `review`)
- актуальная документация библиотек (ctx7) → `context7-cli`

**Безопасность** → `security`
- аудит AI-агентов/LLM/RAG/MCP, threat-model, OWASP 2026 / Agentic → часть `audit`
- шифрование секретов SOPS+age+1Password → часть `secrets`

**Ориентация в репо**
- карта модулей, entry points, where-is, AGENTS.md pointer, draw.io → `codebase-map`
  (части: orient, diagram)

**Мета**
- навигация по библиотеке → `skill-finder` (этот скилл)
- knowledge-base graph hygiene (Obsidian/Logseq) → `graph-surgeon`
- on-disk working memory → `planning-with-files`
- Russian language norms / EGE → `russian-master`

**Пайплайны**
```
product: evaluate → plan → spec-to-code
research: deep-research → research-report
security: audit → secrets
design: direction → tokens → … → anti-slop → review
```

## Fresh inventory scan

For a live list, run the shell snippet that scans `~/.agents/skills/*/SKILL.md`
(and equivalent locations) and prints name + description.

## Conflict resolution

1. **More specific wins**: `research-report` beats `deep-research` for a 30-page report; a named part beats the whole multi-part skill.
2. **Stage-appropriate wins**: idea → product/evaluate; plan → product/plan; visual → design; code review → code-quality/review.
3. **User-built beats generic** where both fit equally.
4. If still ambiguous and the choice materially changes the outcome — name the two candidates and let the user pick. Otherwise pick and announce: «Использую [skill] для [цель]».

## Answer formats

**«Какие скиллы у меня есть?»** → grouped list by category, one line per skill (with parts for multi-part skills).

**«Чем сделать X?»** → the single best skill (or part) plus one alternative.
