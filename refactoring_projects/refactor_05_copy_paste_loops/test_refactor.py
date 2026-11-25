"""Test suite for Refactor 05: Copy-Paste Loops."""

import ast
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_05_copy_paste_loops import messy_code, worked_example


def _parse_messy_module():
    source = Path(messy_code.__file__).read_text(encoding="utf-8")
    return ast.parse(source)


def _get_top_level_functions(tree):
    return {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}


class TestWorkedExample(unittest.TestCase):
    """Verify before_team_stats and after_team_stats agree across normal and edge cases."""

    def test_before_and_after_match(self):
        cases = [
            ([10, 25, 18], [40, 35, 38, 42], []),
            ([], [], []),
            ([0, 0, 0], [5], [100, 50, 75]),
            ([1, 2, 3, 4, 5], [99], [7, 7, 7]),
        ]
        for alpha, beta, gamma in cases:
            with self.subTest(alpha=alpha, beta=beta, gamma=gamma):
                self.assertEqual(
                    worked_example.before_team_stats(alpha, beta, gamma),
                    worked_example.after_team_stats(alpha, beta, gamma),
                )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: summarize_workout_week must return exact stats for every session."""

    def test_typical_active_week(self):
        result = messy_code.summarize_workout_week(
            [20, 0, 35, 40, 0, 25, 30],
            [15, 15, 0, 0, 20, 0, 10],
            [50, 60, 55, 0, 0, 70, 65],
        )
        self.assertEqual(
            result,
            {
                "morning": {"total": 150, "best": 40, "active_days": 5},
                "afternoon": {"total": 60, "best": 20, "active_days": 4},
                "evening": {"total": 300, "best": 70, "active_days": 5},
            },
        )

    def test_all_empty_sessions(self):
        self.assertEqual(
            messy_code.summarize_workout_week([], [], []),
            {
                "morning": {"total": 0, "best": 0, "active_days": 0},
                "afternoon": {"total": 0, "best": 0, "active_days": 0},
                "evening": {"total": 0, "best": 0, "active_days": 0},
            },
        )

    def test_rest_week_with_all_zeros(self):
        self.assertEqual(
            messy_code.summarize_workout_week([0, 0, 0], [0], [0, 0, 0, 0]),
            {
                "morning": {"total": 0, "best": 0, "active_days": 0},
                "afternoon": {"total": 0, "best": 0, "active_days": 0},
                "evening": {"total": 0, "best": 0, "active_days": 0},
            },
        )

    def test_single_day_and_mixed_empty_sessions(self):
        self.assertEqual(
            messy_code.summarize_workout_week([42], [], [0, 99, 0]),
            {
                "morning": {"total": 42, "best": 42, "active_days": 1},
                "afternoon": {"total": 0, "best": 0, "active_days": 0},
                "evening": {"total": 99, "best": 99, "active_days": 1},
            },
        )

    def test_inputs_are_not_mutated(self):
        morning = [10, 20]
        afternoon = [0, 5]
        evening = [30]
        messy_code.summarize_workout_week(morning, afternoon, evening)
        self.assertEqual(morning, [10, 20])
        self.assertEqual(afternoon, [0, 5])
        self.assertEqual(evening, [30])


class TestRefactorGoals(unittest.TestCase):
    """Refactoring checklist: eliminate the 3 copy-pasted loops with a DRY helper function."""

    def test_delegates_to_helper_function(self):
        tree = _parse_messy_module()
        funcs = _get_top_level_functions(tree)
        self.assertIn("summarize_workout_week", funcs, "Function 'summarize_workout_week' must exist.")

        helper_names = {name for name in funcs if name != "summarize_workout_week"}
        self.assertGreaterEqual(
            len(helper_names),
            1,
            "Extract a reusable helper function (e.g. `summarize_session(reps)`) to eliminate the duplicated loops.",
        )

        main_func = funcs["summarize_workout_week"]
        called_helpers = {
            node.func.id
            for node in ast.walk(main_func)
            if isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id in helper_names
        }
        self.assertGreaterEqual(
            len(called_helpers),
            1,
            f"summarize_workout_week must call your helper function ({sorted(helper_names)}) instead of repeating the loop logic!",
        )

    def test_at_most_one_loop_in_summarize_workout_week(self):
        tree = _parse_messy_module()
        funcs = _get_top_level_functions(tree)
        self.assertIn("summarize_workout_week", funcs, "Function 'summarize_workout_week' must exist.")

        main_func = funcs["summarize_workout_week"]
        loop_count = sum(
            1
            for node in ast.walk(main_func)
            if isinstance(node, (ast.For, ast.While, ast.comprehension))
        )
        self.assertLessEqual(
            loop_count,
            1,
            f"Found {loop_count} loops inside summarize_workout_week (must be <= 1). "
            "Move the per-session loop into a single DRY helper function and call it for each session!",
        )

    def test_summarize_workout_week_is_concise(self):
        tree = _parse_messy_module()
        funcs = _get_top_level_functions(tree)
        self.assertIn("summarize_workout_week", funcs, "Function 'summarize_workout_week' must exist.")

        main_func = funcs["summarize_workout_week"]
        stmt_count = sum(1 for node in ast.walk(main_func) if isinstance(node, ast.stmt)) - 1
        self.assertLessEqual(
            stmt_count,
            10,
            f"summarize_workout_week contains {stmt_count} statements (expected <= 10 after extracting your helper). "
            "Keep summarize_workout_week focused on delegating to your helper and assembling the final dictionary!",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
