---
name: codebase-map
description: Explain where behavior lives in a repository, create or refresh an evidence-backed architecture map, or draw real component relationships in Mermaid or draw.io. Use for repository orientation and architecture diagrams.
---

# Codebase Map

Locate the code needed for the user's task and preserve useful orientation when requested. Distinguish source evidence, declared configuration, and observed runtime behavior.

## Route by the requested deliverable

- **Where is X / quick orientation:** read the relevant existing map and verify its paths against the checkout. Answer with a short flow and entrypoint links; no documentation writes are required.
- **Create / refresh a persistent map:** use [orient](references/01-orient.md). Preserve existing documentation layout and local instructions.
- **Architecture visual:** use [diagram](references/02-diagram.md). A diagram can be made from a focused source pass without generating a documentation suite first.

## Parallel discovery

For a large repository, delegate independent bounded regions (for example API/auth, workers/data, UI/navigation). Each scout is read-only and returns real paths/symbols, entrypoints, dependencies with evidence, uncertainties, and the exact revision inspected. Do not ask every scout to scan the whole tree.

The parent owns the index, shared documentation, and cross-region connections. Verify boundary claims, deduplicate, and reconcile inconsistent names before writing. If agents are unavailable or the scope is small, perform the same focused discovery sequentially. Delegation is useful only when it saves work; never create one agent per file.

## Evidence and completion

A package's presence does not prove it runs in production; an import does not prove a network deployment. Record what was inspected and what remains unknown. Verify all delivered local links and diagram source syntax with available tools. Report actual validation and the best starting file, not an entire repository listing.
