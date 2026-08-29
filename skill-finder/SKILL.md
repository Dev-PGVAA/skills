---
name: skill-finder
description: >
  Lightweight skill dispatcher and inventory. Answers "what skills do I have",
  "which skill should I use", routes a task to the right skill or skill part,
  and resolves conflicts between overlapping skills. Also consult this map when
  starting a substantial multi-step task and unsure which skill fits, or when
  two skills seem to match. Unlike forced pre-response scanning, this adds zero
  overhead to simple replies.
---

# Skill Finder

Two jobs: tell the user what their library contains, and pick the right skill
for a task. Keep it cheap — this is a map, not a ritual.

## When to consult this map

- The user asks what skills exist or which skill to use.
- A substantial multi-step task starts and the right skill is unclear.
- Two or more skills seem to match the same request.

Do NOT force a lookup before every reply. Simple questions, one-liners and
trivial edits skip this entirely — that overhead is exactly what this skill
replaces.

## Routing map

Snapshot of the library (August 2026, Komplekt — 14 skills).
Big multi-part skills expose invokable parts — route to the part when the task is narrow.

**Design and sites**
- any design work: direction, typography, grids, color, anti-AI-slop,
  UI components, motion, accessibility, review → `design`
  (parts: direction, tokens, typography, layout, components, motion,
  anti-slop, copy, a11y, review + deep layer with tables)

**Ideas and product** → `product`
- idea validation, BUILD/PIVOT/DROP verdict, contrarian/red-team, MVP → part `evaluate`
- plan with phases and kill criteria → part `plan`
- spec → tickets → implement one ticket → part `spec-to-code`
- long tasks via task_plan/findings/progress → part `file-planning`

**Research and reports**
- deep research with evidence levels A–E + contrarian search → `deep-research`
- long report 30+ pages → `research-report`
- compress long text/transcript → `summary`
- “kill the idea / why this is wrong / devil’s advocate” → `product/evaluate` (contrarian), plus `deep-research` when external facts matter

**Writing and learning**
- humanize prose / UI microcopy → `humanizer`
- teach a topic, learning plan → `teach`
- Russian language norms, EGE, orthography → `russian-master`

**Code**
- coding discipline, surgical edits → `code-quality` (part `guidelines`)
- review a diff/commit → `code-quality` (part `review`)
- current library docs (ctx7) → `context7-cli`

**Security** → `security`
- audit AI agents/LLM/RAG/MCP, threat modeling → part `audit`
- encrypt secrets SOPS+age+1Password → part `secrets`

**Knowledge base / notes** → `graph-surgeon`
- suggest links while writing a note → part `link-weaver`
- orphans, black holes, duplicates, top-20 links → part `graph-surgeon`

**Meta**
- create and iterate skills → plugin `skill-creator` (installed from plugins)
- navigate the library → `skill-finder` (this skill)

**Pipelines** (useful chains):

```
product: evaluate (+contrarian) → plan → spec-to-code
research: deep-research (falsify) → research-report
security: audit → secrets
design:   direction → tokens → … → anti-slop → review
notes:    link-weaver (while writing) | graph-surgeon (vault audit)
```

## Fresh inventory scan

The map above is a snapshot. For a live list, run:

```bash
for d in ~/.agents/skills/*/ ~/.zcode/skills/*/ ~/.codex/skills/*/; do
  n=$(basename "$d")
  [ -f "$d/SKILL.md" ] || continue
  desc=$(awk '
    /^description:/ {
      line = $0
      sub(/^description:[ \t]*/, "", line)
      style = line; gsub(/[ \t]/, "", style)
      if (style ~ /^[>|]([-+])?$/) {
        buf = ""
        while ((getline nxt > 0) && (nxt ~ /^[ \t]/)) {
          sub(/^[ \t]+/, "", nxt); buf = buf (buf ? " " : "") nxt
        }
        print buf
      } else {
        sub(/^[>|][-+]?[ \t]*/, "", line)
        print line
      }
      exit
    }' "$d/SKILL.md")
  echo "- $n: $desc"
done | sort -u
```

Present results grouped by category from the map above, marking skills not
in the snapshot as `new`. Big skills exist in several stores as real copies
(no symlinks) — count each skill once by name.

## Conflict resolution

When several skills match one request:

1. **More specific wins**: `research-report` beats `deep-research` for a
   30-page report; `deep-research` beats `summary` when a decision depends
   on evidence. A named part beats loading the whole multi-part skill.
2. **Stage-appropriate wins**: idea → `product/evaluate`; plan →
   `product/plan`; build → `product/spec-to-code`; visual →
   `design`; code review → `code-quality/review`.
3. **User-built beats generic** where both fit equally.
4. If still ambiguous and the choice materially changes the outcome —
   name the two candidates in one line and let the user pick.
   Otherwise just pick and announce: “Using [skill] for [goal].”

## Answer formats

**“What skills do I have?”** → grouped list by category (from map or fresh
scan), one line per skill: name — when to use (with parts for multi-part skills).

**“How do I do X?”** → the single best skill (or skill part) plus one
alternative, e.g.:

```
Use product, part evaluate (verdict + MVP).
Alternative: deep-research if you need market facts before deciding.
```

**Ambiguous task start** → silently pick per conflict rules, announce the
choice in one line, proceed. Do not list the whole library unprompted.
