# UI type roles and component reference

Attribution retained from the source kit: Material Design 3 (CC BY 4.0), IBM Carbon, and Apple HIG practices. These reference scales are examples, not current-version guarantees or universal size requirements. Check current official platform guidance when exact values matter.

## Roles and platform examples

Map actual text slots to meaningful roles such as display, headline, title, body, and label. Reuse the existing system. Reading, dense operational, native, and presentation surfaces have different needs; dynamic text and actual legibility matter more than matching a copied table.

**Material 3 illustrative type scale (size/line-height, weight; map to the target platform units):**

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

Typical web product subset (mirrors part 2's token roles): display 48, h1 40, h2 32, h3 24, title 20, body 16, body-sm 14, caption 12 — adapt the subset to actual roles.

## Actions and states

Establish priority within each decision region; separate panels can have different primary actions. Destructive treatment, undo, or confirmation should match the consequence. Preserve authorized workflows instead of adding redundant prompts.

Use clear, consistent labels without an arbitrary word limit. Design relevant default, focus, hover, pressed, selected, disabled, loading, empty, success, and error states. Not every component needs every state. Prefer native semantics and platform patterns.

Disabled behavior depends on the element: native disabled controls and aria-disabled custom controls require different handling. Do not disable pointer events indiscriminately or lose keyboard explanations. Preserve input on errors and make asynchronous updates understandable without stealing focus.

## Targets and icons

Apple points, Android dp, and web CSS pixels are different units. Platform guidance commonly favors generous touch targets; web WCAG 2.2 AA includes a 24 CSS px sizing rule with exceptions. There is no universal eight-pixel gap requirement. Use [Accessibility reference](07-accessibility.md) for precise applicability.

Icon-only controls need accessible names; tooltips alone are insufficient. Visible labels help unfamiliar actions, while familiar compact controls can work with reliable naming and affordance. Keep icon style coherent, allowing outlined/filled variants when they convey state.

## Shape, elevation, and platform fit

Reuse shape and elevation roles. A few radius/shadow levels often suffice, but border plus shadow is legitimate when boundary and elevation both matter. Optical alignment can differ from geometric alignment.

Native interfaces should respect platform navigation, typography, focus, and scaling expectations. Web interfaces can reuse a framework or product system. Do not turn a neutral operational UI into an expressive landing page solely for novelty.

## Verify

Inspect actual strings, hit areas, keyboard operation, focus, state changes, responsive layout, and relevant assistive-technology output. Source inspection, a screenshot, and a successful component build establish different evidence; report them separately.
