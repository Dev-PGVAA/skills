# Part 2 — Review (defect-first)

Part of code-quality. Works standalone. Read-only review of a change (uncommitted diff, base-branch diff, or a commit).

## Mission

Return every actionable finding the author would actually fix, ranked P0–P3. Prefer real, demonstrable, change-introduced issues. `No findings.` is a valid result.

## Scope

- Correctness and regressions
- Security (injection, secrets, authz, excessive agency if AI-related)
- Test gaps for new behaviour
- Unnecessary complexity / LLM slop (over-abstraction, dead code)
- File size / cohesion (flag unexplained >~120 LOC growth when avoidable)
- Blast radius of the change (what else can break)
- Breaking API / contract changes without migration note

## Output format

For each finding:
```
[P0|P1|P2|P3] short title — path:line
One short paragraph: evidence + why it matters + concrete fix direction.
```

End with:
- Overall assessment (1–3 sentences)
- Test gaps (if any)
- Blast-radius note (modules/users affected)

## Severity
- **P0** — wrong result, security hole, data loss, secrets exposure
- **P1** — likely bug, missing critical test, clear contract break
- **P2** — maintainability, avoidable complexity, weak tests
- **P3** — style/nit that still improves clarity

Do not invent issues. Do not demand style pure for its own sake.
