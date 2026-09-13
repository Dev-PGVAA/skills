# Review — observable findings and verified fixes

Start from the brief, actual artifact, and scope. Read [Detailed checklist](deep/08-design-review-checklist.md) for a broader audit when useful. Inspect only relevant categories for a narrow change.

## Inspect

1. Compare the current artifact to the user request and prior version. Preserve locked identity, content, behavior, and scope; inspect a new design for fit to its intended task.
2. Walk the primary flow and meaningful empty/loading/error/success states. Use real or clearly labeled representative content, including long strings and realistic data density.
3. Inspect typography, hierarchy, spacing, clipping, alignment, and visual consistency at representative narrow, middle, and wide sizes or rendered pages. Diagnose consequences rather than counting off-scale pixels.
4. Measure relevant contrast pairs and inspect keyboard, focus, zoom/reflow, motion preferences, and accessible naming with available tools. Automated tests and static screenshots cover different things.
5. Check that new UI reuses existing primitives where appropriate and that apparent product proof matches implemented behavior. A successful build does not establish a working live flow.

## Findings and fix loop

Report reproducible issues with location, state/viewport, evidence, user consequence, and smallest useful fix. Separate requirement/functional/accessibility blockers from optional taste suggestions. Do not fail a review because a system font, card, or familiar CTA exists.

Batch independent fixes, rerun affected checks, and inspect the integrated result. Continue while actionable defects remain and useful verification is possible; stop when acceptance criteria pass or a concrete limitation prevents further proof. No arbitrary two-pass ceiling, endless aesthetic exploration, or mandatory removal of an accessory.

## Completion evidence

State what changed, which flows/states/sizes were observed, relevant automated results, and what could not be verified. Link screenshots/pages or describe reproducible evidence when helpful. A screenshot-only review may assess layout and visible contrast but cannot claim keyboard, screen-reader, motion, or live-provider success. Do not label a partial checklist "WCAG compliant."
