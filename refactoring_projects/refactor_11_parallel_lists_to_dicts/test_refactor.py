"""Tests for Refactoring Mission 11: Parallel lists -> clean dictionaries."""

import ast
import inspect
import sys
import time
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_11_parallel_lists_to_dicts import (
    messy_code,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Proves before_lookup_student and after_lookup_student match."""

    def test_lookup_existing_and_missing_students(self):
        records = [
            ("Amara", 88, "Falcon"),
            ("Bongani", 74, "Orion"),
            ("Chidi", 95, "Solar"),
        ]
        for query in ["Amara", "Bongani", "Chidi", "Nobody"]:
            self.assertEqual(
                worked_example.before_lookup_student(records, query),
                worked_example.after_lookup_student(records, query),
            )

    def test_lookup_on_empty_records(self):
        self.assertIsNone(worked_example.before_lookup_student([], "Amara"))
        self.assertIsNone(worked_example.after_lookup_student([], "Amara"))


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net for process_tuckshop_orders (must stay GREEN!)."""

    def test_mixed_fulfilled_and_rejected_orders(self):
        catalog = [
            ("Pie", 18.50, 5),
            ("Juice", 12.00, 10),
            ("Crisps", 8.25, 2),
        ]
        orders = [
            ("Pie", 2),
            ("Juice", 3),
            ("Samosa", 1),       # unknown item
            ("Crisps", 0),       # invalid quantity
            ("Crisps", -1),      # invalid quantity
            ("Pie", 4),          # only 3 left -> insufficient stock
            ("Pie", 3),          # exact remaining stock -> succeeds
        ]
        result = messy_code.process_tuckshop_orders(catalog, orders)
        self.assertEqual(result["total_revenue"], round(18.5 * 5 + 12.0 * 3, 2))
        self.assertEqual(result["fulfilled_count"], 3)
        self.assertEqual(
            result["rejected"],
            [
                ("Samosa", 1, "unknown_item"),
                ("Crisps", 0, "invalid_quantity"),
                ("Crisps", -1, "invalid_quantity"),
                ("Pie", 4, "insufficient_stock"),
            ],
        )
        self.assertEqual(
            result["remaining_stock"],
            {"Pie": 0, "Juice": 7, "Crisps": 2},
        )

    def test_empty_orders_and_empty_catalog(self):
        res_no_orders = messy_code.process_tuckshop_orders([("Water", 5.0, 4)], [])
        self.assertEqual(
            res_no_orders,
            {
                "total_revenue": 0.0,
                "fulfilled_count": 0,
                "rejected": [],
                "remaining_stock": {"Water": 4},
            },
        )
        res_no_catalog = messy_code.process_tuckshop_orders([], [("Water", 1)])
        self.assertEqual(
            res_no_catalog,
            {
                "total_revenue": 0.0,
                "fulfilled_count": 0,
                "rejected": [("Water", 1, "unknown_item")],
                "remaining_stock": {},
            },
        )


class TestRefactorGoals(unittest.TestCase):
    """Goals: dict-based catalog lookup, no range(len(...)) scanning, fast O(1)."""

    def test_no_range_len_index_scanning(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)

        range_len_calls = []
        for node in ast.walk(tree):
            if (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "range"
                and node.args
            ):
                first_arg = node.args[0]
                if (
                    isinstance(first_arg, ast.Call)
                    and isinstance(first_arg.func, ast.Name)
                    and first_arg.func.id == "len"
                ):
                    range_len_calls.append(node.lineno)

        self.assertEqual(
            range_len_calls,
            [],
            f"Remove parallel-list range(len(...)) scans on line(s) {range_len_calls}; "
            "use a dictionary keyed by item name instead.",
        )

    def test_uses_dictionary_lookup_instead_of_parallel_lists(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)

        empty_lists = [
            node
            for node in ast.walk(tree)
            if isinstance(node, ast.List) and len(node.elts) == 0
        ]
        self.assertLessEqual(
            len(empty_lists),
            1,
            f"Found {len(empty_lists)} empty list literals — eliminate parallel lists "
            "(names/prices/stocks) and store catalog items in a dictionary.",
        )

        has_dict_construction = any(
            isinstance(node, (ast.Dict, ast.DictComp))
            or (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Name)
                and node.func.id == "dict"
            )
            for node in ast.walk(tree)
        )
        has_dict_lookup = any(
            (
                isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "get"
            )
            or (
                isinstance(node, ast.Compare)
                and any(isinstance(op, (ast.In, ast.NotIn)) for op in node.ops)
            )
            for node in ast.walk(tree)
        )
        self.assertTrue(
            has_dict_construction and has_dict_lookup,
            "Build a dictionary for the catalog and look up ordered items with .get() or 'in'.",
        )

    def test_fast_execution_on_2000_items_and_2000_orders(self):
        catalog = [(f"item_{i}", 10.0 + (i % 20), 200) for i in range(2000)]
        orders = [
            (f"item_{1999 - (i % 50)}", 1) if i % 5 != 0 else (f"missing_{i}", 1)
            for i in range(2000)
        ]

        start = time.perf_counter()
        result = messy_code.process_tuckshop_orders(catalog, orders)
        elapsed = time.perf_counter() - start

        self.assertEqual(result["fulfilled_count"], 1600)
        self.assertEqual(len(result["rejected"]), 400)
        self.assertLess(
            elapsed,
            0.08,
            f"2,000 items x 2,000 orders took {elapsed:.3f}s (limit: 0.08s). "
            "Use a dictionary for O(1) item lookup!",
        )


if __name__ == "__main__":
    unittest.main()
