#!/usr/bin/env python3
"""Validate skill metadata, packaged resource links, and source syntax. Needs PyYAML."""
import argparse
import ast
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote, urlsplit
import yaml


def validate(root):
    errors, rows = [], []
    skills = sorted(p.parent for p in root.glob('*/SKILL.md'))
    seen = set()
    for skill in skills:
        text = (skill/'SKILL.md').read_text(encoding='utf-8')
        match = re.match(r'^---\n(.*?)\n---(?:\n|$)', text, re.S)
        if not match:
            errors.append(f'{skill.name}: missing frontmatter')
            continue
        try:
            front = yaml.safe_load(match.group(1))
            if not isinstance(front, dict): raise ValueError('frontmatter must be mapping')
            name, desc = front.get('name'), front.get('description')
            if name != skill.name or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', name or ''):
                errors.append(f'{skill.name}: invalid or mismatched name')
            if name in seen: errors.append(f'{skill.name}: duplicate name')
            seen.add(name)
            if not isinstance(desc, str) or not desc.strip() or len(desc) > 1024:
                errors.append(f'{skill.name}: missing/long description')
            unsupported = set(front) - {'name','description','license','allowed-tools','metadata'}
            if unsupported: errors.append(f'{skill.name}: unsupported fields {sorted(unsupported)}')
            ui_file = skill/'agents/openai.yaml'
            ui = yaml.safe_load(ui_file.read_text(encoding='utf-8'))
            interface = ui['interface']
            if not 25 <= len(interface['short_description']) <= 64:
                errors.append(f'{skill.name}: UI short_description must be 25..64 chars')
            if '$'+skill.name not in interface.get('default_prompt', ''):
                errors.append(f'{skill.name}: default_prompt must mention skill')
            for key in ('icon_small','icon_large'):
                if interface.get(key) and not (skill/interface[key]).is_file():
                    errors.append(f'{skill.name}: missing icon {interface[key]}')
        except (ValueError, TypeError, KeyError, OSError, yaml.YAMLError) as exc:
            errors.append(f'{skill.name}: metadata: {exc}')
        for file in skill.rglob('*'):
            if file.is_symlink():
                errors.append(f'{file.relative_to(root)}: unexpected symlink in package')
            if not file.is_file(): continue
            if file.suffix == '.md':
                content = file.read_text(encoding='utf-8')
                for link in re.findall(r'\[[^\]\n]*\]\(([^)\n]+)\)', content):
                    link = link.strip().split(' "', 1)[0].strip('<>')
                    if urlsplit(link).scheme or link.startswith(('#','/')): continue
                    target = unquote(link.split('#',1)[0])
                    if not target or any(c in target for c in ('<','>','*','{','}')): continue
                    if not (file.parent/target).exists():
                        errors.append(f'{file.relative_to(root)}: missing linked resource {target}')
            if file.suffix == '.py':
                try: ast.parse(file.read_text(encoding='utf-8'), filename=str(file))
                except SyntaxError as exc: errors.append(str(exc))
            if file.suffix == '.sh':
                result = subprocess.run(['bash','-n',str(file)],capture_output=True,text=True)
                if result.returncode: errors.append(f'{file.relative_to(root)}: {result.stderr.strip()}')
        rows.append({'skill':skill.name, 'entry_words':len(text.split()),
                     'files':sum(p.is_file() for p in skill.rglob('*') if '__pycache__' not in p.parts)})
    if not skills: errors.append('No skills found')
    return {'skills':rows, 'count':len(skills), 'errors':errors,
            'limit':'Static validation; behavioral evaluations and script fixtures are separate.'}


if __name__ == '__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('root', nargs='?', type=Path, default=Path(__file__).resolve().parents[1])
    args=parser.parse_args()
    report=validate(args.root.resolve())
    print(json.dumps(report,ensure_ascii=False,indent=2))
    sys.exit(bool(report['errors']))
