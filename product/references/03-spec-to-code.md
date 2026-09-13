# Spec to code — requirements into verified behavior

Use the existing conversation, artifacts, repository guidance, code, and tests to choose where to start. Preserve approved decisions and the user's requested scope. Stages are tools, not mandatory gates.

| Current state | Next useful action |
|---|---|
| Clear bounded coding request | Brief acceptance criteria, inspect affected code, implement |
| Important behavior unclear | Resolve the material uncertainty; continue independent inspection |
| Requirements established | Write or update a proportionate spec if useful |
| Substantial approved scope | Order testable slices by dependency and implement authorized slices |
| Existing spec/tickets | Validate against current code and implement the requested scope |

## Clarification without ceremony

Ask only questions whose answers materially change behavior, safety, or scope and cannot be inferred reliably. Bundle closely related blockers; do not force a one-question-per-message interview or an arbitrary quota. Use reasonable low-risk assumptions and state them. Continue useful independent investigation while awaiting a necessary answer.

Prioritize outcome, user flow, inputs/outputs, exclusions, constraints, and unacceptable failure cases. Existing decisions are settled unless current evidence exposes a conflict. Do not invent integrations, screens, retention rules, security promises, budgets, or deadlines.

For a small clear fix, a sentence describing expected behavior and a focused verification plan can be the full spec. Do not create SPEC.md and TICKETS.md merely to satisfy this skill.

## Durable specification for substantial work

Follow the repository's existing conventions and documents. Create a new spec only when needed; do not overwrite a user-maintained root file. Useful sections include:

- Purpose and users.
- Included and excluded behavior.
- Main flow, input/output contract, state transitions, and errors.
- Data, integrations, permissions, and relevant nonfunctional constraints.
- UX/content and accessibility expectations where applicable.
- Observable acceptance criteria.
- Confirmed decisions, assumptions, open questions, risks, and readiness.

State observable behavior rather than implementation guesses. For example: "Submitting the same request twice creates one record and returns its identifier" is testable; "robust architecture" is not. Keep required acceptance behavior distinct from optional implementation choices.

## Testable work slices

For multi-step work, organize slices by dependencies and user-visible outcomes. A useful ticket has an ID, goal, scope, dependencies, acceptance criteria, verification, and relevant implementation constraints. Include migration, rollback, observability, security, or docs only when the behavior needs them.

Do not force a fixed ticket count, one PR per ticket, a one-session duration, or repeated discovery when shared spec context already resolves it. Keep the smallest usable milestone visible. Mark genuine blockers without making deferrable decisions halt unrelated work.

## Implementation loop

1. Inspect current branch/status, applicable repository guidance, affected behavior and tests. Preserve unrelated uncommitted work and repository conventions.
2. Identify the smallest coherent change and how it will be verified. For new behavior or a regression, add a meaningful test when appropriate; reversible cosmetic changes may need visual inspection instead.
3. Implement within the authorized scope. Reuse existing primitives and error handling; avoid speculative abstractions, unsolicited telemetry, and unrelated cleanup.
4. Run proportionate checks that exercise the behavior and relevant failure paths. Type checking cannot prove a build, browser flow, deployment, or provider delivery. Distinguish configuration from live operation.
5. Review the actual diff, boundary cases, acceptance evidence, and data/security implications relevant to the change. Fix identified defects and rerun affected checks; do not loop through unchanged broad suites without reason.
6. Update existing task state when it is used. Continue to the next authorized dependency-ready slice until the user's scope is complete or a real blocker prevents progress.

Use actual available tools. If repository or runtime access is unavailable, prepare the most concrete patch or artifact possible and clearly state unexecuted verification. Do not claim a test, review, commit, build, or deploy occurred without evidence.

## Authorization and handoffs

Respect explicit instructions such as "plan first, wait for approval, then implement." If implementation is already authorized, do not ask again at the spec-to-ticket transition, after every ticket, or before the first implementation merely because a plan was produced. "Do it all" covers the agreed scope, not arbitrary new features or external actions.

Creating a plan or evaluating an idea alone does not authorize coding, deployment, spending, contacting people, deleting data, committing, or publishing. Follow the user's actual authorization and environment permissions for those actions. Prepare a concrete reviewable result before requesting any final permission that is genuinely needed.

## Implementation agents

Use agents for independent components with explicit disjoint file ownership, a bounded technical investigation, or an independent defect review. Define interface contracts and dependencies before concurrent implementation. Agents return changed files, behavior, checks actually run, failures, and unresolved questions.

The parent owns shared contracts, migrations, integration, review, and end-to-end acceptance. Do not assign simultaneous writes to shared specs or the same source files. Rebase or merge according to repository conventions and inspect the integrated result; several passing component tests do not establish integration success. For a small coupled change use sequential work.

## Completion

Report what changed and why, the meaningful checks and results, and material limitations or remaining blockers. Include a commit or deployment only if it occurred and is useful to the user. Avoid templated empty sections and do not offer to continue work that is already authorized and incomplete.
