"""Worked Example: Parking Garage 2D Bay Allocator.

Demonstrates alias-free 2D grid creation, strict coordinate validation,
pure (non-mutating) grid updates, occupancy analytics, and clean ASCII
map rendering with zero trailing spaces.
"""

from __future__ import annotations

OPEN_BAY = "."
OCCUPIED_BAY = "P"


def _clone_grid(grid: list[list[str]]) -> list[list[str]]:
    """Return an independent deep copy of a 2D string grid."""
    return [list(row) for row in grid]


def create_garage(levels: int, bays_per_level: int) -> list[list[str]]:
    """Create a 2D parking garage filled with '.' without row aliasing."""
    if levels < 1 or bays_per_level < 1:
        raise ValueError("levels and bays_per_level must both be at least 1")
    return [[OPEN_BAY for _ in range(bays_per_level)] for _ in range(levels)]


def find_nearest_open_bay(garage: list[list[str]]) -> tuple[int, int] | None:
    """Return the first (level, bay) containing '.', or None if garage is full."""
    for level_idx, row in enumerate(garage):
        for bay_idx, state in enumerate(row):
            if state == OPEN_BAY:
                return (level_idx, bay_idx)
    return None


def reserve_bay(
    garage: list[list[str]],
    level: int,
    bay: int,
) -> list[list[str]]:
    """Return a new garage grid with (level, bay) reserved as 'P'.

    Raises:
        ValueError: If coordinates are out of bounds or bay is already occupied.
    """
    if level < 0 or level >= len(garage):
        raise ValueError(f"Level out of bounds: {level}")
    if bay < 0 or bay >= len(garage[level]):
        raise ValueError(f"Bay out of bounds: {bay}")
    if garage[level][bay] != OPEN_BAY:
        raise ValueError(f"Bay ({level}, {bay}) is already occupied")

    updated = _clone_grid(garage)
    updated[level][bay] = OCCUPIED_BAY
    return updated


def garage_occupancy(garage: list[list[str]]) -> dict[str, object]:
    """Compute total, occupied, available bays, and occupancy percentage."""
    total = sum(len(row) for row in garage)
    occupied = sum(cell == OCCUPIED_BAY for row in garage for cell in row)
    available = total - occupied
    pct = round((occupied / total) * 100.0, 2) if total > 0 else 0.0
    return {
        "total_bays": total,
        "occupied": occupied,
        "available": available,
        "occupancy_pct": pct,
    }


def render_garage_map(garage: list[list[str]]) -> str:
    """Render each garage level as 'L1: . P .' with zero trailing spaces."""
    if not garage:
        return ""
    lines = [
        f"L{idx + 1}: {' '.join(row)}"
        for idx, row in enumerate(garage)
    ]
    return "\n".join(lines)


if __name__ == "__main__":
    g = create_garage(levels=3, bays_per_level=5)
    g = reserve_bay(g, 0, 0)
    g = reserve_bay(g, 0, 1)
    g = reserve_bay(g, 1, 2)

    print("=== Parking Garage Map ===")
    print(render_garage_map(g))
    print("\nNext nearest open bay:", find_nearest_open_bay(g))
    print("Occupancy:", garage_occupancy(g))
