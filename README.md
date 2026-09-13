# Komplekt — revised skills for Codex

16 personal skills, revised from [Dev-PGVAA/skills](https://github.com/Dev-PGVAA/skills), source revision `8256d40f4fbe0242bea7599861d81e943105ee6e` (2026-09-12).

## What changed

Each skill has a focused entrypoint, concrete completion checks, selective references, and task-specific delegation guidance. Subagents are used for independent work when available and useful; the parent owns integration, source checking, and final output. Small tasks stay small. No model override, mandatory agent count, hidden background process, or invented tool is required.

The revision corrects incompatible planning hooks, duplicated planning resources, prompt/output drift, forced approvals and report padding, and identified domain and helper-script defects. The accompanying audit distinguishes structural checks, isolated execution tests, and behavioral examples from untested real-world use.

## Skills

| Skill | Purpose |
|---|---|
| code-quality | Focused code changes and evidence-based diff review |
| codebase-map | Repository orientation and verified architecture diagrams |
| context7-cli | Version-aware library documentation and explicit Context7 setup |
| deep-research | Traceable evidence, counter-evidence, and uncertainty |
| design | Visual direction, components, accessible UX, and visual QA |
| graph-surgeon | Scoped note-link analysis and precise repairs |
| humanizer | Natural writing with facts and voice preserved |
| planning-with-files | Isolated, resumable task state and handoffs |
| product | Evaluate, plan, specify, and implement at the requested stage |
| prompt-enhancer | Improve a prompt without silently executing it |
| research-report | Analytical reports at the requested depth and length |
| russian-master | Russian norms, exam tasks, and year-aware source checks |
| security | AI-system audit and scoped SOPS/age secret workflows |
| skill-finder | Current skill inventory and overlap resolution |
| summary | Faithful condensation with attribution and uncertainty |
| teach | Diagnosis, explanation, practice, feedback, and transfer |

## Local installation

Install the 16 directories containing a top-level `SKILL.md`, including their references, scripts, assets, and `agents/openai.yaml`, into one personal discovery root. Current official Codex documentation lists `~/.agents/skills/` for user skills. Older installations may also contain personal copies under `~/.codex/skills/`; inspect both and back up conflicting copies before replacement. Do not install the root `scripts/` or `tests/` as skills, and do not delete `.system` or plugin caches.

Codex does not merge same-name skills. Keep one active copy per personal skill rather than mirroring directories into both roots. Changes should become available on the next turn; restart Codex if its selector remains stale. See [official skill documentation](https://learn.chatgpt.com/docs/build-skills).

Invoke a skill as `$code-quality`, `$product`, `$teach`, or another listed name, followed by the task. Normal automatic selection remains enabled. `agents/openai.yaml` supplies UI metadata; subagent workflows live in the skill instructions and use the host's available delegation tools.

## Verification

Use Python 3 with PyYAML in an isolated environment for the bundle validator:

```text
python scripts/validate_bundle.py
python -m unittest discover -s tests -v
```

The validator checks metadata, linked local resources, and script syntax. Execution tests and behavioral evaluations are separate evidence. No global package installation or paid model API is needed for static validation. Security helper tests may need installed `sops` and `age`; check their individual test instructions and do not use production credentials.

The original planning shell/PowerShell hooks and active-plan/session-log recovery scripts were replaced with `planning-with-files/scripts/plan.py`. It uses an explicit task directory, preserves existing files, and checks recorded status only. No hooks or schedules are installed.
