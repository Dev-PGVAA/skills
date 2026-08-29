---
name: deep-research
description: >
  Evidence-first research engine for business, technology, markets, competitors,
  products, architecture and policy decisions. Uses source-quality levels A–E,
  uncertainty mapping, query decomposition, triangulation, and aggressive
  falsification (contrarian search that actively hunts counter-evidence,
  failures and disconfirming cases). Use whenever the user asks to research,
  investigate, compare, fact-check, validate assumptions, or when another skill
  (product evaluate, architecture decisions, security threat model) needs
  uncertainty reduced before a decision. Triggers: research, deep research,
  competitor analysis, market research, fact-check, validate, evidence, sources.
---

# Deep Research

Your purpose is to reduce uncertainty that matters for a decision.

Search before reasoning whenever current external information can materially change the answer.
Do not research merely to decorate the response with citations.
Research the assumptions that determine the decision.

---

# 0. Pre-research contract (fix first)

Before any search, lock:

1. **Objective** — one sentence: the decision or deliverable this research supports.
2. **Audience & use** — who will read it and what they will do with it.
3. **Scope** — time frame, geography, domains included/excluded. Unstated dimensions = open-ended (state them explicitly).
4. **Output shape** — short findings, decision memo, or feed into research-report.
5. **Source priorities & exclusions** — prefer primary; note any banned or low-trust classes.

Be exhaustive about objective/scope/audience/sources; be terse about method.

---

# Evidence Stack

Knowledge has two dimensions:

1. SOURCE QUALITY (A–E)
2. RECENCY / RELEVANCE

Always classify every piece of evidence.

## LEVEL A — Primary / authoritative
- Official documentation, company docs, SEC filings, source code, official APIs, technical specs
- Peer-reviewed papers, standards, government datasets, Harvard/HBS primary materials
Use as strongest evidence.

## LEVEL B — Established frameworks
- Respected books, validated academic/business frameworks, recognized technical literature
Strong for models; weaker for current facts.

## LEVEL C — Credible cases
- Engineering blogs, postmortems, documented company/startup cases, technical case reports
Real-world implementation evidence.

## LEVEL D — Operator / creator knowledge
- Founders, practitioners, growth operators, high-signal X/Twitter threads, podcasts, YouTube from known operators
Useful for tactics and emerging patterns. Not universal truth.

## LEVEL E — Anecdotal
- Individual claims, screenshots, unverified revenue numbers, viral posts, isolated observations
Hypothesis-generating only.

Search is a mechanism that surfaces evidence at any level. Classify what you find.

---

# Uncertainty map (mandatory)

Before searching, write:

```
OBJECTIVE: [decision this supports]
UNKNOWN (rank by IMPACT × UNCERTAINTY):
- ...
KNOWN:
- ...
ASSUMPTIONS TO TEST:
- ...
```

Search the highest IMPACT × UNCERTAINTY items first.

---

# Query decomposition

Never one giant query. Split into independent angles.

Example topic: “AI meeting assistant for lawyers”

Research separately:
1. Existing products & positioning
2. Legal/privacy requirements (jurisdiction-specific)
3. Transcription API economics & accuracy limits
4. Willingness-to-pay / budget signals
5. Complaints, churn reasons, negative reviews
6. Security & data-residency constraints
7. Workflow integration points
8. Market adoption signals & substitutes

---

# Triangulation & conflict handling

Important claims need:
- primary source, and/or
- multiple independent sources.

When sources conflict: show the disagreement with levels. Never silently average.

**No-source, no-claim rule** for decision-critical facts: if it cannot be attributed, either drop it or mark explicitly as model knowledge / unverified.

---

# Recency

Prioritize recent evidence for: AI, software, APIs, pricing, laws, cybersecurity, platforms, algorithms, product availability.
Older sources remain valid for foundational frameworks and mechanisms.

---

# Falsification / Contrarian protocol (non-negotiable)

Half the search budget is for killing the claim.

Actively search for:
- failures and shutdowns of analogous products
- complaints, churn reasons, negative reviews
- alternatives and substitutes already in use
- limitations, policy restrictions, price increases
- security incidents and trust breaks
- historical parallels that failed for the same structural reason
- data that would force a different recommendation

When the user challenges a conclusion or product/evaluate needs counter-evidence:

1. State the claim in one sentence.
2. Write 3–5 disconfirming hypotheses (“this fails because…”).
3. Search each hypothesis independently (do not reuse supporting queries).
4. Rank findings by source level (A–E) and decision impact.
5. Report **what would change the conclusion** with a concrete threshold, not a vague caveat.

A report with only confirming sources is incomplete.

---

# Competitor research template

For each important competitor capture:
WHO · TARGET USER · POSITIONING · FEATURES · PRICE · DISTRIBUTION · STRENGTH · WEAKNESS · COMPLAINTS · DIFFERENTIATION

Avoid feature-list-only analysis. Prefer primary sources + real user complaints.

---

# Technical research order of preference

1. Official docs & specifications
2. Source repositories & primary papers
3. Maintainers / release notes
4. Credible postmortems and production experience
5. Developer communities (for bugs, undocumented limits, adoption friction)

---

# Output format (decision-oriented)

```markdown
## Question / Objective
## Decision this research supports
## Scope & assumptions

## Known
## Unknown (ranked)

## Findings
For each key finding:
- CLAIM
- EVIDENCE (short quote or paraphrase + source)
- SOURCE LEVEL (A–E)
- CONFIDENCE (High / Medium / Low)
- IMPLICATION for the decision

## Contradicting evidence
## Missing evidence
## What would change the conclusion? (concrete thresholds)
## Recommendation
## Sources (with levels)
```

For short answers compress to the highest-signal subset. For long work, hand off cleanly to `research-report`.

---

# Quality bar

- Every substantive claim is attributable or explicitly hedged.
- Uncertainty is preserved, not smoothed away.
- Falsification attempts are visible in the output.
- The reader can decide with less residual uncertainty than before the research.
