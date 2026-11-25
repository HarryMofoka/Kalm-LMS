"""Test suite for Refactor 01: Messy Receipt Math."""

import ast
import re
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_01_messy_receipt_math import messy_code, worked_example


def _parse_messy_module():
    source = Path(messy_code.__file__).read_text(encoding="utf-8")
    return ast.parse(source)


def _get_function_node(tree, func_name):
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return node
    return None


class TestWorkedExample(unittest.TestCase):
    """Verify the worked example Before and After produce identical results."""

    def test_before_and_after_match_across_orders(self):
        cases = [
            (0.0, 0, False),
            (0.0, 0, True),
            (45.0, 2, False),
            (45.0, 2, True),
            (19.95, 3, False),
            (19.95, 3, True),
            (120.50, 5, True),
        ]
        for unit_price, quantity, is_takeaway in cases:
            with self.subTest(unit_price=unit_price, quantity=quantity, is_takeaway=is_takeaway):
                self.assertEqual(
                    worked_example.before_calc(unit_price, quantity, is_takeaway),
                    worked_example.after_calculate_order_total(unit_price, quantity, is_takeaway),
                )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: refactoring must NEVER change calculate_shipping_total outputs."""

    def test_standard_parcel_delivery(self):
        # Base 15.0 + weight (2 * 2.5 = 5.0) + dist (10 * 0.5 = 5.0) = 25.0 -> +15% VAT = 28.75
        self.assertEqual(messy_code.calculate_shipping_total(2.0, 10.0, False), 28.75)

    def test_express_parcel_delivery(self):
        # Base 15.0 + weight (2 * 2.5 = 5.0) + dist (10 * 0.5 = 5.0) + express 45.0 = 70.0 -> +15% = 80.50
        self.assertEqual(messy_code.calculate_shipping_total(2.0, 10.0, True), 80.5)

    def test_zero_weight_and_distance_standard(self):
        # Base 15.0 -> +15% VAT = 17.25
        self.assertEqual(messy_code.calculate_shipping_total(0.0, 0.0, False), 17.25)

    def test_zero_weight_and_distance_express(self):
        # Base 15.0 + express 45.0 = 60.0 -> +15% VAT = 69.0
        self.assertEqual(messy_code.calculate_shipping_total(0.0, 0.0, True), 69.0)

    def test_heavy_long_distance_standard(self):
        # 15.0 + (12.5 * 2.5 = 31.25) + (120 * 0.5 = 60.0) = 106.25 -> * 1.15 = 122.1875 -> 122.19
        self.assertEqual(messy_code.calculate_shipping_total(12.5, 120.0, False), 122.19)

    def test_fractional_inputs_rounding_express(self):
        # 15.0 + (0.75 * 2.5 = 1.875) + (3.3 * 0.5 = 1.65) + 45.0 = 63.525 -> * 1.15 = 73.05375 -> 73.05
        self.assertEqual(messy_code.calculate_shipping_total(0.75, 3.3, True), 73.05)


class TestRefactorGoals(unittest.TestCase):
    """Refactoring checklist: these start RED and turn GREEN after you clean up messy_code.py."""

    def test_meaningful_parameter_and_variable_names(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "calculate_shipping_total")
        self.assertIsNotNone(func, "Function 'calculate_shipping_total' must exist.")

        names = [arg.arg for arg in func.args.args]
        for node in ast.walk(func):
            if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
                names.append(node.id)

        cryptic_pattern = re.compile(r"^[a-z]\d*$")
        cryptic_names = sorted({name for name in names if name != "_" and cryptic_pattern.match(name)})
        self.assertEqual(
            cryptic_names,
            [],
            f"Found cryptic variable/parameter names: {cryptic_names}. "
            "Rename them to descriptive names like 'weight_kg', 'distance_km', 'is_express', 'subtotal', etc.",
        )

    def test_named_uppercase_constants_and_no_magic_numbers(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "calculate_shipping_total")
        self.assertIsNotNone(func, "Function 'calculate_shipping_total' must exist.")

        constant_pattern = re.compile(r"^[A-Z][A-Z0-9_]+$")
        defined_constants = []
        for stmt in tree.body:
            if isinstance(stmt, ast.Assign):
                if isinstance(stmt.value, ast.Constant) and isinstance(stmt.value.value, (int, float)):
                    for target in stmt.targets:
                        if isinstance(target, ast.Name) and constant_pattern.match(target.id):
                            defined_constants.append(target.id)
            elif isinstance(stmt, ast.AnnAssign):
                if (
                    isinstance(stmt.target, ast.Name)
                    and constant_pattern.match(stmt.target.id)
                    and isinstance(stmt.value, ast.Constant)
                    and isinstance(stmt.value.value, (int, float))
                ):
                    defined_constants.append(stmt.target.id)

        self.assertGreaterEqual(
            len(defined_constants),
            4,
            f"Expected at least 4 UPPER_CASE numeric constants at module level, found {len(defined_constants)}: "
            f"{defined_constants}. Extract constants like BASE_HANDLING_FEE, WEIGHT_RATE_PER_KG, EXPRESS_SURCHARGE, VAT_RATE.",
        )

        forbidden_magic = {15.0, 2.5, 0.5, 45.0, 0.15}
        inline_magic = []
        for node in ast.walk(func):
            if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
                if float(node.value) in forbidden_magic:
                    inline_magic.append(node.value)

        self.assertEqual(
            inline_magic,
            [],
            f"Found raw magic numbers still inside calculate_shipping_total: {inline_magic}. "
            "Replace them with your named UPPER_CASE module constants.",
        )

    def test_function_has_docstring(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "calculate_shipping_total")
        self.assertIsNotNone(func, "Function 'calculate_shipping_total' must exist.")

        docstring = ast.get_docstring(func)
        self.assertIsNotNone(
            docstring,
            "Add a docstring to calculate_shipping_total explaining what it calculates and its arguments.",
        )
        self.assertGreaterEqual(
            len(docstring.strip()),
            20,
            "Make the docstring descriptive (at least 20 characters explaining the function's purpose).",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
