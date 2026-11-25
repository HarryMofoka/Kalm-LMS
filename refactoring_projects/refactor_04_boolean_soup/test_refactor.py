"""Test suite for Refactor 04: Boolean Soup."""

import ast
import itertools
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_04_boolean_soup import messy_code, worked_example


def _parse_messy_module():
    source = Path(messy_code.__file__).read_text(encoding="utf-8")
    return ast.parse(source)


def _get_function_node(tree, func_name):
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return node
    return None


def _is_bool_constant(node):
    return isinstance(node, ast.Constant) and type(node.value) is bool


class TestWorkedExample(unittest.TestCase):
    """Verify before_has_access and after_has_access match on all 16 truth-table rows."""

    def test_all_sixteen_boolean_combinations(self):
        for is_admin, is_active, has_badge, is_locked_out in itertools.product([False, True], repeat=4):
            with self.subTest(
                is_admin=is_admin,
                is_active=is_active,
                has_badge=has_badge,
                is_locked_out=is_locked_out,
            ):
                self.assertEqual(
                    worked_example.before_has_access(is_admin, is_active, has_badge, is_locked_out),
                    worked_example.after_has_access(is_admin, is_active, has_badge, is_locked_out),
                )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: can_launch_rocket must obey exact launch rules for every combination."""

    def test_full_truth_table_and_fuel_boundaries(self):
        fuel_values = [0, 50, 79, 79.9, 80, 80.0, 95, 100]
        overrides = ["", None, "ALPHA-8", "alpha-9", "ALPHA-9"]

        for fuel, weather_clear, crew_ready, override_code in itertools.product(
            fuel_values, [False, True], [False, True], overrides
        ):
            expected = (fuel >= 80) and crew_ready and (weather_clear or override_code == "ALPHA-9")
            with self.subTest(
                fuel=fuel,
                weather_clear=weather_clear,
                crew_ready=crew_ready,
                override_code=override_code,
            ):
                actual = messy_code.can_launch_rocket(fuel, weather_clear, crew_ready, override_code)
                self.assertIs(type(actual), bool, "can_launch_rocket must return a bool (True or False).")
                self.assertEqual(actual, expected)


class TestRefactorGoals(unittest.TestCase):
    """Refactoring checklist: eliminate boolean soup and use clean boolean expressions."""

    def test_no_comparisons_to_true_or_false(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "can_launch_rocket")
        self.assertIsNotNone(func, "Function 'can_launch_rocket' must exist.")

        bad_compares = []
        for node in ast.walk(func):
            if isinstance(node, ast.Compare):
                operands = [node.left] + list(node.comparators)
                if any(_is_bool_constant(op) for op in operands):
                    bad_compares.append(ast.unparse(node))

        self.assertEqual(
            bad_compares,
            [],
            f"Found explicit comparisons to True/False: {bad_compares}. "
            "Use truthiness directly (e.g. `if crew_ready:` or `not weather_clear`), never `== True` / `== False` / `is True`!",
        )

    def test_no_redundant_if_returning_or_assigning_bool_literals(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "can_launch_rocket")
        self.assertIsNotNone(func, "Function 'can_launch_rocket' must exist.")

        redundant_returns = []
        redundant_flag_assigns = []

        for node in ast.walk(func):
            if isinstance(node, ast.If):
                # Pattern 1: `if cond: return True else: return False`
                if (
                    len(node.body) == 1
                    and isinstance(node.body[0], ast.Return)
                    and _is_bool_constant(node.body[0].value)
                    and len(node.orelse) == 1
                    and isinstance(node.orelse[0], ast.Return)
                    and _is_bool_constant(node.orelse[0].value)
                ):
                    redundant_returns.append(ast.unparse(node))

                # Pattern 2: `if cond: flag = True` (or `flag = False`)
                if (
                    len(node.body) == 1
                    and isinstance(node.body[0], ast.Assign)
                    and _is_bool_constant(node.body[0].value)
                ):
                    redundant_flag_assigns.append(ast.unparse(node.body[0]))

        self.assertEqual(
            redundant_returns,
            [],
            f"Found redundant `if ...: return True else: return False` pattern: {redundant_returns}. "
            "Return the boolean expression directly!",
        )
        self.assertEqual(
            redundant_flag_assigns,
            [],
            f"Found redundant boolean flag assignment inside `if`: {redundant_flag_assigns}. "
            "Assign the condition directly (e.g. `fuel_ok = fuel_pct >= 80`) or combine expressions with `and`/`or`!",
        )

    def test_concise_boolean_expression(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "can_launch_rocket")
        self.assertIsNotNone(func, "Function 'can_launch_rocket' must exist.")

        bool_ops = [node for node in ast.walk(func) if isinstance(node, ast.BoolOp)]
        if_nodes = [node for node in ast.walk(func) if isinstance(node, ast.If)]

        self.assertGreaterEqual(
            len(bool_ops),
            1,
            "Combine conditions directly using Python boolean operators (`and`, `or`) instead of nested `if` blocks.",
        )
        self.assertLessEqual(
            len(if_nodes),
            2,
            f"Found {len(if_nodes)} `if` statements in can_launch_rocket (expected <= 2). "
            "Simplify the launch logic into a concise boolean expression!",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
