# Part 5 — Components and states

Part of design. Works standalone.

Deep layer: M3/Apple type scales, states, platforms — `references/deep/06-ui-design.md`.

- One filled primary button per region; secondary = tonal/outline; tertiary = text. Destructive actions colored, separated from primary, confirmed if irreversible.
- Button labels: verb + object, ≤3 words, sentence case, same action keeps the same label everywhere.
- Design ALL states up front: default, hover, active, focus-visible, selected, disabled, loading, error. Hover gated behind `@media (hover: hover)`.
- Targets ≥44×44px touch (Apple) / 48dp (Material); absolute floor 24×24; ≥8px between adjacent targets; expand hit areas for links/icon buttons.
- Icons: one family, one stroke weight, sizes 16/20/24/32; icon-only controls get names; icons support labels, never replace them in nav/actions.
- Selected/active state carries ≥2 cues (weight + color, or filled indicator).
- Native platforms (iOS/Android): follow platform conventions unless product identity demands a consistent divergence.
