# Motion

Use motion to explain a state change, spatial relationship, progress, or feedback. Frequency, user control, and latency determine whether it helps. Keyboard interaction can have motion when it preserves focus and responsiveness; there is no universal prohibition.

Existing motion conventions win unless they cause a problem. As starting points, brief control feedback may take roughly 100–200ms and overlays 150–300ms. Easing should fit direction and continuity; avoid applying the same scale/opacity entrance to every component.

Prefer efficient properties such as transform and opacity, but choose the property needed by the effect and measure performance where material. Do not animate decoration merely to appear polished or delay essential actions until animation ends.

Respect reduced-motion preferences with a low-motion or static equivalent; do not assume opacity transitions are always harmless. Make applicable moving/auto-updating content pausable and avoid flashing. Precise WCAG applicability is in [Accessibility detail](deep/07-accessibility.md).

Verify interruption, rapid repeat actions, keyboard use, and reduced-motion behavior on the actual component. A static screenshot cannot establish motion quality or performance.
