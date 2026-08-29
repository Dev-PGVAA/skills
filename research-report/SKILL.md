---
name: research-report
description: >
  Produce large (30+ pages) professional analytical research reports — expert
  deep dives with institutional context, taxonomy, comparative tables, precise
  figures, mechanism analysis, falsification notes and strategic recommendations.
  Use whenever the user asks for a big, long, deep or thorough research report,
  analytical report, in-depth study, full breakdown, whitepaper or deep dive of
  20-40+ pages on any topic (technology, market, policy, education, security,
  business domain). Integrates with deep-research for evidence levels A–E.
  Triggers: research report, analytical report, whitepaper, deep dive, 30 pages,
  full study, in-depth analysis.
---

# Research Report

Produce publication-grade analytical reports of 30+ pages (~15,000–20,000+ words)
in a formal expert register.

Two style exemplars live in `references/`:
- `example-report.md` (Russian analytical report — canonical structural form)
- `example-report-usa.md` (US policy/engineering portfolio style)

Read the closest exemplar before writing the first report in a new domain.
Write the report in the user’s language unless told otherwise.

---

# Non-negotiable principles

1. **Research first.** A long report without fresh evidence is padding. Collect facts BEFORE outlining. Prefer the `deep-research` skill (levels A–E + falsification). If web tools are available, use them.
2. **Density, not volume.** Length comes from mechanisms, numbers, entities, comparisons — never from restating the same thought.
3. **Precision.** Every substantive claim carries a number, date, name, threshold, legal act, amount, or explicit hedge. Vague claims are defects.
4. **Never invent facts.** No fabricated laws, statistics, quotes, prices or companies. Uncertain → range + explicit statement.
5. **Citation discipline.** Decision-critical claims must be attributable (source level or URL). “No source, no claim” for high-stakes facts; training knowledge must be marked if used.
6. **Professional register.** Third person, analytical, no chat tone, no hype, no marketing language, no “I think”.
7. **One report = one artifact.** Deliver a single well-structured `.md` file (convert to `.docx`/`.pdf` only if asked).

---

# Workflow

## Phase 0 — Scope (pre-research contract)

Fix before any writing:

- topic and hard boundaries
- audience (decision maker / expert / general professional)
- purpose (strategy, orientation, comparison, due diligence, policy)
- target length and approximate section count
- language
- source priorities and exclusions

State open-ended dimensions explicitly rather than leaving them blank.

## Phase 1 — Research

Gather per subtopic:

- key entities (organizations, products, laws, programs, tools) + specifics
- numbers: thresholds, amounts, quotas, dates, durations, percentages
- mechanisms: how the system actually works step by step
- differentiation: how key players/variants differ
- known contradictions between sources (surface them)
- disconfirming evidence and failure modes (falsification)

Build a **fact sheet first**. The fact sheet, not the outline, is the bottleneck of quality.
Use deep-research levels A–E and uncertainty map.

## Phase 2 — Architecture

Plan 8–12 major sections. Allocate an explicit word budget per section
(e.g. 10 sections × 1,500–2,000 words + tables ≈ 30+ pages).
Use the canonical skeleton below, adapted to the domain. Sections can be
renamed, merged or added; the logical arc must remain.

## Phase 3 — Writing

Write sections in order, saving progressively to the file (append section by
section). Prose carries the analysis; tables and lists support it.
Keep claims + sources structurally linked where possible.

## Phase 4 — Verification pass

Re-check every number and named entity against the fact sheet.
Mark what could not be verified. Fill thin sections with NEW facts, not words.
Confirm falsification attempts are visible.

## Phase 5 — Self-review

Run the checklist at the end of this skill before delivering.

---

# Canonical report skeleton

## Title
Format: `Topic domain: analytical report on [aspect 1], [aspect 2] and [aspect 3]`
(one line, specific, no clickbait).

## Introduction — institutional / systemic framing
Open with the systemic transformation that makes the topic matter now:
global context → why the traditional approach no longer suffices →
the emerging mechanism → key institutions → exact scope and structure of this report.

## Architecture and normative status
Rules of the domain: legal acts, classifications, levels/tiers, validity periods,
obligations. Fundamental dichotomies or taxonomies the reader must grasp first.

## Catalog of key entities
Group entities into 2–4 classes. Every entity gets a substantive paragraph:
status/level, organizer, specificity, what it grants, quirks. Not one-liners.

## Comparative tables
Any multi-entity comparison becomes a table. First column = comparison parameter.
Cells stay short; interpretation lives in surrounding prose.

## Differentiated policies of key players
One sub-block per major player: strategy, thresholds, exceptions, incentive programs.
Contrast players against each other — this is where the report becomes decision-useful.

## Phenomenon / trend analysis
Name the central dynamic, explain the mechanism, consequences, and the ranking/
tie-breaking rules that emerge. Include failure modes and edge cases.

## Methodology and tooling
How practitioners actually operate: preparation tracks, resources, professional
tool stack by category, each tool with a one-line purpose. Specific and named.

## Financial / incentive infrastructure
Money flows: grants, scholarships, pricing, subsidies — amounts, quotas,
eligibility, AND obligations/risks (clawbacks, commitments). Close with a summary table.

## Limitations, contradictions and open questions
Explicit section for residual uncertainty, conflicting sources, missing data,
and what would change conclusions (concrete thresholds). Required for honesty.

## Conclusion — strategic imperatives
4–6 numbered recommendations, each with a bolded imperative header followed by
a dense explanatory paragraph. No new facts — synthesis only.
Close with a one-paragraph elevation of the argument.

## Sources
Attributed list with levels (A–E) where possible. Keep raw URLs out of prose body.

---

# Length strategy (reaching 30+ pages honestly)

Legitimate expansion (in order of preference):
1. More entities in each catalog class (each with real specifics)
2. More key players analyzed individually
3. Deeper mechanism explanations (step-by-step, edge cases, failure modes)
4. More comparative tables across different dimensions
5. Tool/methodology categories with individual tool paragraphs
6. Phenomenon analysis with worked examples and numeric scenarios
7. Obligations/risks/financial detail per program or player
8. Explicit limitations & falsification findings

Forbidden padding (instant quality failure):
- repeating a point from an earlier section in new words
- generic background the audience already knows
- bullet lists that paraphrase what prose already said
- filler phrases (“it should be noted that”, “in the modern world”)
- summarizing the section at its end when nothing follows

If a section cannot be filled with real substance, cut it and redistribute the budget.

---

# Style rules

- Formal analytical register, third person.
- Dense paragraphs: one paragraph = one complete thought + supporting specifics.
- Expand every abbreviation on first use; then use the abbreviation.
- Numbers in numerals with units and currency (83 contests, 75 points, $12,000 per year, order No. 639 dated 31 August 2025).
- Hedge patterns for uncertainty: “as a rule”, “depending on the policy of a given [player]”, “according to other data”, “in some cases”, “estimates vary between X and Y”.
- Confident framing of verified structure + explicit hedging of shaky data.
- Consistent domain terminology.
- No emoji, no exclamation marks, no rhetorical questions in body text.
- Prose-to-table ratio roughly 80/20.

---

# Provenance gate (mandatory)

- Every key fact in tables and every decision-critical claim must carry SOURCE LEVEL (A–E from deep-research) or an explicit “unverified / model knowledge” mark.
- Prefer Level A/B for numbers that drive recommendations.
- Tables: add a column or footnote “Source level” for quantitative rows.
- Hand-off from deep-research: reuse its Findings blocks (CLAIM / EVIDENCE / LEVEL / CONFIDENCE) rather than re-summarising without provenance.

# Fact hygiene

- Every figure traceable to the fact sheet or a source.
- Conflicting sources → show the conflict with levels (“750 (other sources: 150–200, Level C)”).
- No data available → state the gap explicitly.
- Time-sensitive claims anchored to a date (“as of August 2026”).
- Legal/normative claims cite the act number and date when known.
- Training-data knowledge, if used, is marked and never presented as researched fact.

---

# Self-review checklist

Before delivering, verify:

- [ ] 30+ pages / target length met with substance, not padding
- [ ] Every section has a job; none only restates others
- [ ] Each catalog entity and each key player has a substantive paragraph
- [ ] At least 3–5 comparative tables across dimensions
- [ ] Numbers, dates and thresholds present throughout — spot-checked
- [ ] Uncertainties hedged, contradictions surfaced, nothing invented
- [ ] Falsification / disconfirming evidence is present and visible
- [ ] Limitations & open questions section exists
- [ ] Conclusion gives numbered strategic imperatives, no new facts
- [ ] Register formal; no chat tone, no hype, no filler phrases
- [ ] Single `.md` file, correct heading hierarchy, tables render
- [ ] Sources attributed; decision-critical claims have provenance
