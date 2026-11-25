"""
Activity 128: Building a Reusable GridCanvas Class
Difficulty: 128 / 132

Remember rebuilding `grid = [[" "] * width for _ in range(height)]` and formatting
every row by hand across Module 10?
Now encapsulate that ENTIRE grid buffer cleanly into a reusable class!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleBoard
===============================================================================
Problem:
    Build `ExampleBoard(size, fill=".")` representing a `size x size` square
    game board with:
      - `place(row, col, symbol)`: validates bounds (raises `ValueError` out of
        bounds) and writes `symbol`.
      - `get(row, col) -> str`: validates bounds and returns the cell value.
      - `render() -> str`: joins each row with single spaces, strips trailing
        spaces, and joins rows with `"\n"`.

Step-by-Step Breakdown:
    1. Keep a private helper `_check_bounds(row, col)` so both `place` and `get`
       share identical validation without copy-pasting.
    2. Build rows with `[fill] * size` inside a list comprehension — NEVER use
       `[[fill] * size] * size`, which aliases every row to the same list!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — GridCanvas(width, height)
===============================================================================
Problem:
    Implement `GridCanvas` for drawing halo patterns, runners, and ASCII art:
      - `__init__(self, width: int, height: int, fill: str = " ") -> None`
        * Raises `ValueError` if `width <= 0` or `height <= 0`.
        * Stores `self.width = width`, `self.height = height`, and initializes
          a `height x width` 2D grid filled with `fill`.
      - `set_cell(self, row: int, col: int, char: str) -> None`
        * Raises `ValueError` if `not (0 <= row < self.height and 0 <= col < self.width)`.
        * Sets cell `(row, col)` to `char`.
      - `get_cell(self, row: int, col: int) -> str`
        * Raises `ValueError` if out of bounds; otherwise returns cell `(row, col)`.
      - `draw_border(self, char: str = "#") -> None`
        * Paints EVERY border cell of the `width x height` canvas with `char`
          (handles thin `4x1`, `1x3`, `1x1` canvases cleanly!).
      - `render(self) -> str`
        * Formats each row with `" ".join(cells).rstrip(" ")` and joins all
          rows with `"\n"`. ZERO trailing spaces on every line!

    Examples:
        canvas = GridCanvas(5, 3)
        canvas.draw_border("#")
        canvas.set_cell(1, 2, "@")
        canvas.render() ->
            "# # # # #\n"
            "#   @   #\n"
            "# # # # #"

        thin = GridCanvas(4, 1)
        thin.draw_border("*")
        thin.render() -> "* * * *"

    Edge-case hints:
        - Remember: `width` is number of COLUMNS, `height` is number of ROWS!
        - `set_cell(row, col, char)` takes `(row, col)` — check `0 <= row < self.height`
          and `0 <= col < self.width`.
        - Never alias rows (`[[fill] * width] * height` is a classic bug!).
"""
from __future__ import annotations


class ExampleBoard:
    """A reusable square game board with bounds-checked placement and rendering."""

    def __init__(self, size: int, fill: str = ".") -> None:
        if size <= 0:
            raise ValueError("size must be positive")
        self.size = size
        self._grid: list[list[str]] = [[fill] * size for _ in range(size)]

    def _check_bounds(self, row: int, col: int) -> None:
        if not (0 <= row < self.size and 0 <= col < self.size):
            raise ValueError(f"({row}, {col}) is outside {self.size}x{self.size} board")

    def place(self, row: int, col: int, symbol: str) -> None:
        """Write `symbol` at (row, col), raising ValueError if out of bounds."""
        self._check_bounds(row, col)
        self._grid[row][col] = symbol

    def get(self, row: int, col: int) -> str:
        """Return symbol at (row, col), raising ValueError if out of bounds."""
        self._check_bounds(row, col)
        return self._grid[row][col]

    def render(self) -> str:
        """Render the board with one space between cells and zero trailing spaces."""
        return "\n".join(" ".join(row).rstrip(" ") for row in self._grid)


class GridCanvas:
    """A rectangular 2D character canvas with set_cell, draw_border, and render."""

    def __init__(self, width: int, height: int, fill: str = " ") -> None:
        """Initialize a width x height canvas filled with `fill`."""
        pass

    def set_cell(self, row: int, col: int, char: str) -> None:
        """Set cell (row, col) to `char`, raising ValueError if out of bounds."""
        pass

    def get_cell(self, row: int, col: int) -> str:
        """Return character at (row, col), raising ValueError if out of bounds."""
        pass

    def draw_border(self, char: str = "#") -> None:
        """Draw `char` around all outer border cells of the canvas."""
        pass

    def render(self) -> str:
        """Render canvas to a newline-joined string with zero trailing spaces."""
        pass


if __name__ == "__main__":
    board = ExampleBoard(3)
    board.place(0, 0, "X")
    board.place(1, 1, "O")
    board.place(2, 2, "X")
    print(board.render())
