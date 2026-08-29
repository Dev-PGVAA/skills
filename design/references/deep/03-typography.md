# Typography — Rules

Distilled from OERT (CC BY-SA 2.5), Google Fonts Knowledge, and Practical Typography (independent rules, no copied text).

## Table of contents
- Classifications and roles
- Choosing a text face
- Pairing families
- Type scale
- Size
- Line length
- Line height (leading)
- Letter spacing (tracking)
- Paragraphs
- Emphasis
- Numbers and data
- Medium-specific rules
- Decision rules

## Classifications and roles

Assign every family an explicit role before choosing it:

- **Serif** — long-form reading, editorial, tradition. Optional on screen; never required.
- **Sans-serif** — UI, wayfinding, dense information, modern default for interfaces.
- **Monospace** — code, data tables, IDs, terminal aesthetics. Third family, allowed only for these roles.
- **Display** — headlines only. Never set body text in a display face.
- **Script/handwriting** — decoration only (logotype, short accent), never body, never all-caps.

## Choosing a text face

- Prioritize readability over novelty in body text: regular/book weight, open apertures, distinguishable I/l/1 and O/0, generous x-height for small sizes.
- Test candidates at real size, in real content, on the real background — not in a specimen sheet.
- Check coverage before committing: language glyphs needed, italic (true italics, not slanted), tabular figures, weights 400/500/700 minimum, variable axes if used.
- Prefer families with many weights over pairing two decorative families.
- On the web, load 2–4 styles max (e.g., 400, 500, 700 of one family + 1 display); subset to used glyph ranges; `font-display: swap`.

## Pairing families

- Max 2 families (+ monospace for data). Justify every family out loud; default to one family with weight/size contrast.
- Pair by contrast of classification or era (serif display + sans body), not "two similar sans" — similarity reads as a mistake.
- Keep body families neutral; put personality in the display face and use it sparingly.
- A superfamily or variable font (one family, many axes) counts as one family and is the safe route.
- Match optical mood and x-height between paired families at the sizes they'll be used.

## Type scale

- Define a fixed scale of 5–7 named steps covering everything; every text style maps to one step. No off-scale sizes, ever.
- Build from a ratio on the body size: 1.125 (subtle), 1.2 (dense UI), 1.25 (default), 1.333 (editorial), 1.5 (dramatic, few steps only).
- Web example (1.25 on 16px): 12, 14, 16, 20, 25, 31, 39 → round to: 12, 14, 16, 20, 24, 32, 40.
- Steps must be distinguishable at a glance: adjacent steps ≥1.2× apart, or differ in weight too.
- Record the scale as tokens (`text-xs … text-3xl` or role names), reuse across screens/pages/media.

## Size

- Web body: 16–20px; never below 16px for reading text, absolute floor 12px for labels/captions.
- Print/PDF body: 9.5–12pt. Slides: body ≥18pt (24pt+ recommended), never below 14pt.
- UI dense/data contexts: 13–14px body acceptable (see 06-ui-design), captions 12px minimum.
- iOS reference: body 17pt, footnote 13, caption 12, large title 34. Desktop apps: body 13–14.

## Line length (measure)

- Body text: 45–75 characters per line, ~66 ideal. CSS: `max-width: 65ch`.
- Captions/sidebars: 35–50ch. Terminal-like data: 80–100ch acceptable.
- If lines are too long, shorten measure — never shrink font to fit the screen.

## Line height (leading)

- Web body: 1.4–1.6 (unitless values only). Print body: 1.2–1.35 (point leading ≈ 120–135%).
- Headings: tighter, 1.1–1.3. Display sizes: as low as 1.0–1.15.
- Rule of inverse relationship: longer measure ⇒ larger leading; bigger size ⇒ smaller relative leading.
- Small text (<14px) and all-caps: add leading (+0.2–0.3) to compensate.

## Letter spacing (tracking)

- Body text: 0 (normal). Never wide-track lowercase body text.
- Display sizes (≥32–40px): tighten slightly (−0.5% to −2%, e.g., `-0.02em`).
- All-caps labels ≤16px: open up (+0.05 to +0.1em, e.g., `0.08em`) — always with uppercase, never with mixed case.
- Never letter-space so tight that glyphs collide; kern only display headlines, not body.

## Paragraphs

- Separate paragraphs by either indentation (0.5–1em) or vertical space (0.75–1× line-height) — never both.
- Left-align body. Justify only with hyphenation (print/PDF); on the web, justify without hyphenation creates rivers — don't.
- No blank line + no indent + no spacing = unreadable wall; pick one separator and apply it consistently.
- Avoid widows and orphans: never leave a single word on the last line of a paragraph in display contexts (`text-wrap: balance` for headings, `white-space: nowrap` on a final short word pair); minimum 2 lines of a paragraph per column/page.
- One space after periods; no double spaces; no manual line breaks inside paragraphs.

## Emphasis

- Rank: bold (strongest inline) → italic → size change. Use one at a time; bold sparingly (≤1 phrase per paragraph).
- Underline = link on the web. Don't underline for emphasis in UI; in print, underline only as a deliberate stylistic device.
- No all-caps sentences; all-caps only for short labels (1–3 words) with tracking.
- Use true italic/bold fonts, never synthetic (faux) slanting/bolding — check the family ships the style.
- Don't color body text arbitrarily; accent color inline is for links or key figures only.

## Numbers and data

- Tables, prices, timers, IDs: tabular figures (`font-variant-numeric: tabular-nums`) so columns align.
- Running prose: proportional figures are fine; oldstyle figures blend with text (optional).
- Right-align numeric columns for comparison; align decimals when precision matters.
- Currency/units: consistent position and size; de-emphasize units (`14 USD` → `14 USD` with smaller unit).

## Medium-specific rules

**Web/UI:** sizes in `rem`/`px` tokens (not `em` chains); never disable text selection/zoom for reading content; system font stack as fallback; check rendered fallback metrics to avoid layout shift.

**Print/PDF:** pt units; hyphenation + justification allowed; ensure embedded fonts; black body text (100K or rich black per printer spec), never pure gray for small text.

**Slides:** min body 18pt; line length ≤50ch; scale up everything ~1.5× vs. document; one message per slide — typography follows.

## Decision rules

```text
IF unsure how many fonts → 1 family, weights 400/500/700.
IF two families look similar → replace with one family.
IF a size is needed between two scale steps → use the closer step; don't add steps.
IF text is unreadable at default size → fix measure/leading/contrast first, size last.
IF body line length exceeds ~75ch → narrow the container (max-width in ch).
IF leading feels loose in a big heading → reduce toward 1.1.
IF a paragraph block looks like a wall → add paragraph spacing or indentation, shorten paragraphs.
IF numbers misalign in a table → switch to tabular figures + right-align.
IF emphasis appears more than ~2× per screen → cut to the single most important.
```
