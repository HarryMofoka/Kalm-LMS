"""
Activity 020: Triangle Geometry Rules
Difficulty: 20 / 132 (Rank 3 - Logic Architect)

Context:
3D graphics engines represent almost every surface — from video-game mountains
to Pixar characters — as meshes of triangles. Before rendering or computing
surface normals, geometry validators filter out degenerate or impossible
triangles using the Triangle Inequality Theorem.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_is_valid_triangle(a, b, c)` returning `True` if side lengths
`a`, `b`, and `c` can form a valid non-degenerate triangle, and `False`
otherwise.

Triangle Inequality Rules:
1. Every side length must be strictly positive: `a > 0 and b > 0 and c > 0`.
2. The sum of EVERY pair of sides must be **strictly greater** than the third:
       `a + b > c` AND `a + c > b` AND `b + c > a`

Step-by-step walkthrough:
1. Guard against zero or negative sides first (`if a <= 0 or b <= 0 or c <= 0: return False`).
2. Check all three strict inequalities. Why strict `>` instead of `>=`?
   With sides `(1, 2, 3)`, the two short sides lie flat on top of the long side
   forming a flat line segment with area 0 — that's a *degenerate* triangle,
   not a valid triangle!

Edge cases:
- `(3, 4, 5)` -> `True`.
- `(1, 2, 3)` -> `False` (degenerate: `1 + 2 == 3`, NOT `> 3`).
- `(-3, 4, 5)` -> `False` (negative side).
- `(0, 5, 5)` -> `False` (zero side).

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Write `solve_classify_triangle(a, b, c)` that classifies a triangle into one
of four exact lowercase strings:
- `"invalid"`     — if `(a, b, c)` cannot form a valid non-degenerate triangle
- `"equilateral"` — all 3 sides are equal (`a == b == c`)
- `"isosceles"`   — exactly 2 sides are equal (`a == b or b == c or a == c`,
                    after already checking equilateral!)
- `"scalene"`     — all 3 sides are different

Rules:
- ALWAYS check validity FIRST! For example, `(0, 0, 0)` has `a == b == c`,
  and `(5, 5, 12)` has `a == b`, yet BOTH are `"invalid"`!
- Return exact lowercase strings: `"invalid"`, `"equilateral"`, `"isosceles"`,
  or `"scalene"`.

Examples:
- `solve_classify_triangle(5, 5, 5)` -> `"equilateral"`
- `solve_classify_triangle(5, 5, 8)` -> `"isosceles"`
- `solve_classify_triangle(3, 4, 5)` -> `"scalene"`
- `solve_classify_triangle(1, 2, 3)` -> `"invalid"`
- `solve_classify_triangle(0, 0, 0)` -> `"invalid"`
- `solve_classify_triangle(5, 5, 12)` -> `"invalid"`

Hints:
- Check the triangle inequality (and `> 0` sides) in a guard clause at the top.
- Check `"equilateral"` BEFORE `"isosceles"` because every equilateral triangle
  also satisfies `a == b`!
"""

from __future__ import annotations


def example_is_valid_triangle(a: float, b: float, c: float) -> bool:
    """Return True if positive sides (a, b, c) satisfy strict triangle inequality."""
    # Guard clause: lengths must all be strictly positive.
    if a <= 0 or b <= 0 or c <= 0:
        return False
    return (a + b > c) and (a + c > b) and (b + c > a)


def solve_classify_triangle(a: float, b: float, c: float) -> str:
    """Classify (a, b, c) as 'invalid', 'equilateral', 'isosceles', or 'scalene'."""
    pass


if __name__ == "__main__":
    print("(3, 4, 5) valid?", example_is_valid_triangle(3, 4, 5))
    print("(1, 2, 3) valid?", example_is_valid_triangle(1, 2, 3))
    print("(-1, 2, 2) valid?", example_is_valid_triangle(-1, 2, 2))
