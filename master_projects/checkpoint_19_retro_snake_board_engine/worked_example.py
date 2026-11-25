"""Worked Example for Checkpoint 19: Mars Rover Grid Mission Simulator.

Demonstrates immutable grid state transitions, boundary & obstacle collision
handling, battery tracking, and zero-trailing-space ASCII map rendering.
"""

from __future__ import annotations

DIRECTIONS: dict[str, tuple[int, int]] = {
    "N": (-1, 0),
    "E": (0, 1),
    "S": (1, 0),
    "W": (0, -1),
}


def create_mars_map(
    width: int, height: int, obstacles: set[tuple[int, int]]
) -> list[list[str]]:
    """Create a ``height x width`` Mars terrain grid with ``#`` obstacles."""
    if width < 1 or height < 1:
        raise ValueError("width and height must be at least 1")

    grid = [["." for _ in range(width)] for _ in range(height)]
    for r, c in obstacles:
        if 0 <= r < height and 0 <= c < width:
            grid[r][c] = "#"
    return grid


def step_rover(
    state: dict,
    command: str,
    width: int,
    height: int,
    obstacles: set[tuple[int, int]],
) -> dict:
    """Return a NEW rover state after executing a single N/E/S/W command."""
    if command not in DIRECTIONS:
        raise ValueError(f"Unknown rover command: {command!r}")

    pos: tuple[int, int] = state["pos"]
    battery: int = state["battery"]
    blocked_hits: int = state["blocked_hits"]
    trail: list[tuple[int, int]] = list(state["trail"])

    if battery <= 0:
        return {
            "pos": pos,
            "battery": 0,
            "status": "OUT_OF_BATTERY",
            "blocked_hits": blocked_hits,
            "trail": trail,
        }

    dr, dc = DIRECTIONS[command]
    target = (pos[0] + dr, pos[1] + dc)
    in_bounds = 0 <= target[0] < height and 0 <= target[1] < width

    if not in_bounds or target in obstacles:
        return {
            "pos": pos,
            "battery": battery - 1,
            "status": "BLOCKED",
            "blocked_hits": blocked_hits + 1,
            "trail": trail,
        }

    trail.append(target)
    return {
        "pos": target,
        "battery": battery - 1,
        "status": "MOVED",
        "blocked_hits": blocked_hits,
        "trail": trail,
    }


def run_mission(
    width: int,
    height: int,
    start: tuple[int, int],
    battery: int,
    obstacles: set[tuple[int, int]],
    commands: list[str],
) -> dict:
    """Execute a sequence of commands and return the final state + rendered map."""
    if not (0 <= start[0] < height and 0 <= start[1] < width):
        raise ValueError("start position is out of bounds")
    if start in obstacles:
        raise ValueError("start position cannot be on an obstacle")
    if battery < 0:
        raise ValueError("battery cannot be negative")

    state: dict = {
        "pos": start,
        "battery": battery,
        "status": "READY",
        "blocked_hits": 0,
        "trail": [start],
    }
    for cmd in commands:
        state = step_rover(state, cmd, width, height, obstacles)

    state["board"] = render_mars_board(
        width, height, obstacles, state["pos"], state["trail"]
    )
    return state


def render_mars_board(
    width: int,
    height: int,
    obstacles: set[tuple[int, int]],
    rover_pos: tuple[int, int],
    trail: list[tuple[int, int]],
) -> list[str]:
    """Render the Mars mission map with ``*`` trail, ``#`` rocks, and ``R`` rover."""
    grid = create_mars_map(width, height, obstacles)
    for r, c in trail:
        if 0 <= r < height and 0 <= c < width:
            grid[r][c] = "*"
    rr, rc = rover_pos
    grid[rr][rc] = "R"
    return [" ".join(row).rstrip() for row in grid]


if __name__ == "__main__":
    result = run_mission(
        width=6,
        height=4,
        start=(0, 0),
        battery=10,
        obstacles={(0, 2), (2, 3)},
        commands=["E", "E", "S", "E", "E", "S"],
    )
    print(f"Final pos: {result['pos']} | Battery: {result['battery']} | Hits: {result['blocked_hits']}")
    for line in result["board"]:
        print(line)
