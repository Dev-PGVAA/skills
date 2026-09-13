# Orient a repository

## Discover incrementally

1. Confirm checkout, branch/revision, local changes, and applicable instructions. Read an existing architecture index first, then verify the sections needed for this task.
2. Inspect manifests, workspace definitions, entrypoints, build scripts, and deployment configuration. Use `rg --files` and targeted symbol search; exclude generated output, dependencies, caches, and vendored code unless relevant.
3. Trace one representative flow end-to-end. Record how input reaches business logic, persistence, background work, and output. Find tests at those boundaries.
4. Group modules by the actual code organization. Treat path names as clues, not proof. Distinguish checked configuration from live topology.
5. Stop when the user's navigation questions are answered; expand only a material unresolved boundary.

## Persistent outputs scale with the repository

Reuse the established docs location. For a small repository, one `docs/architecture/INDEX.md` can hold the map. Split when sections become hard to navigate:

| File | Useful contents |
|---|---|
| `INDEX.md` | Purpose, inspected revision/date, map links, quickest entrypoints |
| `OVERVIEW.md` | Components, runtime roles, principal flows, known unknowns |
| `MODULES.md` | Real module path, responsibility, entrypoint, key dependency |
| `WHERE.md` | User concept → code/test/config paths, with one-line guidance |
| `DEPS.md` | Important dependency directions, evidenced constraints, cycles worth knowing |

Omit files without useful contents. Do not invent auth/payments/jobs sections for an application that lacks them. Link claims to files and symbols; use line numbers only when verified and helpful.

A short pointer in an existing `AGENTS.md` can make a requested persistent map discoverable. Add it without truncating, rewriting, or overriding existing instructions. Do not impose line limits or “always read the entire map” instructions. Do not create or modify agent instructions for a read-only orientation request.

## Keep it maintainable

Record revision/date and whether the working tree contained relevant local changes. On refresh, use the diff and changed manifests/entrypoints to identify affected sections. Retain valid human-written text, repair moved paths, and mark uncertainty instead of silently substituting a guessed architecture. Declare commands as discovered, executed successfully, or unverified.

Check that linked files exist and that the most important flow can be followed from the index. If a map is stale, use the source of truth and update only within the user's requested write scope.
