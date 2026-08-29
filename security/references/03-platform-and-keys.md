# Platforms and identity profiles

## Tooling

### macOS

```bash
brew install sops age
```

For Secure Enclave:

```bash
brew install age-plugin-se
```

### Debian 12+ / Ubuntu 22.04+

```bash
sudo apt update
sudo apt install age
```

Install SOPS from the official getsops release packages/binaries and verify its published checksum/signature. Do not assume every Debian/Ubuntu release has a current `apt install sops` package.

## Portable identity

Create outside the repository with restrictive permissions:

```bash
umask 077
age-keygen -o /absolute/private/age-identity.txt
age-keygen -y /absolute/private/age-identity.txt
```

The `age1...` line is public. The identity file is private.

SOPS identity discovery:

- Linux: `$XDG_CONFIG_HOME/sops/age/keys.txt`, falling back to `~/.config/sops/age/keys.txt`.
- macOS: `$XDG_CONFIG_HOME/sops/age/keys.txt`, falling back to `~/Library/Application Support/sops/age/keys.txt`.
- Override with `SOPS_AGE_KEY_FILE`; CI may inject `SOPS_AGE_KEY`.

## Secure Enclave identity

Requirements: macOS 14+ and a Secure Enclave processor.

```bash
umask 077
age-plugin-se keygen \
  --access-control any-biometry-or-passcode \
  -o /absolute/private/sops-se-identity.txt
```

Useful access controls:

- `any-biometry-or-passcode`: resilient default.
- `any-biometry`: biometric-only use; keep a tested recovery recipient.
- `current-biometry`: enrollment changes can invalidate access; use cautiously.

The `age1se...` recipient is public. The `AGE-PLUGIN-SE-*` identity is private and device-bound. It cannot be transferred to another Mac.

## Hybrid recipient design

Use multiple recipients in one SOPS creation rule:

```yaml
creation_rules:
  - path_regex: '(^|/)\.env\.sops$'
    age:
      - 'age1se1...mac-local...'
      - 'age1...offline-recovery...'
      - 'age1...dedicated-ci...'
```

Each recipient is an alternative decryption path. This improves availability but expands the trust boundary. Keep recovery material offline or in an appropriate password manager/hardware-backed store.

## Sources

- [SOPS repository and age documentation](https://github.com/getsops/sops)
- [SOPS releases](https://github.com/getsops/sops/releases)
- [age installation and usage](https://github.com/FiloSottile/age)
- [age-plugin-se documentation](https://github.com/remko/age-plugin-se)
- [Homebrew age-plugin-se formula](https://formulae.brew.sh/formula/age-plugin-se)

