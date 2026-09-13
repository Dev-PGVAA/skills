#!/usr/bin/env bash
set -euo pipefail

usage() {
  cat <<'USAGE'
Usage:
  create_age_identity.sh portable --output /absolute/private/identity.txt
  create_age_identity.sh secure-enclave --output /absolute/private/identity.txt \
    [--access-control any-biometry-or-passcode]

The identity file is private. The script refuses to write inside the current
Git repository and never prints private identity contents.
USAGE
}

die() {
  printf 'error: %s\n' "$1" >&2
  exit 1
}

[[ $# -ge 1 ]] || { usage >&2; exit 1; }
[[ "$1" != --help && "$1" != -h ]] || { usage; exit 0; }
profile=$1
shift
output=''
access_control='any-biometry-or-passcode'

while [[ $# -gt 0 ]]; do
  case "$1" in
    --output)
      [[ $# -ge 2 ]] || die '--output requires a path'
      output=$2
      shift 2
      ;;
    --access-control)
      [[ $# -ge 2 ]] || die '--access-control requires a value'
      access_control=$2
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    *) die "unknown argument: $1" ;;
  esac
done

[[ -n "$output" ]] || die '--output is required'
[[ "$output" = /* ]] || die '--output must be an absolute path outside the repository'
[[ ! -e "$output" && ! -L "$output" ]] || die "refusing to overwrite existing identity: $output"

output_dir=$(dirname "$output")
(umask 077; mkdir -p "$output_dir")
output_dir=$(cd "$output_dir" && pwd -P)
output="$output_dir/$(basename "$output")"

if repo_root=$(git -C "$PWD" rev-parse --show-toplevel 2>/dev/null); then
  repo_root=$(cd "$repo_root" && pwd -P)
  case "$output" in
    "$repo_root"|"$repo_root"/*)
      die 'identity output must not be inside the current Git repository'
      ;;
  esac
fi

if output_repo_root=$(git -C "$output_dir" rev-parse --show-toplevel 2>/dev/null); then
  output_repo_root=$(cd "$output_repo_root" && pwd -P)
  case "$output" in
    "$output_repo_root"|"$output_repo_root"/*)
      die 'identity output must not be inside any Git repository'
      ;;
  esac
fi

case "$access_control" in
  none|passcode|any-biometry|any-biometry-and-passcode|any-biometry-or-passcode|current-biometry|current-biometry-and-passcode) ;;
  *) die "unsupported access control: $access_control" ;;
esac

private_stage=$(mktemp -d "$output_dir/.age-keygen.XXXXXX")
trap 'rm -rf "$private_stage"' EXIT
staged_output="$private_stage/identity.txt"
case "$profile" in
  portable)
    command -v age-keygen >/dev/null 2>&1 || die 'age-keygen not found; install age first'
    (
      umask 077
      age-keygen -o "$staged_output"
    )
    ;;
  secure-enclave)
    [[ $(uname -s) == Darwin ]] || die 'Secure Enclave identity generation requires macOS'
    command -v sw_vers >/dev/null 2>&1 || die 'cannot determine macOS version'
    major=$(sw_vers -productVersion | awk -F. '{print $1}')
    [[ "$major" =~ ^[0-9]+$ && "$major" -ge 14 ]] || die 'age-plugin-se requires macOS 14 or newer'
    command -v age-plugin-se >/dev/null 2>&1 || die 'age-plugin-se not found; install it first'
    (
      umask 077
      age-plugin-se keygen --access-control "$access_control" -o "$staged_output"
    )
    ;;
  *)
    die "unknown profile: $profile"
    ;;
esac

chmod 600 "$staged_output"
# Hard-link publication refuses overwrite, including dangling symlinks and races.
ln "$staged_output" "$output" || die 'could not publish identity without overwriting a path'
printf 'Identity created outside Git: %s\n' "$output" >&2
printf 'Back it up only if the profile is portable. Secure Enclave identities are device-bound.\n' >&2
