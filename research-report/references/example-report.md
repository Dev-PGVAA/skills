# Report structures and worked analysis pattern

These are adaptable structures, not sample reports with verified external facts. Choose the arc that matches the reader's job; neither the order nor a section count is mandatory.

## Decision memo

Question and constraints → recommendation with confidence → comparison of realistic options and baseline → economics or implementation tradeoffs → counter-evidence and risks → next decision and evidence needed.

A comparison should keep dimensions comparable: cost period, feature version, geography, evaluation workload, and excluded costs. Unknown data stays unknown. Weights in a scoring model must reflect user priorities; show when rankings reverse under plausible weights.

## Domain analysis

Scope and key conclusions → definitions and system map → mechanisms and institutions → taxonomy of meaningful variants → comparative cases → limitations and competing explanations → practical implications.

A catalog entry earns space through distinctions that matter: eligibility, status, responsibilities, actual mechanism, cost, exceptions, or measured outcome. A longer list is not inherently a better analysis.

## Technical whitepaper

Problem and requirements → baseline → proposed or observed architecture → contracts and data flow → tradeoffs → evaluation method and results → failure modes → limitations and reproducibility.

Distinguish specified, implemented, tested, and deployed behavior. Diagrams must match evidence; benchmark tables need workload and methods. An attractive prototype is not production proof.

## Worked paragraph pattern (hypothetical, not external evidence)

Suppose the supplied dataset contains 80 completed runs out of 100 attempts for option A and 45 out of 50 for B. A has an observed completion rate of 80%; B has 90%. This alone does not establish that B is better: workload composition, sampling uncertainty, and failure severity may differ. The report should show the denominators, compare equivalent workloads, and investigate the failures before recommending migration. It should not turn these observations into a claim about all future workloads.

A good table keeps `completions`, `attempts`, `rate`, `workload`, and `source locator` available. A good narrative explains why the distinction changes the decision. Do not add a certainty label or statistical interval without the data and method to justify it.

## Editorial checks

A paragraph should contribute an observation, mechanism, comparison, qualification, or implication. Remove ornamental introductions, section-ending repeats, and generic strategic imperatives. Figures require units, source, and meaningful captions; tables must remain readable in the chosen format.
