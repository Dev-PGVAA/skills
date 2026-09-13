#!/usr/bin/env python3
"""Isolated helper regressions; real sops/age tests skip if tools are absent."""
import importlib.util
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPTS = Path(__file__).resolve().parents[1] / 'scripts'


def invoke(argv, cwd, env=None):
    return subprocess.run([str(x) for x in argv], cwd=cwd, env=env,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)


class Helpers(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(prefix='security-fixture-')
        self.base = Path(self.temporary.name).resolve()
        self.repo = self.base / 'repo'
        self.repo.mkdir()
        self.git('init', '-q')
        self.git('config', 'commit.gpgsign', 'false')
        self.git('config', 'user.name', 'Fixture')
        self.git('config', 'user.email', 'fixture@example.invalid')
        self.env = os.environ.copy()
        for name in list(self.env):
            if name.startswith('SOPS_AGE_'):
                self.env.pop(name)

    def tearDown(self):
        self.temporary.cleanup()

    def git(self, *args):
        result = invoke(['git', *args], self.repo)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        return result.stdout

    def setup(self, mode, *args):
        return invoke(['bash', SCRIPTS / 'setup_sops_age.sh', mode, '--repo', self.repo, *args],
                      self.base, self.env)

    def scanner(self):
        return invoke([sys.executable, SCRIPTS / 'scan_git_secrets.py', '--repo', self.repo, '--json'], self.base)

    def identity(self):
        if not shutil.which('age-keygen') or not shutil.which('sops'):
            self.skipTest('real age/sops not installed')
        identity = self.base / 'identity.txt'
        result = invoke(['bash', SCRIPTS / 'create_age_identity.sh', 'portable', '--output', identity], self.repo)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertEqual(identity.stat().st_mode & 0o777, 0o600)
        self.assertNotIn(b'AGE-SECRET-KEY-', result.stdout + result.stderr)
        recipient = invoke(['age-keygen', '-y', identity], self.base)
        self.assertEqual(recipient.returncode, 0)
        return identity, recipient.stdout.decode().strip()

    def test_scan_finds_history_alias_and_odd_paths_without_values(self):
        (self.repo / 'safe.txt').write_text('ordinary fixture data\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'first')
        odd = '.env.odd\nname'
        (self.repo / odd).write_text('ordinary fixture data\n')
        (self.repo / 'token.txt').write_text('API_TOKEN=synthetic-value-not-a-real-key\n')
        self.git('add', '.')
        self.git('commit', '-qm', 'second')
        self.git('rm', '-q', odd, 'token.txt')
        self.git('commit', '-qm', 'remove')
        result = self.scanner()
        self.assertEqual(result.returncode, 2, result.stderr.decode())
        body = json.loads(result.stdout)
        self.assertTrue(any(f['scope'] == 'history' and f['path'] == odd for f in body['findings']))
        self.assertNotIn(b'synthetic-value-not-a-real-key', result.stdout + result.stderr)
        self.assertIn('limitations', body)

    def test_scan_empty_repo_and_skips_are_explicit(self):
        result = self.scanner()
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        (self.repo / 'binary').write_bytes(b'\x00binary')
        (self.repo / 'large').write_bytes(b'x' * (2 * 1024 * 1024 + 1))
        self.git('add', '.')
        body = json.loads(self.scanner().stdout)
        self.assertEqual(body['coverage']['binary_blobs'], 1)
        self.assertEqual(body['coverage']['oversized_blobs'], 1)

    def test_migration_encrypts_without_comment_leak_and_verification_is_readonly(self):
        identity, recipient = self.identity()
        secret = b'synthetic-value-not-a-real-key'
        source = b'# private-comment-canary\nAPI_TOKEN=' + secret + b'\nAPP_ENV=dev\nTOKEN_unencrypted=' + secret + b'\n'
        (self.repo / '.env').write_bytes(source)
        (self.repo / '.gitignore').write_text('# no trailing newline')
        result = self.setup('migrate', '--recipient', recipient)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertEqual((self.repo / '.env').read_bytes(), source)
        self.assertEqual((self.repo / '.env.example').read_bytes(), b'API_TOKEN=\nAPP_ENV=\nTOKEN_unencrypted=\n')
        for name in ('.env.example', '.env.sops'):
            self.assertNotIn(secret, (self.repo / name).read_bytes())
            self.assertNotIn(b'private-comment-canary', (self.repo / name).read_bytes())
        before = {p.name: p.read_bytes() for p in self.repo.iterdir() if p.is_file()}
        result = self.setup('verify', '--identity-file', identity)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        self.assertNotIn(secret, result.stdout + result.stderr)
        after = {p.name: p.read_bytes() for p in self.repo.iterdir() if p.is_file()}
        self.assertEqual(before, after)
        decoded = invoke(['sops', 'decrypt', '--input-type', 'dotenv', '--output-type', 'dotenv', '.env.sops'],
                         self.repo, dict(self.env, SOPS_AGE_KEY_FILE=str(identity)))
        self.assertEqual(decoded.returncode, 0)
        self.assertEqual(decoded.stdout, b'API_TOKEN=' + secret + b'\nAPP_ENV=dev\nTOKEN_unencrypted=' + secret + b'\n')

    def test_failed_encryption_and_unsupported_input_leave_no_writes(self):
        (self.repo / '.env').write_text('TOKEN=synthetic-fixture-value\n')
        before = {p.name: p.read_bytes() for p in self.repo.iterdir() if p.is_file()}
        result = self.setup('migrate', '--recipient', 'age1invalid')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(before, {p.name: p.read_bytes() for p in self.repo.iterdir() if p.is_file()})
        (self.repo / '.env').write_text('TOKEN="multiline\nsynthetic-value"\n')
        result = self.setup('migrate', '--recipient', 'age1invalid')
        self.assertEqual(result.returncode, 1)
        self.assertFalse((self.repo / '.env.example').exists())

    def test_unsafe_paths_and_symlink_outputs_are_refused(self):
        (self.repo / '.env').write_text('TOKEN=fixture\n')
        result = self.setup('migrate', '--env-file', '../outside', '--recipient', 'age1invalid')
        self.assertEqual(result.returncode, 1)
        outside = self.base / 'outside'
        outside.write_text('keep')
        (self.repo / '.env.example').symlink_to(outside)
        result = self.setup('migrate', '--force', '--recipient', 'age1invalid')
        self.assertEqual(result.returncode, 1)
        self.assertEqual(outside.read_text(), 'keep')
        (self.repo / '.env.example').unlink()
        (self.repo / '.env').unlink()
        (self.repo / '.env').symlink_to(outside)
        self.assertEqual(self.setup('migrate', '--recipient', 'age1invalid').returncode, 1)

    def test_audit_retains_finding_exit_and_never_mutates(self):
        (self.repo / '.env').write_text('TOKEN=fixture-value\n')
        self.git('add', '.env')
        before = self.git('ls-files', '-s')
        result = self.setup('audit')
        self.assertEqual(result.returncode, 2, result.stderr.decode())
        self.assertEqual(before, self.git('ls-files', '-s'))
        self.assertFalse((self.repo / '.gitignore').exists())

    def test_untracking_is_explicit_and_history_findings_remain(self):
        identity, recipient = self.identity()
        (self.repo / '.env').write_text('TOKEN=fixture-value\n')
        self.git('add', '.env')
        self.git('commit', '-qm', 'fixture exposure')
        result = self.setup('migrate', '--recipient', recipient)
        self.assertEqual(result.returncode, 2, result.stderr.decode())
        self.assertTrue(self.git('ls-files', '--', '.env'))
        result = self.setup('migrate', '--force', '--untrack', '--recipient', recipient)
        self.assertEqual(result.returncode, 2, result.stderr.decode())
        self.assertFalse(self.git('ls-files', '--', '.env'))
        self.assertTrue((self.repo / '.env').exists())
        result = self.setup('verify', '--identity-file', identity)
        self.assertEqual(result.returncode, 2, result.stderr.decode())

    def test_identity_cannot_overwrite_or_follow_dangling_link(self):
        identity, _ = self.identity()
        before = identity.read_bytes()
        result = invoke(['bash', SCRIPTS / 'create_age_identity.sh', 'portable', '--output', identity], self.repo)
        self.assertNotEqual(result.returncode, 0)
        self.assertEqual(identity.read_bytes(), before)
        dangling = self.base / 'dangling'
        dangling.symlink_to(self.base / 'absent')
        result = invoke(['bash', SCRIPTS / 'create_age_identity.sh', 'portable', '--output', dangling], self.repo)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.base / 'absent').exists())
        result = invoke(['bash', SCRIPTS / 'create_age_identity.sh', 'portable', '--output', self.repo / 'key'], self.repo)
        self.assertNotEqual(result.returncode, 0)
        self.assertFalse((self.repo / 'key').exists())

    def test_publish_rolls_back_partial_failure(self):
        spec = importlib.util.spec_from_file_location('setup_fixture', SCRIPTS / 'setup_sops_age.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        (self.repo / '.env.example').write_bytes(b'previous')
        actual_replace = os.replace
        calls = []
        def replace(src, dst):
            calls.append(dst)
            if len(calls) == 2:
                raise OSError('synthetic publish failure')
            return actual_replace(src, dst)
        with patch.object(module.os, 'replace', side_effect=replace):
            with self.assertRaises(OSError):
                module.publish(self.repo, {'.env.example': b'new', '.sops.yaml': b'new'})
        self.assertEqual((self.repo / '.env.example').read_bytes(), b'previous')
        self.assertFalse((self.repo / '.sops.yaml').exists())
        self.assertFalse(list(self.repo.glob('.sops-*')))


if __name__ == '__main__':
    unittest.main(verbosity=2)
