"""Unit tests for Checkpoint 18: Perimeter Patrol Scheduler."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_18_perimeter_patrol_scheduler import (
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Tests verifying the Conveyor Belt Inspection Station worked example."""

    def test_conveyor_loop_rectangle_and_thin_shapes(self) -> None:
        self.assertEqual(worked_example.conveyor_loop(1, 1), [(0, 0)])
        self.assertEqual(
            worked_example.conveyor_loop(4, 1),
            [(0, 0), (0, 1), (0, 2), (0, 3)],
        )
        self.assertEqual(
            worked_example.conveyor_loop(1, 3),
            [(0, 0), (1, 0), (2, 0)],
        )
        rect = worked_example.conveyor_loop(3, 3)
        self.assertEqual(len(rect), 8)
        self.assertEqual(len(set(rect)), 8)
        self.assertEqual(
            rect,
            [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (2, 1), (2, 0), (1, 0)],
        )

    def test_sensor_coordinates_modulo_wrapping(self) -> None:
        pos0 = worked_example.sensor_coordinates(4, 3, num_sensors=2, tick=0)
        self.assertEqual(pos0, [(0, 0), (2, 3)])
        # Perimeter of 4x3 is 10; tick=10 wraps cleanly back to tick=0
        pos10 = worked_example.sensor_coordinates(4, 3, num_sensors=2, tick=10)
        self.assertEqual(pos10, pos0)

    def test_render_factory_floor_snapshot(self) -> None:
        floor = worked_example.render_factory_floor(4, 3, num_sensors=2, tick=0)
        self.assertEqual(
            floor,
            [
                "A . . .",
                ".     .",
                ". . . B",
            ],
        )
        self.assertTrue(all(line == line.rstrip() for line in floor))

    def test_invalid_dimensions_and_sensor_counts(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.conveyor_loop(0, 3)
        with self.assertRaises(ValueError):
            worked_example.sensor_coordinates(2, 2, num_sensors=5, tick=0)


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Security Drone Patrol Planner in project.py."""

    def test_build_perimeter_walk_standard_rectangle(self) -> None:
        walk = project.build_perimeter_walk(4, 3)
        self.assertEqual(
            walk,
            [
                (0, 0),
                (0, 1),
                (0, 2),
                (0, 3),
                (1, 3),
                (2, 3),
                (2, 2),
                (2, 1),
                (2, 0),
                (1, 0),
            ],
        )

    def test_build_perimeter_walk_thin_and_invalid_shapes(self) -> None:
        self.assertEqual(project.build_perimeter_walk(1, 1), [(0, 0)])
        self.assertEqual(
            project.build_perimeter_walk(3, 1), [(0, 0), (0, 1), (0, 2)]
        )
        self.assertEqual(
            project.build_perimeter_walk(1, 3), [(0, 0), (1, 0), (2, 0)]
        )
        with self.assertRaises(ValueError):
            project.build_perimeter_walk(0, 4)
        with self.assertRaises(ValueError):
            project.build_perimeter_walk(4, -1)

    def test_drone_positions_even_spacing_and_modulo_wrap(self) -> None:
        # 4x3 perimeter length is 10
        self.assertEqual(
            project.drone_positions(4, 3, num_drones=2, tick=0),
            [(0, 0), (2, 3)],
        )
        self.assertEqual(
            project.drone_positions(4, 3, num_drones=2, tick=1),
            [(0, 1), (2, 2)],
        )
        self.assertEqual(
            project.drone_positions(4, 3, num_drones=2, tick=11),
            [(0, 1), (2, 2)],
        )
        self.assertEqual(project.drone_positions(4, 3, num_drones=0, tick=5), [])
        with self.assertRaises(ValueError):
            project.drone_positions(2, 2, num_drones=5, tick=0)

    def test_render_patrol_map_standard_and_zero_trailing_spaces(self) -> None:
        rendered = project.render_patrol_map(4, 3, num_drones=2, tick=0)
        self.assertEqual(
            rendered,
            [
                "1 o o o",
                "o     o",
                "o o o 2",
            ],
        )
        self.assertTrue(all(line == line.rstrip() for line in rendered))

    def test_render_patrol_map_ten_plus_drones_uses_D(self) -> None:
        # 4x4 perimeter length is 12; 10th drone (index 9) must render as 'D'
        rendered = project.render_patrol_map(4, 4, num_drones=10, tick=0)
        self.assertEqual(
            rendered,
            [
                "1 2 3 4",
                "o     5",
                "D     o",
                "9 8 7 6",
            ],
        )
        self.assertTrue(all(line == line.rstrip() for line in rendered))

    def test_ticks_until_sync_math_and_edge_cases(self) -> None:
        self.assertEqual(project.ticks_until_sync(12, 1, 3), 6)
        self.assertEqual(project.ticks_until_sync(12, 1, 2), 12)
        self.assertEqual(project.ticks_until_sync(10, 1, -1), 5)
        self.assertEqual(project.ticks_until_sync(12, 2, 2), 1)
        with self.assertRaises(ValueError):
            project.ticks_until_sync(0, 1, 2)


if __name__ == "__main__":
    unittest.main()
