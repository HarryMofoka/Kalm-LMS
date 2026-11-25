"""
Activity 060: 2D Grid Safe Creation & Neighbors  [Unlocks Checkpoint 10!]
Difficulty: 60 / 132

Context:
    Welcome to the Module 05 capstone! Every Python developer hits the famous
    `grid = [[0] * cols] * rows` bug at least once—where mutating `grid[0][0]`
    mysteriously overwrites EVERY row because all rows point to the exact same
    list object! Pair safe grid construction with boundary-checked neighbor
    counting, and you're ready for Minesweeper, Game of Life, and maze exams.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Build a 2D Grid Without the Aliasing Bug
===============================================================================
Problem:
    Create and return a `rows x cols` 2D list filled with `fill_value` such that
    every row is an INDEPENDENT list object (modifying `grid[0][0]` must NEVER
    change `grid[1][0]`). Return `[]` if `rows <= 0` or `cols <= 0`.

Step-by-Step Explanation:
    1. Guard `if rows <= 0 or cols <= 0: return []`.
    2. Use a list comprehension: `[[fill_value for _ in range(cols)] for _ in range(rows)]`.
    3. Because the inner list is re-created on each iteration of the outer loop,
       every row gets its own distinct memory address (`grid[0] is not grid[1]`).

Edge Cases:
    - `(2, 3, 0)` -> `[[0, 0, 0], [0, 0, 0]]` with `grid[0] is not grid[1]`
    - `(0, 3, 1)` -> `[]`
    - `(2, 0, 1)` -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Count 4-Directional Live Neighbors
===============================================================================
Problem:
    Implement `solve_count_live_neighbors(grid: list[list[int]], row: int, col: int) -> int`.
    Given a rectangular 2D grid of `0`s (dead) and `1`s (live) and a target
    coordinate `(row, col)`:
      - Count how many of its 4 orthogonal neighbors—UP `(row - 1, col)`,
        DOWN `(row + 1, col)`, LEFT `(row, col - 1)`, and RIGHT `(row, col + 1)`—
        are INSIDE the grid bounds and have value `1`.
      - Do NOT count diagonal neighbors, and do NOT count `(row, col)` itself!
      - If `grid` is empty (`[]` or `[[]]`) or `(row, col)` is out of bounds,
        return `0`.

Examples:
    Given:
        grid = [
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0],
        ]
    - `(1, 1)` -> `4` (up=1, down=1, left=1, right=1)
    - `(0, 0)` -> `2` (down=1, right=1; up & left out of bounds)
    - `(0, 2)` -> `2` (left=1, down=1)
    - `(1, 0)` -> `1` (up=1; down=0, right=0)
    - `(2, 2)` -> `2` (up=1, left=1)
    - `(-1, 0)` or `(5, 5)` -> `0` (target out of bounds)

Edge-Case Hints:
    - Define `directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]`!
    - ALWAYS check `0 <= nr < num_rows and 0 <= nc < num_cols` BEFORE indexing
      `grid[nr][nc]`—remember Python allows negative indices like `grid[-1][0]`
      which would silently wrap around to the bottom row instead of raising an
      error!
"""

from __future__ import annotations


def example_create_grid(
    rows: int,
    cols: int,
    fill_value: int = 0,
) -> list[list[int]]:
    """Build an independent `rows x cols` 2D grid with no shared-row aliasing."""
    if rows <= 0 or cols <= 0:
        return []
    return [[fill_value for _ in range(cols)] for _ in range(rows)]


def solve_count_live_neighbors(grid: list[list[int]], row: int, col: int) -> int:
    """Count how many of the 4 orthogonal neighbors of `(row, col)` equal 1."""
    pass


if __name__ == "__main__":
    board = example_create_grid(3, 4, 0)
    board[0][0] = 9
    print("Safe grid after mutating board[0][0] = 9:")
    for r in board:
        print(" ", r)
