"""
Activity 002: Basic Arithmetic & Geometry Formulas
Difficulty: 2 / 132 (Rank 1 - Absolute Beginner)

Context:
Architects, game physics engines, and landscape designers constantly compute
lengths and areas from raw dimensions. Python makes math formulas read almost
like textbook algebra — as long as you pay attention to operator precedence
(parentheses first, then `*` and `/`, then `+` and `-`)!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_rectangle_metrics(width, height)` that computes both the
perimeter and area of a rectangle and returns them as a tuple:
    `(perimeter, area)`

Step-by-step walkthrough:
1. Perimeter of a rectangle is twice the sum of its width and height:
       `perimeter = 2 * (width + height)`
   Notice the parentheses! Without them, `2 * width + height` would multiply
   only `width` by 2, producing the wrong answer.
2. Area of a rectangle is width times height:
       `area = width * height`
3. Return both values packaged together in a tuple: `(perimeter, area)`.

Edge cases:
- Floats (like `2.5` and `4.0`) work identically to integers.
- A zero dimension (like `0` and `5`) yields perimeter `10` and area `0`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A rooftop solar contractor needs quick area calculations for triangular and
trapezoidal panels. Write `solve_trapezoid_and_triangle(base_a, base_b, height)`
that returns a 2-tuple `(triangle_area, trapezoid_area)`:
- `triangle_area`: area of a triangle with base `base_a` and height `height`:
      `0.5 * base_a * height`
- `trapezoid_area`: area of a trapezoid with parallel bases `base_a`, `base_b`
  and height `height`:
      `0.5 * (base_a + base_b) * height`

Rules:
- Return `(triangle_area, trapezoid_area)` as floats (using `0.5 * ...` or
  `/ 2` automatically gives floats in Python 3).
- Do not round the results.

Examples:
- `solve_trapezoid_and_triangle(10, 6, 4)` -> `(20.0, 32.0)`
- `solve_trapezoid_and_triangle(5, 5, 3)` -> `(7.5, 15.0)`
- `solve_trapezoid_and_triangle(7.5, 2.5, 4.0)` -> `(15.0, 20.0)`

Hints:
- Don't forget parentheses around `(base_a + base_b)` in the trapezoid formula!
- Order matters in the returned tuple: triangle first, trapezoid second.
"""

from __future__ import annotations


def example_rectangle_metrics(width: float, height: float) -> tuple[float, float]:
    """Return (perimeter, area) for a rectangle with the given width and height."""
    # Parentheses ensure width + height happens before multiplying by 2.
    perimeter = 2 * (width + height)
    area = width * height
    return (perimeter, area)


def solve_trapezoid_and_triangle(
    base_a: float, base_b: float, height: float
) -> tuple[float, float]:
    """Return (triangle_area, trapezoid_area) using base_a, base_b, and height."""
    pass


if __name__ == "__main__":
    print("4 x 7 rectangle:", example_rectangle_metrics(4, 7))
    print("2.5 x 3.5 rectangle:", example_rectangle_metrics(2.5, 3.5))
