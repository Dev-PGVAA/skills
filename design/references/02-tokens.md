# Tokens — reusable roles

Inspect and reuse the existing system first. Introduce tokens only where reuse or theme consistency justifies them; a small isolated artifact does not need an enterprise token architecture.

- **Type:** map actual roles (caption, label, body, title, display) to existing or a compact new scale. A ratio can guide a new scale; optical adjustments and fluid sizing may be appropriate. An illustrative web subset is 12, 14, 16, 20, 24, 32, 40, 48px—not a pure geometric sequence.
- **Spacing:** a 4/8px base and values such as 2, 4, 8, 12, 16, 24, 32, 48, 64, 96 are useful starting points. Relational spacing should explain grouping; do not ban optical corrections or existing values.
- **Color:** semantic roles such as background, surface, text, border, accent, danger, and focus make themes maintainable. A neutral ramp and restrained accents often suffice. Data visualization, brand palettes, and accessibility can require more hues; 60/30/10 is a composition heuristic, not a measured gate.
- **Shape/elevation:** use a small coherent set by component purpose. Borders and shadows may work together where they communicate boundaries and elevation. Avoid decoration that hides hierarchy.

Check final contrast, theme variants, and component states. Dark mode needs deliberate token choices rather than mechanical inversion; pure black and system colors may be correct for the platform or brand.

More detail: [Color](deep/05-color.md), [Spacing](deep/04-layout-grid-spacing.md), and [Component roles](deep/06-ui-design.md).
