# Components and states

Reuse existing primitives and native conventions. A component should make its purpose, state, and available action understandable.

- Prioritize actions per decision region; use secondary and destructive treatment where it clarifies choices. Design appropriate confirmation or undo for the consequence, without redundant prompts for already authorized actions.
- Labels describe the action in the user's language. Brevity helps, but a three-word limit must not remove necessary meaning.
- Implement relevant states: focus, hover where supported, pressed, selected, disabled, loading, success, empty, and error as appropriate to the component. Not every link needs every state.
- Prefer native semantic elements. Icon-only controls need an accessible name; a tooltip alone is not a reliable label. Standard icons can be appropriate without visible text when meaning and accessible naming are clear.
- Touch targets benefit from generous hit areas. Web WCAG 2.2 AA target rules include sizing and exceptions; see [Accessibility detail](deep/07-accessibility.md). Platform points, density-independent pixels, and CSS pixels are not interchangeable units.
- Explain why an action is unavailable where useful. Do not add `pointer-events: none` or remove keyboard access indiscriminately; choose correct disabled semantics for the element and behavior.
- Preserve user input on recoverable error and support a concrete retry path. Ensure loading and completion do not cause unexpected focus loss or duplicate actions.

More detail: [UI roles and platform examples](deep/06-ui-design.md).
