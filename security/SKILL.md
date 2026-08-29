---
name: security
description: Security for AI products and project secrets, in two invokable parts. Audit — evidence-driven audit and threat modeling of AI agents, LLM applications, RAG pipelines, MCP servers, tools and multi-agent systems; treats the model as untrusted, tests prompt injection and attack chains, maps findings to OWASP LLM / Agentic Top 10 and MITRE ATLAS, and produces a P0–P2 remediation roadmap. Secrets — migrate plaintext .env files into Git-safe SOPS + age encrypted files with 1Password as the synchronized identity vault (or macOS Secure Enclave), add GitHub Actions decryption, audit Git history for leaks, onboard devices and rotate recipients without ever printing secret values. Invoke a part by name. Triggers include security audit, threat model, red-team, prompt injection, secure secrets, .env, sops.
---

# Security — audit AI systems, protect project secrets

Two parts, one domain. Load the part that matches the task.

## Parts

| Part | File | Invoke for |
|---|---|---|
| `audit` | `references/01-audit.md` | Threat-model and audit an AI/LLM/agent/MCP system; prompt injection, exfiltration, blast radius |
| `secrets` | `references/02-secrets.md` | SOPS + age setup, .env migration, 1Password identities, CI decryption, rotation, incidents |

## How to invoke

- User names a part (or asks for an audit / encrypt the env) → load that part's file and follow it.
- `secrets` deeper references load on demand — `references/03-platform-and-keys.md` (installs, 1Password CLI, identity profiles), `references/04-github-actions.md` (CI), `references/05-incident-response.md` (leaked plaintext). Scripts live in `scripts/`, CI template in `assets/`.
- Audit modes escalate only with explicit authorization — PASSIVE → SAFE_ACTIVE → AUTHORIZED_RED_TEAM.

Hard boundary for both parts: never print or log secret values; report paths, names and recipient types only; never claim testing that did not happen.
