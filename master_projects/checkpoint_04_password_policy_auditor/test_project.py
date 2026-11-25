"""Tests for Checkpoint 04: Production Password Policy Auditor."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_04_password_policy_auditor import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the reference username compliance auditor works out of the box."""

    def test_valid_username_passes_with_full_score(self) -> None:
        report = worked_example.audit_username("dev_jane99")
        self.assertEqual(report, {"valid": True, "score": 100, "errors": []})

    def test_multiple_simultaneous_violations(self) -> None:
        report = worked_example.audit_username("1a__!")
        self.assertIs(report["valid"], False)
        self.assertEqual(report["score"], 25)
        self.assertEqual(
            set(report["errors"]),
            {"must_start_with_letter", "invalid_characters", "consecutive_underscores"},
        )

    def test_reserved_handle_case_insensitive(self) -> None:
        report = worked_example.audit_username("Admin")
        self.assertIs(report["valid"], False)
        self.assertIn("reserved_handle", report["errors"])

    def test_length_boundaries_too_short_and_too_long(self) -> None:
        short = worked_example.audit_username("ab")
        self.assertIn("too_short", short["errors"])
        long_handle = worked_example.audit_username("a" * 21)
        self.assertIn("too_long", long_handle["errors"])

    def test_non_string_raises_type_error(self) -> None:
        with self.assertRaises(TypeError):
            worked_example.audit_username(12345)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            worked_example.audit_username(None)  # type: ignore[arg-type]


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Production Password Policy Auditor."""

    def test_classify_strength_boundaries_and_errors(self) -> None:
        self.assertEqual(project.classify_strength(0), "weak")
        self.assertEqual(project.classify_strength(49), "weak")
        self.assertEqual(project.classify_strength(50), "medium")
        self.assertEqual(project.classify_strength(79), "medium")
        self.assertEqual(project.classify_strength(80), "strong")
        self.assertEqual(project.classify_strength(100), "strong")

        with self.assertRaises(TypeError):
            project.classify_strength("80")  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            project.classify_strength(True)  # bool must not be accepted as int score
        with self.assertRaises(ValueError):
            project.classify_strength(-1)
        with self.assertRaises(ValueError):
            project.classify_strength(101)

    def test_strong_valid_password(self) -> None:
        report = project.audit_password("S3cur3!Vault99", username="thabo")
        self.assertIsInstance(report, dict)
        self.assertIs(report.get("valid"), True)
        self.assertEqual(report.get("strength"), "strong")
        self.assertEqual(report.get("errors"), [])

    def test_weak_password_collects_all_violations(self) -> None:
        report = project.audit_password("abc")
        self.assertIsInstance(report, dict)
        self.assertIs(report.get("valid"), False)
        self.assertEqual(report.get("strength"), "weak")
        errors = report.get("errors")
        self.assertIsInstance(errors, list)
        self.assertEqual(
            set(errors),
            {"too_short", "missing_uppercase", "missing_digit", "missing_symbol"},
        )

    def test_medium_password_missing_symbol(self) -> None:
        report = project.audit_password("Abcdef12")
        self.assertIsInstance(report, dict)
        self.assertIs(report.get("valid"), False)
        self.assertEqual(report.get("strength"), "medium")
        self.assertEqual(report.get("errors"), ["missing_symbol"])

    def test_whitespace_is_flagged_and_not_counted_as_symbol(self) -> None:
        report = project.audit_password("Abcdef 1")
        self.assertIsInstance(report, dict)
        self.assertIs(report.get("valid"), False)
        errors = report.get("errors")
        self.assertIsInstance(errors, list)
        self.assertIn("contains_whitespace", errors)
        self.assertIn("missing_symbol", errors)

    def test_username_leakage_checked_case_insensitively(self) -> None:
        leaked = project.audit_password("MyALICE99!", username="alice")
        self.assertIsInstance(leaked, dict)
        self.assertIs(leaked.get("valid"), False)
        self.assertEqual(leaked.get("strength"), "medium")
        self.assertEqual(leaked.get("errors"), ["contains_username"])

        empty_user = project.audit_password("MyALICE99!", username="")
        self.assertIsInstance(empty_user, dict)
        self.assertIs(empty_user.get("valid"), True)
        self.assertEqual(empty_user.get("errors"), [])

    def test_audit_password_raises_type_error_on_non_str(self) -> None:
        with self.assertRaises(TypeError):
            project.audit_password(12345678)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            project.audit_password(None)  # type: ignore[arg-type]
        with self.assertRaises(TypeError):
            project.audit_password("Valid1!Pass", username=42)  # type: ignore[arg-type]


if __name__ == "__main__":
    unittest.main()
