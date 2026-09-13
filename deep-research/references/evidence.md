# Evidence protocol

## Claim ledger

For substantial work keep a compact ledger in the task's working directory, not in the installed skill. One row per meaningful claim; supporting evidence may have several rows.

| Field | Record |
|---|---|
| Claim ID and wording | Specific enough to be supported or refuted |
| Source and locator | Original URL/DOI/document path + page, section, table, or dataset field |
| Dates and scope | Publication, effective/data period, access date; jurisdiction/version/population |
| Evidence | Short permitted extract or faithful paraphrase; separate from interpretation |
| Origin and authority | Original study/filing/dataset; author incentives and relevant expertise |
| Method and limitations | Sample, measurement, comparison, exclusions, uncertainty, conflicts |
| Status and confidence | Supported / contradicted / mixed / unverified; high / medium / low with reason |
| Decision impact | What changes if this claim is wrong |

Retain material evidence and sufficient retrieval pointers. Never copy lengthy copyrighted sources merely to accumulate notes.

## Source categories (A–E compatibility)

Use these categories when they help handoffs; they describe provenance, not a universal reliability ranking.

- **A — primary material:** original datasets, laws, standards, documentation, filings, code, original studies. Strong for what was actually observed, required, or claimed in that context. Primary marketing, preliminary studies, and biased measurements remain primary but may support low-confidence conclusions.
- **B — synthesis or established framework:** systematic reviews, authoritative secondary analysis, reference works. Strong when methods and underlying evidence are transparent; a framework is not empirical proof that a market exists.
- **C — documented case:** reproducible postmortem or detailed implementation report. Establishes a case, rarely prevalence or causality across a population.
- **D — practitioner account:** interviews, talks, informed firsthand commentary. Useful for mechanisms and hypotheses; record commercial incentives and unverifiable parts.
- **E — unverified anecdote:** screenshots, anonymous claims, promotional metrics without method. Leads for investigation, not decisive proof.

Peer review, institutional prestige, and popularity are signals to examine, not automatic quality guarantees. An independent rigorous synthesis can support a claim better than one primary study.

## Confidence and independence

Confidence is claim-specific: relevance, directness, methods, precision, consistency, provenance, and replication determine it. High confidence needs strong support for this exact claim and no unresolved material contradiction; medium has meaningful limitations; low depends on sparse, indirect, or conflicted evidence. Avoid pseudo-precise percentages.

For decisive claims, find the original source and seek independent corroboration where useful. Independence means different underlying observations or methods, not different domains quoting the same source. Three vendor pages may independently confirm listed features but not customer demand. A single authoritative current statute may settle its own wording without a second citation; interpretation or application can still be uncertain.

## Quantitative and study checks

- Distinguish totals from rates, medians from means, relative from absolute change, annual from monthly pricing, nominal from inflation-adjusted money, and sample from population. Check denominators, inclusion dates, missingness, duplicates, and comparable units.
- Recompute important derived numbers with an available calculator or reproducible local calculation. Keep inputs and formulas; label scenarios. Do not infer a range without defensible bounds.
- For studies inspect design, sampling, comparison group, outcome definition, effect size and interval, attrition, confounding, multiplicity, preregistration if relevant, and funding. Separate association from causal inference. Absence of statistical significance is not proof of equivalence.
- For benchmarks check dataset versions, leakage, evaluation conditions, baseline fairness, cost/latency and uncertainty. Do not extrapolate one benchmark into universal superiority.
- For market estimates state the unit (buyers, users, accounts, spend), reachable segment, source year, and assumptions. Revenue screenshots, views, stars, and waitlists do not establish retention or willingness to pay.
- For rules cite jurisdiction, exact relevant provision, effective date, exceptions, and authority. Distinguish proposed policy from enacted and effective rules.

## Conflict resolution and falsification

Write the real claim fairly, identify its decisive assumptions, then search plausible failure mechanisms rather than vague negative keywords. Compare conflicting sources on outcome, population, time, version, incentives, and method. Do not average incompatible measurements, suppress inconvenient results, or demand a contrarian finding when the evidence is one-sided.

Return: strongest counter-evidence; why it does or does not overturn the claim; residual gap; feasible observation or threshold that would change the recommendation. Thresholds should be justified by decision costs or user constraints, not invented to look rigorous.

## Source access failures

Try an official mirror, author version, archived version, or another source addressing the same claim if allowed. An abstract supports only its contents. Mark paywalled or unavailable material as uninspected; never manufacture quotes, page numbers, DOI metadata, or citations. Stop retries when the same access condition persists and no useful alternative remains.
