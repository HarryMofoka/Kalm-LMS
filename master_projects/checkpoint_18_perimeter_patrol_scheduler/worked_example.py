"""Worked Example for Checkpoint 18: Conveyor Belt Inspection Station Scheduler.

Demonstrates clockwise rectangular halo walks, degenerate 1D shape handling,
modulo-spaced moving sensors, and zero-trailing-space ASCII floor snapshots.
"""

from __future__ import annotations


def conveyor_loop(width: int, height: int) -> list[tuple[int, int]]:
    """Return clockwise (row, col) coordinates along the outer belt border."""
    if width < 1 or height < 1:
        raise ValueError("width and height must be at least 1")

    if height == 1:
        return [(0, c) for c in range(width)]
    if width == 1:
        return [(r, 0) for r in range(height)]

    walk: list[tuple[int, int]] = []
    # Top edge: left -> right
    for c in range(width):
        walk.append((0, c))
    # Right edge: top + 1 -> bottom
    for r in range(1, height):
        walk.append((r, width - 1))
    # Bottom edge: right - 1 -> left
    for c in range(width - 2, -1, -1):
        walk.append((height - 1, c))
    # Left edge: bottom - 1 -> top + 1
    for r in range(height - 2, 0, -1):
        walk.append((r, 0))
    return walk


def sensor_coordinates(
    width: int, height: int, num_sensors: int, tick: int
) -> list[tuple[int, int]]:
    """Place ``num_sensors`` evenly on the conveyor loop and advance ``tick`` steps."""
    loop = conveyor_loop(width, height)
    perimeter = len(loop)
    if num_sensors < 0 or num_sensors > perimeter:
        raise ValueError(
            f"num_sensors must be between 0 and perimeter length ({perimeter})"
        )
    if num_sensors == 0:
        return []

    return [
        loop[((i * perimeter) // num_sensors + tick) % perimeter]
        for i in range(num_sensors)
    ]


def render_factory_floor(
    width: int, height: int, num_sensors: int, tick: int
) -> list[str]:
    """Render an ASCII snapshot of the factory conveyor and active sensors."""
    loop = conveyor_loop(width, height)
    sensors = sensor_coordinates(width, height, num_sensors, tick)

    grid = [[" " for _ in range(width)] for _ in range(height)]
    for r, c in loop:
        grid[r][c] = "."
    for idx, (r, c) in enumerate(sensors):
        label = chr(ord("A") + idx) if idx < 26 else "S"
        grid[r][c] = label

    return [" ".join(row).rstrip() for row in grid]


if __name__ == "__main__":
    for tick in range(3):
        print(f"=== Conveyor Tick {tick} ===")
        for line in render_factory_floor(width=6, height=4, num_sensors=3, tick=tick):
            print(line)
