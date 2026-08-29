# Part 7 — Anti-slop (2026 ban list + de-slop)

Part of design. Works standalone. This is a **hard gate**, not a mood. A suspect ships only with a product-specific reason written in the direction pass. Swapping one template cliché for another is still slop.

Calibrate overall direction against the three AI look clusters in `01-direction.md`. Copy rules live in `08-copy.md`. After this pass, re-run `10-review.md`.

## Hard rule

If a pattern below appears and the direction pass did **not** justify it for THIS product, replace it. "It looks modern" is not a reason. "The brand uses Inter" is.

## Visual slop — ban by default (2026)

**Type**
- Inter, Roboto, Open Sans, Lato, Montserrat, Poppins, Arial as the only face
- Geist / Space Grotesk / Instrument Serif / Playfair Display chosen with no product reason
- System-ui stack with no characterful display face and no reason for neutrality
- Gradient text on headlines
- All-caps tracked kickers + italic serif hero as a "taste" shortcut

**Color / surface**
- Unmotivated purple, indigo, violet, or cyan as the primary
- Purple-to-blue or cyan-to-purple button/hero gradients
- Radial glow blobs behind the hero
- Glassmorphism as decoration (frosted cards with no content reason)
- Neon-cyberpunk dark UI (acid green on near-black) as a default "tech" look
- Cream `#F4F1EA` + terracotta as automatic "premium"
- Rainbow mesh / aurora backgrounds

**Layout**
- Giant full-sentence hero + eyebrow pill + two CTAs
- Identical 3-column feature cards with icon-above-heading
- Icon-tile above every section heading
- Card-inside-card; "cardocalypse" (every block is a rounded card)
- Everything center-aligned for a whole page
- Same radius on buttons, cards, inputs, images, and the viewport
- Thick colored left-borders on every card
- Hairline border + huge diffuse shadow on the same element
- Identical gaps between all sections (no grouping rhythm)
- Fake browser / fake dashboard screenshot with blur and no real product
- Marquees of logos as a substitute for proof
- Scroll-reveal on every section; pulsing dots; fake terminal cursors
- Meaningless `hover:scale()` on cards
- Decorative SVG blobs / undraw-style illustrations
- Emoji used as icons or section markers

**Motion**
- Entrance animation on every block
- Bounce/elastic on UI chrome
- Auto-playing looping Lottie with no job
- Parallax on body copy

## Copy slop — ban by default

These words and shapes fail the specificity test (the sentence would survive transfer to another product):

seamless, elevate, unlock, empower, supercharge, reimagine, next-level, cutting-edge, world-class, enterprise-grade, vibrant, groundbreaking, harness, leverage, delve, foster, tapestry, landscape, journey, unlock your potential, everything you need in one place, the future of X, a new era of, built for the modern Y

Also:
- Generic benefit sentences with no number, name, or mechanism
- Placeholder claims ("trusted by teams worldwide")
- Three parallel "Fast. Simple. Powerful." stacks
- CTA "Get started" / "Learn more" with no object

## De-slop pass (do this in order)

1. Inventory every suspect on the current surface. List them. Do not skip "small" ones.
2. For each: **real problem** / **deliberate exception**. An exception must cite a product reason from the direction pass (brand font, existing system, a reference the user pinned).
3. Replace reflexes with product-specific choices: a face that belongs to the subject's world, a layout that encodes the actual content shape, a signature that could not be pasted onto a competitor.
4. Re-run `10-review.md`. If any unjustified suspect remains, the review fails.

## Exception format

```
EXCEPTION: Inter as body
REASON: incumbent brand guidelines, file brand/type.md, locked 2024
```

No reason → no exception.

## What "fixed" looks like

The page could not be reused for a different product by swapping the logo and the headline. One signature is loud. Everything else is quiet and on tokens.
