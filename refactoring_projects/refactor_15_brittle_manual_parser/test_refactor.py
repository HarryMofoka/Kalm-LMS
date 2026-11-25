"""Tests for Refactoring Mission 15: Ad-hoc counters -> stack-based validator."""

import ast
import inspect
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_15_brittle_manual_parser import (
    messy_code,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Proves before_check_parens and after_check_parens behave identically."""

    def test_before_and_after_agree_on_valid_and_invalid_parens(self):
        cases = [
            ("", True),
            ("()", True),
            ("((a + b) * (c - d))", True),
            ("no parens here", True),
            ("(", False),
            (")", False),
            ("((a + b)", False),
            ("())", False),
            (")(", False),
        ]
        for expr, expected in cases:
            self.assertEqual(worked_example.before_check_parens(expr), expected)
            self.assertEqual(worked_example.after_check_parens(expr), expected)


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net for validate_formula_brackets (must stay GREEN!)."""

    def test_valid_nested_and_sibling_brackets(self):
        self.assertTrue(messy_code.validate_formula_brackets("({[]})"))
        self.assertTrue(messy_code.validate_formula_brackets("(a + [b * {c - d}])"))
        self.assertTrue(messy_code.validate_formula_brackets("()[]{}"))
        self.assertTrue(messy_code.validate_formula_brackets(""))
        self.assertTrue(messy_code.validate_formula_brackets("x + y = 42"))

    def test_unclosed_and_extra_closing_brackets(self):
        self.assertFalse(messy_code.validate_formula_brackets("(([]"))
        self.assertFalse(messy_code.validate_formula_brackets("())"))
        self.assertFalse(messy_code.validate_formula_brackets("]["))
        self.assertFalse(messy_code.validate_formula_brackets("{{(a + b)}"))


class TestRefactorGoals(unittest.TestCase):
    """Goals: catch interleaved nesting + use a bracket dict and stack."""

    def test_rejects_interleaved_invalid_brackets(self):
        interleaved_cases = [
            "([)]",
            "{[}]",
            "[({)}]",
            "(a + [b * c) + d]",
            "{a + (b * [c} + d])",
        ]
        for expr in interleaved_cases:
            self.assertFalse(
                messy_code.validate_formula_brackets(expr),
                f"Interleaved brackets {expr!r} must return False!",
            )
        # Valid deeply nested case must still pass
        self.assertTrue(
            messy_code.validate_formula_brackets("[({a + b}) * {c - (d + [e])}]")
        )

    def test_uses_bracket_mapping_dictionary(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)
        bracket_chars = {"(", ")", "[", "]", "{", "}"}

        found_bracket_dict = False
        for node in ast.walk(tree):
            if isinstance(node, ast.Dict) and len(node.keys) >= 3:
                pairs = []
                for k, v in zip(node.keys, node.values):
                    if (
                        isinstance(k, ast.Constant)
                        and isinstance(v, ast.Constant)
                        and isinstance(k.value, str)
                        and isinstance(v.value, str)
                    ):
                        pairs.append((k.value, v.value))
                if len(pairs) >= 3 and all(
                    k in bracket_chars and v in bracket_chars for k, v in pairs
                ):
                    found_bracket_dict = True
                    break

        self.assertTrue(
            found_bracket_dict,
            "Define a dictionary mapping the 3 bracket pairs (e.g., {')': '(', ']': '[', '}': '{'}).",
        )

    def test_uses_stack_instead_of_manual_counters(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)

        attr_calls = set()
        aug_assigns = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute):
                attr_calls.add(node.func.attr)
            if isinstance(node, ast.AugAssign) and isinstance(
                node.op, (ast.Add, ast.Sub)
            ):
                aug_assigns.append(node)

        self.assertIn(
            "append",
            attr_calls,
            "Use a stack with .append(...) to push opening brackets.",
        )
        self.assertIn(
            "pop",
            attr_calls,
            "Use a stack with .pop() to match closing brackets.",
        )
        self.assertEqual(
            len(aug_assigns),
            0,
            "Remove manual += / -= counter updates in favor of a stack.",
        )


if __name__ == "__main__":
    unittest.main()
