"""
Activity 006: Powers, Roots & 2D Distance  [Unlocks Checkpoint 01!]
Difficulty: 6 / 132 (Rank 1 - Absolute Beginner)

Context:
In 2D video games, delivery-routing maps, and machine learning nearest-neighbor
classifiers, you constantly need the straight-line distance between two points.
Python's exponentiation operator `**` handles both squaring (`x ** 2`) and
square roots (`x ** 0.5`) without even needing to import a library!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_hypotenuse(side_a, side_b)` to compute the length of the
hypotenuse of a right triangle with legs `side_a` and `side_b`, rounded to 4
decimal places.

Pythagorean Theorem:
    c = sqrt(a^2 + b^2) = (a ** 2 + b ** 2) ** 0.5

Step-by-step walkthrough:
1. Square each leg with `** 2`: `side_a ** 2 + side_b ** 2`.
2. Take the square root by raising the sum to the power `0.5` (or using
   `math.sqrt`).
3. Round to 4 decimal places with `round(..., 4)` so irrational roots like
   `sqrt(2)` cleanly return `1.4142`.

Edge cases:
- Classic 3-4-5 triangle: `example_hypotenuse(3, 4)` -> `5.0`.
- Zero legs: `example_hypotenuse(0, 0)` -> `0.0`.
- One zero leg: `example_hypotenuse(0, 7)` -> `7.0`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A drone delivery app tracks takeoff `(x1, y1)` and drop-off `(x2, y2)` on a
2D city grid. Write `solve_euclidean_distance(x1, y1, x2, y2)` to return the
straight-line (Euclidean) distance between `(x1, y1)` and `(x2, y2)`, rounded
to 4 decimal places.

Formula:
    dx = x2 - x1
    dy = y2 - y1
    distance = (dx ** 2 + dy ** 2) ** 0.5

Rules:
- Works for positive, negative, and floating-point coordinates.
- Return the distance rounded to 4 decimal places (`round(distance, 4)`).

Examples:
- `solve_euclidean_distance(0, 0, 3, 4)` -> `5.0`
- `solve_euclidean_distance(1, 2, 1, 2)` -> `0.0`
- `solve_euclidean_distance(-2, -3, 1, 1)` -> `5.0`
- `solve_euclidean_distance(0, 0, 1, 1)` -> `1.4142`

Hints:
- Squaring `dx` and `dy` automatically turns negative differences positive,
  so the order `(x2 - x1)` vs `(x1 - x2)` gives the exact same result!
- Completing this activity unlocks **Checkpoint 01**!
"""

from __future__ import annotations


def example_hypotenuse(side_a: float, side_b: float) -> float:
    """Return the hypotenuse of a right triangle, rounded to 4 decimal places."""
    # Raise the sum of squares to 0.5 to compute the square root.
    hypotenuse = (side_a**2 + side_b**2) ** 0.5
    return round(hypotenuse, 4)


def solve_euclidean_distance(
    x1: float, y1: float, x2: float, y2: float
) -> float:
    """Return the 2D Euclidean distance between (x1, y1) and (x2, y2), rounded to 4 decimals."""
    pass


if __name__ == "__main__":
    print("3-4-? triangle:", example_hypotenuse(3, 4))
    print("1-1-? triangle:", example_hypotenuse(1, 1))
