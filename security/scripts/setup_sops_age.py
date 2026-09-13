#!/usr/bin/env python3
"""Bootstrap/migrate root .env safely; audit and verify never mutate the repo."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile

OUTPUTS = ('.env.example', '.env.sops', '.sops.yaml', '.gitignore')
RULES = ('.env', '.env.*', '!.env.example', '!.env.sops', '*.env', '*.env.*',
         '!*.env.example', '!*.env.sops', 'keys.txt', '*.agekey', '*age-identity*',
         '*sops-se-identity*')


class SetupError(Exception):
    pass


def run(args, *, cwd, data=None, env=None, discard=False):
    proc = subprocess.run(args, cwd=cwd, input=data, env=env,
                          stdout=subprocess.DEVNULL if discard else subprocess.PIPE,
                          stderr=subprocess.PIPE)
    if proc.returncode:
        # Tool errors can quote input values. Report only the tool and exit code.
        raise SetupError(f'{Path(args[0]).name} failed (exit {proc.returncode}); no tool output displayed')
    return proc.stdout


def git(repo, *args):
    return run(['git', *args], cwd=repo)


def require_root(repo):
    try:
        actual = Path(os.fsdecode(git(repo, 'rev-parse', '--show-toplevel')).strip()).resolve()
    except SetupError:
        return False
    if actual != repo:
        raise SetupError('--repo must be the Git root, not a nested directory')
    return True


def safe_target(path):
    if path.is_symlink() or (path.exists() and not path.is_file()):
        raise SetupError(f'output must be a regular file, not a link or directory: {path.name}')


def dotenv(data):
    try:
        text = data.decode('utf-8')
    except UnicodeDecodeError:
        raise SetupError('dotenv must be UTF-8') from None
    values, names = [], set()
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith('#'):
            continue
        match = re.fullmatch(r'([A-Za-z_][A-Za-z0-9_]*)=(.*)', line)
        if not match or '\x00' in line:
            raise SetupError(f'unsupported dotenv syntax at line {number}; handle explicitly')
        name, value = match.groups()
        if name in names or name.startswith('sops_'):
            raise SetupError(f'duplicate/reserved dotenv variable at line {number}')
        # SOPS dotenv is line based; do not silently change shell/multiline syntax.
        if value[:1] in ('"', "'") and (len(value) < 2 or value[-1:] != value[:1]):
            raise SetupError(f'unsupported multiline dotenv value at line {number}')
        names.add(name)
        values.append((name, value))
    if not values:
        raise SetupError('dotenv contains no assignments')
    # Comments can contain secrets and SOPS may preserve them in plaintext.
    plain = ''.join(f'{name}={value}\n' for name, value in values).encode()
    example = ''.join(f'{name}=\n' for name, _ in values).encode()
    return plain, example


def scan(repo):
    scanner = Path(__file__).with_name('scan_git_secrets.py')
    code = subprocess.run([sys.executable, str(scanner), '--repo', str(repo), '--scope', 'all']).returncode
    if code not in (0, 2):
        raise SetupError('Git secret scan failed; coverage incomplete')
    return code


def is_tracked(repo, name):
    return bool(git(repo, 'ls-files', '-z', '--', name))


def is_ignored(repo, name):
    proc = subprocess.run(['git', 'check-ignore', '--no-index', '-q', '--', name], cwd=repo,
                          stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    if proc.returncode not in (0, 1):
        raise SetupError('could not check Git ignore rules')
    return proc.returncode == 0


def publish(repo, contents):
    """Stage same-filesystem replacements; restore previous files on exceptions."""
    previous, staged, replaced = {}, {}, []
    try:
        for name, data in contents.items():
            path = repo / name
            safe_target(path)
            previous[name] = (path.read_bytes(), path.stat().st_mode & 0o777) if path.exists() else None
            fd, temporary = tempfile.mkstemp(prefix='.sops-setup-', dir=repo)
            staged[name] = Path(temporary)
            with os.fdopen(fd, 'wb') as stream:
                stream.write(data)
            os.chmod(temporary, previous[name][1] if previous[name] else 0o600)
        for name, temporary in staged.items():
            safe_target(repo / name)
            os.replace(temporary, repo / name)
            replaced.append(name)
    except BaseException:
        for name in reversed(replaced):
            path = repo / name
            if previous[name] is None:
                path.unlink(missing_ok=True)
            else:
                data, mode = previous[name]
                fd, temporary = tempfile.mkstemp(prefix='.sops-restore-', dir=repo)
                with os.fdopen(fd, 'wb') as stream:
                    stream.write(data)
                os.chmod(temporary, mode)
                os.replace(temporary, path)
        raise
    finally:
        for path in staged.values():
            path.unlink(missing_ok=True)


def verify(repo, identity):
    for name in OUTPUTS:
        safe_target(repo / name)
        if not (repo / name).is_file():
            raise SetupError(f'{name} is missing')
    runtime = os.environ.copy()
    if identity:
        supplied = Path(identity)
        if not supplied.is_absolute() or not supplied.is_file():
            raise SetupError('--identity-file must be an existing absolute file')
        resolved = supplied.resolve()
        if repo == resolved or repo in resolved.parents:
            raise SetupError('identity file must be outside the repository')
        if resolved.stat().st_mode & 0o077:
            raise SetupError('identity file must have owner-only permissions')
        runtime['SOPS_AGE_KEY_FILE'] = str(resolved)
    run(['sops', 'decrypt', '--input-type', 'dotenv', '--output-type', 'dotenv', '.env.sops'],
        cwd=repo, env=runtime, discard=True)
    if not is_ignored(repo, '.env'):
        raise SetupError('.env is not ignored')
    if is_tracked(repo, '.env'):
        raise SetupError('.env is still tracked in the current index')
    for name in ('.env.sops', '.env.example', '.sops.yaml'):
        if is_ignored(repo, name):
            raise SetupError(f'{name} is unexpectedly ignored')
    result = scan(repo)
    print('Decryption and current Git guardrails verified; scan findings remain.' if result else
          'Decryption and current Git guardrails verified within scanner coverage.')
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('migrate', 'bootstrap', 'verify', 'audit'))
    parser.add_argument('--repo', default='.')
    parser.add_argument('--env-file', default='.env', help='Only root .env is supported')
    parser.add_argument('--recipient', action='append', default=[], help='Public age recipient; repeatable')
    parser.add_argument('--identity-file')
    parser.add_argument('--force', action='store_true', help='Replace existing outputs after reviewed backup')
    parser.add_argument('--untrack', action='store_true', help='Migrate: remove root .env from index, retain local file')
    args = parser.parse_args()
    repo = Path(args.repo).resolve()
    if not repo.is_dir():
        raise SetupError('repository directory does not exist')
    initialized = require_root(repo)
    if args.mode in ('audit', 'verify'):
        if args.force or args.untrack or args.recipient:
            raise SetupError('mutation options are not valid in audit/verify modes')
        if not initialized:
            raise SetupError('audit/verify requires an initialized Git repository')
        if args.mode == 'audit':
            return scan(repo)
        return verify(repo, args.identity_file)
    if args.identity_file:
        raise SetupError('--identity-file is only for verify')
    if args.untrack and args.mode != 'migrate':
        raise SetupError('--untrack is only for migrate')
    if args.env_file != '.env':
        raise SetupError('only root .env is supported; map other environments explicitly')
    if not args.recipient:
        raise SetupError('at least one public --recipient is required')
    if any(not re.fullmatch(r'age1[a-z0-9]+', item) for item in args.recipient):
        raise SetupError('invalid public recipient; private identities are never accepted')
    for name in OUTPUTS:
        safe_target(repo / name)
        if name != '.gitignore' and (repo / name).exists() and not args.force:
            raise SetupError(f'{name} exists; use --force only after reviewing/backing it up')
    if args.mode == 'migrate':
        source = repo / '.env'
        safe_target(source)
        if not source.is_file():
            raise SetupError('root .env is missing')
        plain, example = dotenv(source.read_bytes())
    else:
        plain, example = dotenv(b'APP_ENV=development\nSECRET_KEY=\n')
    if not shutil.which('sops'):
        raise SetupError('sops not found')
    result = scan(repo) if initialized else 0
    config = ("creation_rules:\n  - path_regex: '(^|/)\\.env\\.sops$'\n    encrypted_regex: '.'\n    age:\n" +
              ''.join(f"      - '{item}'\n" for item in dict.fromkeys(args.recipient))).encode()
    with tempfile.TemporaryDirectory(prefix='sops-setup-') as directory:
        stage = Path(directory)
        (stage / '.sops.yaml').write_bytes(config)
        encrypted = run(['sops', '--config', str(stage / '.sops.yaml'), 'encrypt',
                         '--filename-override', '.env.sops', '--input-type', 'dotenv',
                         '--output-type', 'dotenv'], cwd=stage, data=plain)
        if not encrypted or b'ENC[' not in encrypted:
            raise SetupError('SOPS produced no recognizable encrypted values')
    ignore = (repo / '.gitignore').read_bytes() if (repo / '.gitignore').exists() else b''
    if ignore and not ignore.endswith(b'\n'):
        ignore += b'\n'
    existing = set(ignore.splitlines())
    ignore += b''.join(line.encode() + b'\n' for line in RULES if line.encode() not in existing)
    publish(repo, {'.env.example': example, '.env.sops': encrypted, '.sops.yaml': config, '.gitignore': ignore})
    if args.untrack and initialized and is_tracked(repo, '.env'):
        git(repo, 'rm', '--cached', '--quiet', '--', '.env')
        print('Removed .env from index; local plaintext remains.')
    print(f'Completed {args.mode}; verify decryption separately. Git scan findings: {bool(result)}.')
    return result


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (SetupError, OSError, UnicodeError) as exc:
        # Do not show raw OS paths/messages that could contain sensitive input.
        message = str(exc) if isinstance(exc, SetupError) else type(exc).__name__
        print(f'error: {message}', file=sys.stderr)
        sys.exit(1)
