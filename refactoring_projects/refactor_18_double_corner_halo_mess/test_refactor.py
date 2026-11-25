"""Test suite for Refactoring Mission 18: Double-Corner Halo Mess."""

import ast
import inspect
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_18_double_corner_halo_mess import (  # noqa: E402
    messy_code,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Demonstrates the double-corner bug in before_walk_square vs clean after_walk_square."""

    def test_before_has_duplicate_corners_while_after_is_exact(self):
        before = worked_example.before_walk_square(3)
        after = worked_example.after_walk_square(3)

        self.assertEqual(len(before), 12)
        self.assertGreater(len(before), len(set(before)))

        self.assertEqual(
            after,
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)],
        )
        self.assertEqual(len(after), len(set(after)))

    def test_after_handles_small_and_empty_squares(self):
        self.assertEqual(worked_example.after_walk_square(1), [(0, 0)])
        self.assertEqual(worked_example.after_walk_square(0), [])
        self.assertEqual(worked_example.after_walk_square(-2), [])


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net — normal >= 2x2 grids must stay 100% GREEN."""

    def test_patrol_rectangle_path_4x3(self):
        expected = [
            (0, 0), (0, 1), (0, 2), (0, 3),
            (1, 3), (2, 3),
            (2, 2), (2, 1), (2, 0),
            (1, 0),
        ]
        self.assertEqual(messy_code.patrol_rectangle_path(4, 3), expected)

    def test_patrol_rectangle_path_3x3(self):
        expected = [
            (0, 0), (0, 1), (0, 2),
            (1, 2), (2, 2),
            (2, 1), (2, 0),
            (1, 0),
        ]
        self.assertEqual(messy_code.patrol_rectangle_path(3, 3), expected)

    def test_patrol_rectangle_path_5x4(self):
        path = messy_code.patrol_rectangle_path(5, 4)
        self.assertEqual(len(path), 14)
        self.assertEqual(len(path), len(set(path)))
        self.assertEqual(path[0], (0, 0))
        self.assertEqual(path[-1], (1, 0))

    def test_patrol_position_wraps_clockwise(self):
        self.assertEqual(messy_code.patrol_position(4, 3, 0), (0, 0))
        self.assertEqual(messy_code.patrol_position(4, 3, 5), (2, 3))
        self.assertEqual(messy_code.patrol_position(4, 3, 15), (2, 3))


class TestRefactorGoals(unittest.TestCase):
    """Refactoring goals — RED on baseline, GREEN once refactored cleanly."""

    def test_thin_rectangles_exact_deduplicated_paths(self):
        path_4x1 = messy_code.patrol_rectangle_path(4, 1)
        self.assertEqual(path_4x1, [(0, 0), (0, 1), (0, 2), (0, 3)])
        self.assertEqual(len(path_4x1), 4)

        path_1x3 = messy_code.patrol_rectangle_path(1, 3)
        self.assertEqual(path_1x3, [(0, 0), (1, 0), (2, 0)])
        self.assertEqual(len(path_1x3), 3)

        path_1x1 = messy_code.patrol_rectangle_path(1, 1)
        self.assertEqual(path_1x1, [(0, 0)])
        self.assertEqual(len(path_1x1), 1)

    def test_empty_and_non_positive_dimensions_return_empty_path(self):
        self.assertEqual(messy_code.patrol_rectangle_path(0, 5), [])
        self.assertEqual(messy_code.patrol_rectangle_path(5, 0), [])
        self.assertEqual(messy_code.patrol_rectangle_path(0, 0), [])
        self.assertEqual(messy_code.patrol_rectangle_path(-3, 4), [])

    def test_no_not_in_path_dedup_bandaid(self):
        source = inspect.getsource(messy_code.patrol_rectangle_path)
        tree = ast.parse(source)
        for node in ast.walk(tree):
            if isinstance(node, ast.Compare):
                for op in node.ops:
                    if isinstance(op, (ast.NotIn, ast.In)):
                        self.fail(
                            "patrol_rectangle_path still uses an 'in' / 'not in' "
                            "membership check; use exact leg bounds and thin-shape guards instead."
                        )

    def test_is_border_helper_exists_and_classifies_cells(self):
        self.assertTrue(
            hasattr(messy_code, "is_border"),
            "Expected helper function `is_border(row, col, width, height)` in messy_code.py.",
        )
        is_border = getattr(messy_code, "is_border")

        self.assertTrue(is_border(0, 0, 4, 3))
        self.assertTrue(is_border(2, 3, 4, 3))
        self.assertTrue(is_border(1, 0, 4, 3))
        self.assertFalse(is_border(1, 1, 4, 3))
        self.assertFalse(is_border(1, 2, 4, 3))
        self.assertTrue(is_border(0, 2, 4, 1))
        self.assertFalse(is_border(-1, 0, 4, 3))
        self.assertFalse(is_border(3, 0, 4, 3))
        self.assertFalse(is_border(0, 4, 4, 3))


if __name__ == "__main__":
    unittest.main()
