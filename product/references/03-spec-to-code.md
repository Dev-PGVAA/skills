# Part 3 — Spec to Code (interview, SPEC, tickets, implement)

Part of product. Works standalone.


# Spec to Code

Four stages, one skill:

```
INTERVIEW → SPEC → TICKETS → IMPLEMENT
```

Each stage produces an artifact the next stage consumes. Never skip ahead:
code written from a vague understanding is the most expensive kind of code.

## Stage detection

Enter at the stage matching what already exists:

| Already have | Start at |
|---|---|
| Vague idea or request | Stage 1 — Interview |
| Approved requirements, Interview result, evaluate BUILD verdict | Stage 2 — Spec |
| Approved spec | Stage 3 — Tickets |
| Approved ticket | Stage 4 — Implement |

## Proportionality rule

Match ceremony to size. Two paths:

- **Express path** — small bounded change (obvious behavior, ~1-2 files):
  at most 2-3 clarifying questions, a 5-10 line mini-spec, 1-3 tickets,
  then implement. Same stages, minimal weight.
- **Full path** — everything else: complete each stage fully.

If unsure which path, ask once: "Is this a quick change or a full feature?"

## Stage 1 — Interview

Turn an unclear request into shared understanding without exhausting the user.

- Ask **one question per message**. Wait for the answer before the next.
- Start with the uncertainty that most changes the outcome.
- Treat facts already stated as settled. Do not re-ask them.
- Prefer concrete wording and brief examples over abstract jargon.
- Make a low-risk assumption only when cheap; state it and invite correction.
- Do not write spec, tickets, or code while interviewing.

Question priority order:

1. What outcome should exist when this is done?
2. Who uses it and what problem does it solves for them?
3. What is in scope and explicitly out of scope?
4. What inputs, integrations, data, platforms, or technical constraints matter?
5. What makes the result successful, and what failures are unacceptable?
6. What examples, references, deadlines, budget, or compliance constraints apply?

**Timebox:** after 5-7 questions, stop and propose proceeding on stated
assumptions. A perfect interview is not the goal — a testable understanding is.

Finish only when you can state, without inventing material details:
desired outcome and audience; main user flow or behavior; scope boundaries
and constraints; a workable success criterion; deferred assumptions.

Output a compact **Interview result** with those five items, each marked
`confirmed` or `assumption`.

## Stage 2 — Spec

Create a clear, testable definition of what to build.

- Source of truth: the conversation plus the Interview result.
- One or two missing details → ask one targeted question at a time.
- Deferrable detail → an explicit open question, not a blocker.
- Never invent integrations, screens, data retention, security promises,
  or business rules.

Structure (omit sections that truly do not apply):

```markdown
# [Feature or product name]

## Purpose
## Users and problem
## Scope
### Included
### Excluded
## User flows and behavior
## Functional requirements
## Non-functional requirements
## Data, integrations, and permissions
## UX/content requirements
## Acceptance criteria
## Risks, assumptions, and open questions
```

Quality bar:

- Requirements phrased as observable behavior, not implementation guesses.
- Every acceptance criterion has a pass/fail outcome.
- Confirmed facts separated from assumptions and open questions.
- Proportionate: a simple feature does not get enterprise architecture.
- Privacy, security, accessibility, performance called out only when relevant.

Persist the spec to `SPEC.md` in the project root so later sessions
and other agents can resume without losing context.

End with a `Readiness` line: `ready for tickets`, `needs decisions`,
or `needs research`, with the reason.

## Stage 3 — Tickets

Turn the spec into executable slices of work, not a vague checklist.

Principles:

- Each ticket produces a reviewable outcome within one focused session.
- **One ticket = one PR (or one commit group).** Do not batch unrelated tickets into a single change.
- Order by dependency; reduce uncertainty early.
- No "set up everything" tickets. Prefer vertical, testable slices.
- Tests, migrations, rollback, observability, docs, security — include only
  where relevant.
- Do not assume a framework, repo structure, or deployment the spec
  does not establish.

Exact ticket format:

```markdown
## [ID] [Short imperative title]
**Goal:**
**Why now / dependency:**
**Scope:**
**Implementation notes:**
**Acceptance criteria:**
**Verification:**
**Out of scope:**
**Estimated session:** one focused session
```

Plan overview first: dependency order (`T1 → T2 → …`), the smallest usable
milestone, and risks or decisions blocking any ticket.

A ticket is ready only if Stage 4 could start from it alone without reopening
product discovery. If impossible, surface the missing decision explicitly.

Persist to `TICKETS.md` (with a `- [ ]` checkbox per ticket for progress).

## Stage 4 — Implement

Deliver one ticket safely and leave clear evidence of what changed.

Start conditions:

- One approved ticket or a clearly bounded coding request.
- Ticket missing goal/acceptance/scope → ask one question or return to Stage 3.
- Read the relevant code, repo guidance, and existing tests before editing.
- Inspect uncommitted changes; preserve work outside this ticket.

Delivery loop:

1. Restate the ticket goal and a concise implementation plan.
2. Identify the smallest affected surface; avoid unrelated cleanup.
3. Implement with maintainable, idiomatic code.
4. Add or update focused automated tests when feasible.
5. Run the relevant checks. If a check cannot run, report the exact reason
   and the next safe check.
6. Review the diff against acceptance criteria, failure paths,
   security/privacy implications, regressions.
7. Commit only when repo access exists AND the user authorized committing;
   focused conventional message unless the project states a convention.

Boundaries:

- Never claim a test, review, build, or commit happened unless it did.
- Do not broaden the ticket or overwrite unrelated user changes.
- Do not expose secrets, bypass security controls, or add telemetry
  without explicit scope.
- No repo access → provide a minimal patch and exact verification steps
  instead of pretending to execute.

Completion report:

```markdown
## Implemented
- [what changed]

## Verification
- [command/check]: [result]

## Review notes
- [risk, trade-off, or "none found"]

## Commit
- [hash and message, or why no commit was made]

## Next
- [next ticket or remaining blocker]
```

After reporting, tick the ticket in `TICKETS.md`.

## Handoffs between stages

Default — confirm each transition:

- after Stage 1: `Ready for the spec — proceed?`
- after Stage 2: `Spec ready — split into tickets?`
- after Stage 3: name the next executable ticket — `Start implementing [ID]?`
- after Stage 4: propose the next ticket; never start it without instruction.

**Flow mode** — on explicit request (`do it all at once`, `/spec-to-code full`),
run Stages 1-3 without stopping, then pause before the first implementation.

## Integration with the rest of the library

- `evaluate` part verdict **BUILD** → enter at Stage 2; its MVP definition and
  experiments are the spec's purpose section.
- `plan` part output → its phases map to ticket batches.
- `code-quality` skill guidelines applies inside Stage 4:
  surgical changes, no overengineering.
