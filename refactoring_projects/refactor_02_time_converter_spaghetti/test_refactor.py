"""Test suite for Refactor 02: Time Converter Spaghetti."""

import ast
import re
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_02_time_converter_spaghetti import messy_code, worked_example


def _parse_messy_module():
    source = Path(messy_code.__file__).read_text(encoding="utf-8")
    return ast.parse(source)


def _get_top_level_functions(tree):
    return {node.name: node for node in tree.body if isinstance(node, ast.FunctionDef)}


class TestWorkedExample(unittest.TestCase):
    """Verify worked example Before and After produce identical distance summaries."""

    def test_before_and_after_match(self):
        cases = [
            (0, 0),
            (5, 95),
            (1250, 3050),
            (999, 1),
            (10000, 42),
        ]
        for leg_a, leg_b in cases:
            with self.subTest(leg_a=leg_a, leg_b=leg_b):
                self.assertEqual(
                    worked_example.before_convert(leg_a, leg_b),
                    worked_example.after_convert_distance(leg_a, leg_b),
                )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: format_flight_schedule must preserve exact formatting for all flights."""

    def test_same_day_morning_flight(self):
        self.assertEqual(
            messy_code.format_flight_schedule(8, 5, 165),
            "Depart 08:05 | Duration 02h 45m | Arrive 10:50",
        )

    def test_same_day_zero_padding_everywhere(self):
        self.assertEqual(
            messy_code.format_flight_schedule(1, 2, 63),
            "Depart 01:02 | Duration 01h 03m | Arrive 02:05",
        )

    def test_overnight_flight_crossing_midnight(self):
        self.assertEqual(
            messy_code.format_flight_schedule(22, 30, 195),
            "Depart 22:30 | Duration 03h 15m | Arrive 01:45 (+1d)",
        )

    def test_exact_midnight_arrival(self):
        self.assertEqual(
            messy_code.format_flight_schedule(23, 0, 60),
            "Depart 23:00 | Duration 01h 00m | Arrive 00:00 (+1d)",
        )

    def test_multi_day_ultra_long_haul_flight(self):
        # 23:45 + 1500 mins (25h 00m) -> 2 days later at 00:45
        self.assertEqual(
            messy_code.format_flight_schedule(23, 45, 1500),
            "Depart 23:45 | Duration 25h 00m | Arrive 00:45 (+2d)",
        )

    def test_zero_duration_flight(self):
        self.assertEqual(
            messy_code.format_flight_schedule(0, 0, 0),
            "Depart 00:00 | Duration 00h 00m | Arrive 00:00",
        )


class TestRefactorGoals(unittest.TestCase):
    """Refactoring checklist: turns GREEN once constants, helper(s), and clean formatting are used."""

    def test_named_time_constants_and_no_hardcoded_time_numbers(self):
        tree = _parse_messy_module()
        const_pattern = re.compile(r"^[A-Z][A-Z0-9_]+$")

        module_constants = []
        for stmt in tree.body:
            if isinstance(stmt, ast.Assign):
                for target in stmt.targets:
                    if isinstance(target, ast.Name) and const_pattern.match(target.id):
                        module_constants.append(target.id)
            elif isinstance(stmt, ast.AnnAssign):
                if isinstance(stmt.target, ast.Name) and const_pattern.match(stmt.target.id):
                    module_constants.append(stmt.target.id)

        self.assertGreaterEqual(
            len(module_constants),
            2,
            f"Define at least 2 UPPER_CASE time constants at module level (e.g. MINUTES_PER_HOUR = 60, "
            f"MINUTES_PER_DAY = 1440). Found: {module_constants}",
        )

        forbidden_literals = {60, 1440, 24}
        hardcoded_found = []
        for func in _get_top_level_functions(tree).values():
            for node in ast.walk(func):
                if isinstance(node, ast.Constant) and type(node.value) is int and node.value in forbidden_literals:
                    hardcoded_found.append((func.name, node.value))

        self.assertEqual(
            hardcoded_found,
            [],
            f"Found hardcoded time literals inside functions: {hardcoded_found}. "
            "Use your named UPPER_CASE constants instead of raw 60, 24, or 1440.",
        )

    def test_extracts_and_calls_helper_function(self):
        tree = _parse_messy_module()
        funcs = _get_top_level_functions(tree)
        self.assertIn("format_flight_schedule", funcs, "Function 'format_flight_schedule' must exist.")

        helper_names = {name for name in funcs if name != "format_flight_schedule"}
        self.assertGreaterEqual(
            len(helper_names),
            1,
            "Extract at least one helper function (e.g. format_clock, format_duration, or split_minutes).",
        )

        main_func = funcs["format_flight_schedule"]
        called_helpers = set()
        for node in ast.walk(main_func):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in helper_names:
                    called_helpers.add(node.func.id)

        self.assertGreaterEqual(
            len(called_helpers),
            1,
            f"format_flight_schedule should call at least one of your helper functions ({sorted(helper_names)}).",
        )

    def test_clean_formatting_without_manual_zero_padding(self):
        tree = _parse_messy_module()

        # Check for clean formatting mechanisms: f-strings, .format(), .zfill(), or % formatting
        uses_clean_formatting = False
        manual_zero_concat = False
        total_if_statements = 0

        for node in ast.walk(tree):
            if isinstance(node, ast.JoinedStr):
                uses_clean_formatting = True
            elif isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                if node.func.attr in {"format", "zfill"}:
                    uses_clean_formatting = True
            elif isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
                if isinstance(node.left, ast.Constant) and node.left.value == "0":
                    manual_zero_concat = True
            elif isinstance(node, ast.If):
                total_if_statements += 1

        self.assertFalse(
            manual_zero_concat,
            'Remove manual zero-padding like \'"0" + str(...)\' — use f-strings with \':02d\' instead!',
        )
        self.assertTrue(
            uses_clean_formatting,
            "Use clean string formatting (such as f-strings like f'{hours:02d}:{minutes:02d}') instead of '+' string concatenation.",
        )
        self.assertLessEqual(
            total_if_statements,
            2,
            f"Found {total_if_statements} 'if' statements across the module — eliminate the manual '< 10' padding branches "
            "using f-string zero-padding (':02d').",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
