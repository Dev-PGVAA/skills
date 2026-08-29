# Visual Hierarchy

Adapted from OERT (CC BY-SA 2.5) and BCcampus (CC BY 4.0).

## Table of contents
- What hierarchy is
- Hierarchy cues, by strength
- Rules of hierarchy
- Scanning patterns
- Decision rules

## What hierarchy is

Hierarchy is the **intended order of consumption**: what the viewer sees first, second, third. It is created only by perceptible differences between elements. If a design "feels flat" or "busy", hierarchy is missing or ambiguous — fix hierarchy before adding decoration.

Define at most three ranks per view: primary (the one thing), secondary (what's next), tertiary (everything else, deliberately quiet).

## Hierarchy cues, by strength

Combine at least two channels for the primary level; one channel for lower levels:

1. **Size** — strongest, most expensive in space.
2. **Weight** — cheap and precise (regular → medium → bold).
3. **Position** — top-left of the composition (LTR reading) gets first attention.
4. **Color/contrast** — accent color on neutral surroundings; high contrast = importance.
5. **Whitespace isolation** — empty space around an element raises it.
6. **Imagery** — faces and pictures outrank text; use knowingly.

## Rules of hierarchy

- One focal point per view. One primary action per screen; if two actions compete, demote one (secondary button style or reorder).
- Same semantic importance ⇒ same visual treatment (same type token, same color). Different treatment must mean different meaning.
- Hierarchy levels must be unmistakable: heading vs. body must differ in ≥2 channels (size + weight, size + spacing).
- Never create hierarchy by tricking the reader (low-contrast "thin gray on white" text); de-emphasize, don't hide.
- Heading levels encode document structure (h1 → h2 → h3, no skips); visual style follows semantics, not the reverse.
- In long text, hierarchy = consistent heading rhythm + paragraph spacing + emphasis inside paragraphs used sparingly (bold ≤1 phrase per paragraph).
- In UI, hierarchy = component weight: primary button (filled) > secondary (outline/tonal) > tertiary (text). Never two filled buttons side by side in one region.

## Scanning patterns

- Text-heavy pages: F-pattern — first lines of paragraphs and headings get read, body middles get skipped. Front-load headings and first sentences with meaning.
- Sparse/visual layouts: Z-pattern — eye travels top-left → top-right → bottom-left → bottom-right. Put identity top-left, action bottom-right.
- Cards/grids: scan in rows or columns consistently; never mix both orders in one grid.
- Test: blur the screenshot (or squint) — you should still perceive the intended order of importance as blobs.

## Decision rules

```text
IF the interface contains more than 3 heading levels
THEN define an explicit type scale and map each level to a token.

IF two text elements have the same semantic importance
THEN they share the same typography token (and vice versa).

IF hierarchy relies only on color
THEN add size, weight, spacing or another non-color cue.

IF a layout feels cluttered
THEN reduce competing type styles before adding decoration.

IF two actions both look primary
THEN demote one to secondary/tertiary styling.

IF everything is emphasized
THEN nothing is — pick the single element to keep loud.

IF the blur test doesn't show the intended reading order
THEN increase differences (size/weight/space), don't add new elements.
```
