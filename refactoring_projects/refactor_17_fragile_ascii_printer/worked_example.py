"""Worked Example (RF 17): Trailing-space print loops -> format_row & pure builder.

Demonstrates why `print(..., end=" ")` leaks trailing spaces on every row and
how `format_row` + a pure `after_build_box` eliminates both bugs and coupling.
"""

import io
from contextlib import redirect_stdout


def before_print_box(size):
    """Messy version: mixes logic with print() and leaves trailing spaces."""
    if size <= 0:
        return
    for r in range(size):
        for c in range(size):
            if r == 0 or r == size - 1 or c == 0 or c == size - 1:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()


def format_row(cells):
    """Join grid cells with a single space and zero trailing whitespace."""
    return " ".join(cells)


def after_build_box(size):
    """Pure builder returning a list of formatted lines without printing."""
    if size <= 0:
        return []
    lines = []
    for r in range(size):
        cells = [
            "*" if (r == 0 or r == size - 1 or c == 0 or c == size - 1) else "."
            for c in range(size)
        ]
        lines.append(format_row(cells))
    return lines


def after_print_box(size):
    """Thin I/O wrapper that prints the lines built by `after_build_box`."""
    for line in after_build_box(size):
        print(line)


if __name__ == "__main__":
    buf_before = io.StringIO()
    with redirect_stdout(buf_before):
        before_print_box(4)

    buf_after = io.StringIO()
    with redirect_stdout(buf_after):
        after_print_box(4)

    print("Before (notice trailing spaces in repr!):")
    for line in buf_before.getvalue().splitlines():
        print(" ", repr(line))

    print("\nAfter (clean, exact lines):")
    for line in buf_after.getvalue().splitlines():
        print(" ", repr(line))
