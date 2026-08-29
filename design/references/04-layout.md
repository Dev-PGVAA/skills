# Part 4 — Layout (hierarchy, grid, alignment)

Part of design. Works standalone.

Deep layer: hierarchy cues — `references/deep/02-visual-hierarchy.md`; full grid/spacing tables — `references/deep/04-layout-grid-spacing.md`.

- One focal point and one primary action per view; if two things compete, demote one.
- Hierarchy uses ≥2 channels (size + weight, size + spacing); never color alone. Same semantic importance = same token; different treatment must mean different meaning.
- Real heading order h1→h2→h3, no skips, no levels used merely for size.
- Every element aligns to an axis or a sibling; one dominant alignment per composition. Edge alignment beats center for >3 elements.
- Group with whitespace first, background tint second, border third, shadow last — one mechanism per boundary, not stacked.
- Grid: 12 columns desktop (2–4 mobile, 8 tablet), consistent gutters; text containers capped ~65ch; forms 480–640px; app container 1200–1440px.
- Design down to 320px width: no horizontal scroll, explicit stacking order.
- Reading patterns: F for text-heavy, Z for sparse/visual — front-load headings and first sentences; identity top-left, action bottom-right.
- Blur test: the intended reading order must survive a blurred screenshot as blobs of weight.

Decision rules:

```text
IF two elements look almost identical but differ in purpose → make the difference explicit or make them identical.
IF grouping is done with boxes/borders → first try whitespace alone.
IF a layout feels cluttered → reduce competing type styles before removing content.
IF a layout feels cramped → increase whitespace; don't shrink type below floors.
IF every section is separated by the same gap → introduce 2–3 spacing levels.
IF two actions both look primary → demote one.
IF the blur test fails → increase differences (size/weight/space), don't add elements.
```
