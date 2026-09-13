# Defect-first review

## Fix the comparison and scope

Determine whether the user means the working tree, staged changes, a commit, or a base/head comparison. Inspect repository status and resolve revisions. For a branch review, inspect the diff from the appropriate merge base, including renamed/deleted files. Do not assume `main`, review unrelated existing changes, edit files, or post comments externally without authorization.

Read surrounding implementation and callers, not just added lines. Trace the affected input through validation, state/persistence, and user-visible output. Understand an intentional contract change before calling it a regression.

## Find actionable defects

For each candidate establish:

1. Concrete trigger and required preconditions.
2. Affected behavior or security boundary.
3. Evidence in the changed code and relevant caller/configuration.
4. Why an existing guard does not prevent it.
5. Minimal fix direction and a reproducer or verification method.

Prioritize correctness, authorization, data loss, compatibility, concurrency, and failed recovery. A missing test is a coverage note unless it exposes an identifiable defect. Do not turn file length, preferred style, hypothetical future usage, or a speculative abstraction complaint into a bug. Pre-existing defects belong in a clearly separate note only when material to the user's request.

Use targeted, non-mutating checks where useful. Mark static reasoning as static; do not claim reproduction without running it. Avoid weak findings rather than padding the report.

## Severity and confidence

- **P0:** immediate blocker with severe, broadly applicable impact; reserve for urgent failures supported by strong evidence.
- **P1:** high-impact reachable defect needing prompt correction, such as unauthorized access, data corruption, or broken core functionality under stated conditions.
- **P2:** ordinary actionable defect with narrower impact or preconditions.
- **P3:** low-impact concrete defect worth fixing; style nits only when explicitly requested.

Severity describes impact and urgency, not confidence. State uncertainty and preconditions in the finding. Do not classify every wrong result or security concern as P0.

## Report

For each finding use `[P1] Short actionable title — path:line`, followed by one concise paragraph explaining trigger, consequence, evidence, and fix direction. Anchor the smallest useful changed line range and verify line numbers against the reviewed revision. Group duplicates by root cause and rank the final list.

Finish with only material validation/coverage limits. If no supported issue remains, say so and name any meaningful untested behavior. Do not claim that a clean review proves the absence of defects.
