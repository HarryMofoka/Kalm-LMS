"""
Activity 010: Ceiling Division Without `math.ceil`
Difficulty: 10 / 132 (Rank 2 - Foundations Builder)

Context:
How many shipping boxes do you need for 13 mugs if each box holds 4?
`13 // 4` gives `3`, which leaves 1 mug stranded! You actually need `4` boxes.
While `math.ceil(13 / 4)` works for small numbers, floating-point division loses
precision on very large integers — whereas integer ceiling division works
EXACTLY for integers of any size, with zero imports!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_boxes_needed(items, box_capacity)` that returns the minimum
number of boxes needed to hold `items` (>= 0) when each box holds
`box_capacity` (> 0) items — without using `math.ceil`.

The Magic Formula:
    boxes = (items + box_capacity - 1) // box_capacity

Step-by-step walkthrough:
Why does adding `box_capacity - 1` before floor-dividing work?
- Case A: `items` is an EXACT multiple of `box_capacity` (say `12` items, cap `4`):
      `(12 + 3) // 4 = 15 // 4 = 3` (adding 3 wasn't enough to cross the next
      multiple of 4, so we stay at 3!).
- Case B: `items` has ANY remainder `1 .. cap-1` (say `13` items, cap `4`):
      `(13 + 3) // 4 = 16 // 4 = 4` (adding 3 pushes it up to the next multiple!).
- Case C: `items == 0` (say `0` items, cap `4`):
      `(0 + 3) // 4 = 3 // 4 = 0` (no boxes needed for 0 items!).

Edge cases:
- `example_boxes_needed(0, 6)` -> `0`.
- `example_boxes_needed(12, 6)` -> `2` (exact fit, no extra box!).
- `example_boxes_needed(13, 6)` -> `3` (one extra box for the 13th item).

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A school field trip coordinator needs to charter buses for `passengers` (>= 0),
where each bus has `seats_per_bus` (> 0) seats. Write
`solve_bus_seating(passengers, seats_per_bus)` that returns a 2-tuple:
    `(buses_needed, empty_seats)`

Where:
- `buses_needed`: minimum number of buses required to seat every passenger
  (computed with integer ceiling division, no `math.ceil`).
- `empty_seats`: how many seats remain unused across all chartered buses.

Rules:
- `empty_seats = buses_needed * seats_per_bus - passengers`.
- When `passengers == 0`, return `(0, 0)`.
- When `passengers` is an exact multiple of `seats_per_bus`, `empty_seats` is `0`.

Examples:
- `solve_bus_seating(100, 40)` -> `(3, 20)`  # 3 buses = 120 seats -> 20 empty
- `solve_bus_seating(80, 40)` -> `(2, 0)`    # exact fit!
- `solve_bus_seating(0, 40)` -> `(0, 0)`     # nobody going -> 0 buses, 0 empty
- `solve_bus_seating(1, 40)` -> `(1, 39)`    # 1 passenger still needs 1 bus

Hints:
- Compute `buses_needed` first using `(passengers + seats_per_bus - 1) // seats_per_bus`.
- Check how `buses_needed * seats_per_bus - passengers` behaves when `passengers == 0`:
  `0 * 40 - 0 == 0`! Everything works cleanly without special cases.
"""

from __future__ import annotations


def example_boxes_needed(items: int, box_capacity: int) -> int:
    """Return the minimum number of boxes needed using pure integer ceiling division."""
    # Adding (box_capacity - 1) rounds up any nonzero remainder without overshooting exact fits.
    return (items + box_capacity - 1) // box_capacity


def solve_bus_seating(passengers: int, seats_per_bus: int) -> tuple[int, int]:
    """Return (buses_needed, empty_seats) for the given passenger count and bus capacity."""
    pass


if __name__ == "__main__":
    print("12 items, cap 4 ->", example_boxes_needed(12, 4))
    print("13 items, cap 4 ->", example_boxes_needed(13, 4))
    print("0 items,  cap 4 ->", example_boxes_needed(0, 4))
