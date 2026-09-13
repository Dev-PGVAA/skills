# Evaluate — validate and strengthen the proposed idea

Evaluate the strongest faithful interpretation of the user's idea against their goal: a business, portfolio demonstration, learning project, internal tool, public good, or research prototype has different success criteria. Do not demand revenue or a moat for a noncommercial project. Do not silently pivot the user into a different problem.

## Begin with the decision

Reconstruct the target user, problem, current workflow, proposed benefit, constraints, and decision to make. Use supplied facts and artifacts first. Ask only for a missing fact that changes the conclusion; ordinary assumptions can be stated and tested. Choose relevant modules below rather than producing every heading.

If a named mode is requested (market, economics, architecture, security, distribution, red-team, improve, compare, MVP, experiments), keep the response in that mode. Mode labels are conversational selectors, not installed slash commands.

## Problem, demand, and alternatives

- Separate stated, observed, and assumed problems. Determine frequency, severity, existing workaround, who experiences the pain, who controls purchasing, and what causes a switch.
- Research demand where external facts matter. Prefer actual spending, recurring use, retention, procurement, support complaints, and workflow evidence to attention metrics.
- Distinguish interest, intent, willingness to pay, purchase, and retained use. Views, stars, waitlists, and competitor existence are useful signals but establish none of these by themselves.
- Compare doing nothing, manual work, incumbents, adjacent tools, open source, and build-it-yourself. Feature checklists miss switching cost and distribution.
- State the reachable segment and why this team can access it. Separate a broad market estimate from a realistic initial customer pool.

Use available `deep-research` for substantial evidence work; otherwise capture claim, original source and locator, date, scope, limitations, and confidence. A primary vendor page supports advertised capabilities, not independent efficacy. Multiple retellings of the same claim are one source chain. If research is unavailable, label external assumptions as unverified.

## Commercial feasibility (only when relevant)

| Module | Questions that change a decision |
|---|---|
| Buyer and model | Who uses, pays, approves, renews? What is sold and when does value occur? |
| Acquisition | Which reachable channel matches the buyer? What gatekeepers, sales cycle, channel costs, or platform dependence apply? |
| Retention | What recurring job brings users back? What switching friction or onboarding delays prevent first value? |
| Economics | Price, variable delivery cost, support, refunds, payment fees, infrastructure, margins, acquisition spend, payback |
| Defensibility | Data rights, distribution, network effects, workflow integration, community, operational learning; AI or first-mover status alone is not a moat |

Estimate with ranges and explicit assumptions, not invented precision. Early-stage LTV based on guessed retention is a scenario, not a measured metric. Separate gross revenue, gross margin, contribution margin, profit, and founder labor. Use sensitivity analysis on the assumptions most likely to reverse viability. Name relevant single points of failure.

## Software and AI feasibility

Classify required components as **verified**, **plausible**, **uncertain**, or **blocker**, with evidence or a test for each important uncertainty. Existing API documentation does not prove credentials, entitlement, rate limits, or the intended endpoint will work for this user.

Consider only required components: client, backend, database, auth, queue, storage, search, model, external API, deployment, and observability. Do not prescribe a vector database or distributed system by default. Choose the simplest architecture that can test the core behavior within the user's stack and constraints.

Investigate dependency policies, supported interfaces, licensing, version changes, quotas, pricing, app-store restrictions, lock-in, and fallback paths where material. A promising integration remains unverified until the relevant call is exercised or the limitation is disclosed.

For AI components examine:

- Why a deterministic method is insufficient and where human review belongs.
- Expected inputs, output contract, representative evaluation set, baseline, and failure cost.
- Hallucination, prompt injection, data disclosure, tool authority, and recovery when relevant.
- Latency, token and non-token costs, worst-case usage, availability, quality drift, and fallback.
- Difference between demo quality, measured task success, and reliable deployment.

Security depth follows actual data and action risk. Identify material auth, authorization, secrets, privacy, abuse, and data-lifecycle concerns without turning every idea evaluation into a full security audit.

## Creator, content, and digital products

Use when the idea depends on content, templates, courses, influencers, affiliate offers, or paid communities.

Map attention → intent → offer → purchase → repeat value. Check audience fit, credibility of the promised transformation, production cost, distribution dependence, and whether reach reaches a buyer. Compare CTR, conversion, average order value, refund rate, contribution margin, and retention at the relevant funnel stages. Metrics from different denominators cannot be compared directly.

Revenue screenshots and creator claims remain unverified until backed by inspectable evidence; distinguish revenue from profit and owned revenue from affiliate volume. Evaluate policy, copyright, brand trust, audience fatigue, character consistency for synthetic personas, and off-platform access where relevant. Do not publish, contact people, buy traffic, or collect leads as part of analysis without authorization.

## Failure analysis and counter-evidence

First state the strongest fair case for the idea. Then identify the load-bearing assumptions and prioritize plausible failure modes by impact, likelihood, and cost of learning. Avoid numeric probability scores without a basis.

Examples: low pain, no reachable payer, onboarding friction, weak retention, high support cost, blocked API, inaccessible distribution, inaccurate AI output, unaffordable usage, incumbent response, or obligations incompatible with the team's resources.

For decisive assumptions actively seek independent evidence against them: analogous failures, churn, documented restrictions, realistic economics, and stronger substitutes. Do not fabricate a case for DROP, infer the founder's hidden motives, or require a pivot when evidence supports the original idea. Red-team mode should test the idea fairly, not reward hostility.

For each serious risk return evidence, mechanism, impact, mitigation if credible, and the observation that would alter the decision. A lack of evidence does not prove failure; it may justify a bounded experiment.

## Improve without scope drift

Offer stronger variants only when they address a specific weakness: narrower buyer, lower switching cost, simpler workflow, cheaper delivery, different channel, or an alternative business model. Explain the tradeoff and compare against the original goal. Label optional variants; preserve the user's selected direction unless they authorize changing it.

Visual identity can matter for marketing or portfolio goals. Operational software may appropriately use familiar components and a neutral system font. Do not treat screenshot uniqueness as a universal business requirement. Use `design` when UI work is actually in scope.

## MVP and experiment design

The smallest useful test targets the largest actionable uncertainty. It may be a prototype, manual service, offline benchmark, interview guide, landing-page draft, CLI, pilot plan, or a narrow functioning slice. A mockup cannot prove retention; a waitlist cannot prove payment; an interview cannot prove real behavior.

For each chosen experiment record:

| Field | Meaning |
|---|---|
| Assumption | Exact falsifiable proposition |
| Evidence needed | Observable outcome and relevant participant/workload |
| Test | Cheapest credible method and comparison/baseline |
| Measurement | Denominator, instrument, sampling limits, time window |
| Decision rule | Justified success/failure/inconclusive conditions |
| Next action | Continue, revise, collect missing evidence, or stop |
| Constraints | Resources, permissions, participant/data boundaries |

Thresholds are proposals unless agreed. Tie them to decision costs and baseline; do not invent a universal target such as ten paid signups. Respect research ethics and authorization for contact, data collection, payment, or publication.

## Independent evaluation agents

For a substantial evaluation, useful separate assignments are a demand/substitutes investigator, a technical/dependency investigator, and a skeptical economics or counter-evidence reviewer. Use only the roles that reduce important uncertainty. Assign each one a question, input evidence, boundaries, required source locators, and an effort limit. Share raw evidence rather than a desired verdict. The parent evaluates tradeoffs, verifies decisive facts, and owns the recommendation; agreement among agents is not market evidence.

## Output

Lead with a verdict scoped to the user's objective: **BUILD**, **TEST FIRST**, **REWORK**, **PIVOT**, or **DROP**, or a more suitable direct answer for a focused mode. Explain the decisive reasons, strongest evidence and limitations, critical assumptions, feasible MVP/test, optional stronger variant, and immediate next actions. Give claim-specific confidence with reasons rather than one confident label for an uncertain whole.

A BUILD recommendation is not authorization to implement. When implementation was already explicitly authorized, do not create a fresh approval gate merely because evaluation happened along the way.
