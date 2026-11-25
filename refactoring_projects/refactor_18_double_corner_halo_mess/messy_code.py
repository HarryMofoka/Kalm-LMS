"""Legacy warehouse drone patrol module — relies on a 'not in path' hack and breaks on thin shapes.

TODO (Mission 18):
- Remove the O(n^2) `if ... not in path` deduplication band-aid.
- Guard empty/non-positive dimensions (`width <= 0 or height <= 0 -> []`).
- Guard thin shapes (`height == 1`, `width == 1`, `1x1`) with clean leg bounds.
- Extract a pure `is_border(row, col, width, height)` helper.
"""


def patrol_rectangle_path(width, height):
    """Return clockwise outer perimeter (row, col) coordinates for a width x height grid."""
    path = []

    # SMELL: sloppy inclusive loops patched with `not in path` band-aids,
    # missing empty-dimension guards, and broken on thin (height == 1 or width == 1) grids!
    for c in range(width):
        if (0, c) not in path:
            path.append((0, c))

    for r in range(height):
        if (r, width - 1) not in path:
            path.append((r, width - 1))

    # Walks backwards across row 0 when height == 1!
    for c in range(width - 2, -1, -1):
        path.append((height - 1, c))

    # Walks backwards up col 0 when width == 1!
    for r in range(height - 2, 0, -1):
        path.append((r, 0))

    return path


def patrol_position(width, height, step):
    """Return the drone's (row, col) coordinate after `step` moves around the perimeter."""
    path = patrol_rectangle_path(width, height)
    if not path:
        return None
    return path[step % len(path)]
