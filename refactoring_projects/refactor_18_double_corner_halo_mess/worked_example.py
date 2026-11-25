"""Worked Example (RF 18): Double-counted square corners -> clean half-open legs.

Compare `before_walk_square` (naive inclusive loops that hit every corner twice)
with `after_walk_square` (clean half-open legs + guards for size <= 1).
"""


def before_walk_square(size):
    """Buggy version: inclusive ranges double-count every corner!"""
    if size <= 0:
        return []
    path = []
    for c in range(size):
        path.append((0, c))
    for r in range(size):
        path.append((r, size - 1))
    for c in range(size - 1, -1, -1):
        path.append((size - 1, c))
    for r in range(size - 1, -1, -1):
        path.append((r, 0))
    return path


def after_walk_square(size):
    """Clean version: each corner belongs to exactly one half-open leg."""
    if size <= 0:
        return []
    if size == 1:
        return [(0, 0)]

    path = []
    # Top edge: [0 .. size-2]
    for c in range(size - 1):
        path.append((0, c))
    # Right edge: [0 .. size-2]
    for r in range(size - 1):
        path.append((r, size - 1))
    # Bottom edge: [size-1 .. 1]
    for c in range(size - 1, 0, -1):
        path.append((size - 1, c))
    # Left edge: [size-1 .. 1]
    for r in range(size - 1, 0, -1):
        path.append((r, 0))
    return path


if __name__ == "__main__":
    print("3x3 before (double corners):", before_walk_square(3))
    print("  length:", len(before_walk_square(3)))
    print("3x3 after  (clean legs):    ", after_walk_square(3))
    print("  length:", len(after_walk_square(3)))
    print("1x1 after  (thin guard):    ", after_walk_square(1))
