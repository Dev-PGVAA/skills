#!/usr/bin/env bash
# Keep the public shell entrypoint; transactional file operations live in Python.
set -euo pipefail
script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)
exec python3 "$script_dir/setup_sops_age.py" "$@"
