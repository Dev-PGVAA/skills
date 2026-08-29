# Part 9 — Accessibility (blocker gates)

Part of design. Works standalone. Failing any of these blocks shipping, regardless of how good it looks.

Full gates and verification: `references/deep/07-accessibility.md`.

1. Contrast on final rendered background: ≥4.5:1 body text; ≥3:1 large text (≥24px / ≥19px bold), icons, input borders, focus rings. Critical text (prices, legal) aims for 7:1 (AAA — target, not a blocker).
2. Typography in rem; layout survives 200% zoom and 320px reflow; text-spacing overrides don't break containers.
3. Keyboard: every control reachable, logical order, focus ALWAYS visible (≥2px, ≥3:1; never `outline: none` without replacement); Escape closes overlays.
4. Color never the only carrier of state/category/series — pair with icon, label, position, or pattern; survives grayscale.
5. Inputs have persistent visible labels (placeholder ≠ label); errors are text + color + icon adjacent to the field.
6. `prefers-reduced-motion` respected; no >3Hz flashing; auto-moving content pausable.

Quick verification: compute contrast on worst-case pairs (secondary text on tinted surface, text over image/scrim, disabled); tab through the whole flow; zoom to 200%; grayscale screenshot; emulate reduced motion.

## WCAG 2.2 additions (must-check at AA)

- 2.4.11 Focus Not Obscured (Minimum): focused control not entirely hidden by sticky/fixed UI
- 2.5.7 Dragging Movements: single-pointer alternative when drag is used
- 2.5.8 Target Size (Minimum): >=24x24 CSS px or adequate spacing
- 3.2.6 Consistent Help: help mechanisms in consistent location
- 3.3.7 Redundant Entry: do not re-ask data already provided in the flow
- 3.3.8 Accessible Authentication (Minimum): no cognitive tests; allow paste/passkeys/managers
