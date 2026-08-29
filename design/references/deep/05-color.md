# Color — Systems and Rules

Adapted from BCcampus (CC BY 4.0) with token practices from Material 3 / Carbon and WCAG gates.

## Table of contents
- Building a palette
- Palette proportions
- Semantic tokens
- Contrast gates
- Color and meaning
- Dark mode
- Color-blind safety
- Decision rules

## Building a palette

- Structure: **neutral ramp (8–10 lightness steps of one hue) + 1 primary + 1–2 accents + semantic set (success, warning, danger, info)**. Total distinct hues ≤4–5.
- Build ramps in a perceptual space (OKLCH/HSL lightness-ordered): keep hue nearly constant, step lightness evenly, cap chroma so large surfaces don't scream.
- Test: palette must work when reduced to grayscale — hierarchy must survive on lightness alone.
- Saturated colors on small elements (buttons, links, badges); desaturated/darker on large surfaces (backgrounds, headers).
- Brand color = primary. Accent ≠ second brand color; accent exists to spotlight one thing.

## Palette proportions

- Rough **60% neutral / 30% supporting / 10% accent** distribution per view.
- Accent appears in ≤1–2 element classes (primary buttons, links, active state, key data). If accent covers >10% of the view, it stops directing attention.

## Semantic tokens

Layer tokens; never hardcode hex at point of use:

```text
primitives   gray-900, blue-600 …        (the ramps)
semantic     bg, surface, text-primary, text-secondary, border,
             accent, accent-hover, success, warning, danger, focus
component    button-bg, card-border …     (reference semantic only)
```

- One token per meaning, not per value: `text-secondary` may be gray-600 in light theme and gray-300 in dark.
- Interactive states derive from tokens (`accent-hover` = accent shifted 1 lightness step, consistent direction across the palette).
- Don't adopt a default framework palette (Tailwind colors) as brand identity without a deliberate choice.

## Contrast gates (WCAG, on the final rendered background)

| Content | Minimum ratio |
|---|---|
| Body text <24px (<19px bold) | 4.5:1 |
| Large text ≥24px (≥19px bold) | 3:1 |
| Icons, input borders, charts, UI graphics | 3:1 |
| Disabled text | exempt, but keep ≥3:1 where feasible |
| AAA / small critical text (legal, prices) | 7:1 |

- Check the actual stack: text on tinted surface on colored card — compute against the composed background, not the token value.
- Don't fix contrast by making secondary text tiny and gray — de-emphasize by one notch only (e.g., gray-600 on white), never below 4.5:1.

## Color and meaning

- Color is a redundant channel: every color-coded state also carries text or icon (danger = red **and** icon/label).
- Consistent color semantics across the whole product: red=danger/destructive, yellow/amber=warning, green=success, blue=info — don't repurpose these hues decoratively near data.
- Max 5–7 distinguishable categories in charts; beyond that, group or use direct labeling.

## Dark mode

- Don't invert — rebuild: dark surfaces desaturated (chroma ↓), text off-white (white = 100% glare), accents lightened (often +1–2 L steps) to keep 4.5:1.
- Elevation in dark themes is shown by **lighter surfaces**, not shadows; each elevation level = one surface token.
- Avoid saturated colors on dark backgrounds at body-text sizes — they vibrate; reserve for large elements.
- Pure black (#000) only for OLED-saving deliberate cases; default near-black (e.g., #111–#17181A).

## Color-blind safety

- ~8% of men have red-green color vision deficiency. Red/green pairs (danger/success) must differ in lightness or carry icons/labels.
- Never encode order or category by hue alone (green→yellow→red dashboards fail); add position, labels, or lightness ordering.
- Verify: grayscale test + a color-blindness simulator pass for anything data-bearing.

## Decision rules

```text
IF more than ~5 hues are in use
THEN cut to neutral ramp + primary + accents; delete decorative hues.

IF an accent color appears on most components
THEN it is decoration, not accent — reduce to primary actions.

IF hierarchy disappears in grayscale
THEN rebuild it on lightness/size/weight before adding more color.

IF a status is communicated by color only
THEN add an icon, label or position cue.

IF dark mode is just inverted light theme
THEN redo tokens: desaturated surfaces, lightened accents, elevation-by-surface.

IF text sits on image/gradient
THEN add a scrim or solid panel and re-measure contrast at worst-case pixels.
```
