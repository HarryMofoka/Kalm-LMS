"""Test suite for Refactoring Mission 16: Slow Naive Algorithms."""

import ast
import inspect
import sys
import unittest
from pathlib import Path
from time import perf_counter

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_16_slow_naive_algorithms import (  # noqa: E402
    messy_code,
    worked_example,
)


class _CountingSortedSequence:
    """Read-only sorted sequence spy that counts element accesses."""

    def __init__(self, items):
        self._items = list(items)
        self.accesses = 0

    def __len__(self):
        return len(self._items)

    def __bool__(self):
        return bool(self._items)

    def __getitem__(self, index):
        if isinstance(index, slice):
            sliced = self._items[index]
            self.accesses += len(sliced)
            return sliced
        self.accesses += 1
        return self._items[index]

    def __iter__(self):
        for item in self._items:
            self.accesses += 1
            yield item

    def __contains__(self, target):
        for item in self:
            if item == target:
                return True
        return False


class TestWorkedExample(unittest.TestCase):
    """Verifies the before/after worked example behaves identically."""

    def test_before_and_after_match_on_various_inputs(self):
        cases = [
            ([], 0),
            ([10], 0),
            ([7, 1, 5, 3, 6, 4], 5),
            ([7, 6, 4, 3, 1], 0),
            ([2, 4, 1, 9], 8),
            ([5, 5, 5, 5], 0),
        ]
        for prices, expected in cases:
            self.assertEqual(worked_example.before_max_profit(prices), expected)
            self.assertEqual(worked_example.after_max_profit(prices), expected)


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net — must stay 100% GREEN throughout refactoring."""

    def test_best_profit_window_small_cases(self):
        self.assertEqual(
            messy_code.best_profit_window([-2, 1, -3, 4, -1, 2, 1, -5, 4]),
            6,
        )
        self.assertEqual(messy_code.best_profit_window([5, 4, -1, 7, 8]), 23)
        self.assertEqual(messy_code.best_profit_window([-8, -3, -6, -2, -5]), -2)
        self.assertEqual(messy_code.best_profit_window([42]), 42)
        self.assertEqual(messy_code.best_profit_window([]), 0)

    def test_find_sorted_timestamp_small_cases(self):
        data = [100, 150, 200, 260, 310, 405, 500]
        self.assertEqual(messy_code.find_sorted_timestamp(data, 100), 0)
        self.assertEqual(messy_code.find_sorted_timestamp(data, 260), 3)
        self.assertEqual(messy_code.find_sorted_timestamp(data, 500), 6)
        self.assertEqual(messy_code.find_sorted_timestamp(data, 50), -1)
        self.assertEqual(messy_code.find_sorted_timestamp(data, 275), -1)
        self.assertEqual(messy_code.find_sorted_timestamp(data, 999), -1)
        self.assertEqual(messy_code.find_sorted_timestamp([], 100), -1)


class TestRefactorGoals(unittest.TestCase):
    """Refactoring goals — RED on baseline, GREEN once refactored cleanly."""

    def test_best_profit_window_fast_on_3000_items(self):
        # 3,000 items with a clear known best contiguous sum (1000 * 5 = 5000).
        changes = [-10] * 1000 + [5] * 1000 + [-10] * 1000
        t0 = perf_counter()
        result = messy_code.best_profit_window(changes)
        elapsed = perf_counter() - t0

        self.assertEqual(result, 5000)
        self.assertLess(
            elapsed,
            0.05,
            f"best_profit_window took {elapsed:.4f}s on 3,000 items; "
            "expected < 0.05s using O(n) Kadane's algorithm.",
        )

    def test_best_profit_window_has_no_nested_loops(self):
        source = inspect.getsource(messy_code.best_profit_window)
        tree = ast.parse(source)
        func_node = tree.body[0]

        for node in ast.walk(func_node):
            if isinstance(node, (ast.For, ast.While)):
                for child in ast.walk(node):
                    if child is not node and isinstance(child, (ast.For, ast.While)):
                        self.fail(
                            "best_profit_window still contains nested loops; "
                            "refactor to a single-pass O(n) Kadane loop."
                        )
                    if (
                        isinstance(child, ast.Call)
                        and isinstance(child.func, ast.Name)
                        and child.func.id == "sum"
                    ):
                        self.fail(
                            "best_profit_window calls sum() inside a loop; "
                            "track a running sum in O(n) instead."
                        )

    def test_find_sorted_timestamp_logarithmic_hit(self):
        spy = _CountingSortedSequence(range(0, 20_000, 2))  # 10,000 items
        idx = messy_code.find_sorted_timestamp(spy, 19_996)

        self.assertEqual(idx, 9_998)
        self.assertLessEqual(
            spy.accesses,
            30,
            f"find_sorted_timestamp accessed {spy.accesses} elements on 10,000 items; "
            "use O(log n) binary search instead of a linear scan.",
        )

    def test_find_sorted_timestamp_logarithmic_miss(self):
        spy = _CountingSortedSequence(range(0, 20_000, 2))  # 10,000 items
        idx = messy_code.find_sorted_timestamp(spy, 19_999)

        self.assertEqual(idx, -1)
        self.assertLessEqual(
            spy.accesses,
            30,
            f"find_sorted_timestamp accessed {spy.accesses} elements for a missing target; "
            "use O(log n) binary search instead of a linear scan.",
        )


if __name__ == "__main__":
    unittest.main()
