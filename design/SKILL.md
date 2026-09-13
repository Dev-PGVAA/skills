---
name: design
description: Design, refine, or review visual interfaces and artifacts using product-specific hierarchy, typography, layout, components, copy, motion, and accessibility. Preserve the existing visual language unless redesign is requested; choose only the relevant design parts.
---

# Design

Make the artifact serve its users and subject. The user's brief, existing product behavior, brand, content, platform, and accessibility requirements take precedence over taste heuristics. Inspect the current artifact or relevant code/assets before making design claims.

Refinement preserves established identity and working flows. Redesign changes the dimensions the user actually requested; it does not automatically discard all existing choices. An operational tool may benefit from familiar patterns and neutral typography. Novelty is useful only when it supports the brief.

## Routing

Read only parts that affect this task. A narrow spacing fix does not require a direction manifesto or ten-stage workflow.

| Part | Reference | Use for |
|---|---|---|
| direction | [Direction](references/01-direction.md) | Product intent, surface mode, existing visual language, deliberate new direction |
| tokens | [Tokens](references/02-tokens.md) | Type, spacing, color, shape, and component roles |
| typography | [Typography](references/03-typography.md) | Fonts, glyph coverage, measure, size, leading, data |
| layout | [Layout](references/04-layout.md) | Hierarchy, grouping, grids, content order, responsive behavior |
| components | [Components](references/05-components.md) | Controls, relevant states, interaction and platform patterns |
| motion | [Motion](references/06-motion.md) | Feedback and state transitions with reduced-motion support |
| anti-slop | [Specificity review](references/07-anti-slop.md) | Generic visual/copy patterns that obscure the product |
| copy | [Copy](references/08-copy.md) | Labels, errors, empty states, marketing claims |
| a11y | [Accessibility](references/09-accessibility.md) | Applicable WCAG requirements and practical checks |
| review | [Review](references/10-review.md) | Evidence-based verification and prioritized findings |

The deep references linked from each part provide optional domain detail. Numerical design scales are starting points, not universal requirements or proof of accessibility. Applicable standards, user requirements, and actual usability decide blockers.

## Independent design agents

For a substantial artifact use bounded independent review or nonoverlapping implementation when useful and permitted:

- **Flow/content reviewer:** actual screens and user tasks; identify missing states, unclear actions, domain inaccuracies, and broken journeys.
- **Accessibility reviewer:** specific flow, rendered UI and relevant source; return reproducible barriers, applicable criterion, severity, and untested areas.
- **Visual reviewer:** current artifact, brief and prior version; assess hierarchy, typography, responsive behavior, and preservation of identity with screenshot/page evidence.

Provide the real brief, assets, scope, input states, allowed actions, output format, and effort limit; avoid priming reviewers with desired findings. The parent owns direction, shared tokens, final implementation, and synthesis. Only assign disjoint files for concurrent edits. Do not send multiple designers to redesign the whole product. No recursive delegation by default; use sequential reviews for small work or unavailable tools.

## Evidence and delivery

Render or run the actual artifact when possible, inspect relevant states and representative sizes, then verify fixes. Code inspection and screenshots alone do not prove keyboard behavior, assistive-technology support, or live integration. State what was observed, what was checked in source, and what remains unverified. Do not claim WCAG conformance from a partial checklist or automated scan.

Deep reference attributions are retained from the source kit. They are attribution notices, not a claim that current platform documentation or all license terms have been independently audited. Use official current standards when precise compliance or platform-version details matter.
