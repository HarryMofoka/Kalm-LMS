"""Tests for Refactoring Mission 10: Grid Aliasing Disaster."""

import ast
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_10_grid_aliasing_disaster import messy_code, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the Before and After worked example implementations."""

    def test_before_and_after_initial_values_match(self):
        self.assertEqual(
            worked_example.before_make_board(3, 4),
            worked_example.after_make_board(3, 4),
        )
        self.assertEqual(
            worked_example.before_make_board(2, 2, "O"),
            worked_example.after_make_board(2, 2, "O"),
        )

    def test_after_rows_are_independent_unlike_before(self):
        buggy = worked_example.before_make_board(3, 4)
        self.assertIs(buggy[0], buggy[1])

        clean = worked_example.after_make_board(3, 4)
        self.assertIsNot(clean[0], clean[1])
        clean[0][0] = "X"
        self.assertEqual(clean[0], ["X", ".", ".", "."])
        self.assertEqual(clean[1], [".", ".", ".", "."])
        self.assertEqual(clean[2], [".", ".", ".", "."])


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: passes on baseline untouched grids and single-row maps."""

    def test_create_empty_grid_dimensions_and_values(self):
        expected = [
            [".", ".", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "."],
        ]
        self.assertEqual(messy_code.create_empty_grid(3, 4), expected)
        self.assertEqual(messy_code.create_empty_grid(2, 2, "O"), [["O", "O"], ["O", "O"]])
        self.assertEqual(messy_code.create_empty_grid(0, 0), [])

    def test_render_grid_output(self):
        grid = [
            [".", "C", "."],
            ["C", ".", "."],
        ]
        self.assertEqual(messy_code.render_grid(grid), ". C .\nC . .")
        self.assertEqual(messy_code.render_grid([]), "")

    def test_build_warehouse_map_single_row(self):
        grid = messy_code.build_warehouse_map(1, 4, [(0, 1)])
        self.assertEqual(grid, [[".", "C", ".", "."]])
        self.assertEqual(messy_code.render_grid(grid), ". C . .")

    def test_build_warehouse_map_ignores_out_of_bounds_on_single_row(self):
        grid = messy_code.build_warehouse_map(1, 4, [(0, 2), (5, 0), (-1, 1), (0, 9)])
        self.assertEqual(grid, [[".", ".", "C", "."]])

    def test_place_crate_returns_bounds_status(self):
        grid = messy_code.create_empty_grid(1, 3)
        self.assertTrue(messy_code.place_crate(grid, 0, 2, "C"))
        self.assertEqual(grid, [[".", ".", "C"]])
        self.assertFalse(messy_code.place_crate(grid, 1, 0, "C"))
        self.assertFalse(messy_code.place_crate(grid, -1, 0, "C"))
        self.assertFalse(messy_code.place_crate([], 0, 0, "C"))


class TestRefactorGoals(unittest.TestCase):
    """Anti-aliasing & multi-row accuracy goals: starts RED on baseline, turn GREEN!"""

    def test_grid_rows_are_distinct_objects(self):
        grid = messy_code.create_empty_grid(3, 4)
        self.assertIsNot(
            grid[0],
            grid[1],
            "Row 0 and Row 1 are the exact same list object (row-aliasing bug)!",
        )
        self.assertIsNot(
            grid[1],
            grid[2],
            "Row 1 and Row 2 are the exact same list object (row-aliasing bug)!",
        )
        self.assertIsNot(
            grid[0],
            grid[2],
            "Row 0 and Row 2 are the exact same list object (row-aliasing bug)!",
        )

    def test_placing_crate_on_row_0_does_not_modify_other_rows(self):
        grid = messy_code.create_empty_grid(3, 4)
        messy_code.place_crate(grid, 0, 1, "C")
        self.assertEqual(grid[0], [".", "C", ".", "."])
        self.assertEqual(
            grid[1],
            [".", ".", ".", "."],
            "Placing a crate on row 0 contaminated row 1!",
        )
        self.assertEqual(
            grid[2],
            [".", ".", ".", "."],
            "Placing a crate on row 0 contaminated row 2!",
        )

    def test_build_warehouse_map_multi_row_exact_coordinates(self):
        grid = messy_code.build_warehouse_map(3, 4, [(0, 1), (2, 3)])
        expected = [
            [".", "C", ".", "."],
            [".", ".", ".", "."],
            [".", ".", ".", "C"],
        ]
        self.assertEqual(
            grid,
            expected,
            "Crates contaminated other rows! Fix row aliasing in `create_empty_grid`.",
        )
        self.assertEqual(
            messy_code.render_grid(grid),
            ". C . .\n. . . .\n. . . C",
        )

    def test_no_nested_list_multiplication_aliasing(self):
        source = Path(messy_code.__file__).read_text(encoding="utf-8")
        tree = ast.parse(source)
        aliasing_lines = []
        for node in ast.walk(tree):
            if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Mult):
                for side in (node.left, node.right):
                    if isinstance(side, ast.List) and any(
                        isinstance(el, (ast.List, ast.BinOp, ast.ListComp))
                        for el in side.elts
                    ):
                        aliasing_lines.append(node.lineno)
        self.assertEqual(
            aliasing_lines,
            [],
            f"Detected `[[...] * ...] * ...` nested list multiplication on line(s) {aliasing_lines}; "
            "use a list comprehension such as `[[fill for _ in range(cols)] for _ in range(rows)]`.",
        )


if __name__ == "__main__":
    unittest.main()
