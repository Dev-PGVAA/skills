# Part 1 — Direction (understand the product, build the visual world)

Part of design. Works standalone. Establishes everything BEFORE any code. **No layout, tokens, or components until this pass is written down.**

Deep layer: elements, principles, Gestalt — `references/deep/01-design-fundamentals.md`.

## Understand before designing

Establish (infer from context/code/assets if unstated, and state assumptions):

1. What the product is, who uses it, and the single primary action per surface.
2. Brand character: seriousness/playfulness, density, market clichés to avoid, existing fonts/colors/assets.
3. **Anti-references (required):** 2–3 looks this must NOT resemble. Name them. Typical defaults: "generic AI SaaS landing", "Linear clone", "Dribbble glass dashboard", "cream editorial template".
4. **Reference lock:** if the user pinned screenshots, fonts, or a live site, those win over your taste. Quote what is locked.
5. The surface's **mode** — it decides what "good" means:

| Mode | Surface | Success looks like |
|---|---|---|
| Persuade | Landing, marketing, pricing | Visitor decides and acts; design is the product |
| Operate | App UI, dashboards, settings | Task completion; scanability, consistency, native expectations outrank expression |
| Read | Docs, articles, changelogs | Comprehension; structure first, then a reading experience worth staying in |
| Experience | Portfolios, galleries | The artifact leads; the interface recedes |

## Signature gate (hard — before any code)

Write this block. If it is missing, stop and write it. Do not generate UI.

```
SURFACE MODE: persuade | operate | read | experience
ANTI-REFERENCES: …
LOCKED: (fonts / palette / components the brief pinned, or "none")
SIGNATURE (1–2): the thing this will be remembered by
  — must come from the subject's world (materials, tools, vernacular, data shape)
  — examples of valid signatures: a display face used only on one word; a numbering system that is real content; a material (newsprint, machined aluminum, warehouse stencil); one component treated as a character
BOLD MOVE: the single place taste is spent. Everywhere else is quiet.
VISUAL TENSION: what stops this from being average (contrast, density, asymmetry, crop, type size jump)
STACK: if the repo already has Tailwind / shadcn / CSS tokens — name them; new work consumes them
```

Rules for the signature:
- One or two. Not five.
- It is loud. The rest of the system is disciplined around it.
- It cannot be a gradient, a blob, or "a unique color palette". Those are not signatures.
- Structure must encode something true (numbering only if the content is a sequence).

## Build a visual world (before any code)

Plan in a compact written pass before building:

- **Palette**: 4–6 named hex values with roles (bg, surface, text, accent, +1). No gradients without a product reason. ≤5 hues. Accent ≤10% of the view.
- **Type**: 2–3 roles — a characterful display face used with restraint, a neutral body face, optionally a utility/mono face for data. Name the families. Do not pick from the anti-slop ban list unless locked.
- **Layout concept**: one sentence + ASCII wireframe of the hero/first screen. Not "three cards under a hero".
- **Signature + bold move**: copied from the gate above.
- **Spend boldness in one place**: signature loud, everything else quiet.

## Calibrate against AI defaults

Known AI-default clusters — refuse these unless the brief is literally that look:

- (a) cream `#F4F1EA` + high-contrast serif + terracotta accent
- (b) near-black + single acid-green/vermilion accent
- (c) broadsheet hairlines + zero radius + dense columns as a "editorial" costume
- plus the 2026 ban list in `07-anti-slop.md`

Any match must be a justified choice for THIS brief, not a reflex. Where the brief leaves an axis free, don't spend it on a default.

Confirm the plan is something you would not produce for any other similar product — then build exactly to plan, deriving every value from it. If you cannot tell this product from a competitor by squinting at the first screen, the direction has failed; rewrite the signature, do not start coding.
