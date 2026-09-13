# Vault audit and repair

## Inventory before inference

Record scanned and excluded paths, snapshot time, supported formats, total notes, and parsing limitations. A canvas export may cover only one canvas and is not automatically a vault inventory. For large vaults, batch the requested full scope; do not silently replace it with a sample.

Use a parser appropriate to the actual format when available. A regex scan is candidate extraction, not proof of a complete graph. Ignore links inside code examples, respect relative paths and percent encoding, distinguish attachment embeds from note transclusions, resolve aliases/duplicate titles, and retain ambiguous targets for review. Resolve heading/block anchors separately from note-level edges. Account for Logseq page identities and block UUIDs only if their source index is accessible.

Compute unique directed non-self note edges, in/out degree, unresolved links, weak components, and coverage. A link to an excluded folder is out-of-scope, not necessarily broken. A partial graph cannot establish that a node is globally orphaned.

## Prioritize repairs

1. Broken or ambiguous links on frequently used paths, with a verified replacement.
2. Missing relationships that reconnect useful material to the user's active projects or navigation.
3. Content-based duplicate candidates, with overlap and meaningful differences.
4. Hubs or sinks whose content fails the navigation purpose; do not require every reference leaf to link outward.

For each recommendation provide source, target, exact proposed change, reader benefit, evidence, and confidence or open question. Prefer a short actionable list over a fixed quota. Do not recommend deletion merely because a node is empty or disconnected. Cycles are often useful and are not intrinsically bad.

## Apply and verify

An audit alone does not authorize edits. For requested repairs, preview a compact patch when helpful, preserve original note identities and formatting, and check changed references after saving. Authorized renames or merges require inbound-link migration and a scoped recoverable copy. Recompute the affected metrics and report actual resolved changes, skipped ambiguities, and remaining scan limitations. Do not present fewer orphans as proof of higher knowledge quality.
