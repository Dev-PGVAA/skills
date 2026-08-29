---
name: security
description: >
  Security for AI products and project secrets, in two invokable parts.
  Audit — evidence-driven audit and threat modeling of AI agents, LLM applications,
  RAG pipelines, MCP servers, tools and multi-agent systems; treats the model as
  untrusted, tests prompt injection and attack chains, maps findings to OWASP
  GenAI LLM Top 10 2026 and OWASP Top 10 for Agentic Applications (ASI01–ASI10)
  plus MITRE ATLAS, and produces a P0–P2 remediation roadmap with runtime
  guardrail recommendations. Secrets — migrate plaintext .env files into Git-safe
  SOPS + age encrypted files with 1Password as the synchronized identity vault
  (or macOS Secure Enclave), add GitHub Actions decryption, audit Git history for
  leaks, onboard devices and rotate recipients without ever printing secret values.
  Invoke a part by name. Triggers include security audit, threat model, red-team,
  prompt injection, excessive agency, memory poisoning, secure secrets, .env, sops,
  OWASP LLM, agentic security.
---

# Security — audit AI systems, protect project secrets

Two parts, one domain. Load the part that matches the task.

## Parts

| Part | File | Invoke for |
|---|---|---|
| `audit` | `references/01-audit.md` | Threat-model and audit an AI/LLM/agent/MCP system; prompt injection, exfiltration, blast radius, excessive agency, memory poisoning |
| `secrets` | `references/02-secrets.md` | SOPS + age setup, .env migration, 1Password identities, CI decryption, rotation, incidents |

## How to invoke

- User names a part (or asks for an audit / encrypt the env) → load that part’s file and follow it.
- `secrets` deeper references load on demand — `references/03-platform-and-keys.md`, `references/04-github-actions.md`, `references/05-incident-response.md`. Scripts in `scripts/`, CI template in `assets/`.
- Audit modes escalate only with explicit authorization — PASSIVE → SAFE_ACTIVE → AUTHORIZED_RED_TEAM.

## 2026 framework anchors (audit)

Map findings to:

**OWASP GenAI LLM Top 10 2026** (high-level):
1. Prompt Injection
2. Sensitive Information Disclosure
3. Excessive Agency
4. Supply Chain
5. Data and Model Poisoning
6. Unbounded Consumption
7. Misinformation
8. Hidden Context Exposure
9. Vector and Embedding Weaknesses
10. Improper Output Handling

**OWASP Top 10 for Agentic Applications (ASI)**:
- ASI01 Agent Goal Hijack
- ASI02 Tool Misuse & Exploitation
- ASI03 Identity & Privilege Abuse
- ASI04 Agentic Supply Chain Vulnerabilities
- ASI05 Unexpected Code Execution
- ASI06 Memory & Context Poisoning
- ASI07 (and remaining entries for inter-agent, cascading failures, rogue agents, human-agent trust exploitation)

Also reference MITRE ATLAS techniques where applicable.

Hard boundary for both parts: never print or log secret values; report paths, names and recipient types only; never claim testing that did not happen. Security must hold even when the model behaves incorrectly.
