"""Tests for Refactoring Mission 06: while Loop Traps."""

import ast
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_06_while_loop_traps import messy_code, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the Before and After worked example implementations match."""

    def test_before_and_after_match_typical(self):
        readings = [19.0, 25.0, 26.5, 24.9, 30.1, 25.1]
        expected = [(2, 26.5), (4, 30.1), (5, 25.1)]
        self.assertEqual(worked_example.before_find_spikes(readings, 25.0), expected)
        self.assertEqual(worked_example.after_find_spikes(readings, 25.0), expected)

    def test_before_and_after_match_edge_cases(self):
        cases = [
            ([], 10.0),
            ([10.0, 10.0, 9.9], 10.0),
            ([-5.0, -1.0, 0.0], -2.0),
            ([100.0], 50.0),
        ]
        for readings, threshold in cases:
            self.assertEqual(
                worked_example.before_find_spikes(readings, threshold),
                worked_example.after_find_spikes(readings, threshold),
            )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: must stay 100% GREEN before, during, and after refactoring."""

    def test_typical_readings(self):
        readings = [21.5, 25.0, 28.4, 24.0, 30.1]
        result = messy_code.analyze_temperature_readings(readings, 25.0)
        self.assertEqual(
            result,
            {
                "count": 5,
                "average": 25.8,
                "max_temp": 30.1,
                "min_temp": 21.5,
                "high_indices": [1, 2, 4],
                "deltas": [3.5, 3.4, -4.4, 6.1],
            },
        )

    def test_empty_readings(self):
        result = messy_code.analyze_temperature_readings([], 25.0)
        self.assertEqual(
            result,
            {
                "count": 0,
                "average": 0.0,
                "max_temp": None,
                "min_temp": None,
                "high_indices": [],
                "deltas": [],
            },
        )

    def test_single_reading(self):
        below = messy_code.analyze_temperature_readings([19.5], 20.0)
        self.assertEqual(below["count"], 1)
        self.assertEqual(below["average"], 19.5)
        self.assertEqual(below["max_temp"], 19.5)
        self.assertEqual(below["min_temp"], 19.5)
        self.assertEqual(below["high_indices"], [])
        self.assertEqual(below["deltas"], [])

        at_threshold = messy_code.analyze_temperature_readings([20.0], 20.0)
        self.assertEqual(at_threshold["high_indices"], [0])

    def test_negative_and_fluctuating_readings(self):
        readings = [-2.5, -5.0, -1.0, -5.0]
        result = messy_code.analyze_temperature_readings(readings, -2.0)
        self.assertEqual(
            result,
            {
                "count": 4,
                "average": -3.38,
                "max_temp": -1.0,
                "min_temp": -5.0,
                "high_indices": [2],
                "deltas": [-2.5, 4.0, -4.0],
            },
        )

    def test_all_above_and_none_above_threshold(self):
        readings = [30.0, 31.2, 32.5]
        all_high = messy_code.analyze_temperature_readings(readings, 30.0)
        self.assertEqual(all_high["high_indices"], [0, 1, 2])
        none_high = messy_code.analyze_temperature_readings(readings, 40.0)
        self.assertEqual(none_high["high_indices"], [])


class TestRefactorGoals(unittest.TestCase):
    """Structural refactoring goals: starts RED on baseline, turn GREEN!"""

    def _parse_messy_ast(self):
        source = Path(messy_code.__file__).read_text(encoding="utf-8")
        return ast.parse(source)

    def test_no_while_loops_in_module(self):
        tree = self._parse_messy_ast()
        while_nodes = [node for node in ast.walk(tree) if isinstance(node, ast.While)]
        self.assertEqual(
            len(while_nodes),
            0,
            f"Found {len(while_nodes)} `while` loop(s) in messy_code.py; "
            "replace manual-index `while` loops with Pythonic `for` loops.",
        )

    def test_uses_for_loops_or_comprehensions(self):
        tree = self._parse_messy_ast()
        for_nodes = [
            node
            for node in ast.walk(tree)
            if isinstance(node, (ast.For, ast.ListComp, ast.GeneratorExp))
        ]
        self.assertGreaterEqual(
            len(for_nodes),
            1,
            "Expected at least one Pythonic `for` loop or comprehension in messy_code.py.",
        )

    def test_uses_enumerate_for_index_tracking(self):
        tree = self._parse_messy_ast()
        uses_enumerate = any(
            isinstance(node, ast.Call)
            and isinstance(node.func, ast.Name)
            and node.func.id == "enumerate"
            for node in ast.walk(tree)
        )
        self.assertTrue(
            uses_enumerate,
            "Use `enumerate(...)` to track indices cleanly instead of manual counters.",
        )


if __name__ == "__main__":
    unittest.main()
