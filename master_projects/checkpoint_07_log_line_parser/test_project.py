"""Automated tests for Checkpoint 07: Web Access Log Parser & PII Sanitizer."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_07_log_line_parser import (  # noqa: E402
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Verify the App Audit Event Parser & Secret Redactor reference works."""

    def test_parse_audit_event_valid(self) -> None:
        line = "2026-11-25 09:15:02 | warn | auth-service | Retry exceeded"
        parsed = worked_example.parse_audit_event(line)
        self.assertEqual(
            parsed,
            {
                "timestamp": "2026-11-25 09:15:02",
                "severity": "WARN",
                "service": "auth-service",
                "message": "Retry exceeded",
            },
        )

    def test_parse_audit_event_invalid(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.parse_audit_event("only | two")
        with self.assertRaises(ValueError):
            worked_example.parse_audit_event("2026-11-25 | DEBUG | api | hi")

    def test_redact_secrets_preserves_suffix_and_punctuation(self) -> None:
        msg = "Failed api_key=sk_live_99812abx44, secret=1234 tenant=acme"
        self.assertEqual(
            worked_example.redact_secrets(msg),
            "Failed api_key=***bx44, secret=**** tenant=acme",
        )

    def test_sanitize_audit_event_end_to_end(self) -> None:
        raw = "2026-11-25 09:15:02 | ERROR | billing | Bad token=tok_live_9988"
        self.assertEqual(
            worked_example.sanitize_audit_event(raw),
            "2026-11-25 09:15:02 | ERROR | billing | Bad token=***9988",
        )

    def test_summarize_audit_events_counts(self) -> None:
        lines = [
            "2026-11-25 09:00:00 | INFO | auth | ok",
            "2026-11-25 09:01:00 | ERROR | billing | fail",
            "   ",
            "broken line",
            "2026-11-25 09:02:00 | WARN | auth | slow",
        ]
        summary = worked_example.summarize_audit_events(lines)
        self.assertEqual(
            summary,
            {
                "total_events": 3,
                "by_severity": {"INFO": 1, "WARN": 1, "ERROR": 1},
                "services": ["auth", "billing"],
                "malformed_count": 1,
            },
        )


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Web Access Log Parser & PII Sanitizer."""

    def test_parse_log_line_valid_fields(self) -> None:
        line = (
            "2026-11-25 14:22:01 | get | /api/users | 200 | 42ms | "
            "user=alice@mail.com"
        )
        parsed = project.parse_log_line(line)
        self.assertEqual(
            parsed,
            {
                "timestamp": "2026-11-25 14:22:01",
                "method": "GET",
                "endpoint": "/api/users",
                "status_code": 200,
                "latency_ms": 42,
                "metadata": "user=alice@mail.com",
            },
        )

    def test_parse_log_line_rejects_malformed_inputs(self) -> None:
        bad_lines = [
            "2026-11-25 14:22:01 | GET | /api/users | 200",  # too few fields
            "2026-11-25 14:22:01 | GET | api/users | 200 | 42ms | ok",  # no leading /
            "2026-11-25 14:22:01 | GET | /api/users | 999 | 42ms | ok",  # bad HTTP status
            "2026-11-25 14:22:01 | GET | /api/users | 200 | 42s | ok",  # missing ms
            "2026-11-25 14:22:01 | GET | /api/users | 200 | -5ms | ok",  # negative latency
        ]
        for bad in bad_lines:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    project.parse_log_line(bad)

    def test_mask_email_standard_short_and_invalid(self) -> None:
        self.assertEqual(project.mask_email("alice@mail.com"), "a***@mail.com")
        self.assertEqual(project.mask_email(" z@shop.co.za "), "z***@shop.co.za")
        for invalid in ["no-at-sign.com", "@mail.com", "alice@", "alice@localhost", "a@b@c.com"]:
            with self.subTest(invalid=invalid):
                with self.assertRaises(ValueError):
                    project.mask_email(invalid)

    def test_sanitize_log_line_masks_emails_and_tokens(self) -> None:
        raw = (
            "2026-11-25 14:22:01 | POST | /api/login | 401 | 85ms | "
            "user=alice@mail.com, token=tok_live_secret99 api_key=sk_12345"
        )
        expected = (
            "2026-11-25 14:22:01 | POST | /api/login | 401 | 85ms | "
            "user=a***@mail.com, token=[REDACTED] api_key=[REDACTED]"
        )
        self.assertEqual(project.sanitize_log_line(raw), expected)

        standalone = "Alert sent to bob@company.org; password=hunter2"
        self.assertEqual(
            project.sanitize_log_line(standalone),
            "Alert sent to b***@company.org; password=[REDACTED]",
        )

    def test_summarize_logs_metrics_and_slowest_endpoint(self) -> None:
        logs = [
            "2026-11-25 14:22:01 | GET | /api/users | 200 | 40ms | user=alice@mail.com",
            "2026-11-25 14:22:02 | POST | /api/orders | 201 | 125ms | user=bob@mail.com",
            "2026-11-25 14:22:03 | GET | /api/reports | 500 | 310ms | timeout",
            "2026-11-25 14:22:04 | DELETE | /api/users | 403 | 25ms | forbidden",
        ]
        summary = project.summarize_logs(logs)
        self.assertEqual(
            summary,
            {
                "total_requests": 4,
                "error_count": 2,
                "avg_latency_ms": 125.0,
                "max_latency_ms": 310,
                "slowest_endpoint": "/api/reports",
                "malformed_count": 0,
            },
        )

    def test_summarize_logs_empty_and_malformed_resilience(self) -> None:
        empty_summary = project.summarize_logs(["", "   "])
        self.assertEqual(
            empty_summary,
            {
                "total_requests": 0,
                "error_count": 0,
                "avg_latency_ms": 0.0,
                "max_latency_ms": 0,
                "slowest_endpoint": None,
                "malformed_count": 0,
            },
        )

        mixed = [
            "corrupted log entry",
            "2026-11-25 14:22:01 | GET | /api/ping | 200 | 15ms | ok",
            "2026-11-25 14:22:02 | GET | /api/health | 200 | 15ms | ok",
            "bad | line | count",
        ]
        mixed_summary = project.summarize_logs(mixed)
        self.assertEqual(
            mixed_summary,
            {
                "total_requests": 2,
                "error_count": 0,
                "avg_latency_ms": 15.0,
                "max_latency_ms": 15,
                "slowest_endpoint": "/api/ping",
                "malformed_count": 2,
            },
        )


if __name__ == "__main__":
    unittest.main()
