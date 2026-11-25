# Refactor 13 — Decouple Business Logic from `print()`

## Backstory & Problem Statement

Your school's registrar asked you to reuse the grade-report script written by an intern last semester. You want to:

1. Show the class pass rate on a web dashboard,
2. Export the report lines to a `.txt` file, and
3. Unit-test the statistics without scraping terminal output.

You open `messy_code.py` and discover a nightmare: **every single calculation, pass/fail decision, average formula, and string format is glued directly inside `print(...)` calls** in `print_grade_report(students)`. Calling it dumps text straight to the screen and returns `None`!

## Code Smells Checklist

- [ ] **Print-coupled business logic**: Computing totals, pass counts, averages, and highest scores inline inside `print()` statements.
- [ ] **Zero reusability**: Callers cannot retrieve statistics as data or capture formatted lines without hijacking `sys.stdout`.
- [ ] **Hard to test**: Testing math logic requires capturing terminal output instead of asserting directly on return values.
- [ ] **Mixed responsibilities**: Computation, string formatting, and console I/O all live in one tangled function.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to compare `before_print_summary(sales)` against `after_format_summary(sales)` + `after_print_summary(sales)`:

- **Before (`before_print_summary`)**: Computes `total`, `average`, and `best` while calling `print(...)` six times. You cannot reuse the formatted lines for a file, email, or UI.
- **After (`after_format_summary` + `after_print_summary`)**:
  - `after_format_summary(sales)` is a **pure function** — it touches no I/O, prints nothing, and returns a clean `list[str]` of report lines.
  - `after_print_summary(sales)` is a **thin display wrapper** that calls `after_format_summary(sales)` and prints the joined output in a single `print()` call.

## Your Refactoring Mission

Refactor `messy_code.py` while keeping `print_grade_report(students)` producing the **exact same console output**:

1. Extract a pure function `compute_grade_stats(students)` that prints **nothing** and returns a dictionary with keys:
   - `"count"`: total number of students (`int`)
   - `"passed"`: number of students with `score >= 50` (`int`)
   - `"failed"`: number of students with `score < 50` (`int`)
   - `"average"`: mean score as `float` (`0.0` when `students` is empty)
   - `"highest_name"`: name of the first student with the highest score (`None` when empty)
   - `"highest_score"`: highest score (`None` when empty)
2. Extract a pure function `format_grade_report(students)` that calls `compute_grade_stats(students)`, prints **nothing**, and returns a `list[str]` containing each line of the report.
3. Simplify `print_grade_report(students)` into a thin wrapper that delegates to `format_grade_report(students)` and prints the lines with at most one `print(...)` call.

## Run the Tests

From the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_13_print_coupled_logic/test_refactor.py -v
```

Or run the test file directly:

```bash
python ExamPrep/refactoring_projects/refactor_13_print_coupled_logic/test_refactor.py -v
```

Start by confirming `TestWorkedExample` and `TestBehaviorSafetyNet` are **GREEN** and `TestRefactorGoals` is **RED**, then refactor `messy_code.py` until all three test classes turn **GREEN**!
