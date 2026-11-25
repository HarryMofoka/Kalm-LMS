"""Tests for Refactoring Mission 12: O(n^2) nested-list scans -> O(n) sets/dicts."""

import ast
import inspect
import sys
import time
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_12_quadratic_lookup_rescue import (
    messy_code,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Proves before_common_users and after_common_users behave identically."""

    def test_common_users_overlap_duplicates_and_empty(self):
        cases = [
            (["alice", "bob", "cara", "alice"], ["cara", "dave", "alice"]),
            (["a", "b"], ["c", "d"]),
            ([], ["a", "b"]),
            (["x", "x"], ["x", "x"]),
        ]
        for group_a, group_b in cases:
            self.assertEqual(
                worked_example.before_common_users(group_a, group_b),
                worked_example.after_common_users(group_a, group_b),
            )


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net for audit_access_logs (must stay GREEN!)."""

    def test_mixed_authorized_unauthorized_and_duplicates(self):
        allowed = ["alice", "bob", "cara", "dan"]
        seen = ["alice", "eve", "bob", "alice", "eve", "mallory"]
        result = messy_code.audit_access_logs(allowed, seen)
        self.assertEqual(
            result,
            {
                "unauthorized": ["eve", "mallory"],
                "duplicates": ["alice", "eve"],
                "active_allowed": ["alice", "bob"],
            },
        )

    def test_all_authorized_unique_and_duplicate_allowed_input(self):
        allowed = ["zoe", "amy", "zoe"]
        seen = ["amy", "zoe"]
        result = messy_code.audit_access_logs(allowed, seen)
        self.assertEqual(
            result,
            {
                "unauthorized": [],
                "duplicates": [],
                "active_allowed": ["amy", "zoe"],
            },
        )

    def test_empty_inputs(self):
        self.assertEqual(
            messy_code.audit_access_logs(["alice"], []),
            {"unauthorized": [], "duplicates": [], "active_allowed": []},
        )
        self.assertEqual(
            messy_code.audit_access_logs([], ["eve", "eve"]),
            {"unauthorized": ["eve"], "duplicates": ["eve"], "active_allowed": []},
        )
        self.assertEqual(
            messy_code.audit_access_logs([], []),
            {"unauthorized": [], "duplicates": [], "active_allowed": []},
        )


class TestRefactorGoals(unittest.TestCase):
    """Goals: eliminate nested/quadratic scans, use sets/dicts, run fast."""

    def test_no_nested_loops_or_count_inside_loop(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)

        nested_loops = []
        count_in_loop = []

        def visit(node, loop_depth=0):
            is_loop = isinstance(node, (ast.For, ast.While))
            if is_loop and loop_depth >= 1:
                nested_loops.append(node.lineno)
            if (
                loop_depth >= 1
                and isinstance(node, ast.Call)
                and isinstance(node.func, ast.Attribute)
                and node.func.attr == "count"
            ):
                count_in_loop.append(node.lineno)
            next_depth = loop_depth + 1 if is_loop else loop_depth
            for child in ast.iter_child_nodes(node):
                visit(child, next_depth)

        visit(tree)
        self.assertEqual(
            nested_loops,
            [],
            f"Remove nested loops on line(s) {nested_loops}; use O(1) set/dict operations.",
        )
        self.assertEqual(
            count_in_loop,
            [],
            f"Remove .count() inside loop on line(s) {count_in_loop}; count in one O(n) pass.",
        )

    def test_uses_set_or_counter_dict_structures(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)

        uses_set_or_dict_index = False
        for node in ast.walk(tree):
            if isinstance(node, (ast.Set, ast.SetComp, ast.DictComp)):
                uses_set_or_dict_index = True
                break
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                if node.func.id in {"set", "frozenset", "Counter", "defaultdict"}:
                    uses_set_or_dict_index = True
                    break
            if isinstance(node, ast.Subscript) and isinstance(node.ctx, ast.Store):
                uses_set_or_dict_index = True
                break

        self.assertTrue(
            uses_set_or_dict_index,
            "Use sets and/or a counting dictionary (or Counter) for O(n) log auditing.",
        )

    def test_fast_linear_performance(self):
        n = 2500
        allowed = [f"user_{i}" for i in range(n)]
        seen = [f"user_{i}" for i in range(n // 2, n + n // 2)] + [
            f"user_{i}" for i in range(n // 2, n // 2 + 150)
        ]

        start = time.perf_counter()
        result = messy_code.audit_access_logs(allowed, seen)
        elapsed = time.perf_counter() - start

        self.assertEqual(len(result["unauthorized"]), n // 2)
        self.assertEqual(len(result["duplicates"]), 150)
        self.assertEqual(len(result["active_allowed"]), n // 2)
        self.assertLess(
            elapsed,
            0.05,
            f"audit_access_logs took {elapsed:.3f}s on {len(seen)} logs (limit: 0.05s). "
            "Replace O(n^2) list scans with O(n) sets and dicts!",
        )


if __name__ == "__main__":
    unittest.main()
