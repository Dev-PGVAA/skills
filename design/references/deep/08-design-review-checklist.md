# Design review checklist

Use relevant rows for the actual artifact. Product requirements and applicable accessibility criteria can establish blockers; typography ratios, color counts, and grid choices are contextual craft heuristics. A partial review is not a conformance certificate.

## Task and content

- Does the artifact preserve the requested scope, locked identity, and real product behavior?
- Can the intended audience understand the subject, complete the primary task, and recover from expected failures?
- Are copy, data, screenshots, and proof real or clearly labeled examples?
- Are empty, loading, long-content, error, and success states covered where needed?

## Typography and hierarchy

- Are fonts readable at actual size, with required script/glyph coverage and reliable fallback?
- Are roles, heading semantics, emphasis, measure, and leading coherent?
- Can readers distinguish priorities without relying only on color?
- Are numeric columns, units, precision, and table labels easy to compare?
- Do text resizing, localization, and long labels preserve content and controls?

## Layout and visual consistency

- Do grouping, alignment, spacing, surfaces, and elevation explain relationships?
- Are components and semantic tokens reused appropriately without forced new architecture?
- Do representative narrow, intermediate, and wide layouts or rendered pages avoid unintended clipping and overlap?
- Are genuine two-dimensional views scrollable and understandable rather than compressed into unreadability?
- Do theme variants preserve hierarchy and meaning?

## Interaction and accessibility

Use [Accessibility reference](07-accessibility.md) for criterion scope and exceptions.

- Measure applicable text and non-text contrast against real composed backgrounds and states.
- Verify keyboard operation, visible/logical focus, unobscured focus, dialog behavior, and recovery after changes.
- Check semantic names/roles/states, labels and error association, relevant status announcements, and color independence.
- Check target size/spacing with actual exceptions, drag alternatives, motion controls, and reduced-motion behavior where applicable.
- Test text resizing, reflow, and spacing overrides separately.
- Record assistive-technology and live-integration checks only when actually performed.

## Findings format

For each actionable finding: location + observed state or reproduction + user consequence + requirement or rationale + smallest useful correction. Prioritize blocked tasks/data loss/access barriers before visual polish. Label suggestions separately; do not require a user to justify every familiar design pattern.

After fixing, rerun affected checks and inspect integration. Report passes narrowly, failures concretely, and untested areas honestly. Stop when acceptance criteria are satisfied or a real limitation prevents further verification.
