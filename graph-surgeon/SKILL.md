---
name: graph-surgeon
description: >
  Knowledge-base graph hygiene and live link suggestions for notes (Obsidian,
  Logseq, Markdown wikilinks, Zettelkasten). Two invokable parts: link-weaver —
  while writing or editing a note, propose concrete inbound/outbound links in
  real time; graph-surgeon — audit an existing vault for orphans, black holes,
  near-duplicates, and a prioritized “link these 20 now” list. Triggers include
  graph, vault, wikilinks, orphans, link suggestions, knowledge base, Obsidian.
---

# Graph Surgeon — links that earn their keep

One skill, two parts. Both treat a knowledge base as a **directed graph of notes**, not a folder of files.

| Part | File | Invoke for |
|---|---|---|
| `link-weaver` | `references/01-link-weaver.md` | While writing/editing one note — live link proposals |
| `graph-surgeon` | `references/02-graph-surgeon.md` | Audit the whole (or scoped) vault — orphans, hubs, duplicates, repair plan |

## How to invoke

- User is drafting or revising a single note → `link-weaver`.
- User asks to clean the graph, find orphans, densify links, find duplicates → `graph-surgeon`.

## Shared model

- **Node** = a note (page, card).
- **Edge** = explicit link (wikilink `[[…]]`, markdown link, block ref) — not “same folder” and not tag-only unless the user says tags count as edges.
- **Orphan** = no inbound *and* no outbound (or only self-links).
- **Dead-end** = has inbound, zero outbound (sink / black hole if many inbounds).
- **Hub** = high inbound; useful only if it also routes outward or is a true index.
- **Near-duplicate** = high title/embedding/overlap similarity with weak or no link between the pair.

Never invent links to notes that do not exist unless the user asks to create stubs. Prefer **specific anchors** (why this link) over dumping 30 related titles.

Quality bar: every proposed edge must state **why a future reader benefits**. Cosmetic densification is a defect.
