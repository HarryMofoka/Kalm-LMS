"""Checkpoint 19 Master Project: Retro Arcade Track & Multi-Runner Race Simulator.

Build a walled arena with an inner clockwise halo track, advance runners with
lap counting, detect tick-by-tick cell collisions, and render the final board
with zero trailing spaces.
"""

from __future__ import annotations


def create_race_board(
    width: int, height: int
) -> tuple[list[list[str]], list[tuple[int, int]]]:
    """Build a walled race arena and its clockwise inner halo track.

    Raises ``ValueError`` if ``width < 4`` or ``height < 4``.
    Returns ``(board, track_path)`` where ``board`` uses ``'#'`` for outer
    walls, ``'.'`` for the inner halo track, and ``' '`` for the inner
    courtyard, and ``track_path`` lists clockwise ``(row, col)`` coordinates
    starting at ``(1, 1)``.
    """
    pass


def step_runner(
    path: list[tuple[int, int]], current_index: int, speed: int
) -> tuple[int, int]:
    """Advance a runner along ``path`` and return ``(new_index, laps_gained)``.

    Raises ``ValueError`` if ``path`` is empty, ``current_index < 0``, or
    ``speed < 0``.
    """
    pass


def simulate_race(
    width: int, height: int, racers: list[dict], ticks: int
) -> dict:
    """Simulate a multi-runner race for ``ticks`` steps on a walled halo track.

    Each racer dict has keys ``"name"``, ``"symbol"``, ``"start"``, ``"speed"``.
    Returns a dictionary containing:
    - ``"positions"``: ``dict[str, tuple[int, int]]``
    - ``"indices"``: ``dict[str, int]``
    - ``"laps"``: ``dict[str, int]``
    - ``"collisions"``: list of ``{"tick": int, "cell": (r, c), "racers": list[str]}``
    - ``"board"``: ``list[str]`` rendered final board with ZERO trailing spaces
    """
    pass
