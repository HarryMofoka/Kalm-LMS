"""Tests for Checkpoint 02: Transit Timetable Clock."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_02_transit_timetable_clock import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Verify the reference global conference clock engine works out of the box."""

    def test_hm_to_minutes_valid_and_invalid(self) -> None:
        self.assertEqual(worked_example.hm_to_minutes(0, 0), 0)
        self.assertEqual(worked_example.hm_to_minutes(23, 59), 1439)
        with self.assertRaises(ValueError):
            worked_example.hm_to_minutes(24, 0)
        with self.assertRaises(ValueError):
            worked_example.hm_to_minutes(12, 60)

    def test_minutes_to_clock_wrapping(self) -> None:
        self.assertEqual(worked_example.minutes_to_clock(65), "01:05")
        self.assertEqual(worked_example.minutes_to_clock(1440), "00:00")
        self.assertEqual(worked_example.minutes_to_clock(1530), "01:30")
        self.assertEqual(worked_example.minutes_to_clock(-30), "23:30")

    def test_convert_timezone_slot_same_next_and_prev_day(self) -> None:
        self.assertEqual(worked_example.convert_timezone_slot(14, 0, +120), ("16:00", 0))
        self.assertEqual(worked_example.convert_timezone_slot(22, 30, +180), ("01:30", 1))
        self.assertEqual(worked_example.convert_timezone_slot(2, 15, -300), ("21:15", -1))

    def test_format_countdown_with_and_without_days(self) -> None:
        self.assertEqual(worked_example.format_countdown(0), "00h 00m")
        self.assertEqual(worked_example.format_countdown(75), "01h 15m")
        self.assertEqual(worked_example.format_countdown(1505), "1d 01h 05m")

    def test_format_countdown_rejects_negative(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.format_countdown(-1)


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's City Bus & Train Wrap-Around Timetable Engine."""

    def test_to_minutes_valid_and_invalid(self) -> None:
        self.assertEqual(project.to_minutes(0, 0), 0)
        self.assertEqual(project.to_minutes(8, 30), 510)
        self.assertEqual(project.to_minutes(23, 59), 1439)
        with self.assertRaises(ValueError):
            project.to_minutes(-1, 10)
        with self.assertRaises(ValueError):
            project.to_minutes(24, 0)
        with self.assertRaises(ValueError):
            project.to_minutes(10, 60)

    def test_format_clock_24h_padding_and_modulo_wrap(self) -> None:
        self.assertEqual(project.format_clock_24h(5), "00:05")
        self.assertEqual(project.format_clock_24h(545), "09:05")
        self.assertEqual(project.format_clock_24h(1440), "00:00")
        self.assertEqual(project.format_clock_24h(1505), "01:05")
        self.assertEqual(project.format_clock_24h(-15), "23:45")

    def test_arrival_time_same_day_overnight_and_multiday(self) -> None:
        same_day = project.arrival_time(14, 15, 35)
        self.assertIsInstance(same_day, tuple)
        self.assertEqual(same_day, ("14:50", 0))

        overnight = project.arrival_time(23, 40, 45)
        self.assertEqual(overnight, ("00:25", 1))

        multiday = project.arrival_time(22, 0, 1600)
        self.assertEqual(multiday, ("00:40", 2))

        with self.assertRaises(ValueError):
            project.arrival_time(10, 0, -5)

    def test_trip_duration_minutes_daytime_and_overnight(self) -> None:
        self.assertEqual(project.trip_duration_minutes(8, 10, 9, 5), 55)
        self.assertEqual(project.trip_duration_minutes(23, 30, 0, 15), 45)
        self.assertEqual(project.trip_duration_minutes(10, 0, 10, 0), 0)
        self.assertEqual(project.trip_duration_minutes(22, 0, 6, 30), 510)

    def test_next_departure_default_24h_schedule(self) -> None:
        mid_wait = project.next_departure(8, 7, 15)
        self.assertIsInstance(mid_wait, tuple)
        self.assertEqual(mid_wait, ("08:15", 8))

        exact_hit = project.next_departure(8, 15, 15)
        self.assertEqual(exact_hit, ("08:15", 0))

        midnight_wrap = project.next_departure(23, 50, 20)
        self.assertEqual(midnight_wrap, ("00:00", 10))

    def test_next_departure_custom_first_bus_and_validation(self) -> None:
        before_first = project.next_departure(5, 45, 20, first_hour=6, first_minute=0)
        self.assertIsInstance(before_first, tuple)
        self.assertEqual(before_first, ("06:00", 15))

        after_first = project.next_departure(6, 25, 20, first_hour=6, first_minute=0)
        self.assertEqual(after_first, ("06:40", 15))

        with self.assertRaises(ValueError):
            project.next_departure(8, 0, 0)
        with self.assertRaises(ValueError):
            project.next_departure(8, 0, -10)


if __name__ == "__main__":
    unittest.main()
