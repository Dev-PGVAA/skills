# Typography reference

Attribution retained from the source kit: distilled from OERT (CC BY-SA 2.5), Google Fonts Knowledge, and Practical Typography. Treat sizes and ratios as examples, not a normative standard.

## Roles and selection

Assign families to actual roles: body, interface, display, code, or data. Serif can support editorial reading, sans can support interfaces, mono can align code and identifiers; none is mandatory for those domains. Script or decorative faces need careful readability checks outside short accents.

Preserve incumbent fonts unless changing them is in scope. Test candidates with real text at actual size and background. Check required scripts, I/l/1 and O/0 distinction where important, available weights/styles, italic behavior, numerals, and licensed files. A single family or superfamily can provide sufficient hierarchy; pair families only when the contrast serves a role.

## Scale and responsive sizing

A small set of semantic roles keeps interfaces coherent. A geometric ratio (for example 1.2 or 1.25) can guide a new scale; rounded role sizes and fluid interpolation are legitimate. An illustrative web subset is 12, 14, 16, 20, 24, 32, 40px. It is not an exact 1.25 progression, and not every product needs seven steps.

Use existing tokens first. Add or adjust a role when real content needs it rather than snapping every value to an arbitrary nearest step. Check responsive sizing with browser zoom and font preferences; a `clamp()` that caps growth can undermine text resizing.

## Starting ranges by medium

| Context | Starting point | Verify |
|---|---|---|
| Web reading | 16–20px body, around 1.4–1.6 leading | Actual typeface, script, measure, zoom |
| Dense UI | Often 13–14px, with stronger legibility and suitable targets | User task, platform convention, scaling |
| Print/PDF | Often 9.5–12pt body, 1.2–1.35 leading | Physical size, audience, font, printer/output |
| Slides | Often 24pt+ for body; 18pt only when viewing conditions allow | Viewing distance, export, projection |
| Native apps | Platform text roles and user scaling | Current platform and dynamic text support |

These are design starting points. WCAG does not set a universal minimum body font size; test actual accessibility requirements separately.

## Measure, leading, and spacing

For Latin/Cyrillic reading prose, around 45–75 characters per line is a useful starting range. Adapt for scripts, sidebars, data, and format. CSS `ch` is based on the zero glyph width and only approximates character count. Do not solve overflow by making text unreadable.

Longer measures and small text can need more leading; large headings often tolerate tighter leading. Avoid clipping ascenders, descenders, accents, and fallback glyphs. Unitless web line height usually scales well; print uses physical units.

Tracking depends on the font and script. Slightly tighter display Latin type or extra space in short all-caps labels can help, but do not apply mechanically to Arabic or other scripts. Preserve letter shapes and text semantics.

## Paragraphs and emphasis

Use coherent paragraph separation through space or indentation, adapted to the medium. Left-align LTR prose by default; respect RTL and script conventions. Justification needs appropriate hyphenation and visual inspection. Avoid fragile forced line breaks or nonbreaking spans that cause mobile overflow.

Bold and italic should identify meaning, not decorate every sentence. Underlined text is commonly recognized as a web link; avoid misleading decoration. True font styles improve fidelity, but assess the actual rendering rather than banning all browser synthesis without context.

Control widows/orphans when they materially harm headings or page flow. Do not distort content solely to eliminate one short line.

## Numbers, fonts, and output

Use tabular figures for aligned numeric data, right or decimal alignment for comparison, and consistent precision/units. Proportional numerals can work in prose. Distinguish IDs, currency, dates, and localized formats.

For the web, load only required styles and glyph ranges while preserving language coverage. Choose a loading strategy balancing readability and layout shift; verify fallback metrics. For print/PDF, inspect font embedding and actual output, using printer-specific black/color guidance rather than generic rich-black rules. For slides, judge text at presentation scale, not only a zoomed editor view.
