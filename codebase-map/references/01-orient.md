# Part 1 — Orient

Create or refresh a **living map** so future sessions start oriented.

## Outputs (write these)

1. `docs/architecture/INDEX.md` — 1-page table of contents + how to use the map
2. `docs/architecture/OVERVIEW.md` — purpose, stack, high-level layers, runtime topology
3. `docs/architecture/MODULES.md` — major modules/packages: path, responsibility, key entry files
4. `docs/architecture/WHERE.md` — “where to look for X” index (auth, payments, jobs, UI shells, config, tests…)
5. Optional: `docs/architecture/DEPS.md` — important dependency directions / forbidden imports
6. Root `AGENTS.md` (or update existing): **≤ ~80–100 lines**, pointer-style only:
   - 2–3 sentence project blurb
   - “Read docs/architecture/INDEX.md first”
   - build/test commands
   - 3–5 critical constraints
   - link to conventions if any

## Method

1. Detect stack from manifests and entrypoints (do not guess).
2. List top-level dirs and assign each a one-line role.
3. Find entry points (main, app router, server bootstrap, workers).
4. Group into layers or features from **evidence in the tree**, not ideal theory.
5. Build WHERE.md from real paths (grep/symbols when needed).
6. Prefer update-in-place: mark stale sections, do not rewrite what is still true.

## Rules

- Evidence only: every module claim must map to a path that exists.
- No essay: short bullets and tables.
- Do not invent microservices or CQRS if the repo is a simple app.
- After writing, state: “Orientation ready — start from docs/architecture/INDEX.md”.
