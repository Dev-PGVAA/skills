#!/usr/bin/env python3
"""Create isolated planning files or check their recorded state (Python 3 stdlib)."""
import argparse
import json
from pathlib import Path
import re
import sys

FILES = ('task_plan.md', 'findings.md', 'progress.md')
STATUS = re.compile(r'^\s*(?:-\s*)?\*\*Status:\*\*\s*(\S+)\s*$')
PHASE = re.compile(r'^###\s+Phase\s+.+')
UNCHECKED = re.compile(r'^\s*[-*]\s+\[ \]\s+')
VALID = {'pending', 'in_progress', 'blocked', 'complete'}


def checked_dir(value):
    path = Path(value).expanduser().absolute()
    # Do not follow user-controlled active pointers or directory symlinks.
    for item in (path, *path.parents):
        if item.is_symlink():
            raise ValueError('Planning path contains a symlink: ' + str(item))
    if path.exists() and not path.is_dir():
        raise ValueError('Planning path is not a directory')
    return path


def init(directory, title):
    if not title.strip() or '\n' in title or '\r' in title:
        raise ValueError('Title must be a nonempty single line')
    templates = Path(__file__).resolve().parents[1] / 'templates'
    # Preflight all files before creating any, preserving existing content.
    for name in FILES:
        target = directory / name
        if target.is_symlink() or (target.exists() and not target.is_file()):
            raise ValueError('Unsafe planning target: ' + str(target))
    directory.mkdir(parents=True, exist_ok=True)
    created = []
    for name in FILES:
        content = (templates / name).read_text(encoding='utf-8')
        if name == 'task_plan.md':
            content = content.replace('{title}', title)
        try:
            with (directory / name).open('x', encoding='utf-8') as stream:
                stream.write(content)
            created.append(name)
        except FileExistsError:
            pass
    return {'directory': str(directory), 'created': created,
            'preserved': [name for name in FILES if name not in created]}


def parse_phases(content):
    phases, fence = [], None
    for line in content.splitlines():
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})(.*)$', line)
        if marker:
            run, tail = marker.groups()
            if fence is None:
                fence = run
            elif run[0] == fence[0] and len(run) >= len(fence) and not tail.strip():
                fence = None
            continue
        if fence is not None:
            continue
        if PHASE.match(line):
            phases.append({'title': line[4:], 'statuses': [], 'unchecked': 0})
        elif phases:
            # A section of level 1/2 ends phase fields; narrative statuses don't count.
            if re.match(r'^#{1,2}\s', line):
                phases[-1]['closed'] = True
            if phases[-1].get('closed'):
                continue
            match = STATUS.match(line)
            if match:
                phases[-1]['statuses'].append(match.group(1))
            if UNCHECKED.match(line):
                phases[-1]['unchecked'] += 1
    return phases


def check(directory):
    target = directory / 'task_plan.md'
    if target.is_symlink() or not target.is_file():
        raise ValueError('Missing regular task_plan.md in requested directory')
    phases = parse_phases(target.read_text(encoding='utf-8'))
    errors = []
    if not phases:
        errors.append('No recognized phases; inspect this plan manually')
    for phase in phases:
        statuses = phase['statuses']
        if len(statuses) != 1 or statuses[0] not in VALID:
            errors.append(phase['title'] + ': requires exactly one valid status')
        elif statuses[0] == 'complete' and phase['unchecked']:
            errors.append(phase['title'] + ': complete but contains unchecked work')
        phase.pop('closed', None)
    if errors:
        return 2, {'state': 'invalid', 'errors': errors, 'phases': phases}
    complete = all(p['statuses'] == ['complete'] for p in phases)
    return (0 if complete else 1), {
        'state': 'recorded_complete' if complete else 'unfinished',
        'phases': phases,
        'limit': 'Recorded status only; verify artifacts and behavior separately.'}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    for name in ('init', 'check'):
        command = sub.add_parser(name)
        command.add_argument('--dir', required=True, help='Exact task directory')
        if name == 'init':
            command.add_argument('--title', required=True)
    args = parser.parse_args()
    try:
        directory = checked_dir(args.dir)
        if args.command == 'init':
            result, code = init(directory, args.title), 0
        else:
            code, result = check(directory)
    except (OSError, ValueError) as exc:
        result, code = {'state': 'error', 'error': str(exc)}, 2
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return code


if __name__ == '__main__':
    sys.exit(main())
