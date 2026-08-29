# UI Design — Type Roles and Components

Practices from Material Design 3 (CC BY 4.0), IBM Carbon, Apple HIG. Reference numbers, not legal law — map them to your tokens.

## Table of contents
- Type roles (concept)
- Reference scales: Material 3 / Apple
- Assigning roles in a product
- Actions and buttons
- States
- Touch targets and hit areas
- Icons
- Radius, elevation, borders
- Platform conventions
- Decision rules

## Type roles (concept)

Never size text per component ad hoc. Define named **roles**, then every text slot uses a role:

```text
display   marketing hero numbers (rare, 1–2 per product)
headline  page/section titles
title     card headers, list group titles
body      reading text and control labels
label     buttons, chips, tabs, table headers, captions (often 500 weight)
```

Material 3 also fixes weight/tracking per role; Carbon splits **productive** (UI/data, 14px body, tight leading) vs **expressive** (reading/marketing, larger, looser) — adopt this split per surface.

## Reference scales

**Material 3 (px, size/line-height, weight):**

| Role | Size/LH | Weight |
|---|---|---|
| display large | 57/64 | 400 |
| display medium | 45/52 | 400 |
| display small | 36/44 | 400 |
| headline large | 32/40 | 400 |
| headline medium | 28/36 | 400 |
| headline small | 24/32 | 400 |
| title large | 22/28 | 400 |
| title medium | 16/24 | 500 |
| title small | 14/20 | 500 |
| body large | 16/24 | 400 |
| body medium | 14/20 | 400 |
| body small | 12/16 | 400 |
| label large | 14/20 | 500 |
| label medium | 12/16 | 500 |
| label small | 11/16 | 500 |

**Apple (iOS, pt):** Large Title 34, Title 1/2/3 = 28/22/20, Headline 17 semibold, Body 17, Callout 16, Subheadline 15, Footnote 13, Caption 12/11. (macOS body: 13.)

Typical web product subset (mirrors part 2's token roles): display 48, h1 40, h2 32, h3 24, title 20, body 16, body-sm 14, caption 12 — exactly one definition each.

## Assigning roles in a product

- Map every text slot to a role token before writing CSS: `title-medium`, `body-large`…; components consume tokens only.
- Reading surfaces (articles, onboarding text): body 16–18px, LH 1.5+ (expressive mode).
- Dense surfaces (tables, consoles, settings): body 13–14px, LH 1.4 (productive mode) — never below 12px.
- Buttons/labels: label role (14/500 or 12/500), sentence case, no all-caps except short system labels.
- Number-heavy UI: tabular numerics everywhere data aligns (see 03).

## Actions and buttons

- Per view: exactly one primary (filled/accent) action; secondary = tonal/outline; tertiary = text button. Emergency aside, never two filled buttons in the same region.
- Destructive actions: danger color on the button or its label, confirmation for irreversible ones; place destructive away from primary (not adjacent).
- Button label = verb + object ("Save changes"), ≤3 words; same action keeps the same label everywhere.
- Button height: comfortable 40–48px (touch), compact ≥32px (pointer-only, e.g., toolbars); horizontal padding scales with label.

## States

Design all states up front for every interactive component: default, hover, active/pressed, focus-visible, selected, disabled, loading, error. Missing states read as broken.

- Hover: subtle (bg lightness ±1 step or underline for links) — gate hover effects behind `@media (hover: hover)`.
- Disabled: reduced contrast (≥3:1 where feasible), no pointer events, keep informative.
- Focus: always visible, never `outline: none` without replacement (see 07).
- Selected/active nav item: ≥2 cues (weight + color, or filled indicator), not color alone.

## Touch targets and hit areas

- Minimum target: 44×44pt (Apple) / 48dp (Material); WCAG 2.2 floor 24×24px CSS.
- Visual may be smaller than target: expand hit area with padding/pseudo-element (links in prose, icon buttons).
- Gap between adjacent targets ≥8px to prevent mis-taps.

## Icons

- One icon family per product (same stroke weight, corner style, grid). Don't mix outline and filled sets.
- Sizes from scale: 16, 20, 24 (default), 32; align optically to text (cap-height centering).
- Icon-only controls require an accessible name (tooltip + aria-label).
- Icons support labels, they don't replace them in navigation and actions.

## Radius, elevation, borders

- Radius scale of 3–4 steps (e.g., 4 controls / 8 cards / 16 large surfaces / full pill for tags) — consistent per component class; not one radius everywhere, not arbitrary values.
- Elevation: 2–3 levels max (sticky header, dropdown, modal). Prefer surface tint or border over shadow (Carbon's flat approach); shadows soft and low-opacity on light themes.
- Never combine hairline border + large radius + big diffuse shadow on the same element — pick one separation mechanism (see 04).
- 1px borders at 1×, drawn inside (box-sizing), `hairline` only for deliberate delicate dividers.

## Platform conventions

| Context | Follow |
|---|---|
| Web app/site | Own token system; this skill's rules |
| iOS | HIG: San Francisco (system), Dynamic Type support, 44pt targets, native nav patterns |
| Android | Material 3: roles above, 48dp targets, ripple feedback |
| Desktop apps | Platform font/UI kit; denser spacing acceptable |

On native platforms, users expect native patterns — diverge only where the product's identity demands it and the divergence is consistent.

## Decision rules

```text
IF a component defines a font size directly
THEN replace with a type role token.

IF a screen has two filled buttons
THEN demote one to secondary/tertiary.

IF an interactive element has only :hover styling
THEN add focus-visible, active, disabled states.

IF an icon button is 24×24 visual
THEN expand the hit area to ≥44×44.

IF every card has a different radius
THEN fix a radius scale and map component classes to steps.

IF body text in a data table is 16px+ and wraps
THEN switch the surface to productive mode (13–14px, tabular figures) or restructure.

IF focus ring was removed for aesthetics
THEN restore a visible custom focus style (never ship invisible focus).
```
