# Part 2 — Secrets (SOPS + age + 1Password)

Part of security. Works standalone.


# SOPS + age + 1Password project secrets

Protect project secrets while keeping an encrypted dotenv file in Git.

Path convention: `<skill-base>` in the examples below is the installed skill folder — typically `~/.agents/skills/security`; substitute the real path when running the commands.

Use **1Password as the primary synchronized vault** for portable age identities and developer credentials.

Use **SOPS + age** to encrypt project environment files that need to be safely committed to Git.

Support four identity profiles:

1. `1password-portable` — recommended for personal multi-device use. A regular age identity is stored in 1Password and provisioned to SOPS at runtime through 1Password CLI.
2. `portable-file` — regular age identity stored outside the repository in a local private file. Use when 1Password is unavailable or explicitly not desired.
3. `mac-secure-enclave` — device-bound age-plugin-se identity protected by macOS Secure Enclave and normally unlocked with Touch ID/passcode.
4. `hybrid` — Secure Enclave for local Mac usage plus a synchronized 1Password recovery recipient and/or a dedicated CI recipient.

For a user who wants seamless recovery on another device after signing into 1Password, **`1password-portable` is the default recommendation**.

For maximum device-bound protection on a primary Mac, use `hybrid`.

A Secure Enclave identity cannot be synchronized or moved to another Mac.

## Requirements

Base requirements:

- macOS or Linux
- shell
- Git
- Python 3.9+
- SOPS
- age

For `1password-portable`:

- 1Password account
- 1Password desktop application
- 1Password CLI (`op`)
- CLI integration authenticated through the user's 1Password account

For Secure Enclave:

- macOS 14+
- Secure Enclave capable Mac
- age-plugin-se
- SOPS version supporting age plugins

## Trust model

Understand the difference between storage layers.

### 1Password

1Password is the synchronized private vault.

It may contain:

- passwords
- passkeys
- OTP/TOTP
- SSH private keys
- API tokens
- GitHub PATs
- database credentials
- portable age identities
- recovery identities

The user can sign into 1Password on another authorized device and recover synchronized portable secrets.

### SOPS

SOPS does not replace the vault.

It encrypts structured files such as:

- `.env`
- YAML
- JSON
- INI

The encrypted result may be committed to Git.

### age

age provides recipients and identities used by SOPS to protect the SOPS data key.

Public recipients may be committed.

Private identities must never be committed.

### Secure Enclave

An age-plugin-se private key is device-bound.

It provides stronger protection against key extraction but intentionally does not synchronize.

## Recommended architecture

For normal personal development:

```text
1Password
├── passwords
├── passkeys
├── OTP
├── SSH keys
├── API tokens
├── GitHub PATs
└── SOPS age identity
        │
        ↓
     1Password CLI
        │
        ↓
       SOPS
        │
        ↓
    .env.sops
        │
        ↓
      GitHub
```

On a new authorized device:

```text
Install 1Password
→ sign in
→ install op + sops + age
→ authenticate CLI
→ clone repository
→ decrypt .env.sops
```

No manual copying of the portable age private key between devices should be necessary.

## Non-negotiable safety boundary

- Never print, paste into chat, commit, stage, log, or put directly on a command line an `AGE-SECRET-KEY-*` or `AGE-PLUGIN-SE-*` identity.
- Never place an age private identity directly in a shell command argument.
- Never reveal the value returned by `op read`.
- Do not use `echo "$(op read ...)"` or equivalent constructs that may expose the identity through shell debugging, history, logs, or accidental output.
- Prefer `op run` with `SOPS_AGE_KEY` secret references when using 1Password.
- Treat 1Password secret references such as `op://Vault/Item/field` as configuration metadata, not as secret values. Avoid committing them when vault/item names themselves are sensitive.
- Never display dotenv values during discovery, examples, logs, or verification.
- Report only paths, variable names, finding categories, public recipients, and commit/blob IDs.
- Never store a portable age identity in the repository, including encrypted-to-itself schemes.
- Do not delete the last tested working recipient.
- Verify decryption through a new recipient before removing an old recipient.
- Encryption does not revoke an exposed application credential.
- If plaintext reached any commit, fork, log, artifact, cache, issue, CI output, or PR, rotate/revoke that application credential at the provider.
- Do not rewrite shared Git history automatically.
- Explain coordination and use `git filter-repo` only after explicit approval and a verified backup.
- Do not enable secret decryption for workflows triggered by untrusted forks or `pull_request_target` code.
- Do not give GitHub Actions access to the user's main personal age identity.
- Use a dedicated CI recipient whenever CI needs to decrypt SOPS files.
- Do not claim that “only the user can decrypt” when CI, recovery, another device, or another recipient can also decrypt.

## Start every run

1. State the operation:
   - `migrate`
   - `bootstrap`
   - `audit`
   - `onboard-device`
   - `rotate`

2. State the intended identity profile:
   - `1password-portable`
   - `portable-file`
   - `mac-secure-enclave`
   - `hybrid`

3. Unless the user explicitly requests otherwise, prefer:
   - `1password-portable` for synchronized personal development;
   - `hybrid` when device-bound Secure Enclave protection is explicitly desired.

4. Inspect repository status, ignore rules, candidate env filenames, tracked paths, and Git history without printing secret values.

5. Read `references/03-platform-and-keys.md` when:
   - installing tools;
   - configuring 1Password CLI;
   - choosing an identity profile;
   - onboarding a new machine.

6. Read `references/04-github-actions.md` for CI/CD.

7. Read `references/05-incident-response.md` if any plaintext secret may have been committed.

8. Prefer bundled scripts for deterministic setup and scanning.

9. Review planned writes before running scripts inside a user's repository.

# Identity profile: 1password-portable

This is the default profile for users who want secrets to synchronize across their authorized devices.

## Storage

Generate one regular age identity.

Store:

- the **private age identity** in a dedicated 1Password item;
- the **public age recipient** in `.sops.yaml`.

Recommended 1Password structure:

```text
Vault: Developer Secrets

Item: SOPS Personal Age Identity

Fields:
- private-key     [concealed]
- recipient       [text]
- purpose         [text]
```

Never store the private identity in `.sops.yaml`.

Never commit it.

## Provisioning to SOPS

Prefer providing the identity through `SOPS_AGE_KEY` at runtime.

Create a local environment mapping that contains a **1Password secret reference**, not the actual private key.

Example conceptual mapping:

```text
SOPS_AGE_KEY=op://Developer Secrets/SOPS Personal Age Identity/private-key
```

Then run SOPS under 1Password CLI:

```bash
op run --env-file=/absolute/private/sops-1password.env -- \
  sops .env.sops
```

The local mapping file contains only an `op://` reference.

It must not contain the actual `AGE-SECRET-KEY-*` value.

For application execution:

```bash
op run --env-file=/absolute/private/sops-1password.env -- \
  sops exec-env .env.sops 'your-start-command'
```

This allows 1Password CLI to inject `SOPS_AGE_KEY` into the SOPS process environment without maintaining a permanent plaintext age identity file.

SOPS supports receiving age identities through `SOPS_AGE_KEY`.

## Local 1Password reference file

Recommended path:

```text
~/.config/sops/1password.env
```

Example contents:

```text
SOPS_AGE_KEY=op://Developer Secrets/SOPS Personal Age Identity/private-key
```

Protect it even though it contains only a reference:

```bash
chmod 600 ~/.config/sops/1password.env
```

Do not place this file inside a project repository.

Do not commit it.

## Alternative: SOPS_AGE_KEY_CMD

SOPS also supports `SOPS_AGE_KEY_CMD`.

A wrapper may retrieve the identity from 1Password and return it directly to SOPS.

Use this only through a reviewed helper script.

The helper must:

- invoke `op` directly;
- output only the requested age identity to stdout;
- never log it;
- never invoke shell tracing;
- never write it to disk;
- fail closed when 1Password authentication fails.

Do not dynamically build shell command strings containing secrets.

Prefer the simpler `op run + SOPS_AGE_KEY` method unless there is a clear reason to use `SOPS_AGE_KEY_CMD`.

# Identity profile: portable-file

Use when 1Password is unavailable or explicitly not desired.

Generate an age identity outside the repository:

```bash
<skill-base>/scripts/create_age_identity.sh portable --output /absolute/private/identity.txt
```

Store it in an operating-system-private path.

Set permissions to owner-only.

Use:

```bash
SOPS_AGE_KEY_FILE=/absolute/private/identity.txt \
  sops .env.sops
```

This profile does not automatically synchronize the identity.

The user is responsible for secure backup and device transfer.

# Identity profile: mac-secure-enclave

Use only on a compatible Mac.

Install:

- age
- sops
- age-plugin-se

Generate outside Git:

```bash
<skill-base>/scripts/create_age_identity.sh secure-enclave \
  --output "/absolute/private/sops-se-identity.txt" \
  --access-control any-biometry-or-passcode
```

The identity file is a private plugin handle.

The underlying private key remains in the Secure Enclave.

Losing or replacing the Mac can make that recipient permanently unusable.

This profile does not satisfy seamless cross-device synchronization.

Always add a separate recovery recipient for long-lived data.

For strict biometric behavior, `any-biometry` may be used only when:

- explicitly requested;
- a recovery recipient exists;
- recovery has been tested.

`current-biometry` may stop working after biometric enrollment changes.

Do not use it without an explicit recovery plan.

# Identity profile: hybrid

Use when the user wants both:

- Secure Enclave protection on the primary Mac;
- recovery or synchronization through 1Password.

Recommended recipients:

```text
Recipient 1:
Mac Secure Enclave

Recipient 2:
1Password portable recovery identity

Recipient 3:
Dedicated CI identity, only when required
```

Any corresponding private identity can decrypt.

Therefore do not describe this mode as “Secure Enclave only”.

Recommended architecture:

```text
.env.sops
   │
   ├── age-plugin-se recipient
   │      ↓
   │   Primary Mac
   │   Secure Enclave
   │   Touch ID
   │
   ├── portable age recipient
   │      ↓
   │   1Password
   │   synchronized recovery
   │
   └── CI recipient
          ↓
       GitHub Actions
```

# Mode 1: migrate an existing project

## 1. Inventory safely

Locate likely plaintext files:

- `.env`
- `.env.local`
- `.env.production`
- `.env.development`
- `*.env`
- framework-specific dotenv variants

Exclude:

- `.env.example`
- `*.example`
- `.env.sops`
- `*.sops.*`
- already encrypted files

List variable names only.

Never display values.

If more than one active dotenv file exists, map each file to its runtime before choosing what to encrypt.

Do not silently merge environment-specific secrets.

Run:

```bash
python3 <skill-base>/scripts/scan_git_secrets.py \
  --repo . \
  --scope all
```

Exit code `2` means potential exposure was found.

Treat it as a security finding, not a script crash.

## 2. Select recipients

### 1password-portable

Use an existing public recipient associated with the age identity stored in 1Password, or generate a new portable identity and store it in 1Password before continuing.

Verify that the private identity can be retrieved through `op run` without displaying it.

### portable-file

Use an existing public `age1...` recipient or generate a private identity outside the repository.

### mac-secure-enclave

Generate a device-bound identity with the bundled Secure Enclave helper.

### hybrid

Collect:

- Secure Enclave recipient;
- 1Password recovery recipient;
- dedicated CI recipient, if CI decrypts.

Only public recipients belong in `.sops.yaml`.

## 3. Create Git-safe structure

Run:

```bash
<skill-base>/scripts/setup_sops_age.sh migrate \
  --repo . \
  --env-file .env \
  --recipient age1...
```

For multiple recipients:

```bash
<skill-base>/scripts/setup_sops_age.sh migrate \
  --repo . \
  --env-file .env \
  --recipient age1... \
  --recipient age1se1... \
  --recipient age1...
```

The script:

- adds plaintext dotenv guardrails to `.gitignore`;
- adds age identity filename patterns to `.gitignore`;
- creates a redacted `.env.example` containing names with empty values;
- creates `.sops.yaml` containing only public recipients;
- encrypts the selected dotenv file into `.env.sops`;
- removes the plaintext env path from the current Git index while leaving the local file on disk;
- never rewrites Git history;
- never rotates provider credentials.

Review `.env.example`.

Restore only clearly non-secret development defaults.

Never copy tokens, passwords, private URLs, credentials, or connection strings containing credentials into it.

## 4. Verify with 1Password

For `1password-portable`:

```bash
op run --env-file="$HOME/.config/sops/1password.env" -- \
  <skill-base>/scripts/setup_sops_age.sh verify --repo .
```

The verification script must allow SOPS to use `SOPS_AGE_KEY` inherited from its environment.

Do not require an identity file when `SOPS_AGE_KEY` is already present.

Then run:

```bash
python3 <skill-base>/scripts/scan_git_secrets.py \
  --repo . \
  --scope all

git diff --cached --name-only
```

Verify:

- `.env.sops` decrypts;
- `.env` is ignored;
- `.env` is absent from the Git index;
- no age identity is tracked;
- `.env.example`, `.env.sops`, and `.sops.yaml` are intended to be tracked;
- no command output contains secret values.

For hybrid mode, test every required recovery path independently.

If Git history findings exist, follow incident response before claiming completion.

# Mode 2: bootstrap a new project

## 1. Choose identity profile

Default:

```text
1password-portable
```

unless the user explicitly requests device-bound Secure Enclave protection.

## 2. Bootstrap

Run:

```bash
<skill-base>/scripts/setup_sops_age.sh bootstrap \
  --repo . \
  --recipient age1...
```

## 3. Edit encrypted values

For 1Password:

```bash
op run --env-file="$HOME/.config/sops/1password.env" -- \
  sops .env.sops
```

For portable-file:

```bash
SOPS_AGE_KEY_FILE=/absolute/private/identity.txt \
  sops .env.sops
```

For Secure Enclave, use the configured plugin identity.

## 4. Run application without plaintext .env

Preferred:

```bash
op run --env-file="$HOME/.config/sops/1password.env" -- \
  sops exec-env .env.sops 'your-start-command'
```

Do not invent the start command.

Discover the actual package manager, runtime, Docker command, Make target, or executable first.

## 5. Framework requires a file

If the framework cannot consume environment variables:

- prefer `sops exec-file`;
- prefer FIFO-based behavior where supported;
- otherwise decrypt to a restrictive temporary location;
- set owner-only permissions;
- install a cleanup trap;
- remove the file on normal exit and signals;
- never write plaintext output inside the repository;
- never stage the plaintext path.

# Mode 3: onboard a new device

Use for a user who has cloned a repository on another authorized machine.

## 1password-portable onboarding

1. Install 1Password desktop application.
2. Sign into the existing account.
3. Install 1Password CLI.
4. Authenticate CLI integration.
5. Install age and SOPS.
6. Create the local `~/.config/sops/1password.env` mapping containing only the `op://` secret reference.
7. Set owner-only permissions.
8. Clone or open the repository.
9. Test decryption without printing plaintext:

```bash
op run --env-file="$HOME/.config/sops/1password.env" -- \
  sops filestatus .env.sops
```

Then perform a controlled decryption verification whose plaintext output is discarded or consumed by a non-logging verification helper.

Do not use `sops -d .env.sops` directly during verification because it prints secrets to stdout.

10. Report that the synchronized 1Password identity path works.

## Secure Enclave onboarding

A new Mac needs a new age-plugin-se identity.

Do not attempt to copy the original Secure Enclave identity.

Procedure:

1. generate a new Secure Enclave recipient;
2. decrypt using an existing recovery recipient;
3. add the new public recipient to `.sops.yaml`;
4. run `sops updatekeys`;
5. verify decryption with the new Mac;
6. keep or remove old Mac recipients according to the user's device-retirement plan.

# GitHub Actions / CI profile

CI must not use the user's personal 1Password login session.

CI must not use the user's Secure Enclave identity.

Use one of two explicit designs.

## CI design A: dedicated age identity in GitHub Actions secret

Recommended for simple personal repositories.

Create a dedicated regular age identity only for CI.

Store its private identity in a GitHub Actions secret such as:

```text
SOPS_AGE_KEY
```

Store only its public recipient in `.sops.yaml`.

Then:

```text
GitHub Actions secret
       ↓
SOPS_AGE_KEY
       ↓
SOPS
       ↓
.env.sops
```

The CI recipient is an additional trusted decryption path.

Do not say “only I can decrypt” when this recipient exists.

## CI design B: 1Password automation

Use only when the user's 1Password plan and account configuration support the required automation mechanism.

Use a dedicated automation identity/service account with access only to a dedicated CI vault.

Never grant CI access to the user's general Personal/Private vault.

Do not assume availability of service accounts on every 1Password subscription.

Check the current 1Password plan and supported automation method before configuring this mode.

## CI safety rules

- Never decrypt on untrusted fork code.
- Never expose secrets to `pull_request_target` execution of untrusted changes.
- Restrict GitHub environments and repository permissions.
- Pin third-party actions to reviewed versions or commit SHAs where appropriate.
- Do not print decrypted environment variables.
- Prefer `sops exec-env`.
- Keep CI recipients separate from personal recipients.
- Rotate CI identities independently.

Start from:

```text
assets/github-actions-sops.yml
```

Replace the application command.

Review current action and SOPS versions before committing.

# Recipient rotation

## Rotate portable 1Password identity

1. Generate a new regular age identity.
2. Store the new private identity in 1Password.
3. Record the new public recipient.
4. Keep the old private identity available.
5. Add the new public recipient to `.sops.yaml`.
6. Run:

```bash
sops updatekeys .env.sops
```

under a working identity.

7. Test decryption using only the new 1Password identity.
8. Remove the old public recipient from `.sops.yaml`.
9. Run `sops updatekeys` again.
10. Remove/archive the old private identity from 1Password only after successful verification.
11. If compromise is suspected, renew the SOPS data key:

```bash
sops rotate -i .env.sops
```

12. Rotate actual application credentials separately when their plaintext may have been exposed.

## Rotate Secure Enclave recipient

1. Add the new Secure Enclave public recipient.
2. Run `sops updatekeys`.
3. Verify on the new device.
4. Remove the old public recipient.
5. Run `sops updatekeys` again.
6. Retire the old device identity.

## Rotate CI recipient

Treat CI as a separate security principal.

Rotate it without rotating the user's portable personal identity unless compromise scope requires both.

# 1Password usage rules

## Allowed

Store in 1Password:

- portable age private identities;
- SSH private keys;
- GitHub PATs;
- API keys;
- OTP seeds;
- passwords;
- recovery credentials.

Use:

```text
op://Vault/Item/field
```

secret references.

Use `op run` to inject secrets into process environments.

## Forbidden

Never:

```text
op read ... > repository-file
```

unless explicitly using a secured temporary-file workflow.

Never:

```text
echo "$(op read ...)"
```

Never:

```text
export SOPS_AGE_KEY="$(op read ...)"
```

in an interactive shell where shell tracing/history/logging could expose it.

Prefer:

```bash
op run --env-file="$HOME/.config/sops/1password.env" -- \
  sops ...
```

Do not log the resulting environment.

Do not inspect `SOPS_AGE_KEY`.

Do not run `env`, `printenv`, shell tracing, or debug tooling that dumps process environments while secrets are injected.

# Git-safe repository structure

Recommended:

```text
project/
├── .gitignore
├── .sops.yaml
├── .env.example
├── .env.sops
└── source...
```

Never commit:

```text
.env
.env.local
.env.production
age identity files
1Password exports
1Password emergency kit
temporary decrypted files
```

`.sops.yaml` may contain public age recipients.

`.env.sops` may contain encrypted secret values.

`.env.example` may contain variable names and safe non-secret defaults.

# What “synchronized” means

For `1password-portable`:

```text
Mac #1
   ↓
1Password encrypted vault
   ↓
Mac #2 / Linux / Windows
```

The portable age identity is recoverable after authorized sign-in.

For `mac-secure-enclave`:

```text
Mac #1 Secure Enclave
```

The private key does not synchronize.

For `hybrid`:

```text
Secure Enclave recipient
+
1Password portable recovery recipient
```

The first is device-bound.

The second is synchronized.

Be explicit about this distinction in completion reports.

# Incident handling

If `.env` or another plaintext secret file may ever have been committed:

1. do not assume SOPS migration fixes the exposure;
2. identify affected files and commits without printing values;
3. determine whether the repository was pushed or shared;
4. rotate affected credentials at their providers;
5. remove plaintext from the current index;
6. discuss Git history rewriting separately;
7. do not rewrite shared history without explicit approval and backup.

# Completion report

Report:

- operation:
  - migrate
  - bootstrap
  - audit
  - onboard-device
  - rotate

- identity profile:
  - 1password-portable
  - portable-file
  - mac-secure-enclave
  - hybrid

- files created or modified, without values;

- public recipient types only:
  - personal portable age
  - 1Password recovery
  - age-plugin-se
  - CI

- whether 1Password CLI provisioning was actually tested;

- whether decryption was tested without printing plaintext;

- current Git index scan result;

- Git history scan result;

- decryption paths actually tested;

- whether another synchronized device was tested;

- credentials requiring provider-side rotation;

- unverified:
  - CI
  - backup
  - Touch ID
  - recovery
  - secondary-device onboarding

Never report:

```text
"only you can decrypt"
```

when any recovery, synchronized secondary identity, CI recipient, automation identity, or other recipient also has access.

Instead say exactly which trust paths can decrypt.
