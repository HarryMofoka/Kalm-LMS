# Refactoring Mission 18 — Double-Corner Halo Mess (CP 18)

## Backstory & Problem Statement

A warehouse security drone patrols the outer perimeter (halo) of a rectangular storage grid clockwise, starting at `(0, 0)`.

The original programmer wrote `patrol_rectangle_path(width, height)` in `messy_code.py` by copy-pasting four sloppy `for` loops. When they noticed corners appearing twice, instead of fixing their loop bounds, they slapped an `O(n²)` band-aid (`if (r, c) not in path:`) onto the top and right edges and called it a day.

It passed the team's tests on `4×3`, `3×3`, and `5×4` warehouses — until a narrow `4×1` hallway and a `1×3` aisle caused the drone to bounce backwards over duplicate tiles, and a `0×5` empty zone sent it to negative coordinates `(0, -1)`!

Your mission: rip out the `not in path` band-aid, write clean non-overlapping perimeter legs with proper thin-shape & empty-dimension guards, and extract an `is_border` helper!

---

## Code Smells Checklist

- [ ] **Post-hoc `if (r, c) not in path` deduplication band-aid** hiding off-by-one loop bounds (`O(n²)` list membership check!).
- [ ] **Missing empty-dimension guard** (`width <= 0 or height <= 0`) causing negative coordinates like `(0, -1)`.
- [ ] **Broken thin-shape logic** (`height == 1` or `width == 1`) re-walking the same row/column backwards.
- [ ] **No reusable `is_border(row, col, width, height)` helper** to cleanly classify perimeter cells.

---

## Worked Refactoring Walkthrough (`worked_example.py`)

In `worked_example.py`, we compare a buggy square-perimeter walk with clean half-open legs:

### Before (inclusive loops double-count all 4 corners!)
```python
def before_walk_square(size):
    path = []
    for c in range(size):               # top: (0, 0) .. (0, n-1)
        path.append((0, c))
    for r in range(size):               # right: includes (0, n-1) AGAIN!
        path.append((r, size - 1))
    for c in range(size - 1, -1, -1):   # bottom: includes (n-1, n-1) AGAIN!
        path.append((size - 1, c))
    for r in range(size - 1, -1, -1):   # left: includes (n-1, 0) & (0, 0) AGAIN!
        path.append((r, 0))
    return path
```

### After (half-open legs + guards — zero duplicates by construction!)
```python
def after_walk_square(size):
    if size <= 0:
        return []
    if size == 1:
        return [(0, 0)]
    path = []
    for c in range(size - 1):              # top: [0 .. n-2]
        path.append((0, c))
    for r in range(size - 1):              # right: [0 .. n-2]
        path.append((r, size - 1))
    for c in range(size - 1, 0, -1):       # bottom: [n-1 .. 1]
        path.append((size - 1, c))
    for r in range(size - 1, 0, -1):       # left: [n-1 .. 1]
        path.append((r, 0))
    return path
```

For general rectangles `(width, height)`, watch out for thin shapes:
- If `width <= 0 or height <= 0`: return `[]`.
- Top edge: `c` from `0` to `width - 1`.
- Right edge: `r` from `1` to `height - 1`.
- Bottom edge **only if `height > 1`**: `c` from `width - 2` down to `0`.
- Left edge **only if `width > 1`**: `r` from `height - 2` down to `1`.

Trace that on `4×3`, `4×1`, `1×3`, and `1×1` — every cell is visited **exactly once**, in clockwise order, with zero deduplication hacks!

---

## Your Refactoring Mission

Refactor `messy_code.py` so **all three test classes pass**:

1. **`patrol_rectangle_path(width, height)`**:
   - Return clockwise perimeter `(row, col)` coordinates starting at `(0, 0)` with **no duplicate cells**.
   - Handle empty/non-positive dimensions (`width <= 0 or height <= 0`) by returning `[]`.
   - Handle thin shapes cleanly:
     - `(4, 1)` -> `[(0, 0), (0, 1), (0, 2), (0, 3)]` (length `4`)
     - `(1, 3)` -> `[(0, 0), (1, 0), (2, 0)]` (length `3`)
     - `(1, 1)` -> `[(0, 0)]` (length `1`)
   - Must **NOT** use `not in` / `in` membership deduplication band-aids inside `patrol_rectangle_path` — use clean loop bounds and `height > 1` / `width > 1` guards!

2. **`patrol_position(width, height, step)`**:
   - Keep working for normal shapes (and safely return `None` when the patrol path is empty).

3. **`is_border(row, col, width, height)`**:
   - Extract a clean pure helper returning `True` if `(row, col)` is inside the `width × height` grid **and** lies on its outer perimeter (`row == 0 or row == height - 1 or col == 0 or col == width - 1`), otherwise `False`.

---

## Run the Tests

```bash
python -m unittest ExamPrep/refactoring_projects/refactor_18_double_corner_halo_mess/test_refactor.py
```

When you start:
- `TestWorkedExample` -> **PASS**
- `TestBehaviorSafetyNet` -> **PASS** (your safety net!)
- `TestRefactorGoals` -> **FAIL** (your refactoring targets!)

When you finish, **all 3 test classes should be GREEN**!
