#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  setup_sops_age.sh migrate --repo PATH --env-file .env --recipient age1... [--recipient age1...]
  setup_sops_age.sh bootstrap --repo PATH --recipient age1... [--recipient age1...]
  setup_sops_age.sh verify --repo PATH [--identity-file /absolute/private/identity]
  setup_sops_age.sh audit --repo PATH

Options:
  --force   Replace existing .env.example, .env.sops, and .sops.yaml.

Only public recipients may be supplied. Private age identities are rejected.
USAGE
}

die() {
  printf 'error: %s\n' "$1" >&2
  exit 1
}

[[ $# -ge 1 ]] || { usage >&2; exit 1; }
mode=$1
shift
repo='.'
env_file='.env'
identity_file=''
force=0
recipients=()

while [[ $# -gt 0 ]]; do
  case "$1" in
    --repo)
      [[ $# -ge 2 ]] || die '--repo requires a path'
      repo=$2
      shift 2
      ;;
    --env-file)
      [[ $# -ge 2 ]] || die '--env-file requires a path'
      env_file=$2
      shift 2
      ;;
    --recipient)
      [[ $# -ge 2 ]] || die '--recipient requires a public age recipient'
      recipients+=("$2")
      shift 2
      ;;
    --identity-file)
      [[ $# -ge 2 ]] || die '--identity-file requires a path'
      identity_file=$2
      shift 2
      ;;
    --force)
      force=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *) die "unknown argument: $1" ;;
  esac
done

skill_script_path=${BASH_SOURCE[0]}
if [[ "$skill_script_path" != /* ]]; then
  skill_script_path="$PWD/$skill_script_path"
fi
skill_script_dir=$(cd "$(dirname "$skill_script_path")" && pwd -P)
scanner="$skill_script_dir/scan_git_secrets.py"

[[ -d "$repo" ]] || die "repository directory not found: $repo"
repo=$(cd "$repo" && pwd -P)
cd "$repo"

append_ignore() {
  local line=$1
  touch .gitignore
  grep -Fqx "$line" .gitignore 2>/dev/null || printf '%s\n' "$line" >> .gitignore
}

install_ignore_rules() {
  append_ignore '# SOPS + age: local plaintext and private identities'
  append_ignore '.env'
  append_ignore '.env.*'
  append_ignore '!.env.example'
  append_ignore '!.env.sops'
  append_ignore '*.env'
  append_ignore '*.env.*'
  append_ignore '!*.env.example'
  append_ignore '!*.env.sops'
  append_ignore 'keys.txt'
  append_ignore '*.agekey'
  append_ignore '*age-identity*'
  append_ignore '*sops-se-identity*'
}

validate_recipients() {
  [[ ${#recipients[@]} -gt 0 ]] || die 'at least one --recipient is required'
  local recipient
  for recipient in "${recipients[@]}"; do
    case "$recipient" in
      AGE-SECRET-KEY-*|AGE-PLUGIN-*) die 'private age identity supplied where a public recipient is required' ;;
      age1*) ;;
      *) die "invalid or unsupported public age recipient: $recipient" ;;
    esac
    [[ "$recipient" =~ ^[a-z0-9]+$ ]] || die 'recipient contains unexpected characters'
  done
}

write_sops_config() {
  {
    printf 'creation_rules:\n'
    printf "  - path_regex: '(^|/)\\.env\\.sops$'\n"
    printf '    age:\n'
    local recipient
    for recipient in "${recipients[@]}"; do
      printf "      - '%s'\n" "$recipient"
    done
  } > .sops.yaml
}

redact_example() {
  local source=$1
  local destination=$2
  awk '
    /^[[:space:]]*(export[[:space:]]+)?[A-Za-z_][A-Za-z0-9_]*[[:space:]]*=/ {
      line=$0
      pos=index(line, "=")
      print substr(line, 1, pos)
      next
    }
    /^[[:space:]]*#/ || /^[[:space:]]*$/ { print; next }
    { print "# REVIEW: unsupported dotenv line omitted" }
  ' "$source" > "$destination"
}

encrypt_source() {
  local source=$1
  local encrypted_tmp
  encrypted_tmp=$(mktemp "${TMPDIR:-/tmp}/sops-age-encrypted.XXXXXX")
  trap 'rm -f "${encrypted_tmp:-}" "${bootstrap_plain:-}"' EXIT
  sops encrypt \
    --config .sops.yaml \
    --filename-override .env.sops \
    --input-type dotenv \
    --output-type dotenv \
    < "$source" > "$encrypted_tmp"
  [[ -s "$encrypted_tmp" ]] || die 'SOPS produced an empty encrypted file'
  mv "$encrypted_tmp" .env.sops
  trap 'rm -f "${bootstrap_plain:-}"' EXIT
}

check_overwrite() {
  local path
  for path in .env.example .env.sops .sops.yaml; do
    if [[ -e "$path" && $force -ne 1 ]]; then
      die "$path already exists; review it and rerun with --force only if replacement is intended"
    fi
  done
}

run_scanner() {
  if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
    set +e
    python3 "$scanner" --repo . --scope all
    scan_status=$?
    set -e
    if [[ $scan_status -eq 2 ]]; then
      printf 'warning: potential current/history exposure found; rotate provider credentials before cleanup\n' >&2
    elif [[ $scan_status -ne 0 ]]; then
      return "$scan_status"
    fi
  else
    printf 'Git repository not initialized; skipped index/history scan.\n' >&2
  fi
}

case "$mode" in
  migrate)
    command -v sops >/dev/null 2>&1 || die 'sops not found; install it first'
    validate_recipients
    [[ "$env_file" != /* ]] || die '--env-file must be relative to the repository'
    [[ -f "$env_file" ]] || die "plaintext dotenv file not found: $env_file"
    check_overwrite
    run_scanner
    install_ignore_rules
    redact_example "$env_file" .env.example
    write_sops_config
    encrypt_source "$env_file"
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1 && git ls-files --error-unmatch -- "$env_file" >/dev/null 2>&1; then
      git rm --cached --quiet -- "$env_file"
      printf 'Removed plaintext dotenv path from the current Git index; the local file remains.\n' >&2
    fi
    ;;
  bootstrap)
    command -v sops >/dev/null 2>&1 || die 'sops not found; install it first'
    validate_recipients
    check_overwrite
    install_ignore_rules
    printf '# Safe public defaults; add secret values through SOPS.\nAPP_ENV=development\nSECRET_KEY=\n' > .env.example
    write_sops_config
    bootstrap_plain=$(mktemp "${TMPDIR:-/tmp}/sops-age-plaintext.XXXXXX")
    trap 'rm -f "${bootstrap_plain:-}"' EXIT
    cp .env.example "$bootstrap_plain"
    encrypt_source "$bootstrap_plain"
    ;;
  verify)
    command -v sops >/dev/null 2>&1 || die 'sops not found; install it first'
    [[ -f .env.example ]] || die '.env.example is missing'
    [[ -f .env.sops ]] || die '.env.sops is missing'
    [[ -f .sops.yaml ]] || die '.sops.yaml is missing'
    install_ignore_rules
    if [[ -n "$identity_file" ]]; then
      [[ "$identity_file" = /* ]] || die '--identity-file must be absolute'
      [[ -f "$identity_file" ]] || die 'identity file not found'
      case "$identity_file" in
        "$repo"|"$repo"/*) die 'identity file must not be inside the repository' ;;
      esac
      SOPS_AGE_KEY_FILE="$identity_file" sops decrypt --input-type dotenv --output-type dotenv .env.sops >/dev/null
    else
      sops decrypt --input-type dotenv --output-type dotenv .env.sops >/dev/null
    fi
    if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
      git check-ignore -q .env || die '.env is not ignored'
      if git ls-files --error-unmatch -- .env >/dev/null 2>&1; then
        die '.env is still tracked in the current index'
      fi
    fi
    run_scanner
    printf 'Verified SOPS decryption and local plaintext guardrails.\n'
    ;;
  audit)
    run_scanner
    ;;
  *)
    usage >&2
    die "unknown mode: $mode"
    ;;
esac

printf 'Completed %s in %s\n' "$mode" "$repo"
