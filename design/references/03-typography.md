# Typography

Preserve the established font system unless changing it is in scope. Choose readability, language coverage, and platform fit before novelty. One family with clear role/weight contrast often works; additional families need a useful role, not an arbitrary ban or quota.

- Check required glyphs (including Cyrillic when applicable), true styles, numerals, fallback metrics, available font files, and licensing before depending on a font.
- Start reading text around 16–20px on the web; dense interfaces may use smaller text when actual legibility, scaling, and interaction remain sound. No single font-size floor establishes WCAG compliance. Slides and print need checks at their intended viewing size.
- Body leading around 1.4–1.6 and a 45–75-character measure are starting points for Latin/Cyrillic text. Adapt to script, typeface, density, screen, and content. Do not shrink unreadable text to fit; fix size, measure, and layout together.
- Use semantic headings, coherent role tokens, and restrained emphasis. Left-align long LTR prose by default; respect RTL and script-specific conventions. Justification needs suitable hyphenation and rendering checks.
- Use tabular figures and aligned numeric columns when comparison matters; keep units and precision consistent.
- Web font loading should balance readability, layout shift, transfer size, and required language coverage. Relative units and flexible line height generally help scaling; test actual zoom and font-size changes.

More detail: [Typography reference](deep/03-typography.md). Numerical values there are heuristics and platform examples; retain appropriate existing choices.
