# Part 10 — Review (bounded verify loop + acceptance)

Part of design. Works standalone. Verify in bounded passes, not an endless polish loop.

Full pass/fail checklist: `references/deep/08-design-review-checklist.md`.

## Gate 0 — direction and slop (fail = not done)

Run this before craft. A single fail stops the review; go back to `01-direction.md` / `07-anti-slop.md`.

- [ ] Direction pass exists (mode, anti-references, signature, bold move)
- [ ] Signature is visible on the first screen
- [ ] The first screen could not be reused for a different product by swapping the logo
- [ ] No unjustified item from the 2026 ban list in `07-anti-slop.md`
- [ ] Copy would not survive transfer to another product unchanged
- [ ] Tokens exist and the UI consumes them (no raw one-off hex/px at point of use)

## Pass 1 — inspect (batched)

- Blur/squint the screenshot: reading order intact? one focal point?
- Walk the hard-rule checklist: every size on scale? every spacing from scale? stray 13/15/17/22px values? ≤2 families? measure ≤75ch? body ≥16px?
- Contrast: compute worst pairs (secondary text on surface, text over images/scrim, disabled).
- Responsive: 320 / 768 / 1440 representative checks; no horizontal overflow.
- Keyboard tab-through; reduced-motion emulation; grayscale screenshot.
- Stack: if the project uses Tailwind/shadcn, new components reuse existing tokens and primitives.

## Pass 2 — fix everything found in ONE batch, re-verify once. Stop.

A second full round only if pass 2 surfaced new blockers. Open-ended self-QA burns money and makes things worse.

Self-critique during build: take one accessory off before shipping (Chanel). Report honestly what passed and what was deliberately excepted.

## Acceptance criteria

Done means ALL of:

1. Direction is product-specific (couldn't be pasted onto another product)
2. One signature element, everything else disciplined
3. Tokens defined and consumed (type/spacing/color/radius)
4. Typography, hierarchy, spacing pass every hard rule
5. All component states designed
6. Targets and contrast gates pass
7. Motion purposeful, within part 6 bounds (feedback <300ms, overlays ≤500ms)
8. Copy specific; no banned marketing words without a claim
9. Responsive to 320px
10. Accessibility gates green
11. Anti-slop inventory empty or fully excepted
12. Verified in bounded passes with fixes batched

If any box is unchecked, the artifact is not done. Do not call it "almost".
