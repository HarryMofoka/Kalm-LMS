# Refactoring Mission 06 — `while` Loop Traps (CP 06)

## Backstory & Problem Statement

A junior engineer ported a greenhouse temperature analyzer from C to Python. It works and passes its behavioral tests, **but** every single loop in `messy_code.py` is a manual-index `while` loop (`i = 0; while i < len(readings): ... i = i + 1`).

Manual-index `while` loops are notorious bug magnets in Python: one misplaced `i += 1`, one wrong starting index, or an early `continue` can cause an **infinite loop** or an **off-by-one `IndexError`**.

Your mission: rescue `analyze_temperature_readings` by replacing all clunky manual-index `while` loops with clean, Pythonic `for` loops and `enumerate()`.

## Code Smells Checklist

- [ ] **Manual loop counters (`i = 0`, `j = 0`, `k = 1`)** incremented by hand with `i = i + 1`.
- [ ] **Index gymnastics (`readings[i]`, `readings[j]`, `readings[k] - readings[k - 1]`)** where direct iteration, `enumerate()`, or paired iteration (`zip` / `range`) is cleaner and safer.
- [ ] **Repeated `len(readings)` boilerplate** scattered across three separate `while` blocks.
- [ ] **Risk of infinite loops** if any branch forgets to increment the counter.

## Worked Refactoring Walkthrough (Before -> After)

Open [`worked_example.py`](worked_example.py) to compare a sensor spike finder before and after refactoring:

### Before (`before_find_spikes`)
```python
def before_find_spikes(readings, threshold):
    spikes = []
    i = 0
    while i < len(readings):
        val = readings[i]
        if val > threshold:
            spikes.append((i, val))
        i = i + 1
    return spikes
```

### After (`after_find_spikes`)
```python
def after_find_spikes(readings, threshold):
    spikes = []
    for index, value in enumerate(readings):
        if value > threshold:
            spikes.append((index, value))
    return spikes
```

Notice how `enumerate(readings)` hands us `(index, value)` automatically — no manual `i = 0`, no `i < len(readings)`, and no chance of forgetting `i = i + 1`!

## Your Refactoring Mission

Refactor [`messy_code.py`](messy_code.py) so that `analyze_temperature_readings(readings, high_threshold)`:

1. **Eliminates all `while` loops** (zero `while` loops anywhere in `messy_code.py`).
2. **Uses Pythonic `for` loops** to compute totals, extremes, high-temperature indices, and consecutive deltas.
3. **Uses `enumerate()`** to track the indices of readings at or above `high_threshold`.
4. **Preserves 100% identical behavior** (all `TestBehaviorSafetyNet` tests remain GREEN!).

> **Tip:** For consecutive differences (`deltas`), try iterating over pairs with `zip(readings, readings[1:])` or `for i in range(1, len(readings)):`!

## Run the Tests

Run from the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_06_while_loop_traps/test_refactor.py -v
```

Watch `TestWorkedExample` and `TestBehaviorSafetyNet` stay GREEN while you turn `TestRefactorGoals` from RED to GREEN!
