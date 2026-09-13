# Evidence-driven AI security audit

## Scope and test mode

Record the target repository/revision or service, actors/tenants, assets, permitted operations, data sensitivity, and required deliverable. Establish enough architecture to follow the attacker's input to the protected operation. Read-only scope stays read-only.

- **PASSIVE:** source/configuration/documentation analysis; no live payloads.
- **SAFE_ACTIVE:** authorized isolated or non-destructive tests with synthetic tenants, canary values, and controlled destinations. Local fixture tests within an authorized review need no separate ritual approval.
- **AUTHORIZED_RED_TEAM:** broader adversarial testing only within an explicitly established target and impact scope. Set rate/cost ceilings, cleanup, evidence handling, and stop conditions before execution.

Use the authorization already present. If one live test is unauthorized or unsafe, continue passive/local work and report that specific gap. Stop the affected test if it reaches an unrelated tenant, exposes real secrets, threatens availability, or crosses scope. Do not turn a request for source review into a mandatory production audit.

## Build a minimal threat model

For each meaningful flow capture:

`attacker-controlled input → trust transition → agent/tool identity → protected resource → possible impact`

Inventory real entrypoints, data stores, models, agents, tools/MCP servers, external I/O, execution environments, and observability. Classify tool effects (pure compute, public read, sensitive read, external write, privileged/destructive). Compare the user's permissions with the credentials actually used by each tool, including workers and background jobs.

Treat retrieved content, memory, peer output, skills, and tool descriptions as untrusted task data. Follow provenance through URLs, shell/SQL arguments, identifiers, filenames, and outbound channels. A prompt injection is security-relevant when it reaches a protected operation; model obedience alone does not establish impact.

## Risk-driven inspection matrix

Use rows that exist in this system. Mark uninspected relevant rows `NOT_TESTED` and absent surfaces `NOT_APPLICABLE`, with a reason. No need to force every framework category into every finding.

| Surface | Concrete checks and test direction |
|---|---|
| Identity and authorization | Verify server-side per-user/per-tenant authorization at the final resource access, token audience, delegated scopes, stale permissions, role changes, confused deputy, IDOR/BOLA; test denied and allowed cases. |
| Agent/user mismatch | Trace whether a low-privilege caller can induce a stronger service identity to act. Check caller identity propagation through queue, cache, tool, and subagent. |
| Direct/indirect injection | Place synthetic instructions in the actual untrusted entrypoint: user input, document, webpage, image, email, metadata, or tool output. Observe the downstream policy/tool decision, including encoded/multilingual forms when relevant. |
| RAG and vectors | Check ingestion provenance and permissions, retrieval-time ACLs, cross-tenant filters, cache keys, metadata leakage, poisoned citations, deletion/revocation propagation, and stale embeddings. |
| Memory/context | Check who can create/read/update memory, scope and provenance, persistent instructions, cross-session/tenant contamination, deletion/retention, and whether suggested preferences become privileged policy. TTL is context-dependent, not universally required. |
| Tool arguments | Validate types and semantic constraints at execution; test path traversal, command/SQL/template/header injection, deserialization, parser ambiguity, and untrusted URLs only where the tool supports that surface. |
| SQL agents | Prefer a constrained domain API and database least privilege. Inspect tenant constraints, parameterization, metadata access, writes/schema changes, query cost, stored procedures, and duplicate side effects. |
| Network/SSRF | Check schemes, redirect hops, DNS/IP binding and rebinding defenses, IPv6/alternate forms, internal ranges, metadata access, and egress enforcement. DNS validation disconnected from the actual connection can race; use controlled local fixtures, not real metadata credentials. |
| Code/sandbox | Verify OS/container boundary, mounted secrets, host/Docker sockets, non-root identity, filesystem scope, outbound access, lifecycle cleanup, CPU/memory/process/disk/time limits. A declared sandbox is not proof of isolation. |
| MCP | Inspect transport-appropriate authentication, OAuth audience/scopes/redirects/state, consent, token passthrough, tool/resource/prompt metadata, roots and real filesystem enforcement. Local stdio and remote HTTP have different trust models. |
| Cross-tool/server chains | Combine sensitive read access in one tool with external send/write in another. Check whether provenance, destination, data classification, and principal survive the transition. |
| Multi-agent systems | Inspect task ownership, peer identity, message integrity, authority propagation, shared state, recursive delegation, compromised worker output, cancellation and revocation. Parent/worker messages do not become trusted policy merely by transit. |
| Excessive agency | Compare required functionality/autonomy with actual read/write/execute/send capability. Limit impact outside the model; broad capability is a risk to evaluate, not automatically a vulnerability. |
| Approval workflows | Bind approval to exact action, principal, resource/destination, data, and effect. Test action changes after approval, replay, ambiguous UI, cancellation, and time-of-check/time-of-use races. Respect prior scoped approval. |
| Output consumers | Trace model text into HTML/Markdown, shell, SQL, templates, spreadsheets, URLs, and generated code. Verify escaping/validation for the actual sink rather than generic sanitization. |
| Exfiltration | Trace HTTP, DNS, email/chat, tool parameters, issue text, telemetry/logs, filenames, images/QRs and links. Use synthetic canaries and controlled sinks; do not transmit real protected data. |
| Secrets | Inspect injection paths, process environments, logs/traces, crash dumps, prompts, caches and persistence without displaying values. Credential access should stay outside model context where possible. |
| Supply chain | Inspect origins, pinned revisions/hashes, lockfiles, dependency install scripts, models/adapters, container images, MCP/plugins/skills, datasets and mutable external instructions. Review update/revocation mechanisms. |
| Skills/plugins | Inspect manifests, scripts, remote fetch/exec, privilege requests, metadata, symlinks, cross-platform capability changes, and update drift. Treat arbitrary “AST” labels as local unless verified against an official source. |
| Cost/availability | Check bounded loops/retries/delegation/concurrency, idempotency, deadlines, token/API/query quotas, circuit breakers, backpressure, cancellation, and degraded-mode behavior. Do not run load tests without a suitable scope. |
| Logging/detection | Verify identity/session/tool, resource, allow/deny decision and cause, approval binding, destination, unusual sequences and failure signals. Redact parameters; logging all raw tool arguments can create a new leak. |
| Guardrails | Assess false positives/negatives and representative adversarial inputs separately from access control. A finite passing sample or a classifier cannot establish that injection is impossible. |

## Test and evidence contract

Write only the details required to reproduce and assess the test:

```yaml
id: local-identifier
preconditions: actor permissions and synthetic setup
attacker_control: entrypoint and controlled fields
attack_path: trust transitions and target capability
method: command or exact reproducible procedure
expected: observable secure outcome
observed: actual result or not run
evidence: redacted artifact, source lines, or test output
result: PASS | FAIL | PARTIAL | NOT_TESTED | NOT_APPLICABLE
```

For probabilistic model behavior, record model/configuration, number of attempts, successful violations, and material variability. Do not turn a single failed attack into a prevention rate. Compare a denied test with an allowed control to ensure the system was actually functioning.

Preserve the relevant snapshot and redacted evidence. Avoid copying entire sensitive files or exposing secrets while proving their presence. Automated scanners add coverage but require manual reachability and false-positive checks; install/run them only when appropriate to scope.

## Findings and prioritization

Separate evidence status from severity:

- **Confirmed:** directly reproduced, or deterministic implementation evidence establishes the defect; name which.
- **Likely:** a reachable path has strong evidence, but an important runtime condition remains unverified.
- **Potential / hardening:** a hypothesis or defense-in-depth opportunity; never present it as a demonstrated vulnerability.

Each actionable finding includes component/path/line, trigger and preconditions, boundary crossed, evidence, impact/blast radius, confidence, root cause, minimal mitigation, durable fix, and retest. Group duplicate symptoms by cause. Check potential counter-evidence before reporting.

Severity considers impact, reachability, privilege, interaction, tenant breadth, persistence, and realistic attacker capability. Reserve critical urgency for severe supported paths. Keep remediation priority (P0 immediate, P1 prompt, P2 planned) distinct from confidence; do not present invented CVSS/AIVSS scores.

## Framework mapping and sources

Map only when a verified category actually helps; include the edition and direct source. Do not silently relabel 2025 IDs as 2026, reconstruct numbering from memory, or require a mapping for every observation. Different OWASP landing pages may show different editions.

- [OWASP LLM and GenAI 2026 resource](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)
- [OWASP LLM Top 10 archive](https://genai.owasp.org/llm-top-10/)
- [OWASP Agentic Applications 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [MITRE ATLAS](https://atlas.mitre.org/)
- [MCP security best practices](https://modelcontextprotocol.io/specification/latest/basic/security_best_practices)

Use NIST AI RMF, CWE, CAPEC, or another taxonomy only if requested or useful and the exact reference is verified.

## Deliverable

Lead with the supported risks and affected behavior. For a broad audit, include trust boundaries/attack chains, ranked findings, inspected vs untested coverage, remediation and retest. For a focused review, concise findings plus limitations suffice. An overall rating needs a stated scope and evidence; use “insufficient coverage” when an overall rating would mislead.

The central question is what limits real-world impact after attacker influence succeeds. Passing prompt tests, documentation promises, or a clean scan do not by themselves answer it.
