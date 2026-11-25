"""Tests for Refactoring Mission 13: Decouple business logic from print()."""

import ast
import inspect
import io
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_13_print_coupled_logic import (
    messy_code,
    worked_example,
)


def _capture_stdout(fn, *args, **kwargs):
    buf = io.StringIO()
    with redirect_stdout(buf):
        result = fn(*args, **kwargs)
    return result, buf.getvalue()


class TestWorkedExample(unittest.TestCase):
    """Proves the worked example Before & After produce identical output."""

    def test_before_and_after_match_on_sample_sales(self):
        sales = [("Tea", 3.5), ("Burger", 12.0), ("Pie", 5.25)]
        _, before_out = _capture_stdout(worked_example.before_print_summary, sales)
        _, after_out = _capture_stdout(worked_example.after_print_summary, sales)
        self.assertEqual(before_out, after_out)

    def test_before_and_after_match_on_empty_sales(self):
        _, before_out = _capture_stdout(worked_example.before_print_summary, [])
        _, after_out = _capture_stdout(worked_example.after_print_summary, [])
        self.assertEqual(before_out, after_out)

    def test_after_format_summary_is_pure_and_silent(self):
        lines, out = _capture_stdout(
            worked_example.after_format_summary, [("Juice", 4.0)]
        )
        self.assertEqual(out, "")
        self.assertIsInstance(lines, list)
        self.assertEqual(lines[0], "=== DAILY SALES ===")
        self.assertIn("Total Revenue: $4.00", lines)


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net for print_grade_report (must stay GREEN!)."""

    def test_mixed_students_report(self):
        students = [("Ada", 92), ("Ben", 45), ("Cleo", 74), ("Dan", 50)]
        ret, out = _capture_stdout(messy_code.print_grade_report, students)
        self.assertIsNone(ret)
        expected = "\n".join(
            [
                "=== GRADE REPORT ===",
                "Ada: 92 (PASS)",
                "Ben: 45 (FAIL)",
                "Cleo: 74 (PASS)",
                "Dan: 50 (PASS)",
                "--------------------",
                "Total Students: 4",
                "Passed: 3 | Failed: 1",
                "Average Score: 65.25",
                "Highest: Ada (92)",
            ]
        ) + "\n"
        self.assertEqual(out, expected)

    def test_empty_students_report(self):
        ret, out = _capture_stdout(messy_code.print_grade_report, [])
        self.assertIsNone(ret)
        self.assertEqual(out, "=== GRADE REPORT ===\nNo students to report.\n")

    def test_all_fail_and_highest_tie_keeps_first(self):
        students = [("Zoe", 49), ("Max", 49), ("Leo", 20)]
        _, out = _capture_stdout(messy_code.print_grade_report, students)
        expected = "\n".join(
            [
                "=== GRADE REPORT ===",
                "Zoe: 49 (FAIL)",
                "Max: 49 (FAIL)",
                "Leo: 20 (FAIL)",
                "--------------------",
                "Total Students: 3",
                "Passed: 0 | Failed: 3",
                "Average Score: 39.33",
                "Highest: Zoe (49)",
            ]
        ) + "\n"
        self.assertEqual(out, expected)


class TestRefactorGoals(unittest.TestCase):
    """Refactoring goals: pure stats & formatting helpers + thin print wrapper."""

    def test_compute_grade_stats_is_pure_and_accurate(self):
        self.assertTrue(
            hasattr(messy_code, "compute_grade_stats"),
            "Extract a pure function named 'compute_grade_stats(students)' in messy_code.py.",
        )
        students = [("Ada", 92), ("Ben", 45), ("Cleo", 74), ("Dan", 50)]
        stats, out = _capture_stdout(messy_code.compute_grade_stats, students)
        self.assertEqual(out, "", "compute_grade_stats must NOT print to stdout.")
        self.assertIsInstance(stats, dict)
        self.assertEqual(stats["count"], 4)
        self.assertEqual(stats["passed"], 3)
        self.assertEqual(stats["failed"], 1)
        self.assertAlmostEqual(stats["average"], 65.25, places=2)
        self.assertEqual(stats["highest_name"], "Ada")
        self.assertEqual(stats["highest_score"], 92)

        empty_stats, empty_out = _capture_stdout(messy_code.compute_grade_stats, [])
        self.assertEqual(empty_out, "")
        self.assertEqual(
            empty_stats,
            {
                "count": 0,
                "passed": 0,
                "failed": 0,
                "average": 0.0,
                "highest_name": None,
                "highest_score": None,
            },
        )

    def test_format_grade_report_is_pure_and_returns_lines(self):
        self.assertTrue(
            hasattr(messy_code, "format_grade_report"),
            "Extract a pure function named 'format_grade_report(students)' in messy_code.py.",
        )
        students = [("Ada", 92), ("Ben", 45)]
        lines, out = _capture_stdout(messy_code.format_grade_report, students)
        self.assertEqual(out, "", "format_grade_report must NOT print to stdout.")
        self.assertIsInstance(lines, list)
        self.assertTrue(all(isinstance(line, str) for line in lines))
        self.assertEqual(
            lines,
            [
                "=== GRADE REPORT ===",
                "Ada: 92 (PASS)",
                "Ben: 45 (FAIL)",
                "--------------------",
                "Total Students: 2",
                "Passed: 1 | Failed: 1",
                "Average Score: 68.50",
                "Highest: Ada (92)",
            ],
        )

        empty_lines, empty_out = _capture_stdout(messy_code.format_grade_report, [])
        self.assertEqual(empty_out, "")
        self.assertEqual(empty_lines, ["=== GRADE REPORT ===", "No students to report."])

    def test_print_grade_report_delegates_and_helpers_have_no_print(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)
        funcs = {
            node.name: node
            for node in tree.body
            if isinstance(node, ast.FunctionDef)
        }
        self.assertIn("compute_grade_stats", funcs)
        self.assertIn("format_grade_report", funcs)
        self.assertIn("print_grade_report", funcs)

        def called_names(func_node):
            names = []
            for node in ast.walk(func_node):
                if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
                    names.append(node.func.id)
            return names

        self.assertNotIn(
            "print",
            called_names(funcs["compute_grade_stats"]),
            "compute_grade_stats must not contain print() calls.",
        )
        self.assertNotIn(
            "print",
            called_names(funcs["format_grade_report"]),
            "format_grade_report must not contain print() calls.",
        )

        wrapper_calls = called_names(funcs["print_grade_report"])
        self.assertIn(
            "format_grade_report",
            wrapper_calls,
            "print_grade_report should delegate formatting to format_grade_report.",
        )
        self.assertLessEqual(
            wrapper_calls.count("print"),
            1,
            "print_grade_report should be a thin wrapper with at most 1 print() call.",
        )


if __name__ == "__main__":
    unittest.main()
