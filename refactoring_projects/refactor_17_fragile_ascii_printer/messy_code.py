"""Legacy ASCII badge printer — prints trailing spaces and couples logic to stdout.

TODO (Mission 17):
- Extract `format_row(cells)` returning `" ".join(cells)`.
- Extract pure `build_badge_frame(width, height)` returning `list[str]` without printing.
- Refactor `print_badge_frame(width, height)` to delegate to `build_badge_frame`
  with zero trailing spaces.
"""


def print_badge_frame(width, height):
    """Print a width x height conference badge frame with '#' border and '.' fill."""
    if width <= 0 or height <= 0:
        return

    # SMELL: mixes border math directly with print(..., end=" ") leaving trailing spaces!
    for r in range(height):
        for c in range(width):
            if r == 0:
                print("#", end=" ")
            elif r == height - 1:
                print("#", end=" ")
            elif c == 0:
                print("#", end=" ")
            elif c == width - 1:
                print("#", end=" ")
            else:
                print(".", end=" ")
        print()
