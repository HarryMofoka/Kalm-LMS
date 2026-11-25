# Refactor 02 — Time Converter Spaghetti (Checkpoint 02)

> **Mission:** Untangle a flight-schedule formatter full of repeated `60` / `1440` / `24` arithmetic and six copies of manual `"0" + str(...)` zero-padding.

## Backstory & Problem Statement

SkyHop Airlines built an internal boarding-pass display string using `format_flight_schedule(dep_h, dep_m, dur_mins)`. It works — even for red-eye flights that land two days later!

Unfortunately, the original author didn't know about named constants, helper functions, or Python's f-string format specifiers (`:02d`). The result is 45 lines of copy-pasted division/modulo formulas (`* 60`, `// 1440`, `% 60`) and a wall of `if x < 10: s = "0" + str(x)` blocks.

Your mission is to clean up `messy_code.py` so the math is computed once, constants are named, formatting uses clean Python tools, and reusable logic lives in helper function(s).

## Code Smells Checklist

Look for these classic Checkpoint 02 smells inside `messy_code.py`:

- [ ] **Hardcoded time magic numbers** (`60`, `1440`, `24`) scattered throughout expressions instead of named `UPPER_CASE` constants (`MINUTES_PER_HOUR`, `HOURS_PER_DAY`, `MINUTES_PER_DAY`).
- [ ] **Repeated conversion arithmetic** recalculating `dep_h * 60 + dep_m + dur_mins` multiple times instead of computing once or delegating to a helper.
- [ ] **Manual zero-padding boilerplate** (`if dep_h < 10: s1 = "0" + str(dep_h)`) copy-pasted six times instead of using clean f-strings like `f"{hours:02d}:{minutes:02d}"`.
- [ ] **No helper functions** for reusable time conversion or clock formatting.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to see a sibling multi-leg hiking distance formatter refactored from spaghetti into clean helpers:

**Before (`before_convert`)**:
```python
def before_convert(meters_leg_a, meters_leg_b):
    a_km = meters_leg_a // 1000
    a_m = meters_leg_a % 1000
    if a_m < 10:
        a_m_str = "00" + str(a_m)
    elif a_m < 100:
        a_m_str = "0" + str(a_m)
    else:
        a_m_str = str(a_m)
    # ... repeated twice more for Leg B and Total!
```

**After (`after_convert_distance`)**:
```python
METERS_PER_KM = 1000


def format_distance(total_meters):
    """Format a distance in meters as '<km> km <mmm> m'."""
    kilometers = total_meters // METERS_PER_KM
    remaining_meters = total_meters % METERS_PER_KM
    return f"{kilometers} km {remaining_meters:03d} m"


def after_convert_distance(meters_leg_a, meters_leg_b):
    total_meters = meters_leg_a + meters_leg_b
    return (
        f"Leg A: {format_distance(meters_leg_a)} | "
        f"Leg B: {format_distance(meters_leg_b)} | "
        f"Total: {format_distance(total_meters)}"
    )
```

One tiny helper + one named constant + `:03d` formatting wiped out 30 lines of fragile duplication!

## Your Refactoring Mission

Edit `messy_code.py` while respecting these rules:

1. **Preserve the exact function signature:**
   `format_flight_schedule(dep_h, dep_m, dur_mins)`
   (Keep the same function name and 3 positional parameters.)
2. **Define named `UPPER_CASE` time constants** at module level (such as `MINUTES_PER_HOUR = 60`, `HOURS_PER_DAY = 24`, `MINUTES_PER_DAY = HOURS_PER_DAY * MINUTES_PER_HOUR` or `1440`) and remove raw `60`, `24`, and `1440` literals from function bodies.
3. **Extract at least one helper function** (for example `format_clock(hours, minutes)`, `format_duration(total_minutes)`, or `split_minutes(total_minutes)`) and call it from `format_flight_schedule`.
4. **Replace manual zero-padding** (`"0" + str(...)` and repetitive `< 10` `if` checks) with clean f-string formatting (like `f"{hours:02d}:{minutes:02d}"`).
5. **Keep `TestBehaviorSafetyNet` green** at all times!

## Running the Tests

From inside the `ExamPrep/` folder:

```bash
python -m unittest refactoring_projects.refactor_02_time_converter_spaghetti.test_refactor -v
```

Or run directly from this folder:

```bash
python test_refactor.py
```

Goal: turn `TestRefactorGoals` from **RED** to **GREEN** while keeping `TestWorkedExample` and `TestBehaviorSafetyNet` **GREEN**!
