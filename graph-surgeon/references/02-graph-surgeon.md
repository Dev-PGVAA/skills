# Part 2 — Graph Surgeon (audit and repair an existing vault)

Part of graph-surgeon. Works standalone.

## Goal

Make the graph denser **where density helps navigation and retrieval**, not everywhere. Surgical edits: add/remove edges, flag merges, leave healthy structure alone.

## Inputs

Prefer, in order:

1. Machine-readable graph (Obsidian JSON canvas/export, CSV edges, `jq` over wikilinks, etc.)
2. Full file tree of notes + ability to grep `[[` / markdown links
3. User-pasted backlink report or plugin output

State which input you actually used. If the vault is huge, **scope** first (folder, tag, or date range) unless the user demands a full pass.

## Metrics to compute

| Signal | Definition | Typical action |
|---|---|---|
| Orphan | 0 in + 0 out | link to a hub, or archive/delete if junk |
| Dead-end (sink) | in > 0, out = 0 | add 1–3 outbound “next/see” links, or mark as terminal leaf on purpose |
| Black hole | high in, out = 0 | must gain structure (index sections + outbound) or stop attracting links |
| Island | small connected component | bridge to the main graph with 1–2 edges |
| Near-duplicate | high similarity, no or weak link | merge, split responsibilities, or explicit “vs” link |
| Over-linked hub | extreme degree, shallow content | split into index + children |

## Procedure

1. **Inventory** nodes and edges; report counts (notes, edges, orphans, sinks, components).
2. **List orphans** — prioritize those with substantial body text over empty stubs.
3. **List black holes / heavy sinks** — pages everyone points at that never route further.
4. **Near-duplicates** — pairs with similar titles or overlapping openings; recommend merge / rename / distinguish.
5. **Repair plan** — ranked actions, not a vague “add more links”.

## Default deliverable

```markdown
## Graph audit — [scope]

Stats: N notes, E edges, O orphans, S sinks, C components > 1 note

### Top orphans (link or drop)
1. [[…]] — why it matters / suggested neighbors

### Black holes & sinks
1. [[…]] — in:X out:0 — suggested outbound

### Near-duplicates
1. [[A]] ≈ [[B]] — merge / keep both because…

### Top-20 links to add now
| # | From | To | Why |
|---|---|---|---|
| 1 | [[…]] | [[…]] | … |

### Edges to remove or avoid
- [[…]] → [[…]] — reason (noise, wrong level, circular junk)

### Leave alone
- Short note on healthy hubs / intentional leaves
```

## Rules

- **Top-20** must be actionable in one sitting; prefer bridges that reduce islands over decorating hubs.
- Do not propose linking every note to a single MOC unless that MOC is maintained.
- Empty stubs: recommend delete or fill, not more inbound.
- If data is incomplete, output a **partial audit** and list what scan would unlock the rest.
- After edits, a second short pass may confirm orphans dropped — optional, only if user wants.

## Pairing

- Writing one note while auditing → run `link-weaver` on that note with surgeon’s candidate list as the index.
- Product research notes → after `deep-research`, surgeon can attach evidence notes into a claim map.
