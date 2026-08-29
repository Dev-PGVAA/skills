# Part 6 — Motion (animation craft)

Part of design. Works standalone.

- Frequency test first: used 100×/day (command palettes, shortcuts) = no animation; tens/day = minimal; rare = may delight. Never animate keyboard-initiated actions.
- Every animation has a stated purpose (spatial, state, feedback, explanation) — "looks cool" is not one.
- Easing: entering = ease-out; moving on screen = ease-in-out; hover/color = ease; constant = linear. Durations: press 100–160ms, tooltips 125–200ms, dropdowns 150–250ms, modals 200–500ms; UI stays <300ms.
- Entrances start from scale 0.95 + opacity 0 — never scale(0). Press feedback scale 0.97.
- Animate transform/opacity only. Stagger 30–80ms max. Popovers scale from their trigger; modals stay centered.
- Respect `prefers-reduced-motion`; nothing flashes >3Hz.
