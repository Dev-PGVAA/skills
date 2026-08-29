# Part 3 — Typography (hard rules)

Part of design. Works standalone.

Deep layer: classifications, pairing, full rules by medium — `references/deep/03-typography.md`.

- ≤2 font families (+ monospace for code/data only). Default to one family with weight/size contrast.
- Body: web ≥16px (dense data UI 13–14px, floor 12px), print 9.5–12pt, slides ≥18pt.
- Line-height: body 1.4–1.6 unitless; headings 1.1–1.3; display down to 1.0–1.15.
- Measure: 45–75 chars per line (`max-width ~65ch`); never fix overlong lines by shrinking type.
- Tracking: 0 on body; slightly negative on display ≥32px; +0.05–0.1em only on short all-caps labels.
- Left-align body; justify only with hyphenation (print/PDF). Center only short display text.
- Paragraphs: indent OR vertical space, never both; no walls of text; widows/orphans controlled in display text.
- Emphasis: bold/italic one at a time, ≤2 marked phrases per view; underline = link (web); no all-caps sentences; true italic/bold styles only (no faux).
- Numbers in tables/prices/timers: tabular figures, right-aligned columns.
- Web: sizes in rem; load 2–4 styles, subset, `font-display: swap`; check fallback metrics.

Decision rules:

```text
IF unsure how many fonts → 1 family, weights 400/500/700.
IF a size is needed between two scale steps → use the closer step; don't add steps.
IF body line length exceeds ~75ch → narrow the container (max-width in ch).
IF text is unreadable → fix measure/leading/contrast first, size last.
IF numbers misalign in a table → tabular figures + right-align.
IF emphasis appears more than ~2× per screen → cut to the single most important.
```
