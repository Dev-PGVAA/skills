# Layout, Grid, Spacing

Adapted from OERT (CC BY-SA 2.5), IBM Carbon (spacing tokens, 2x grid), BCcampus (CC BY 4.0).

## Table of contents
- Spacing scale
- Spacing levels and grouping
- Grid
- Content widths
- Vertical rhythm and section spacing
- Density
- Alignment
- Decision rules

## Spacing scale

- Build all spacing (padding, margin, gap, inset) from one scale on a **4/8px base unit**. No arbitrary values (13px, 15px, 22px) — snap to the scale, then make deliberate optical exceptions only.
- Default scale (Carbon-derived; part 2's scale extended with 40, 80, 160 for dense tables and large-format surfaces): 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 128, 160.
- Tokenize: `space-1 … space-N`; reference tokens only, never raw px, in component code.
- This is a normalization rule, not a creativity rule: exact optical adjustments (icon nudges, caps compensation) are allowed but must be few and deliberate.

## Spacing levels and grouping

Define semantic levels, each strictly larger than the previous:

```text
within-component   4–12    (icon↔label, label↔field)
between-related    12–24   (field↔field, title↔body inside a card)
between-groups     24–48   (card↔card, list↔list)
between-sections   48–128+ (major regions of a page)
```

- Iron rule of proximity: **space inside a group is always smaller than space between groups**. If two cards are 24px apart, elements inside them sit ≤16px apart.
- Prefer whitespace separation → then background tint → then border → then shadow, in that order of cost. Don't use all four at once.

## Grid

- Web page layout: 12-column grid (2–4 columns on mobile, 8 on tablet, 12 on desktop), consistent gutters (16–24px), margins ≥ gutters on desktop.
- Base unit discipline: snap component dimensions and spacing to multiples of 4 (mobile 4/8, desktop 8). Carbon 2x grid: all layout on multiples of 8.
- Baseline rhythm (text): round line-heights to the base unit (e.g., 16px text ×1.5 = 24px line) so text blocks sit on the grid.
- Don't center-align entire page sections by default; choose per-section alignment with intent (see 02).
- Break the grid rarely and deliberately (full-bleed image, pulled quote) — one exception reads as design, many read as noise.

## Content widths

- Running text: 45–75ch (`max-width: 65ch`).
- App content container: 1200–1440px max; admin/data UI often 100% with max ~1600px.
- Single-column forms: 480–640px. Modals: 400/600/800px steps. Sidebars: 240–320px.
- Minimum layout viewport: design down to 320px width without horizontal scroll.

## Vertical rhythm and section spacing

- Use 2–3 distinct section spacings (e.g., 64 for tight, 96 medium, 128 airy) — not one uniform gap everywhere, and not a different value per section.
- Within a section, heading-to-content gap < section-to-section gap (proximity again).
- Consistent card padding per surface class (e.g., compact 16, default 24, spacious 32–48).

## Density

Choose density per surface, don't mix randomly:

- **Comfortable (reading/marketing):** 16px body, generous 24–48 gaps, roomy padding.
- **Compact (data-dense tools):** 13–14px body, 8–12 gaps, tight padding — accept smaller sizes only with full contrast and hit-area compensation.

## Alignment

- Every element aligns to at least one axis; each composition has one dominant axis.
- Align labels and values consistently in forms (top-aligned labels: fastest scanning; left-aligned labels in narrow forms; right-aligned only for short label sets in wide layouts).
- Text aligns to text; numbers align to numbers (right/decimal); icons optically center to cap-height/x-height, not to bounding box.
- Edge alignment beats center alignment for anything with more than 3 elements.

## Decision rules

```text
IF a spacing value is not in the scale
THEN snap it to the scale, or document it as a deliberate optical exception.

IF gap between groups ≤ gap inside groups
THEN increase between-group spacing (proximity is broken).

IF every section is separated by the same gap
THEN introduce 2–3 section-spacing levels matching importance.

IF a layout feels cramped
THEN increase whitespace and reduce competing elements — don't shrink type below floors.

IF two elements are separated by both border and background and shadow
THEN remove separators until one mechanism remains.

IF columns of a grid all collapse on mobile
THEN define explicit stacking order and full-bleed rules at 320–375px.

IF text lines run past ~75ch at desktop
THEN cap the text container, keep the grid for chrome.
```
