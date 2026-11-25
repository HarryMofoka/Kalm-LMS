"""Tests for Refactoring Mission 14: Break up a monolithic god-function."""

import ast
import inspect
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_14_god_function_breakup import (
    messy_code,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Proves the worked example monolithic and modular bookings match."""

    def test_member_and_non_member_bookings_match(self):
        for args in [
            ("Nadia", 3, 120.0, True),
            ("  Sam ", 2, 85.5, False),
            ("Toby", 1, 200.0, True),
        ]:
            self.assertEqual(
                worked_example.before_process_booking(*args),
                worked_example.after_process_booking(*args),
            )

    def test_invalid_inputs_raise_value_error(self):
        bad_cases = [
            ("", 2, 100.0, False),
            ("Nadia", 0, 100.0, False),
            ("Nadia", 2, -10.0, False),
        ]
        for args in bad_cases:
            with self.assertRaises(ValueError):
                worked_example.before_process_booking(*args)
            with self.assertRaises(ValueError):
                worked_example.after_process_booking(*args)


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net for generate_invoice_summary (must stay GREEN!)."""

    def test_standard_invoice_with_save10_and_receipt_text(self):
        items = [("Notebook", 2, 15.0), ("Pen Pack", 1, 10.0)]
        result = messy_code.generate_invoice_summary("  Ada Lovelace ", items, "save10", 0.15)
        self.assertEqual(result["customer"], "Ada Lovelace")
        self.assertEqual(result["subtotal"], 40.0)
        self.assertEqual(result["discount"], 4.0)
        self.assertEqual(result["tax"], 5.4)
        self.assertEqual(result["total"], 41.4)
        self.assertEqual(result["total_units"], 3)
        self.assertEqual(result["loyalty_points"], 3)
        self.assertEqual(result["loyalty_tier"], "Bronze")
        expected_receipt = "\n".join(
            [
                "INVOICE FOR: Ada Lovelace",
                "================================",
                "- Notebook x2 @ $15.00 = $30.00",
                "- Pen Pack x1 @ $10.00 = $10.00",
                "--------------------------------",
                "Subtotal: $40.00",
                "Discount: -$4.00",
                "Tax (15.0%): $5.40",
                "TOTAL: $41.40",
                "Loyalty: 3 pts (Bronze)",
            ]
        )
        self.assertEqual(result["receipt"], expected_receipt)

    def test_save20_threshold_and_gold_bonus_loyalty(self):
        # Below $100 -> SAVE20 gives $0 discount
        small = messy_code.generate_invoice_summary(
            "Ben", [("Cable", 2, 25.0)], "SAVE20", 0.10
        )
        self.assertEqual(small["discount"], 0.0)
        self.assertEqual(small["total"], 55.0)

        # >= $100 and big order -> 20% off + 25 bonus points -> Gold tier
        big = messy_code.generate_invoice_summary(
            "Cleo", [("Monitor", 5, 70.0)], "SAVE20", 0.10
        )
        self.assertEqual(big["subtotal"], 350.0)
        self.assertEqual(big["discount"], 70.0)
        self.assertEqual(big["tax"], 28.0)
        self.assertEqual(big["total"], 308.0)
        self.assertEqual(big["loyalty_points"], 28 + 25)
        self.assertEqual(big["loyalty_tier"], "Gold")

    def test_welcome5_caps_at_subtotal_and_silver_tier(self):
        tiny = messy_code.generate_invoice_summary(
            "Dan", [("Sticker", 1, 3.0)], "WELCOME5", 0.10
        )
        self.assertEqual(tiny["discount"], 3.0)
        self.assertEqual(tiny["total"], 0.0)

        mid = messy_code.generate_invoice_summary(
            "Eva", [("Chair", 2, 110.0)], None, 0.05
        )
        self.assertEqual(mid["discount"], 0.0)
        self.assertEqual(mid["loyalty_points"], 22)
        self.assertEqual(mid["loyalty_tier"], "Silver")

    def test_validation_errors(self):
        valid_items = [("Book", 1, 20.0)]
        with self.assertRaises(ValueError):
            messy_code.generate_invoice_summary("   ", valid_items, None, 0.1)
        with self.assertRaises(ValueError):
            messy_code.generate_invoice_summary("Ada", [], None, 0.1)
        with self.assertRaises(ValueError):
            messy_code.generate_invoice_summary("Ada", [("Book", 0, 20.0)], None, 0.1)
        with self.assertRaises(ValueError):
            messy_code.generate_invoice_summary("Ada", [("Book", 1, -5.0)], None, 0.1)
        with self.assertRaises(ValueError):
            messy_code.generate_invoice_summary("Ada", valid_items, None, 1.5)
        with self.assertRaises(ValueError):
            messy_code.generate_invoice_summary("Ada", valid_items, "BOGUS", 0.1)


class TestRefactorGoals(unittest.TestCase):
    """Structural goals: small orchestrator, >=3 helpers, no function >35 lines."""

    def _get_module_functions(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)
        return {
            node.name: node
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
        }

    def test_generate_invoice_summary_is_at_most_30_lines(self):
        funcs = self._get_module_functions()
        main_fn = funcs["generate_invoice_summary"]
        length = main_fn.end_lineno - main_fn.lineno + 1
        self.assertLessEqual(
            length,
            30,
            f"generate_invoice_summary is {length} lines long; refactor it to <= 30 lines.",
        )

    def test_delegates_to_at_least_three_extracted_helpers(self):
        funcs = self._get_module_functions()
        main_fn = funcs["generate_invoice_summary"]
        helper_names = set(funcs.keys()) - {"generate_invoice_summary"}

        called_helpers = set()
        for node in ast.walk(main_fn):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in helper_names:
                    called_helpers.add(node.func.id)

        self.assertGreaterEqual(
            len(called_helpers),
            3,
            f"generate_invoice_summary calls only {len(called_helpers)} helper(s) "
            f"({sorted(called_helpers)}); delegate to at least 3 extracted helper functions.",
        )

    def test_no_function_exceeds_35_lines(self):
        funcs = self._get_module_functions()
        oversized = {
            name: node.end_lineno - node.lineno + 1
            for name, node in funcs.items()
            if (node.end_lineno - node.lineno + 1) > 35
        }
        self.assertEqual(
            oversized,
            {},
            f"Every function in messy_code.py should be <= 35 lines, found oversized: {oversized}",
        )


if __name__ == "__main__":
    unittest.main()
