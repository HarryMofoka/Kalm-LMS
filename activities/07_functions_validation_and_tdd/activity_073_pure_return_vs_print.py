"""
Activity 073 — Pure Return vs Printing
Difficulty: 73 / 132

Context:
    You are building a terminal display engine for a retro arcade scoreboard.
    Automated test suites cannot inspect pixels on a screen easily, and calling
    `print()` directly inside formatting logic couples display to calculation.
    The golden rule of testable Python: build and RETURN the data in a pure
    function, then keep `print()` in a thin outer wrapper!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Write `example_format_row(cells)` that takes a list of single-cell strings
    and returns them joined by a single space with NO trailing space.
    Then show a tiny wrapper `print_rows(rows)` that prints formatted rows.

Step-by-Step Explanation:
    1. A naive loop might print each cell with `end=" "`, which leaves an
       unwanted trailing space AND returns `None` instead of a string.
    2. `" ".join(cells)` places exactly one space *between* adjacent cells:
       - `["#", " ", "#"]` -> `"#   #"`
       - `["X"]` -> `"X"` (zero spaces added!)
       - `[]` -> `""`
    3. Because `example_format_row` is *pure* (no `print`, no input mutation),
       unit tests can assert `example_format_row(["#", " ", "#"]) == "#   #"`
       directly.

Edge Cases:
    - Empty list `[]` -> `""`
    - Single element `["@"]` -> `"@"`
    - Cells that are spaces `[" ", " "]` -> `"   "` (preserved faithfully!)

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_build_banner_lines(title, border_char="=")` as a PURE
    function that returns a list of 3 strings forming a framed banner — WITHOUT
    calling `print()`.

Rules:
    1. Middle line: `f"{border_char} {title} {border_char}"`
    2. Top and bottom lines: `border_char` repeated to match the exact length
       of the middle line (`len(title) + 4`).
    3. Return `[top_line, middle_line, bottom_line]`.
    4. Do NOT print anything; return the list of 3 strings.

Examples:
    solve_build_banner_lines("GAME OVER") ->
        [
            "=============",
            "= GAME OVER =",
            "=============",
        ]

    solve_build_banner_lines("HI", "*") ->
        [
            "******",
            "* HI *",
            "******",
        ]

    solve_build_banner_lines("") ->
        [
            "====",
            "=  =",
            "====",
        ]

Edge-Case Hints:
    - An empty title still has 2 border characters + 2 padding spaces = length 4.
    - Every returned line must have the exact same length (assuming a 1-char
      `border_char`).
"""

from __future__ import annotations


def example_format_row(cells: list[str]) -> str:
    """Return cells joined by exactly one space, with no trailing spaces."""
    # `" ".join(...)` inserts spaces strictly between elements, never at ends.
    return " ".join(cells)


def print_grid_rows(grid: list[list[str]]) -> None:
    """Thin I/O wrapper demonstrating how printing stays outside pure logic."""
    for row in grid:
        print(example_format_row(row))


def solve_build_banner_lines(title: str, border_char: str = "=") -> list[str]:
    """Return a 3-line framed banner as a list of strings (pure, no printing).

    Args:
        title: Text displayed inside the banner.
        border_char: Single-character border symbol (default ``"="``).

    Returns:
        A 3-element list ``[top_border, middle_line, bottom_border]``.
    """
    pass


if __name__ == "__main__":
    sample_grid = [
        ["#", "#", "#"],
        ["#", " ", "#"],
        ["#", "#", "#"],
    ]
    print("Pure formatted row:", repr(example_format_row(["#", " ", "#"])))
    print("Printed via wrapper:")
    print_grid_rows(sample_grid)
