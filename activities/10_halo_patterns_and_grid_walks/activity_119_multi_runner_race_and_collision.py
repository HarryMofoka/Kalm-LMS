"""
Activity 119: Multi-Runner Race & Collision Detector
Difficulty: 119 / 132

What happens when TWO runners race on the same halo track at different speeds —
or even in OPPOSITE directions?
Now your perimeter walk becomes a discrete 1D circular track of length `n`!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Snapshot of Two Runners at Tick `t`
===============================================================================
Problem:
    Write `example_simulate_two_runners(width, height, start_a, speed_a, start_b, speed_b, t)`
    that simulates two runners on a `width x height` clockwise rectangle halo:
      - `start_a`, `start_b` are starting indices along the perimeter path.
      - `speed_a`, `speed_b` are integer steps per tick (positive = CW,
        negative = CCW, 0 = stationary).
      - At tick `t`:
            idx_a = (start_a + speed_a * t) % n
            idx_b = (start_b + speed_b * t) % n
      - Return `{"pos_a": path[idx_a], "pos_b": path[idx_b], "collided": idx_a == idx_b}`.
      - Raise `ValueError` if `width <= 0` or `height <= 0`.

Draw -> Index -> Rule:
    On a 4x3 rectangle (`n = 10` border cells):
        path = [(0,0), (0,1), (0,2), (0,3), (1,3), (2,3), (2,2), (2,1), (2,0), (1,0)]
        Runner A starts at index 0 with speed +1.
        Runner B starts at index 4 with speed -1.
        - t = 0: A at idx 0 `(0,0)`, B at idx 4 `(1,3)` -> collided = False
        - t = 1: A at idx 1 `(0,1)`, B at idx 3 `(0,3)` -> collided = False
        - t = 2: A at idx 2 `(0,2)`, B at idx 2 `(0,2)` -> collided = True!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — First Collision Detector
===============================================================================
Problem:
    Write `solve_first_collision(width, height, start_a, speed_a, start_b, speed_b, max_steps)`
    that checks ticks `t = 0, 1, 2, ..., max_steps` (inclusive) to find the
    EARLIEST tick `t` where Runner A and Runner B land on the exact same cell!

    Rules:
    - Raise `ValueError` if `width <= 0`, `height <= 0`, or `max_steps < 0`.
    - Return a dictionary:
        * If they collide at earliest tick `t` on cell `(r, c)`:
              {"collided": True, "step": t, "cell": (r, c)}
        * If they NEVER collide during ticks `0 .. max_steps`:
              {"collided": False, "step": None, "cell": None}

    Examples (4x3 rectangle, perimeter n = 10):
        # Opposite directions meeting at t = 2 on (0, 2):
        solve_first_collision(4, 3, 0, 1, 4, -1, 10)
            -> {"collided": True, "step": 2, "cell": (0, 2)}

        # Already starting on the same cell (e.g., 0 and 10 both map to (0, 0)):
        solve_first_collision(4, 3, 0, 2, 10, -1, 5)
            -> {"collided": True, "step": 0, "cell": (0, 0)}

        # Faster runner laps slower runner (A: +2, B: +1, gap = 3 -> meet at t = 3):
        solve_first_collision(4, 3, 0, 2, 3, 1, 10)
            -> {"collided": True, "step": 3, "cell": (2, 2)}

        # Parity trap! On even n = 10, A at 0 (+1) and B at 1 (-1) have opposite
        # parities at every tick — they swap past each other and NEVER collide!
        solve_first_collision(4, 3, 0, 1, 1, -1, 25)
            -> {"collided": False, "step": None, "cell": None}

    Edge-case hints:
        - Check `t = 0` first! `range(max_steps + 1)` includes BOTH `0` and `max_steps`.
        - Handle thin shapes (`4x1`, `1x3`, `1x1`) cleanly by using a thin-shape-safe
          rectangle walk!
"""
from __future__ import annotations


def _rectangle_perimeter(width: int, height: int) -> list[tuple[int, int]]:
    """Build thin-shape-safe clockwise rectangle outline from (0, 0)."""
    if width <= 0 or height <= 0:
        return []
    last_row = height - 1
    last_col = width - 1
    path: list[tuple[int, int]] = []
    for col in range(0, last_col + 1):
        path.append((0, col))
    for row in range(1, last_row + 1):
        path.append((row, last_col))
    if height > 1:
        for col in range(last_col - 1, -1, -1):
            path.append((last_row, col))
    if width > 1:
        for row in range(last_row - 1, 0, -1):
            path.append((row, 0))
    return path


def example_simulate_two_runners(
    width: int,
    height: int,
    start_a: int,
    speed_a: int,
    start_b: int,
    speed_b: int,
    t: int,
) -> dict[str, object]:
    """Return positions of runners A and B at tick `t` and whether they collided."""
    if width <= 0 or height <= 0:
        raise ValueError("width and height must be positive")
    path = _rectangle_perimeter(width, height)
    n = len(path)
    idx_a = (start_a + speed_a * t) % n
    idx_b = (start_b + speed_b * t) % n
    return {
        "pos_a": path[idx_a],
        "pos_b": path[idx_b],
        "collided": idx_a == idx_b,
    }


def solve_first_collision(
    width: int,
    height: int,
    start_a: int,
    speed_a: int,
    start_b: int,
    speed_b: int,
    max_steps: int,
) -> dict[str, object]:
    """Find the earliest tick in 0..max_steps where runners A and B share a cell."""
    pass


if __name__ == "__main__":
    print("Worked Example — Two Runners on 4x3 Rectangle:")
    for tick in range(4):
        print(f"  t={tick}:", example_simulate_two_runners(4, 3, 0, 1, 4, -1, tick))
