"""Messy warehouse grid builder — rescue this file!

It passes TestBehaviorSafetyNet on untouched grids and single-row maps,
BUT `create_empty_grid` suffers from the classic `[[fill] * cols] * rows`
aliasing disaster, and the grid helpers use cryptic single-letter indexing!
"""


def create_empty_grid(rows, cols, fill="."):
    """Create a rows x cols 2D grid filled with `fill`."""
    # Classic Python aliasing trap! Every row references the SAME list object.
    return [[fill] * cols] * rows


def place_crate(grid, r, c, symbol="C"):
    """Place `symbol` at (r, c) if inside grid bounds; return True if placed."""
    if len(grid) == 0:
        return False
    if r >= 0 and r < len(grid):
        if c >= 0 and c < len(grid[0]):
            grid[r][c] = symbol
            return True
    return False


def render_grid(grid):
    """Render a 2D grid as lines of space-separated cell symbols."""
    out = ""
    i = 0
    while i < len(grid):
        line = ""
        j = 0
        while j < len(grid[i]):
            line = line + grid[i][j] + " "
            j = j + 1
        if len(line) > 0:
            line = line[:-1]
        out = out + line + "\n"
        i = i + 1
    if len(out) > 0:
        out = out[:-1]
    return out


def build_warehouse_map(rows, cols, crates):
    """Build a rows x cols grid and place `'C'` at each valid `(row, col)` in `crates`."""
    g = create_empty_grid(rows, cols, ".")
    k = 0
    m = len(crates)
    while k < m:
        x = crates[k][0]
        y = crates[k][1]
        place_crate(g, x, y, "C")
        k = k + 1
    return g
