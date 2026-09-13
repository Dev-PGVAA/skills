# Accessibility — requirements and evidence

Identify the artifact, platform, intended conformance target, and task scope. The checks below cover common web issues, not all WCAG requirements. Distinguish a demonstrated barrier, an applicable criterion failure, a best-practice suggestion, and something untested. A screenshot review cannot certify accessibility.

- Measure text contrast against the final background and relevant states. Normal text generally needs 4.5:1 and large text 3:1 at AA; applicable non-text UI information needs 3:1. Exceptions and enhanced targets are in [Accessibility detail](deep/07-accessibility.md).
- Verify keyboard operation, logical focus order, visible focus, modal behavior, and focus restoration. WCAG AA visible focus does not universally require a two-pixel perimeter; enhanced focus appearance is AAA.
- Test text resizing to 200%, text-spacing overrides, and reflow at a 320 CSS px equivalent width. These are distinct checks. Two-dimensional content has specific reflow exceptions.
- Check accessible names, persistent labels where needed, instructions, textual error identification, status announcements, and preservation of entered data.
- Do not rely on color alone. Evaluate chart labels/patterns and interface states in actual use; grayscale is a useful diagnostic, not a complete color-vision assessment.
- Check target size and applicable exceptions, dragging alternatives, accessible authentication, and consistent help when relevant.
- Provide appropriate motion controls and reduced-motion behavior. Avoid flashing and inspect applicable thresholds rather than simplifying the entire standard to a universal 3Hz ban.

Fix in-scope barriers and verify the result. Record material preexisting issues outside the requested change without silently expanding a narrow task into a full redesign. Report checks actually performed, their environment, and limits. Use current official criteria for a formal conformance assessment.
