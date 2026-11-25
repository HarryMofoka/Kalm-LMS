# Refactor 04 — Boolean Soup (Checkpoint 04)

> **Mission:** Clean up a rocket-launch safety check drowning in `== True`, `== False`, pointless boolean flag variables, and `if ready_flag == True: return True else: return False`.

## Backstory & Problem Statement

OrbitalGo's mission-control checklist uses `can_launch_rocket(fuel_pct, weather_clear, crew_ready, override_code)` right before ignition.

The launch rules themselves are wonderfully simple:
1. Fuel must be at least **80%** (`fuel_pct >= 80`).
2. The crew must be ready (`crew_ready`).
3. Either the weather is clear (`weather_clear`) **or** Mission Control supplies the emergency override code `"ALPHA-9"`.

Sadly, whoever wrote `messy_code.py` didn't trust Python's booleans to stay boolean unless they were checked three times with `== True`, copied into three temporary flags (`fuel_ok`, `override_valid`, `ready_flag`), and finally passed through `if ready_flag == True: return True else: return False`.

Your mission is to turn 28 lines of boolean soup into crisp, direct boolean logic!

## Code Smells Checklist

Look for these classic Checkpoint 04 smells inside `messy_code.py`:

- [ ] **Explicit comparisons to `True` / `False`** (`if fuel_ok == True:`, `elif weather_clear == False:`).
- [ ] **Redundant `if cond: flag = True else: flag = False`** when `flag = cond` already produces a boolean!
- [ ] **Redundant `if ready_flag == True: return True else: return False`** when `return ready_flag` (or directly returning the boolean expression!) does the exact same thing.
- [ ] **Nested `if` statements replacing `and` / `or`** boolean operators.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to see a building security access check cleaned up:

**Before (`before_has_access`):**
```python
def before_has_access(is_admin, is_active, has_badge, is_locked_out):
    allowed = False
    if is_active == True:
        if is_locked_out == False:
            if is_admin == True:
                allowed = True
            else:
                if has_badge == True:
                    allowed = True
                else:
                    allowed = False
        else:
            allowed = False
    else:
        allowed = False

    if allowed == True:
        return True
    else:
        return False
```

**After (`after_has_access`):**
```python
def after_has_access(is_admin, is_active, has_badge, is_locked_out):
    """Return True if an active, unlocked user is an admin or holds a badge."""
    account_in_good_standing = is_active and not is_locked_out
    has_credentials = is_admin or has_badge
    return account_in_good_standing and has_credentials
```

Notice how readable that is — no `== True`, no `== False`, no temporary `allowed` flag, and zero `if ...: return True else: return False`!

## Your Refactoring Mission

Edit `messy_code.py` while respecting these rules:

1. **Preserve the exact function signature:**
   `can_launch_rocket(fuel_pct, weather_clear, crew_ready, override_code)`
2. **Eliminate all comparisons to `True` or `False`** (`== True`, `== False`, `!= True`, `is True`, `is False`).
3. **Eliminate redundant boolean `if/else` patterns** (`if cond: return True else: return False` and `if cond: flag = True`).
4. **Use direct boolean expressions** with `and` / `or` (you may name helper boolean variables like `has_enough_fuel = fuel_pct >= 80` for clarity!).
5. **Keep `TestBehaviorSafetyNet` green** across every single launch scenario!

## Running the Tests

From inside the `ExamPrep/` folder:

```bash
python -m unittest refactoring_projects.refactor_04_boolean_soup.test_refactor -v
```

Or run directly from this folder:

```bash
python test_refactor.py
```

Goal: turn `TestRefactorGoals` from **RED** to **GREEN** while keeping `TestWorkedExample` and `TestBehaviorSafetyNet` **GREEN**!
