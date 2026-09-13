# GitHub Actions with a dedicated age identity

## Trust model

Touch ID protects only local Mac decryption. CI needs its own portable age identity.

1. Generate a dedicated CI identity outside the repository.
2. Add only its public recipient to `.sops.yaml`.
3. Store the full private identity as a GitHub Actions secret such as `SOPS_AGE_KEY`.
4. Use a protected GitHub Environment for deployment secrets when appropriate.
5. Do not expose the secret to forked PRs, `pull_request_target` execution of untrusted code, debug logs, artifacts, caches, or step outputs.

## Safe workflow shape

Start from `assets/github-actions-sops.yml`. It installs a pinned SOPS version and runs the application command through `sops exec-env`, keeping plaintext out of the checkout. Bind the age identity only to the command step, never to the job or installer steps. The child command removes the identity environment variables before starting the application; encrypted application values are still plaintext in its environment.

Review before use:

- pin actions by a reviewed commit SHA for higher assurance;
- update the pinned SOPS version from the official release page;
- set the actual test/deploy command;
- set minimum `permissions`;
- ensure secret-bearing jobs do not run for untrusted code;
- use environment reviewers for production.

## Updating recipients

After adding the CI recipient:

```bash
sops updatekeys .env.sops
```

Verify locally, then run a protected manual CI test. Do not remove the previous working recipient until both pass.

## Sources

- [GitHub Actions secrets](https://docs.github.com/en/actions/concepts/security/secrets)
- [Using secrets in GitHub Actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
- [SOPS exec-env](https://github.com/getsops/sops)

