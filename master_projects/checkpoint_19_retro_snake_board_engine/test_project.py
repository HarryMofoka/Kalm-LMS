"""Unit tests for Checkpoint 19: Retro Arcade Track & Multi-Runner Race Simulator."""

from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_19_retro_snake_board_engine import (
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Tests verifying the Mars Rover Grid Mission Simulator worked example."""

    def test_step_rover_is_immutable_and_tracks_trail(self) -> None:
        initial = {
            "pos": (0, 0),
            "battery": 5,
            "status": "READY",
            "blocked_hits": 0,
            "trail": [(0, 0)],
        }
        snapshot = copy.deepcopy(initial)
        nxt = worked_example.step_rover(initial, "E", 4, 4, obstacles=set())
        self.assertEqual(initial, snapshot)  # Original state untouched
        self.assertEqual(nxt["pos"], (0, 1))
        self.assertEqual(nxt["battery"], 4)
        self.assertEqual(nxt["status"], "MOVED")
        self.assertEqual(nxt["trail"], [(0, 0), (0, 1)])

    def test_obstacle_and_boundary_collision(self) -> None:
        result = worked_example.run_mission(
            width=3,
            height=3,
            start=(0, 0),
            battery=5,
            obstacles={(0, 1)},
            commands=["N", "E", "S"],
        )
        self.assertEqual(result["pos"], (1, 0))
        self.assertEqual(result["blocked_hits"], 2)
        self.assertEqual(result["battery"], 2)

    def test_out_of_battery_stops_movement(self) -> None:
        result = worked_example.run_mission(
            width=4,
            height=2,
            start=(0, 0),
            battery=1,
            obstacles=set(),
            commands=["E", "E", "E"],
        )
        self.assertEqual(result["pos"], (0, 1))
        self.assertEqual(result["battery"], 0)
        self.assertEqual(result["status"], "OUT_OF_BATTERY")

    def test_render_mars_board_zero_trailing_spaces(self) -> None:
        result = worked_example.run_mission(
            width=4,
            height=3,
            start=(0, 0),
            battery=4,
            obstacles={(1, 1)},
            commands=["E", "E"],
        )
        self.assertEqual(
            result["board"],
            [
                "* * R .",
                ". # . .",
                ". . . .",
            ],
        )
        self.assertTrue(all(line == line.rstrip() for line in result["board"]))


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Retro Arcade Track Race Simulator in project.py."""

    def test_create_race_board_structure_and_clockwise_path(self) -> None:
        board, path = project.create_race_board(6, 5)
        self.assertEqual(len(board), 5)
        self.assertEqual(len(board[0]), 6)
        self.assertEqual(
            ["".join(row) for row in board],
            [
                "######",
                "#....#",
                "#.  .#",
                "#....#",
                "######",
            ],
        )
        self.assertEqual(
            path,
            [
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 4),
                (3, 4),
                (3, 3),
                (3, 2),
                (3, 1),
                (2, 1),
            ],
        )

    def test_create_race_board_minimum_and_invalid_sizes(self) -> None:
        board, path = project.create_race_board(4, 4)
        self.assertEqual(path, [(1, 1), (1, 2), (2, 2), (2, 1)])
        self.assertEqual(board[0], ["#", "#", "#", "#"])
        with self.assertRaises(ValueError):
            project.create_race_board(3, 4)
        with self.assertRaises(ValueError):
            project.create_race_board(4, 3)

    def test_step_runner_wrapping_and_multi_laps(self) -> None:
        dummy_path = [(0, i) for i in range(10)]
        self.assertEqual(project.step_runner(dummy_path, 2, 3), (5, 0))
        self.assertEqual(project.step_runner(dummy_path, 8, 3), (1, 1))
        self.assertEqual(project.step_runner(dummy_path, 2, 25), (7, 2))
        self.assertEqual(project.step_runner(dummy_path, 0, 0), (0, 0))
        with self.assertRaises(ValueError):
            project.step_runner([], 0, 1)
        with self.assertRaises(ValueError):
            project.step_runner(dummy_path, 0, -1)

    def test_simulate_race_positions_laps_collisions_and_board(self) -> None:
        racers = [
            {"name": "Bolt", "symbol": "B", "start": 0, "speed": 2},
            {"name": "Dash", "symbol": "D", "start": 3, "speed": 1},
        ]
        racers_backup = copy.deepcopy(racers)
        result = project.simulate_race(6, 5, racers, ticks=5)

        self.assertEqual(racers, racers_backup)  # Must not mutate input
        self.assertEqual(result["positions"], {"Bolt": (1, 1), "Dash": (3, 1)})
        self.assertEqual(result["indices"], {"Bolt": 0, "Dash": 8})
        self.assertEqual(result["laps"], {"Bolt": 1, "Dash": 0})
        self.assertEqual(
            result["collisions"],
            [{"tick": 3, "cell": (3, 3), "racers": ["Bolt", "Dash"]}],
        )
        self.assertEqual(
            result["board"],
            [
                "# # # # # #",
                "# B . . . #",
                "# .     . #",
                "# D . . . #",
                "# # # # # #",
            ],
        )
        self.assertTrue(all(line == line.rstrip() for line in result["board"]))

    def test_simulate_race_renders_collision_marker_X_on_final_tick(self) -> None:
        racers = [
            {"name": "Bolt", "symbol": "B", "start": 0, "speed": 2},
            {"name": "Dash", "symbol": "D", "start": 3, "speed": 1},
        ]
        result = project.simulate_race(6, 5, racers, ticks=3)
        self.assertEqual(
            result["board"],
            [
                "# # # # # #",
                "# . . . . #",
                "# .     . #",
                "# . . X . #",
                "# # # # # #",
            ],
        )
        self.assertTrue(all(line == line.rstrip() for line in result["board"]))

    def test_simulate_race_zero_ticks_and_negative_tick_guard(self) -> None:
        racers = [{"name": "Solo", "symbol": "S", "start": 0, "speed": 3}]
        result = project.simulate_race(4, 4, racers, ticks=0)
        self.assertEqual(result["positions"], {"Solo": (1, 1)})
        self.assertEqual(result["laps"], {"Solo": 0})
        self.assertEqual(result["collisions"], [])
        with self.assertRaises(ValueError):
            project.simulate_race(4, 4, racers, ticks=-1)


if __name__ == "__main__":
    unittest.main()
