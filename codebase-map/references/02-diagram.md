# Part 2 — Diagram

Produce a **neat, evidence-based** diagram for humans. Prefer files on disk over chat dumps.

## Outputs (choose what the user needs)

- `docs/architecture/system.drawio` — primary human artifact (draw.io / diagrams.net)
- Optional: `docs/architecture/system.mmd` — Mermaid source for GitHub/docs
- Optional short caption in INDEX.md pointing to the files

## Method

1. Prefer an existing orient map; if missing, run a minimal orient pass first.
2. Nodes = real modules/services/packages from the map (labels = path or public name).
3. Edges = real imports, HTTP calls, queue links, or documented contracts — **no decorative arrows**.
4. Layout: left-to-right or top-down layers; group by layer/feature; avoid crossing edges when possible.
5. For `.drawio`: valid XML the user can open in diagrams.net; keep style restrained (few colors, clear labels).
6. For Mermaid: flowchart or C4-style; validate syntax mentally; keep under ~40 nodes unless asked for detail.

## Rules

- Evidence-based only: if a relationship is uncertain, omit or mark “inferred?” once — never invent topology.
- Dual audience: map files serve the agent; drawio/mermaid serve the human.
- Do not paste multi-thousand-line XML into the chat; write the file and report the path.
