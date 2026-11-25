r"""
Activity 116: Triangle & Diamond Perimeter Walks
Difficulty: 116 / 132

Perimeter walks aren't just for axis-aligned boxes!
Diagonal legs move BOTH `row` and `col` on every step — and the exact same
Legs Table discipline guarantees zero duplicate vertices!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Right-Triangle Clockwise Walk
===============================================================================
Problem:
    Write `example_triangle_walk(height)` returning the clockwise outline cells
    of a left-aligned right triangle starting at the apex `(0, 0)`.

Draw -> Index -> Legs Table:
    DRAW & INDEX (height = 4, last = 3):
        (0,0)
          ^ \
          |  (1,1)
        (1,0)  \
          ^    (2,2)
          |      \
        (2,0)    (3,3)
          ^       |
          |       v
        (3,0) <- (3,1) <- (3,2) <-

    LEGS TABLE (for height >= 2, last = height - 1):
        | Leg    | Formula       | Loop variable        | Starts at     | Ends at        |
        |--------|---------------|----------------------|---------------|----------------|
        | Slope  | (i, i)        | i: 0 -> last         | (0, 0)        | (last, last)   |
        | Bottom | (last, col)   | col: last - 1 -> 0   | (last, last-1)| (last, 0)      |
        | Left   | (row, 0)      | row: last - 1 -> 1   | (last - 1, 0) | (1, 0)         |

    INVARIANTS:
        - `height <= 0` -> `[]`
        - `height == 1` -> `[(0, 0)]`
        - `height >= 2` -> `len(path) == 3 * height - 3` and no duplicate cells!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Diamond Halo Clockwise Walk
===============================================================================
Problem:
    Write `solve_diamond_walk(radius: int) -> list[tuple[int, int]]` returning the
    outline cells of a Manhattan diamond (from Activity 113) in CLOCKWISE order
    starting at the TOP vertex `(0, radius)`, with ZERO duplicate vertices!

Draw -> Index -> Legs Table (radius = r, grid size = 2*r + 1):
    DRAW & INDEX (radius = 2, vertices: Top (0,2), Right (2,4), Bottom (4,2), Left (2,0)):
                (0,2)
               /     \
           (1,1)     (1,3)
            /           \
        (2,0)           (2,4)
            \           /
           (3,1)     (3,3)
               \     /
                (4,2)

    LEGS TABLE (for radius = r >= 1; each leg takes `r` cells for `i` in `range(r)`!):
        | Leg          | Formula               | Starts at  | Ends at          |
        |--------------|-----------------------|------------|------------------|
        | Top-Right    | (i, r + i)            | (0, r)     | (r - 1, 2r - 1)  |
        | Bottom-Right | (r + i, 2 * r - i)    | (r, 2r)    | (2r - 1, r + 1)  |
        | Bottom-Left  | (2 * r - i, r - i)    | (2r, r)    | (r + 1, 1)       |
        | Top-Left     | (r - i, i)            | (r, 0)     | (1, r - 1)       |

    Examples:
        solve_diamond_walk(-1) -> []
        solve_diamond_walk(0)  -> [(0, 0)]
        solve_diamond_walk(1)  -> [(0, 1), (1, 2), (2, 1), (1, 0)]
        solve_diamond_walk(2)  -> [
            (0, 2), (1, 3),
            (2, 4), (3, 3),
            (4, 2), (3, 1),
            (2, 0), (1, 1),
        ]

    Edge-case hints:
        - Notice how clean `range(r)` is: each leg OWNS its starting vertex and
          stops ONE step before the next vertex!
        - For `radius >= 1`, `len(path) == 4 * radius` and EVERY cell satisfies
          `abs(row - radius) + abs(col - radius) == radius`!
"""
from __future__ import annotations


def example_triangle_walk(height: int) -> list[tuple[int, int]]:
    """Return clockwise outline cells of a right triangle from (0, 0)."""
    if height <= 0:
        return []
    if height == 1:
        return [(0, 0)]

    last = height - 1
    path: list[tuple[int, int]] = []
    for i in range(0, last + 1):                 # Slope:  (0, 0) -> (last, last)
        path.append((i, i))
    for col in range(last - 1, -1, -1):          # Bottom: (last, last-1) -> (last, 0)
        path.append((last, col))
    for row in range(last - 1, 0, -1):           # Left:   (last-1, 0) -> (1, 0)
        path.append((row, 0))
    return path


def solve_diamond_walk(radius: int) -> list[tuple[int, int]]:
    """Return clockwise outline cells of a diamond halo starting at (0, radius)."""
    pass


if __name__ == "__main__":
    print("Worked Example — Right Triangle Clockwise Walk (height=4):")
    print(example_triangle_walk(4))
