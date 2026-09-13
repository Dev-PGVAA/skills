# Color reference

Attribution retained from the source kit: adapted from BCcampus (CC BY 4.0), Material/Carbon token practices, and WCAG guidance. Palette choices are contextual design heuristics.

## Palette and roles

Preserve an established brand and theme unless changes are requested. A neutral ramp, primary accent, and semantic roles often suffice for a new interface; complex charts or an expressive brand may need more colors. A 60/30/10 distribution can help composition but is not a measurable quality gate.

Use perceptual tools such as OKLCH when useful for building ramps, then check gamut, rendering, and contrast. HSL lightness is not perceptually uniform. Even perceptual lightness spacing does not guarantee accessible contrast.

A practical token structure separates primitives (color values), semantic roles (surface, text, accent, error, focus), and component roles when needed. Do not add layers solely for ceremony; reuse the existing system. State colors should be consistent with local conventions and labels, not a universal red/yellow/green mapping.

## Contrast and meaning

Measure actual composed backgrounds and relevant states. WCAG AA generally uses 4.5:1 normal text, 3:1 large text, and 3:1 for applicable non-text information; decorative and inactive content has exceptions. Enhanced AAA text contrast is 7:1 normal and 4.5:1 large. See [Accessibility](07-accessibility.md) for scope, large-text definition, and sources.

Do not use color as the only carrier of status, category, action, or sequence. Add meaningful text, shapes, patterns, or position as appropriate. Charts need clear labels and distinguishable series; palette size depends on task and encoding rather than a universal five-category maximum.

A grayscale screenshot can reveal weak luminance hierarchy; it cannot prove color-vision accessibility. Use simulations or task-based checks where valuable and retain non-color cues.

## Themes

Dark mode needs deliberate surface, text, accent, state, and elevation choices rather than mechanical inversion. Pure black, near-black, tinted surfaces, and shadows can all be appropriate for a particular platform. Test disabled, selected, hover, error, and focus states in every supported theme. Check system/forced-color behavior when relevant.

For text over images or gradients, inspect worst-case backgrounds and consider a scrim or solid region. Never trade readability for a preferred palette or conceal important information by making it tiny and low contrast.
