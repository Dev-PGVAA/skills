---
name: security
description: Audit security boundaries in AI, agent, RAG, and MCP systems, or manage project secrets with SOPS and age. Use for threat models, scoped security reviews, encrypted dotenv migration, recipient rotation, and secret exposure response.
---

# Security

Find evidence-backed security failures and keep project secrets out of logs and Git. A model, prompt, or classifier is not a deterministic authorization boundary.

## Choose the work

- **Audit:** [audit workflow](references/01-audit.md), then the relevant rows of its domain matrix. A focused review does not require every category or live payload testing.
- **Secrets:** [secret workflows](references/02-secrets.md). Preserve the user's existing vault and identity profile; SOPS+age is a supported option, not a requirement to migrate an already suitable system.
- **Special cases:** [platforms/keys](references/03-platform-and-keys.md), [GitHub Actions](references/04-github-actions.md), [incident response](references/05-incident-response.md).

## Boundaries

Use existing task authorization. Passive review and isolated local tests with synthetic data can proceed within scope; new external targets, destructive tests, real-data exfiltration, shared-history rewriting, and credential revocation require authority for that concrete action. Do not ask again for already-authorized work or treat this skill as granting more permission.

Never print secret values, private identities, or decrypted dotenv contents. Report redacted evidence, paths, categories, public recipient types, and coverage. Do not claim decryption, CI, provider rotation, recovery, or live security testing unless actually verified.

## Parallel audit and verification

Use subagents only for independent, bounded work. Give each the target revision, allowed surfaces, test mode, synthetic fixtures, resource limits, and an evidence contract. Suitable roles: authorization/data-flow reviewer; tool/MCP/sandbox reviewer; independent reproducer for a proposed finding. Keep the parent on cross-boundary attack chains, severity, duplicate removal, and synthesis.

Workers are read-only unless assigned specific isolated fixture files. No worker receives live credentials, expands target scope, or shares sensitive evidence with another service. For secret migrations, the parent alone owns keys, repository writes, and rotation; a worker may inspect scripts or test synthetic fixtures. If delegation is unavailable or unnecessary, use these roles sequentially. Never fan out offensive testing or recursive agents by default.

## Bundled helpers

- `scripts/scan_git_secrets.py`: heuristic Git index/reachable-history scan; findings contain no values. A clean result is not proof that no secrets exist.
- `scripts/setup_sops_age.sh`: scoped root `.env` bootstrap/migration, read-only verification, and audit. Read its help and the secrets reference before mutation.
- `scripts/create_age_identity.sh`: identity generation outside Git with owner-only output.

Helpers have specific coverage limits. Check them and installed tool help before running against user data. Framework IDs and tool releases drift; use current primary sources linked from the references rather than inventing versions.

For helper maintenance, run `python3 tests/test_helpers.py` from this skill directory. Tests use disposable repositories and synthetic values; real SOPS/age checks skip explicitly when those tools are absent.
