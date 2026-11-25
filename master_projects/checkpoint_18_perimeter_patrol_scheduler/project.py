"""Checkpoint 18 Master Project: Security Drone Perimeter Patrol Planner.

Implement clockwise perimeter walks, modulo-based fleet scheduling, ASCII map
rendering with zero trailing spaces, and fleet synchronization timing.
"""

from __future__ import annotations


def build_perimeter_walk(width: int, height: int) -> list[tuple[int, int]]:
    """Return clockwise (row, col) perimeter coordinates starting at (0, 0).

    Must handle degenerate thin shapes (1x1, 1xW, Hx1) without duplicating
    corners. Raises ``ValueError`` if ``width < 1`` or ``height < 1``.
    """
    pass


def drone_positions(
    width: int, height: int, num_drones: int, tick: int
) -> list[tuple[int, int]]:
    """Return (row, col) positions of ``num_drones`` evenly spaced drones at ``tick``.

    Drone ``i`` starts at ``(i * P) // num_drones`` and advances ``tick`` steps
    clockwise modulo ``P`` (perimeter length). Raises ``ValueError`` if
    ``num_drones < 0`` or ``num_drones > P``.
    """
    pass


def render_patrol_map(
    width: int, height: int, num_drones: int, tick: int
) -> list[str]:
    """Render the patrol perimeter map with ZERO trailing spaces per line.

    Uses ``'o'`` for unoccupied perimeter track, ``'1'``..``'9'`` for the first
    9 drones, ``'D'`` for the 10th+ drones, ``' '`` for interior cells, and
    single spaces between columns.
    """
    pass


def ticks_until_sync(perimeter_len: int, speed_a: int, speed_b: int) -> int:
    """Return the smallest ``t >= 1`` when two drones starting at 0 re-sync.

    Finds the minimum positive integer ``t`` such that
    ``(speed_a * t) % perimeter_len == (speed_b * t) % perimeter_len``.
    Raises ``ValueError`` if ``perimeter_len <= 0``.
    """
    pass
