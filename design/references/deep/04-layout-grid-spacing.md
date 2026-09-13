# Layout, grid, and spacing reference

Attribution retained from the source kit: adapted from OERT (CC BY-SA 2.5), IBM Carbon spacing/grid practices, and BCcampus (CC BY 4.0). Numerical values are examples, not universal constraints.

## Spacing and grouping

Reuse an existing spacing system. For a new system, a 4/8px base with values such as 2, 4, 8, 12, 16, 24, 32, 40, 48, 64, 80, 96, 128, 160 can cover many web needs. Choose the useful subset. Optical corrections and platform-native measurements can justify off-scale values.

Within-component, between-field, between-group, and between-section gaps should make relationships clear. Related items often sit closer than separate groups, but labels, common regions, density, and task structure can override a pure spacing rule. Do not mechanically fail a table because cell padding exceeds a gutter.

Whitespace, tint, borders, and shadows can complement each other when they communicate distinct roles. Remove redundant boundaries; do not require one separation mechanism for every component.

## Grids and widths

A 12-column desktop / 8-column tablet / 2–4-column mobile grid is one option for responsive layouts. Simple flow, flexbox, content-sized grid, and split panes may suit the product better. Choose breakpoints when content stops working, not solely by device labels.

| Surface | Illustrative width | Constraint |
|---|---|---|
| Reading prose | Around 45–75ch | Actual script, font, content |
| Single-column form | Often 480–640px | Label length and input purpose |
| App content | Often 1200–1440px or fluid | Data density and usable scan range |
| Sidebar | Often 240–320px | Navigation labels and available space |
| Dialog | Content-sized, viewport-constrained | Task, scrolling, focus, mobile behavior |

These examples do not authorize resizing established layouts outside scope. Use fluid constraints, appropriate min/max dimensions, and overflow behavior.

## Rhythm and density

A few consistent section gaps can show hierarchy; equal sections can legitimately use equal spacing. Baseline alignment can help editorial layouts, but snapping every line height to a pixel grid must not break text resizing or glyph clearance.

Comfortable reading surfaces and compact operational surfaces have different needs. Do not shrink text to rescue a broken layout or remove important content to create empty space. Consider progressive disclosure, column priority, filters, and scoped scrolling based on the task.

## Responsive and reading order

Define meaningful stacking order for narrow layouts. Preserve DOM and focus order, long labels, zoom, localization, empty states, and realistic data volume. Test intermediate widths as well as mobile/desktop endpoints.

For web accessibility, reflow has a 320 CSS px equivalent width requirement with specific exceptions for content needing two dimensions. Scope horizontal scrolling to a table/map region where appropriate; do not hide required data merely to satisfy an overflow detector.

## Alignment

Use consistent axes and optical relationships. Align numeric data for comparison and labels to their controls; adjust icon placement to visual balance. Top-aligned, side-aligned, and inline labels each have contexts—there is no universal fastest form layout without task evidence.
