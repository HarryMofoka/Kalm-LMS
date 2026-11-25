"""
Activity 059: Coordinate Tuples & Manhattan Distance
Difficulty: 59 / 132

Context:
    City-block GPS routers, warehouse robots, and grid games measure distance
    using Manhattan (taxicab) distance: `|x1 - x2| + |y1 - y2|`. Representing
    coordinates as immutable `(x, y)` tuples lets you unpack them cleanly in
    loops (`for x, y in points:`).

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Nearest Point to Origin
===============================================================================
Problem:
    Given a list of `(x, y)` integer coordinate tuples, return the point with
    the smallest Manhattan distance `abs(x) + abs(y)` to the origin `(0, 0)`.
    If two points tie for closest, return the FIRST one encountered.
    Return `None` if `points` is empty.

Step-by-Step Explanation:
    1. Guard `if not points: return None`.
    2. Seed `best_point = points[0]` and `best_dist = abs(x0) + abs(y0)`.
    3. Loop through `points[1:]`, unpacking `x, y` cleanly. Update `best_point`
       only on strict `<` so ties keep the first point.

Edge Cases:
    - `[(3, 4), (-1, 2), (2, -1)]` -> `(-1, 2)` (dist 3, ties with `(2, -1)`, first wins)
    - `[(0, 0), (1, 1)]`           -> `(0, 0)`
    - `[]`                         -> `None`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Total Path Manhattan Distance Across Waypoints
===============================================================================
Problem:
    Implement `solve_path_manhattan_distance(waypoints: list[tuple[int, int]]) -> int`.
    Given an ordered list of `(x, y)` waypoint tuples, compute the total
    Manhattan distance traveled walking sequentially from:
      `waypoints[0]` -> `waypoints[1]` -> `waypoints[2]` -> ... -> `waypoints[-1]`.
    Return `0` if `waypoints` has fewer than 2 points (empty or single waypoint).

Examples:
    - `[(0, 0), (3, 4), (3, 1)]`         -> `10`  (`(|3-0|+|4-0|) + (|3-3|+|1-4|) = 7 + 3`)
    - `[(-2, 5), (1, 1), (-1, -1)]`      -> `11`  (`(3 + 4) + (2 + 2) = 11`)
    - `[(2, 2), (2, 2)]`                 -> `0`
    - `[(5, 5)]`                         -> `0`
    - `[]`                               -> `0`

Edge-Case Hints:
    - Pair consecutive waypoints with `for i in range(len(waypoints) - 1):`
      using `x1, y1 = waypoints[i]` and `x2, y2 = waypoints[i + 1]`
      (or `zip(waypoints, waypoints[1:])`!).
    - Don't forget `abs(...)` on BOTH coordinate differences (`abs(x2 - x1) + abs(y2 - y1)`)!
"""

from __future__ import annotations


def example_nearest_to_origin(
    points: list[tuple[int, int]],
) -> tuple[int, int] | None:
    """Return the `(x, y)` point closest to `(0, 0)` by Manhattan distance (first tie wins)."""
    if not points:
        return None

    best_point = points[0]
    best_dist = abs(best_point[0]) + abs(best_point[1])

    for x, y in points[1:]:
        dist = abs(x) + abs(y)
        if dist < best_dist:
            best_dist = dist
            best_point = (x, y)
    return best_point


def solve_path_manhattan_distance(waypoints: list[tuple[int, int]]) -> int:
    """Return total Manhattan distance along consecutive `(x, y)` waypoints."""
    pass


if __name__ == "__main__":
    coords = [(3, 4), (-1, 2), (2, -1), (5, 0)]
    print("Nearest to origin:", example_nearest_to_origin(coords))
