# Part 2 — Tokens (the system before anything is built)

Part of design. Works standalone. Define tokens first; components consume tokens only, never raw values.

Exact tables: color ramps and semantic tokens — `references/deep/05-color.md`; extended spacing values (40, 80, 160) — `references/deep/04-layout-grid-spacing.md`.

## Type scale

5–8 fixed steps from one ratio (1.2 dense, 1.25 default, 1.333 editorial). Example web scale on 16px: `12, 14, 16, 20, 24, 32, 40, 48` mapped to roles `caption, label, body, title, h3, h2, h1, display`. Adjacent steps ≥1.2× apart or differ in weight too. No one-off sizes ever.

## Spacing scale

4/8px base: `2, 4, 8, 12, 16, 24, 32, 48, 64, 96, 128` with semantic levels, each strictly larger than the last:

```text
within-component 4–12   <   between-related 12–24   <   between-groups 24–48   <   between-sections 48–128
```

Iron rule: space inside a group is always smaller than space between groups. Use 2–3 section-spacing levels, not one uniform gap everywhere.

## Color tokens

Layered: primitives (ramps) → semantic (`bg, surface, text-primary, text-secondary, border, accent, accent-hover, success, warning, danger, focus`) → component. Ramps built in OKLCH: neutral ramp (8–10 steps, one hue) + 1 primary + ≤2 accents + semantic set; ≤5 hues total; accent covers ≤10% of any view (60/30/10).

Dark mode is rebuilt, not inverted: desaturated surfaces, lightened accents, elevation via lighter surfaces.

## Shape and elevation

Radius scale 3–4 steps (e.g., 4 controls / 8 cards / 16 surfaces / pill); shadows ≤3 levels, prefer border/surface-tint over shadow; never stack border + big radius + diffuse shadow on one element.
