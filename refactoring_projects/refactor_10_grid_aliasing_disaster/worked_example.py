"""Worked Example for RF 10: 2D Board Initializer (row aliasing -> independent rows)."""


def before_make_board(rows, cols, fill="."):
    """Messy version: classic aliasing trap where every row is the SAME list object."""
    return [[fill] * cols] * rows


def after_make_board(rows, cols, fill="."):
    """Clean version: builds a brand-new list for every single row."""
    return [[fill for _ in range(cols)] for _ in range(rows)]


if __name__ == "__main__":
    buggy = before_make_board(3, 4)
    buggy[0][0] = "X"
    print("=== Before (all rows contaminated!) ===")
    for row in buggy:
        print(" ".join(row))

    fixed = after_make_board(3, 4)
    fixed[0][0] = "X"
    print("=== After (only row 0 updated!) ===")
    for row in fixed:
        print(" ".join(row))
