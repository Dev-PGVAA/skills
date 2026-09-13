# Accessibility reference — common web checks

Based on W3C WCAG 2.2 and its Understanding documents. This is a selected implementation checklist, not a substitute for the full standard or a conformance audit. Applicability, exceptions, supported environments, and evidence matter. Official pages below were consulted on 2026-09-12; verify the relevant criterion for formal or version-sensitive work.

## Contrast

- Under 1.4.3 (AA), normal text generally needs 4.5:1 and large text 3:1. Large means at least 18pt (24 CSS px), or 14pt bold (about 18.67 CSS px). Incidental/inactive text and logos have exceptions.
- Under 1.4.11 (AA), required visual information identifying active UI components/states and meaningful graphics generally needs 3:1 against adjacent colors. This is not a rule that every decorative border or icon must have that ratio. Inactive controls and certain unmodified native appearances are excepted.
- 1.4.6 (AAA) raises text contrast to 7:1 normal and 4.5:1 large. Choosing stronger contrast for critical information is useful, but "legal text" does not create a separate AA 7:1 requirement.

Measure the actual composed background, including images, tints, gradients, overlays, hover/selected states, and focus. Do not round a failing ratio upward. Source: [Non-text contrast](https://www.w3.org/WAI/WCAG22/Understanding/non-text-contrast.html), [Text contrast](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html).

## Text resizing, reflow, and spacing

These are separate checks:

- 1.4.4 (AA): text can resize to 200% without loss of content or functionality, with specified exceptions.
- 1.4.10 (AA): vertically scrolling content works at a width equivalent to 320 CSS px without requiring two-dimensional scrolling. For horizontal writing/scrolling cases the criterion includes a 256 CSS px equivalent height. Content requiring two dimensions, such as some tables and maps, is excepted; keep scrolling scoped and usable.
- 1.4.12 (AA): applicable markup content tolerates text-spacing overrides—line height 1.5 times font size, paragraph spacing twice font size, letter spacing 0.12em, word spacing 0.16em—without loss. These are test overrides, not mandatory default typography.

Relative units, flexible text boxes, and avoiding disabled zoom help implementation; a unit choice alone proves nothing. Test 200% text/zoom and a narrow or 400%-zoom equivalent reflow case separately. Source: [Reflow](https://www.w3.org/WAI/WCAG22/Understanding/reflow.html).

## Keyboard and focus

Verify keyboard access, operation, logical sequence, absence of traps, visible focus, and predictable transitions. Modal focus containment can be intentional when users can close the dialog and return to a sensible location. Escape behavior should match the widget pattern; it is not a universal rule for every overlay.

2.4.7 (AA) requires visible focus. 2.4.11 (AA) requires that focused components are not entirely obscured by author-created content. 2.4.13 Focus Appearance is **AAA** and specifies enhanced indicator area and contrast with exceptions. A strong two-pixel outline is a useful design technique, not a universal AA geometry requirement.

Check native versus custom focus behavior, sticky UI, scroll containers, dialogs, skip links, and restoration after deletion or async changes. Source: [Focus appearance](https://www.w3.org/WAI/WCAG22/Understanding/focus-appearance.html).

## Pointer targets and alternatives

2.5.8 (AA) generally requires a target to contain a 24×24 CSS px square. Exceptions cover spacing, equivalent controls, inline targets, unmodified user-agent controls, and essential presentation. For undersized targets, its spacing exception evaluates 24px-diameter circles centered on target bounding boxes against other targets/circles; there is no universal eight-pixel gap rule.

44pt Apple and 48dp Material targets are platform design guidance in different units. Larger web targets often improve usability, but do not substitute platform numbers for the actual WCAG rule. Check pointer cancellation, accessible alternatives to dragging (2.5.7), and complex gestures when relevant. Source: [Target size minimum](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html).

## Meaning, forms, and status

- Color alone must not carry information; pair state and chart categories with text, icon, pattern, shape, or another suitable cue.
- Native semantic controls are preferable where suitable. Verify name, role, value, and state for custom widgets; icon-only controls need accessible names and a tooltip alone is insufficient.
- Inputs need appropriate labels or instructions. Placeholders are often inadequate because they disappear; bind labels programmatically and preserve visible context.
- Identify errors in text, connect them to fields, offer a correction when known, and preserve valid input. An extra icon is optional, not universally mandatory.
- Announce relevant status messages without stealing focus. Evaluate screen-reader output for critical dynamic flows when tools permit.
- Check redundant entry (3.3.7), consistent help (3.2.6), and accessible authentication (3.3.8) where applicable. Authentication cognitive-test rules have conditions and exceptions; supporting password managers and paste is useful but not the whole criterion.

## Motion and flashing

Honor user motion preferences and provide a static or low-motion equivalent when needed. WCAG 2.3.3 (AAA) specifically addresses interaction-triggered motion animation; reduced-motion CSS support alone does not establish conformance with all motion criteria.

2.2.2 (A) governs qualifying moving, blinking, scrolling, and auto-updating content, with controls and exceptions. 2.3.1 (A) permits either no more than three flashes per second or flashes below specified general/red-flash thresholds. Avoid flashing; do not claim safety from frequency alone when content needs formal analysis.

## Practical evidence record

For each relevant check record the flow/state, browser or renderer, viewport/zoom, method, observation, and result: pass, fail, not applicable with reason, or untested. A contrast calculator checks color pairs; an automated scan catches some structural issues; a screenshot shows visible layout; a keyboard pass shows keyboard behavior. None alone establishes full accessibility.

Use [WCAG 2.2](https://www.w3.org/TR/WCAG22/) and its current Understanding documents to resolve precise questions. Avoid treating a local checklist or heuristic as the normative standard.
