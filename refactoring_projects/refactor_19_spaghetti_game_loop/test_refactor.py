"""Test suite for Refactoring Mission 19: Spaghetti Game Loop."""

import ast
import copy
import inspect
import sys
import types
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_19_spaghetti_game_loop import (  # noqa: E402
    messy_code,
    worked_example,
)


def _snapshot_module_data_globals(module):
    """Capture a deep copy of non-callable, non-module top-level variables."""
    snap = {}
    for name, value in vars(module).items():
        if name.startswith("__"):
            continue
        if isinstance(value, types.ModuleType) or callable(value):
            continue
        snap[name] = copy.deepcopy(value)
    return snap


class TestWorkedExample(unittest.TestCase):
    """Verifies the worked example matches and pure state transitions never mutate inputs."""

    def test_before_and_after_rover_match(self):
        sequences = [
            [],
            ["R", "R", "L", "R"],
            ["L", "L", "R"],
            ["R", "R", "R", "L", "L"],
        ]
        for cmds in sequences:
            self.assertEqual(
                worked_example.before_run_rover(cmds),
                worked_example.after_run_rover(cmds),
            )

    def test_after_step_rover_is_pure(self):
        original = {"pos": 2, "steps": 3}
        nxt = worked_example.after_step_rover(original, "R")
        self.assertEqual(original, {"pos": 2, "steps": 3})
        self.assertEqual(nxt, {"pos": 3, "steps": 4})


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net — must stay 100% GREEN throughout refactoring."""

    def test_run_commands_standard_path(self):
        result = messy_code.run_commands(5, 5, ["R", "R", "D", "L"])
        self.assertEqual(result, {"position": (1, 1), "visited_count": 5})

    def test_run_commands_wall_clamping_and_revisits(self):
        result = messy_code.run_commands(3, 3, ["U", "L", "R", "L", "D", "D", "D"])
        self.assertEqual(result, {"position": (2, 0), "visited_count": 4})

    def test_run_commands_empty_commands_and_empty_grid(self):
        self.assertEqual(
            messy_code.run_commands(4, 4, []),
            {"position": (0, 0), "visited_count": 1},
        )
        self.assertEqual(
            messy_code.run_commands(0, 4, ["R"]),
            {"position": None, "visited_count": 0},
        )


class TestRefactorGoals(unittest.TestCase):
    """Refactoring goals — RED on baseline, GREEN once refactored cleanly."""

    def test_zero_global_statements_in_module(self):
        source = inspect.getsource(messy_code)
        tree = ast.parse(source)
        global_nodes = [n for n in ast.walk(tree) if isinstance(n, ast.Global)]
        self.assertEqual(
            len(global_nodes),
            0,
            f"Found {len(global_nodes)} `global` statement(s) in messy_code.py; "
            "refactor to pure local state and explicit parameters.",
        )

    def test_step_robot_pure_helper_exists_and_clamps_walls(self):
        self.assertTrue(
            hasattr(messy_code, "step_robot"),
            "Expected pure helper `step_robot(pos, command, width, height)` in messy_code.py.",
        )
        step_robot = getattr(messy_code, "step_robot")

        self.assertEqual(step_robot((0, 0), "R", 5, 5), (0, 1))
        self.assertEqual(step_robot((0, 1), "D", 5, 5), (1, 1))
        self.assertEqual(step_robot((1, 1), "L", 5, 5), (1, 0))
        self.assertEqual(step_robot((1, 0), "U", 5, 5), (0, 0))
        # Wall clamping on all four edges:
        self.assertEqual(step_robot((0, 0), "U", 5, 5), (0, 0))
        self.assertEqual(step_robot((0, 0), "L", 5, 5), (0, 0))
        self.assertEqual(step_robot((4, 4), "D", 5, 5), (4, 4))
        self.assertEqual(step_robot((4, 4), "R", 5, 5), (4, 4))
        # Unknown command leaves position intact:
        self.assertEqual(step_robot((2, 2), "WAIT", 5, 5), (2, 2))

    def test_interleaved_simulations_do_not_clobber_each_other(self):
        self.assertTrue(
            hasattr(messy_code, "step_robot"),
            "Expected pure helper `step_robot(pos, command, width, height)` for isolated stepping.",
        )
        step_robot = getattr(messy_code, "step_robot")

        pos_a = (0, 0)  # 5x5 arena
        pos_b = (2, 2)  # 4x4 arena

        pos_a = step_robot(pos_a, "R", 5, 5)
        pos_b = step_robot(pos_b, "U", 4, 4)
        # Interleave a full run_commands call right between robot steps:
        mid_run = messy_code.run_commands(3, 3, ["D", "D", "R"])
        self.assertEqual(mid_run, {"position": (2, 1), "visited_count": 4})

        pos_a = step_robot(pos_a, "D", 5, 5)
        pos_b = step_robot(pos_b, "L", 4, 4)

        self.assertEqual(pos_a, (1, 1))
        self.assertEqual(pos_b, (1, 1))

    def test_run_commands_does_not_mutate_module_globals(self):
        # Run one simulation first so any baseline globals are populated,
        # then snapshot and run a distinct simulation to verify zero mutation.
        messy_code.run_commands(5, 5, ["R"])
        before_snapshot = _snapshot_module_data_globals(messy_code)

        messy_code.run_commands(5, 5, ["D", "D", "R", "R", "R"])
        after_snapshot = _snapshot_module_data_globals(messy_code)

        self.assertEqual(
            before_snapshot,
            after_snapshot,
            "run_commands mutated module-level globals! Keep all simulation state local.",
        )


if __name__ == "__main__":
    unittest.main()
