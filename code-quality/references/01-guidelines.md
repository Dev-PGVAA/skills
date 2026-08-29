# Part 1 — Guidelines (LLM coding discipline)

Part of code-quality. Works standalone.

## Mission

Write the **minimum code that correctly solves the stated problem**, looks intentional, and leaves no garbage.

Priority order (always):
1. **Works** — correct behaviour, real tests or verifiable criteria
2. **Clean** — readable, intentional structure, no dead paths
3. **Minimal** — fewer lines and fewer abstractions than the average LLM default
4. **Beautiful** — consistent naming, clear flow, no noise

## Hard rules

### Less code, higher signal
- Prefer the smallest change that satisfies the task (surgical edit).
- Do not invent helpers, wrappers, or “future flexibility” unless the task requires them.
- Delete dead code you touch; do not leave commented-out blocks.
- One concern per function/module. Split only when mixing concerns hurts clarity.

### File size soft limit (~120 lines of real code)
- Target ≤ ~120 lines of non-comment, non-blank code per file when practical.
- Exceptions (document why in a one-line comment or PR note): generated code, dense pure data, unavoidable framework boilerplate, single cohesive algorithm that is clearer kept together.
- Prefer extracting a focused module over growing a “god file”.

### TDD when behaviour is new or changed
- Prefer **red → green → refactor**: one failing test that specifies the behaviour, then minimal implementation, then cleanup.
- No production code for a new behaviour without a failing test (or an explicit, documented exception for pure glue / one-off scripts).
- Tests describe behaviour with independent expected values — not mirrors of implementation.

### LLM anti-patterns (2026) — reject these
- Speculative abstractions (“BaseX”, “XManager”, “ISomethingService” with one implementation)
- Hallucinated APIs or flags not present in the project
- Over-wide try/except that swallows errors
- Duplicated utility logic instead of using existing project helpers
- Massive multi-file rewrites when a local edit suffices
- Comments that narrate “what” instead of non-obvious “why”
- Feature flags / config for hypothetical future needs

### Architecture principles (framework-agnostic, extractable)
- **Feature isolation**: keep UI, logic, and data access for one feature close; avoid scattering across global folders without reason.
- **Dependency direction**: UI → domain/hooks → services → external I/O. Never invert without a deliberate boundary.
- **Single responsibility** at file and module level.
- Prefer explicit boundaries over clever shared bags of helpers.
- For UI frameworks (e.g. Next-style): keep route/entry files thin; push real logic into feature modules; respect server/client boundaries when they exist.

### Assumptions and verification
- State assumptions explicitly when unclear; ask the single highest-value question if blocked.
- Define verifiable success criteria before large edits.
- Plan → implement → check (tests, typecheck, or manual verification path).

## When writing

1. Restate the goal in one sentence.
2. List the files that must change (prefer fewer).
3. If new behaviour → write/adjust the failing test first.
4. Implement the minimum.
5. Remove anything that did not earn its place.
6. Confirm the success criteria.

## Output discipline

- Prefer unified diffs / focused edits over full-file rewrites.
- Do not claim tests passed unless they were run.
- If the 120-line soft limit is exceeded, say so and justify or split.
