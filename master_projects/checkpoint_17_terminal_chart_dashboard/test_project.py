"""Unit tests for Checkpoint 17: Terminal Chart Dashboard."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_17_terminal_chart_dashboard import (
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Tests verifying the CLI Build Status Box & Progress Bar worked example."""

    def test_render_meter_standard_and_clamped(self) -> None:
        self.assertEqual(
            worked_example.render_meter(8, 16, width=10),
            "[#####.....] 50%",
        )
        self.assertEqual(
            worked_example.render_meter(25, 10, width=8),
            "[########] 100%",
        )
        self.assertEqual(
            worked_example.render_meter(-5, 10, width=8),
            "[........] 0%",
        )

    def test_render_meter_invalid_args(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.render_meter(5, 0)
        with self.assertRaises(ValueError):
            worked_example.render_meter(5, 10, width=0)

    def test_render_kv_panel_alignment_and_borders(self) -> None:
        lines = worked_example.render_kv_panel(
            "STATUS", [("Env", "prod"), ("Region", "eu-west-1")]
        )
        self.assertEqual(
            lines,
            [
                "+--------------------+",
                "| STATUS             |",
                "+--------------------+",
                "| Env    : prod      |",
                "| Region : eu-west-1 |",
                "+--------------------+",
            ],
        )

    def test_render_build_summary_zero_trailing_spaces(self) -> None:
        lines = worked_example.render_build_summary(
            "auth-svc", 9, 10, [("Branch", "release")]
        )
        self.assertTrue(all(line == line.rstrip() for line in lines))
        self.assertIn("Progress: [##################..] 90%", lines)


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Terminal Metrics Dashboard in project.py."""

    def test_render_progress_bar_standard_and_clamping(self) -> None:
        self.assertEqual(
            project.render_progress_bar(50, 100, width=20),
            "[##########----------] 50%",
        )
        self.assertEqual(
            project.render_progress_bar(0, 100, width=10),
            "[----------] 0%",
        )
        self.assertEqual(
            project.render_progress_bar(150, 100, width=10),
            "[##########] 100%",
        )
        self.assertEqual(
            project.render_progress_bar(-10, 100, width=10),
            "[----------] 0%",
        )

    def test_render_progress_bar_validation(self) -> None:
        with self.assertRaises(ValueError):
            project.render_progress_bar(10, 0)
        with self.assertRaises(ValueError):
            project.render_progress_bar(10, 20, width=0)

    def test_render_bar_chart_proportional_and_aligned(self) -> None:
        data = [("CPU", 100), ("Memory", 50), ("Idle", 0)]
        chart = project.render_bar_chart(data, max_bar_width=10)
        self.assertEqual(
            chart,
            [
                "CPU    | ########## 100",
                "Memory | ##### 50",
                "Idle   | 0",
            ],
        )
        self.assertTrue(all(line == line.rstrip() for line in chart))

    def test_render_bar_chart_edge_cases(self) -> None:
        self.assertEqual(project.render_bar_chart([]), [])
        self.assertEqual(
            project.render_bar_chart([("A", 0), ("B", 0)], max_bar_width=10),
            ["A | 0", "B | 0"],
        )
        with self.assertRaises(ValueError):
            project.render_bar_chart([("A", -1)])
        with self.assertRaises(ValueError):
            project.render_bar_chart([("A", 5)], max_bar_width=0)

    def test_render_kpi_box_formatting(self) -> None:
        box = project.render_kpi_box(
            "API HEALTH", ["Uptime: 99.9%", "Errors: 0"]
        )
        self.assertEqual(
            box,
            [
                "+---------------+",
                "| API HEALTH    |",
                "+---------------+",
                "| Uptime: 99.9% |",
                "| Errors: 0     |",
                "+---------------+",
            ],
        )
        empty_box = project.render_kpi_box("EMPTY", [])
        self.assertEqual(
            empty_box,
            [
                "+-------+",
                "| EMPTY |",
                "+-------+",
            ],
        )

    def test_render_dashboard_combines_kpi_and_chart_cleanly(self) -> None:
        metrics = {"API": 80, "Worker": 40, "Cache": 20}
        lines = project.render_dashboard("CLUSTER LOAD", metrics)
        self.assertIsInstance(lines, list)
        self.assertTrue(all(line == line.rstrip() for line in lines))
        joined = "\n".join(lines)
        self.assertIn("CLUSTER LOAD", joined)
        self.assertIn("Metrics: 3", joined)
        self.assertIn("Total: 140", joined)
        self.assertIn("Peak: API (80)", joined)
        self.assertIn("", lines)
        self.assertIn("API    | #################### 80", lines)
        self.assertIn("Worker | ########## 40", lines)
        self.assertIn("Cache  | ##### 20", lines)

    def test_render_dashboard_empty_metrics(self) -> None:
        lines = project.render_dashboard("EMPTY CLUSTER", {})
        self.assertEqual(
            lines,
            [
                "+----------------------+",
                "| EMPTY CLUSTER        |",
                "+----------------------+",
                "| No metrics available |",
                "+----------------------+",
            ],
        )


if __name__ == "__main__":
    unittest.main()
