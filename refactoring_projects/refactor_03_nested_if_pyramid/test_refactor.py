"""Test suite for Refactor 03: Nested If Pyramid."""

import ast
import itertools
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_03_nested_if_pyramid import messy_code, worked_example


def _parse_messy_module():
    source = Path(messy_code.__file__).read_text(encoding="utf-8")
    return ast.parse(source)


def _get_function_node(tree, func_name):
    for node in tree.body:
        if isinstance(node, ast.FunctionDef) and node.name == func_name:
            return node
    return None


def _max_if_nesting_depth(node, current_depth=0):
    """Compute maximum nested `if` depth, keeping flat `elif` chains at the same depth."""
    best = current_depth
    if isinstance(node, ast.If):
        next_depth = current_depth + 1
        best = max(best, next_depth)
        for stmt in node.body:
            best = max(best, _max_if_nesting_depth(stmt, next_depth))
        if len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If):
            # Treat `elif` as the same nesting level as its parent `if`
            best = max(best, _max_if_nesting_depth(node.orelse[0], current_depth))
        else:
            for stmt in node.orelse:
                best = max(best, _max_if_nesting_depth(stmt, next_depth))
        return best

    for child in ast.iter_child_nodes(node):
        best = max(best, _max_if_nesting_depth(child, current_depth))
    return best


def _count_non_elif_else_blocks(func_node):
    count = 0
    for node in ast.walk(func_node):
        if isinstance(node, ast.If) and node.orelse:
            is_elif = len(node.orelse) == 1 and isinstance(node.orelse[0], ast.If)
            if not is_elif:
                count += 1
    return count


class TestWorkedExample(unittest.TestCase):
    """Verify before_can_borrow and after_can_borrow agree on every combination."""

    def test_before_and_after_match_all_paths(self):
        for has_card, is_suspended, late_fees, active_loans, book_available, is_ref in itertools.product(
            [False, True],
            [False, True],
            [0, 10],
            [0, 5],
            [False, True],
            [False, True],
        ):
            with self.subTest(
                has_card=has_card,
                is_suspended=is_suspended,
                late_fees=late_fees,
                active_loans=active_loans,
                book_available=book_available,
                is_ref=is_ref,
            ):
                self.assertEqual(
                    worked_example.before_can_borrow(
                        has_card, is_suspended, late_fees, active_loans, book_available, is_ref
                    ),
                    worked_example.after_can_borrow(
                        has_card, is_suspended, late_fees, active_loans, book_available, is_ref
                    ),
                )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Safety net: every branch and priority order of evaluate_delivery_discount must stay intact."""

    def test_empty_cart_has_highest_priority(self):
        for is_member, cart_total, item_count, has_coupon, is_weekend in itertools.product(
            [False, True], [0, 50, 500], [-1, 0], [False, True], [False, True]
        ):
            self.assertEqual(
                messy_code.evaluate_delivery_discount(
                    is_member, cart_total, item_count, has_coupon, is_weekend
                ),
                "No discount: cart is empty",
            )

    def test_minimum_cart_total_rule(self):
        for is_member, cart_total, item_count, has_coupon, is_weekend in itertools.product(
            [False, True], [0, 50, 99.99], [1, 5], [False, True], [False, True]
        ):
            self.assertEqual(
                messy_code.evaluate_delivery_discount(
                    is_member, cart_total, item_count, has_coupon, is_weekend
                ),
                "No discount: minimum order is R100",
            )

    def test_non_member_denied_even_with_big_cart_and_coupon(self):
        for cart_total, item_count, has_coupon, is_weekend in itertools.product(
            [100, 250], [1, 3, 10], [False, True], [False, True]
        ):
            self.assertEqual(
                messy_code.evaluate_delivery_discount(
                    False, cart_total, item_count, has_coupon, is_weekend
                ),
                "No discount: members only",
            )

    def test_small_member_order_discount(self):
        for cart_total, item_count, has_coupon, is_weekend in itertools.product(
            [100, 300], [1, 2], [False, True], [False, True]
        ):
            self.assertEqual(
                messy_code.evaluate_delivery_discount(
                    True, cart_total, item_count, has_coupon, is_weekend
                ),
                "5% discount: small member order",
            )

    def test_member_bulk_order_all_four_coupon_weekend_tiers(self):
        self.assertEqual(
            messy_code.evaluate_delivery_discount(True, 100, 3, True, True),
            "25% discount: weekend coupon VIP",
        )
        self.assertEqual(
            messy_code.evaluate_delivery_discount(True, 250, 6, True, False),
            "20% discount: weekday coupon member",
        )
        self.assertEqual(
            messy_code.evaluate_delivery_discount(True, 100.0, 3, False, True),
            "15% discount: weekend member",
        )
        self.assertEqual(
            messy_code.evaluate_delivery_discount(True, 150, 4, False, False),
            "10% discount: standard member",
        )


class TestRefactorGoals(unittest.TestCase):
    """Refactoring checklist: flatten the 6-level pyramid using clean guard clauses."""

    def test_max_if_nesting_depth_at_most_two(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "evaluate_delivery_discount")
        self.assertIsNotNone(func, "Function 'evaluate_delivery_discount' must exist.")

        depth = _max_if_nesting_depth(func)
        self.assertLessEqual(
            depth,
            2,
            f"Maximum `if` nesting depth in evaluate_delivery_discount is {depth} (must be <= 2). "
            "Flatten the pyramid by inverting checks into early-return guard clauses!",
        )

    def test_uses_early_return_guard_clauses(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "evaluate_delivery_discount")
        self.assertIsNotNone(func, "Function 'evaluate_delivery_discount' must exist.")

        return_count = sum(1 for node in ast.walk(func) if isinstance(node, ast.Return))
        self.assertGreaterEqual(
            return_count,
            4,
            f"Found only {return_count} `return` statement(s) in evaluate_delivery_discount. "
            "Use early `return` guard clauses (at least 4 returns) instead of assigning to a temporary `result` variable.",
        )

    def test_eliminates_else_pyramid(self):
        tree = _parse_messy_module()
        func = _get_function_node(tree, "evaluate_delivery_discount")
        self.assertIsNotNone(func, "Function 'evaluate_delivery_discount' must exist.")

        else_count = _count_non_elif_else_blocks(func)
        self.assertLessEqual(
            else_count,
            2,
            f"Found {else_count} `else:` blocks in evaluate_delivery_discount (must be <= 2). "
            "Once a guard clause returns early, you do not need an `else:` block for the rest of the function!",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
