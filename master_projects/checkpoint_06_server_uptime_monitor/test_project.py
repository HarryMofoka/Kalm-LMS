"""Automated tests for Checkpoint 06: Server Heartbeat & SLA Uptime Analyzer."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_06_server_uptime_monitor import (  # noqa: E402
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Verify the IoT Weather Station Sensor Health Analyzer reference works."""

    def test_valid_and_invalid_readings(self) -> None:
        self.assertTrue(worked_example.is_valid_reading(23.5))
        self.assertTrue(worked_example.is_valid_reading(-50.0))
        self.assertTrue(worked_example.is_valid_reading(60.0))
        self.assertFalse(worked_example.is_valid_reading(None))
        self.assertFalse(worked_example.is_valid_reading(-50.1))
        self.assertFalse(worked_example.is_valid_reading(125.0))

    def test_calculate_health_pct_and_empty(self) -> None:
        self.assertEqual(worked_example.calculate_health_pct([]), 0.0)
        readings = [20.0, None, 21.5, 999.0, 22.0, 23.0]
        self.assertEqual(worked_example.calculate_health_pct(readings), 66.67)

    def test_longest_error_streak_patterns(self) -> None:
        self.assertEqual(worked_example.longest_error_streak([]), 0)
        self.assertEqual(worked_example.longest_error_streak([20.0, 21.0]), 0)
        readings = [None, 20.0, None, 999.0, None, 22.0, -99.0, None]
        self.assertEqual(worked_example.longest_error_streak(readings), 3)

    def test_find_error_bursts_threshold(self) -> None:
        readings = [None, 20.0, None, None, 21.0, 999.0, None, None]
        self.assertEqual(
            worked_example.find_error_bursts(readings, min_burst=2),
            [(2, 3), (5, 7)],
        )
        self.assertEqual(
            worked_example.find_error_bursts(readings, min_burst=3),
            [(5, 7)],
        )

    def test_sensor_health_summary_statuses(self) -> None:
        healthy = worked_example.sensor_health_summary([21.0] * 10)
        self.assertEqual(healthy["status"], "HEALTHY")
        self.assertFalse(healthy["alert_triggered"])

        critical = worked_example.sensor_health_summary(
            [21.0, None, None, None, 22.0]
        )
        self.assertEqual(critical["status"], "CRITICAL")
        self.assertTrue(critical["alert_triggered"])
        self.assertEqual(critical["longest_error_streak"], 3)

        empty = worked_example.sensor_health_summary([])
        self.assertEqual(empty["status"], "NO_DATA")
        self.assertTrue(empty["alert_triggered"])


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Server Heartbeat & SLA Uptime Analyzer."""

    def test_calculate_uptime_pct_standard_and_rounding(self) -> None:
        self.assertEqual(project.calculate_uptime_pct([True, True, False]), 66.67)
        self.assertEqual(project.calculate_uptime_pct([True, True, True]), 100.0)
        self.assertEqual(project.calculate_uptime_pct([False, False]), 0.0)
        self.assertEqual(project.calculate_uptime_pct([]), 0.0)

    def test_longest_outage_streak_various_patterns(self) -> None:
        self.assertEqual(project.longest_outage_streak([]), 0)
        self.assertEqual(project.longest_outage_streak([True, True, True]), 0)
        self.assertEqual(project.longest_outage_streak([False, False, False]), 3)
        stream = [False, True, False, False, False, True, False, False]
        self.assertEqual(project.longest_outage_streak(stream), 3)
        trailing = [True, False, True, False, False, False, False]
        self.assertEqual(project.longest_outage_streak(trailing), 4)

    def test_find_outage_windows_multiple_and_edges(self) -> None:
        self.assertEqual(project.find_outage_windows([]), [])
        self.assertEqual(project.find_outage_windows([True, True]), [])
        stream = [True, False, False, True, False]
        self.assertEqual(project.find_outage_windows(stream), [(1, 2), (4, 4)])
        edge_stream = [False, False, True, False, True, False, False, False]
        self.assertEqual(
            project.find_outage_windows(edge_stream),
            [(0, 1), (3, 3), (5, 7)],
        )

    def test_sla_report_healthy_server(self) -> None:
        heartbeats = [True] * 99 + [False]
        report = project.sla_report(heartbeats, target_sla=99.0)
        self.assertEqual(
            report,
            {
                "total_checks": 100,
                "up_checks": 99,
                "down_checks": 1,
                "uptime_pct": 99.0,
                "target_sla": 99.0,
                "sla_met": True,
                "longest_outage": 1,
                "outage_windows": [(99, 99)],
                "incident_count": 1,
                "status": "HEALTHY",
            },
        )

    def test_sla_report_degraded_and_critical_breaches(self) -> None:
        # Meets 99.0% SLA overall (99.4%), but has a sustained 3-check outage -> DEGRADED
        sustained = [True] * 200 + [False, False, False] + [True] * 297
        sustained_report = project.sla_report(sustained, target_sla=99.0)
        self.assertEqual(
            sustained_report,
            {
                "total_checks": 500,
                "up_checks": 497,
                "down_checks": 3,
                "uptime_pct": 99.4,
                "target_sla": 99.0,
                "sla_met": True,
                "longest_outage": 3,
                "outage_windows": [(200, 202)],
                "incident_count": 1,
                "status": "DEGRADED",
            },
        )

        # Minor breach (96.0% vs 99.0% target -> within 5%) -> DEGRADED
        minor_breach = [True] * 96 + [False, False] + [True] * 0 + [False, False]
        minor_report = project.sla_report(minor_breach, target_sla=99.0)
        self.assertIsInstance(minor_report, dict)
        self.assertFalse(minor_report["sla_met"])
        self.assertEqual(minor_report["status"], "DEGRADED")

        # Severe breach (90.0% vs 99.0% target) -> CRITICAL
        severe = [True] * 90 + [False] * 10
        severe_report = project.sla_report(severe, target_sla=99.0)
        self.assertIsInstance(severe_report, dict)
        self.assertFalse(severe_report["sla_met"])
        self.assertEqual(severe_report["status"], "CRITICAL")
        self.assertEqual(severe_report["incident_count"], 1)

    def test_sla_report_empty_heartbeats(self) -> None:
        report = project.sla_report([], target_sla=99.5)
        self.assertEqual(
            report,
            {
                "total_checks": 0,
                "up_checks": 0,
                "down_checks": 0,
                "uptime_pct": 0.0,
                "target_sla": 99.5,
                "sla_met": False,
                "longest_outage": 0,
                "outage_windows": [],
                "incident_count": 0,
                "status": "NO_DATA",
            },
        )


if __name__ == "__main__":
    unittest.main()
