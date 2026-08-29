# Design Review Checklist

Run against any visual artifact (screenshot, page, PDF, slide, component). A gate either passes or the artifact fails it — no partial credit. Quote the violated rule when reporting.

Synthesized from this skill's deep layer (01–07); WCAG gates from deep/07 (W3C).

## How to run

1. Blur/squint the screenshot: does the intended reading order survive? (If not — hierarchy gate.)
2. Walk the sections below in order; fix violations with the matching reference file (03–07).
3. Re-check after fixing; stop when no **hard gate** fails. Improvement suggestions beyond gates are optional and labeled as such.

## Typography

- [ ] ≤2 font families (+ mono for data); every family has an assigned role.
- [ ] Every font size belongs to a defined scale of 5–7 steps (no one-off sizes).
- [ ] Body ≥16px web / 9.5–12pt print / ≥18pt slides; nothing below 12px.
- [ ] Body line-height 1.4–1.6; headings 1.1–1.3.
- [ ] Body line length 45–75ch (check widest paragraphs).
- [ ] Body left-aligned; justification only with hyphenation.
- [ ] Tracking: 0 on body; negative only on large display; positive only on short all-caps labels.
- [ ] Tables/data use tabular figures; numeric columns right-aligned.
- [ ] Underlines only for links (web); all-caps only ≤3-word labels.
- [ ] True italic/bold styles used (no faux).

## Hierarchy

- [ ] One focal point per view; one primary action per screen.
- [ ] Heading vs body differ in ≥2 channels (size+weight, size+spacing).
- [ ] Same semantic elements share the same type token (and vice versa).
- [ ] Heading order is real (h1→h2→h3, no skips, no levels used for sizing).
- [ ] Hierarchy never depends on color alone.
- [ ] Emphasis ≤2 marked phrases per screen of body text.

## Spacing and layout

- [ ] All spacing values come from one scale (4/8 base) — inventory and check for 13/15/17/22 strays.
- [ ] Inside-group spacing < between-group spacing everywhere (proximity).
- [ ] 2–3 section-spacing levels; not one uniform gap everywhere.
- [ ] Every element aligns to an axis or sibling; no free-floating offsets.
- [ ] Separation uses one mechanism (space OR tint OR border OR shadow), not stacked.
- [ ] Text containers capped ~65ch on wide screens.
- [ ] Layout survives 320px width without horizontal scroll.
- [ ] Radius and icon sizes each come from a small fixed scale.

## Color

- [ ] Palette = neutral ramp + 1 primary + ≤2 accents + semantic set; ≤5 hues.
- [ ] Colors exposed as semantic tokens; no raw hex at point of use.
- [ ] Contrast on rendered backgrounds: body 4.5:1, large 3:1, UI/icons 3:1.
- [ ] Status/category never color-only (icon, label, or position present).
- [ ] Grayscale test: hierarchy and states still distinguishable.
- [ ] Dark mode (if present) rebuilt, not inverted; accents adjusted; elevation via surface.

## UI components (for interfaces)

- [ ] One filled/primary button per view; secondaries clearly secondary.
- [ ] All interactive states designed: hover, focus-visible, active, disabled, (loading/error).
- [ ] Targets ≥44×44 (touch) / ≥24px absolute floor; ≥8px between adjacent targets.
- [ ] Focus indicator visible with ≥3:1 contrast.
- [ ] Icon-only buttons have accessible names; one icon family, sizes from scale.
- [ ] Destructive actions colored, separated, confirmed if irreversible.

## Accessibility gates (blockers)

- [ ] Contrast pairs measured, including secondary text on tinted surfaces.
- [ ] Text in rem, layout survives 200% zoom / larger root font.
- [ ] Keyboard pass: every control reachable, focus always visible, Escape closes overlays.
- [ ] `prefers-reduced-motion` respected; no >3Hz flashing.
- [ ] Inputs have persistent labels; errors are text + color + icon, adjacent to field.

## Craft polish (soft — report as suggestions)

- Widows/orphans in headings and pull quotes (balance or re-break lines).
- Consistent optical icon alignment (cap-height, not bounding box).
- Empty/loading/error states designed, not just the happy path.
- Copy: sentence case buttons, specific verbs, no placeholder lorem.

## Report format

```text
FAIL gates:   [section.rule] — what violates it, where, exact fix.
Warnings:     soft findings, clearly separated.
Passed:       one line, no elaboration.
```
