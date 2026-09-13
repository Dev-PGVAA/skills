import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'planning-with-files/scripts/plan.py'
spec = importlib.util.spec_from_file_location('planner', SCRIPT)
planner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(planner)


class PlanTests(unittest.TestCase):
    def test_init_preserves_existing(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            self.assertEqual(len(planner.init(p, 'Обновление скиллов')['created']), 3)
            (p/'findings.md').write_text('keep exact')
            self.assertEqual(planner.init(p, 'Another title')['created'], [])
            self.assertEqual((p/'findings.md').read_text(), 'keep exact')
            self.assertEqual(planner.check(p)[0], 1)

    def test_complete_and_false_completion(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            for status, extra, code in [('complete', '', 0), ('pending', '', 1),
                    ('complete', '- [ ] unfinished', 2), ('mystery', '', 2),
                    ('complete', '- **Status:** pending', 2)]:
                (p/'task_plan.md').write_text(f'### Phase 1: Work\n- **Status:** {status}\n{extra}\n')
                self.assertEqual(planner.check(p)[0], code)

    def test_unrelated_sections_and_code_not_status(self):
        text = '```md\n### Phase X: Example\n**Status:** pending\n```\n'
        text += '### Phase 1: Real\n**Status:** complete\n## Notes\n**Status:** pending\n'
        self.assertEqual(planner.parse_phases(text)[0]['statuses'], ['complete'])
        self.assertEqual(len(planner.parse_phases(text)), 1)

    def test_missing_status_and_empty_are_invalid(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            for text in ['', '### Phase 1: no status\n', 'No phases\n**Status:** complete']:
                (p/'task_plan.md').write_text(text)
                self.assertEqual(planner.check(p)[0], 2)

    def test_symlink_targets_rejected_without_partial_init(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            outside = p/'outside'; outside.write_text('private')
            task = p/'task'; task.mkdir()
            (task/'findings.md').symlink_to(outside)
            with self.assertRaises(ValueError): planner.init(task, 'task')
            self.assertFalse((task/'task_plan.md').exists())
            self.assertEqual(outside.read_text(), 'private')
            link = p/'linked'; link.symlink_to(task, target_is_directory=True)
            with self.assertRaises(ValueError): planner.checked_dir(str(link))

    def test_missing_task_not_selected_from_other_directory(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            planner.init(p/'task-a', 'A')
            with self.assertRaises(ValueError): planner.check(p/'task-b')


if __name__ == '__main__': unittest.main()
