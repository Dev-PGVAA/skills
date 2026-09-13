# Project secrets with SOPS and age

## Choose the existing or appropriate identity profile

Do not replace an established suitable secrets system just because this skill is loaded. For SOPS+age, preserve the user's selected vault and recovery constraints:

| Profile | Property / operational consequence |
|---|---|
| `1password-portable` | Portable age identity stored in 1Password; authorized devices retrieve it through `op`. Use when the user has or chooses 1Password and wants synchronization. |
| `portable-file` | Owner-only identity outside repositories; needs secure backup and deliberate device transfer. |
| `mac-secure-enclave` | Device-bound identity; compatible Mac and plugin required. A copied identity cannot move the underlying key to another Mac. |
| `hybrid` | Local device-bound recipient plus portable recovery and optional CI recipient. Every added recipient is another trusted decryption path. |

Use [platform/key guidance](03-platform-and-keys.md) for tooling and device setup. Do not create a new vault subscription or assume 1Password access. SOPS encrypts file values; it does not revoke credentials, hide filenames/variable names, or protect plaintext once used by the application.

## Safe inventory

Confirm repository root, status/index, active environment files and the runtime that consumes each. List paths and variable names only. Do not `cat`, diff, source, or log plaintext dotenv files; comments and malformed/multiline values can contain secrets too. Public `.env.example` should be a reviewed allowlist of variable names and safe defaults.

Run the bundled scanner without printing values:

```bash
python3 <skill-base>/scripts/scan_git_secrets.py --repo . --scope all
```

`<skill-base>` means the actual installed skill directory; substitute its path. Exit `0` means no heuristic matches in the inspected coverage, `2` means potential exposure, `1` means an error/incomplete scan. The scanner covers the index and reachable Git history, not untracked worktree files, remote-only refs, reflogs, deleted unreachable objects, LFS payloads, encrypted/binary data or arbitrary secret formats. Review reported coverage/skips. Use broader approved tooling when that gap matters.

If credentials were committed, handle [the incident](05-incident-response.md). Encrypting the current file is still useful but does not resolve prior exposure. Do not rewrite shared history or revoke provider credentials without the relevant authorization.

## Prepare identity and recovery

Public `age1...` recipients belong in `.sops.yaml`. Private `AGE-SECRET-KEY-*` and `AGE-PLUGIN-*` identities never belong in chat, arguments, logs, repository files, or agent context.

For a portable file:

```bash
<skill-base>/scripts/create_age_identity.sh portable --output /absolute/private/identity.txt
```

For 1Password, store the generated identity in a concealed field using a secure UI or supported secret-safe CLI input. Verify vault storage before deleting the only local working copy. A local owner-only mapping can contain a secret reference, not its value:

```text
SOPS_AGE_KEY=op://ChosenVault/ChosenItem/private-key
```

Run through the actual mapping file:

```bash
op run --env-file=/absolute/private/sops-1password.env --   sops decrypt --input-type dotenv --output-type dotenv .env.sops >/dev/null
```

Do not run `env`, `printenv`, tracing, or environment-dumping debugging in that process tree. Do not log `op read` results. Reference names can themselves be sensitive metadata. A reviewed `SOPS_AGE_KEY_CMD` helper is an alternative only if supported by installed SOPS and it fails closed without logs or disk writes.

## Bootstrap or migrate one root dotenv

The helper deliberately supports **only the root `.env` → `.env.sops`** layout. It refuses unsafe paths, symlink outputs, existing targets unless `--force`, and unsupported dotenv syntax. It is not a general environment merger. For `.env.production`, nested files, existing SOPS policies or multiple environments, make a deliberate per-file mapping and preserve the existing rules instead of forcing this helper.

```bash
<skill-base>/scripts/setup_sops_age.sh migrate --repo . --recipient age1...
<skill-base>/scripts/setup_sops_age.sh bootstrap --repo . --recipient age1...
```

Use one mode, with real public recipients; repeat `--recipient` for alternatives. Before `--force`, review/back up the named outputs. The helper stages encryption/example/config in a private temporary directory and only publishes after encryption succeeds. It preserves local plaintext and existing index state: removing plaintext from the index is a separate explicit `--untrack` option for an authorized migration. Never hide a staged plaintext deletion inside verification.

`.env.example` contains variable names with empty values, never original comments. The helper accepts ordinary single-line `NAME=value` assignments and blank/comment lines; unsupported/multiline/export syntax fails safely for explicit handling. Review application compatibility and add only known-safe defaults later.

## Verify separately

```bash
<skill-base>/scripts/setup_sops_age.sh verify --repo .   --identity-file /absolute/private/identity.txt
```

Or omit `--identity-file` when the selected runtime identity is provided through `op run`/the existing SOPS environment. Verification is read-only: it discards plaintext, checks tracked/ignored paths and encrypted-file structure, and retains scanner findings/failure exit codes. It does not fix `.gitignore` while declaring it verified.

Confirm that `.env` is ignored and untracked; `.env.example`, `.env.sops`, and `.sops.yaml` are not accidentally ignored; decryption works; and scans did not silently skip material coverage. Test every required recipient separately. Supplying one identity file does not prove exclusive use if other SOPS key environment variables/default stores remain available: isolate identity sources for recovery proof.

SOPS may preserve dotenv comments unencrypted. Never assume `.env.sops` is wholly opaque: use the helper's comment-free validated input, and inspect metadata/keys for unintended disclosure without printing plaintext.

## Run and edit

Use the discovered application command; do not invent it:

```bash
sops exec-env .env.sops 'your-start-command'
```

The application receives plaintext in its environment and may inherit key-related variables. Inspect installed SOPS process-environment behavior; explicitly remove identity variables from the child command if they are not needed. Do not claim that `exec-env` alone isolates the key from the application.

Interactive SOPS editing intentionally exposes plaintext to the editor and may use temporary files; use a suitable private editor/session. When a runtime requires a file, prefer supported `exec-file`/FIFO, or an owner-only temporary file outside the checkout with cleanup on exit/signals. Do not silently redirect decrypted output into the repository.

## Onboard and rotate

For another authorized device, install the needed tools and provision the selected portable identity or a new device-bound recipient. `sops filestatus` checks format/state; it does not demonstrate decryption. Perform a discarded-output decrypt and test the actual application path when appropriate.

Rotation sequence:

1. Add the new public recipient while retaining a working old one.
2. Run `sops updatekeys` against every intended encrypted file.
3. Verify decryption using the new identity alone, including the real destination device/CI when required.
4. Remove the old recipient and update keys again.
5. If compromise is suspected, rotate the SOPS data key and the affected application credentials; historical ciphertext may remain decryptable by old identities.

Never remove the last tested recovery path. Secure Enclave replacement needs the corresponding new Mac; a local stub test cannot prove Touch ID or hardware recovery.

## CI and final evidence

Read [CI guidance](04-github-actions.md) for a dedicated CI identity and protected execution. Do not give CI the user's general personal vault or primary age identity.

Report operation/profile, changed files, trusted recipient types, decryption and scan coverage actually tested, and outstanding provider rotation/recovery/device/CI work. Distinguish local encryption success from functioning backup, vault synchronization, live app behavior, and completed incident response.

Sources: [SOPS](https://getsops.io/docs/), [age](https://github.com/FiloSottile/age), [1Password op run](https://developer.1password.com/docs/cli/reference/commands/run/). Verify installed versions and current help before version-sensitive commands.
