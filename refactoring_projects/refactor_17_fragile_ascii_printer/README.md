# Refactoring Mission 17 — Fragile ASCII Printer (CP 17)

## Backstory & Problem Statement

A conference check-in tool prints ASCII badge frames to thermal receipt printers using `messy_code.py`. To human eyes on a terminal, the output *looks* okay — until automated grading and strict receipt parsers reject every single line because of **invisible trailing spaces** left by `print("#", end=" ")`!

Worse, the border-calculation logic is permanently glued to `print()`, so no other module can inspect, save, or unit-test the badge lines without capturing `stdout`.

Your mission: separate row formatting and frame building into clean pure functions, eliminate every trailing space, and make `print_badge_frame` a thin printing wrapper!

---

## Code Smells Checklist

- [ ] **Trailing-space bug** caused by `print(cell, end=" ")` inside a row loop.
- [ ] **No `format_row(cells)` helper** using `" ".join(cells)` to place spaces strictly *between* tokens.
- [ ] **Border logic coupled directly to `print()`** — impossible to reuse or test without redirecting `stdout`.
- [ ] **Duplicated border-condition checks** scattered across nested printing loops.

---

## Worked Refactoring Walkthrough (`worked_example.py`)

In `worked_example.py`, we refactor a messy hollow-box printer:

### Before (trailing spaces + coupled printing)
```python
def before_print_box(size):
    for r in range(size):
        for c in range(size):
            if r == 0 or r == size - 1 or c == 0 or c == size - 1:
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()
```
Every line silently ends with `" "` (`"* * * "` instead of `"* * *"`).

### After (`format_row` + pure `after_build_box` + thin printer)
```python
def format_row(cells):
    return " ".join(cells)

def after_build_box(size):
    if size <= 0:
        return []
    lines = []
    for r in range(size):
        row = [
            "*" if (r == 0 or r == size - 1 or c == 0 or c == size - 1) else "."
            for c in range(size)
        ]
        lines.append(format_row(row))
    return lines

def after_print_box(size):
    for line in after_build_box(size):
        print(line)
```

---

## Your Refactoring Mission

Refactor `messy_code.py` so **all three test classes pass**:

1. **`format_row(cells)`**:
   - Pure helper that joins a sequence of cell strings with a single space (`" ".join(cells)`), with **zero trailing spaces**.
   - Example: `format_row(["#", ".", "#"]) == "# . #"`, `format_row([]) == ""`.

2. **`build_badge_frame(width, height)`**:
   - Pure function that returns a `list[str]` representing a `width × height` badge frame using `"#"` on the outer border and `"."` inside, formatted with `format_row`.
   - Must **not** print anything!
   - Returns `[]` if `width <= 0` or `height <= 0`.
   - Example for `build_badge_frame(5, 4)`:
     ```python
     [
         "# # # # #",
         "# . . . #",
         "# . . . #",
         "# # # # #",
     ]
     ```

3. **`print_badge_frame(width, height)`**:
   - Keep this public function working! Delegate directly to `build_badge_frame(width, height)` and print each line cleanly with **zero trailing spaces** (no `print(..., end=" ")` loops).

---

## Run the Tests

```bash
python -m unittest ExamPrep/refactoring_projects/refactor_17_fragile_ascii_printer/test_refactor.py
```

When you start:
- `TestWorkedExample` -> **PASS**
- `TestBehaviorSafetyNet` -> **PASS** (your safety net!)
- `TestRefactorGoals` -> **FAIL** (your refactoring targets!)

When you finish, **all 3 test classes should be GREEN**!
