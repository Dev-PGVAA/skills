# Accessibility — Hard Gates

WCAG 2.1/2.2 (W3C) AA numbers relevant to visual design. These are gates, not advice: an artifact is not "done" while any fails.

## Table of contents
- Contrast
- Text and sizing
- Focus and keyboard
- Color independence
- Targets and spacing
- Motion
- Forms and states
- Reading-friendly typography
- Quick verification

## Contrast

| Element | Minimum |
|---|---|
| Body/normal text | 4.5:1 |
| Large text (≥24px, or ≥19px bold) | 3:1 |
| Icons, focus indicators, input borders | 3:1 |
| Critical small text (prices, legal, medical) | 7:1 (AAA) |

Measure against the final composed background (cards, images, gradients included).

## Text and sizing

- Size typography in `rem` (root-relative) so user font-size settings scale it. Avoid fixed `px` for fonts; never use `px` in `line-height` (unitless only).
- Support 200% browser zoom and 320px width without horizontal scrolling (reflow, WCAG 1.4.10).
- No text inside images (except logos). If unavoidable, provide equivalent real text.
- Respect text-spacing overrides: layouts must survive increased line-height (1.5×), letter/word spacing (WCAG 1.4.12) — use flexible containers, no fixed-height text boxes.
- Never disable pinch zoom (`user-scalable=no`) on reading content.

## Focus and keyboard

- Every interactive element reachable and operable by keyboard, in logical order.
- Focus indicator always visible: ≥2px, ≥3:1 contrast against adjacent colors, ≥2px offset or clear outline replacement (e.g., inner ring). Never `outline: none` without a substitute.
- No keyboard traps; modals trap focus intentionally and restore it on close; `Escape` closes overlays.
- Skip-to-content link on pages with repeated navigation.

## Color independence

- Color is never the only signal for state, category, required fields, errors, or chart series (WCAG 1.4.1) — pair with icon, text, pattern, position, or underline for links.
- Distinguish states also when viewed in grayscale and by color-blind users (see 05).

## Targets and spacing

- Minimum pointer target 24×24 CSS px (WCAG 2.2 AA); recommended 44×44 (Apple) / 48dp (Android).
- Adjacent targets ≥8px apart; inline link lists add spacing so targets don't overlap.

## Motion

- Respect `prefers-reduced-motion: reduce`: remove movement/parallax/auto-carousels; keep opacity/color transitions.
- Nothing flashes more than 3 times/second (WCAG 2.3.1).
- Auto-playing/moving content >5s needs pause/stop/hide (2.2.2).

## Forms and states

- Every input has a persistent visible label (placeholder is not a label).
- Errors: text message (what happened + how to fix) + color + icon; errors appear adjacent to the field; don't clear user input on error.
- Required fields marked by more than color/asterisk convention alone (label or "(required)").
- Disabled controls: visually distinct, ≥3:1 where feasible, plus tooltip/legend explaining why.

## Reading-friendly typography

- Body line-height ≥1.4 in dense UI and ≥1.5 on reading surfaces (part 3 range 1.4–1.6). Layout must tolerate user text-spacing overrides (WCAG 1.4.12): line-height 1.5×, paragraph spacing 2× font size, letter-spacing 0.12em, word-spacing 0.16em.
- Left-align (LTR) long text; no justified text without hyphenation (rivers harm dyslexic readers).
- Avoid all-italic or all-caps long passages; underline links inside text so they're findable without color vision.
- Content in plain language; abbreviations expanded on first use.

## Quick verification

- Compute contrast with a checker (or formula) on worst-case pairs: secondary text on surface, text over scrim, disabled labels.
- Tab through the whole flow — focus visible and ordered everywhere?
- Zoom to 200% / set root font to 18–20px — does layout survive?
- Grayscale screenshot — is every state/series still distinguishable?
- `prefers-reduced-motion` emulation — does anything essential depend on motion?

## Decision rules

```text
IF contrast can't reach 4.5:1 at current size
THEN darken text or enlarge (≥24px = 3:1 allowed) — never lighten to "look nicer".

IF focus is invisible on a dark or busy background
THEN use a double ring / offset outline with its own contrast.

IF an error state is red border only
THEN add icon + message text adjacent to the field.

IF controls are 24px targets in a touch context
THEN enlarge to ≥44px hit areas.

IF animation is essential to understanding
THEN provide a static equivalent under reduced motion.
```
