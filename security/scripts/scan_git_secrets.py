#!/usr/bin/env python3
"""Scan Git index/history for likely plaintext secrets without printing values."""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable, Optional

MAX_BLOB_BYTES = 2 * 1024 * 1024

SECRET_PATTERNS = (
    ("age_private_identity", re.compile(rb"AGE-(?:SECRET-KEY|PLUGIN-[A-Z0-9-]+)-[A-Z0-9]+")),
    ("private_key_pem", re.compile(rb"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----")),
    ("github_token", re.compile(rb"\b(?:gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,})\b")),
    ("aws_access_key", re.compile(rb"\b(?:AKIA|ASIA)[A-Z0-9]{16}\b")),
    ("openai_style_key", re.compile(rb"\bsk-(?:proj-)?[A-Za-z0-9_-]{20,}\b")),
)

ASSIGNMENT = re.compile(
    rb"(?im)^\s*(?:export\s+)?"
    rb"(?:[A-Z0-9_]*(?:SECRET|TOKEN|PASSWORD|PASSWD|API_KEY|PRIVATE_KEY)[A-Z0-9_]*)"
    rb"\s*=\s*([^\r\n#]+)"
)

PLACEHOLDERS = (
    b"",
    b"changeme",
    b"change-me",
    b"example",
    b"placeholder",
    b"replace-me",
    b"<redacted>",
    b"redacted",
    b"null",
)


@dataclass(frozen=True)
class Finding:
    scope: str
    path: str
    category: str
    object_id: str = ""


def git(repo: Path, *args: str, input_bytes: Optional[bytes] = None) -> bytes:
    proc = subprocess.run(
        ["git", "-C", str(repo), *args],
        input=input_bytes,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"git command failed (exit {proc.returncode}); output suppressed")
    return proc.stdout


def is_plain_env(path: str) -> bool:
    name = Path(path).name.lower()
    if "example" in name or "sample" in name or ".sops" in name or name.endswith(".enc"):
        return False
    return name == ".env" or name.startswith(".env.") or name.endswith(".env") or ".env." in name


def looks_binary(data: bytes) -> bool:
    return b"\x00" in data[:8192]


def content_categories(data: bytes) -> set[str]:
    if not data or len(data) > MAX_BLOB_BYTES or looks_binary(data):
        return set()
    categories = {name for name, pattern in SECRET_PATTERNS if pattern.search(data)}
    for match in ASSIGNMENT.finditer(data):
        value = match.group(1).strip().strip(b"'\"").lower()
        if value.startswith(b"enc[") or value in PLACEHOLDERS or value.startswith(b"${"):
            continue
        categories.add("sensitive_assignment")
    return categories


def parse_index(repo: Path) -> Iterable[tuple[str, str]]:
    raw = git(repo, "ls-files", "-s", "-z")
    for record in raw.split(b"\0"):
        if not record:
            continue
        meta, path = record.split(b"\t", 1)
        fields = meta.split()
        if len(fields) >= 3:
            yield fields[1].decode(), path.decode("utf-8", "surrogateescape")


def parse_history_objects(repo: Path) -> Iterable[tuple[str, str]]:
    # Raw NUL-delimited records retain unusual names and every historical path.
    # rev-list --objects only provides one representative path per shared blob.
    raw = git(repo, "log", "--all", "--format=", "--raw", "-z", "--no-abbrev", "--no-renames", "--root", "-m")
    records = iter(raw.split(b"\0"))
    for record in records:
        header = record.lstrip(b"\n")
        if not header.startswith(b":"):
            continue
        fields = header.split()
        if len(fields) != 5:
            raise RuntimeError("unrecognized Git history record; scan incomplete")
        path = next(records, None)
        if path is None:
            raise RuntimeError("missing Git history path; scan incomplete")
        oid = fields[3] if set(fields[3]) != {ord("0")} else fields[2]
        yield oid.decode(), path.decode("utf-8", "surrogateescape")


def read_blob(repo: Path, oid: str, coverage: dict[str, int]) -> Optional[bytes]:
    obj_type = git(repo, "cat-file", "-t", oid).strip()
    if obj_type != b"blob":
        coverage["non_blob_objects"] += 1
        return None
    size_raw = git(repo, "cat-file", "-s", oid).strip()
    try:
        size = int(size_raw)
    except ValueError:
        raise RuntimeError("invalid Git object size; scan incomplete") from None
    if size > MAX_BLOB_BYTES:
        coverage["oversized_blobs"] += 1
        return None
    data = git(repo, "cat-file", "blob", oid)
    if looks_binary(data):
        coverage["binary_blobs"] += 1
        return None
    if data.startswith(b"version https://git-lfs.github.com/spec/v1\n"):
        coverage["lfs_pointers"] += 1
        return None
    coverage["text_blobs_scanned"] += 1
    return data


def scan_entries(repo: Path, entries: Iterable[tuple[str, str]], scope: str, coverage: dict[str, int]) -> list[Finding]:
    findings: set[Finding] = set()
    seen: set[tuple[str, str]] = set()
    for oid, path in entries:
        key = (oid, path)
        if key in seen:
            continue
        seen.add(key)
        if is_plain_env(path):
            findings.add(Finding(scope, path, "tracked_plaintext_env", oid[:12]))
        data = read_blob(repo, oid, coverage)
        if data is None:
            continue
        for category in content_categories(data):
            findings.add(Finding(scope, path, category, oid[:12]))
    return sorted(findings, key=lambda item: (item.scope, item.path, item.category, item.object_id))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", default=".", help="Git repository path")
    parser.add_argument("--scope", choices=("index", "history", "all"), default="all")
    parser.add_argument("--json", action="store_true", help="Emit JSON; values are never included")
    args = parser.parse_args()

    repo = Path(args.repo).resolve()
    try:
        root = Path(git(repo, "rev-parse", "--show-toplevel").decode().strip()).resolve()
    except (RuntimeError, OSError) as exc:
        print(f"error: not a readable Git repository ({type(exc).__name__})", file=sys.stderr)
        return 1

    findings: list[Finding] = []
    coverage = dict.fromkeys(("text_blobs_scanned", "oversized_blobs", "binary_blobs", "lfs_pointers", "non_blob_objects"), 0)
    try:
        if args.scope in ("index", "all"):
            findings.extend(scan_entries(root, parse_index(root), "index", coverage))
        if args.scope in ("history", "all"):
            findings.extend(scan_entries(root, parse_history_objects(root), "history", coverage))
    except (RuntimeError, OSError) as exc:
        print(f"error: scan incomplete ({type(exc).__name__})", file=sys.stderr)
        return 1

    unique = sorted(set(findings), key=lambda item: (item.scope, item.path, item.category, item.object_id))
    shallow = git(root, "rev-parse", "--is-shallow-repository").strip() == b"true"
    limitations = ["Heuristic index/reachable-history scan; excludes untracked files, remote-only refs, reflogs, unreachable objects, binary/LFS payloads and unknown secret formats."]
    if shallow and args.scope in ("history", "all"):
        limitations.append("Shallow repository: history coverage is incomplete.")
    if args.json:
        print(json.dumps({"findings": [asdict(item) for item in unique], "coverage": coverage, "limitations": limitations}, indent=2))
    elif unique:
        print("Potential secret exposure found. Values are intentionally redacted.")
        for item in unique:
            object_suffix = f" object={item.object_id}" if item.object_id else ""
            print(f"- scope={item.scope} path={json.dumps(item.path)} category={item.category}{object_suffix}")
    else:
        print("No matching plaintext env paths or high-confidence secret patterns found.")

    if not args.json:
        print("Coverage: " + json.dumps(coverage, sort_keys=True))
        for limitation in limitations:
            print("Limit: " + limitation)
    return 1 if shallow and args.scope in ("history", "all") else (2 if unique else 0)


if __name__ == "__main__":
    sys.exit(main())
