# Refactor 05 — Copy-Paste Loops (Checkpoint 05)

> **Mission:** Eliminate three copy-pasted identical `for` loops inside `summarize_workout_week` by extracting one clean **DRY (Don't Repeat Yourself)** helper function!

## Backstory & Problem Statement

FitTrack's weekly workout dashboard summarizes daily push-up reps across three sessions: **morning**, **afternoon**, and **evening**. For each session, it computes:
- `"total"` — total reps done across the week
- `"best"` — highest single-day rep count (`0` if the list is empty)
- `"active_days"` — number of days with strictly more than `0` reps

Instead of writing one reusable function, the previous intern copy-pasted the exact same 12-line loop **three times**, renaming `m_` to `a_` and `e_`. Tomorrow, product wants to add a `"late_night"` session and a new `"average"` stat — which currently means editing the same bug-prone logic in three (or four!) separate places.

Your mission is to apply the **DRY principle**: extract a single session-summarizing helper function and make `summarize_workout_week` delegate to it!

## Code Smells Checklist

Look for these classic Checkpoint 05 smells inside `messy_code.py`:

- [ ] **Copy-pasted loop logic** duplicated three times with only variable prefixes (`m_`, `a_`, `e_`) changed.
- [ ] **Shotgun surgery risk:** Changing how `"active_days"` or `"best"` is computed requires updating three separate blocks identically.
- [ ] **Bloated main function:** `summarize_workout_week` is 45+ lines long when its actual job is simply combining three session summaries.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to see a sibling 3-team tournament score summarizer refactored from three copy-pasted loops to one clean helper:

**Before (`before_team_stats`):**
```python
def before_team_stats(alpha_scores, beta_scores, gamma_scores):
    a_total = 0
    a_count = 0
    a_highest = 0
    for score in alpha_scores:
        a_total += score
        a_count += 1
        if score > a_highest:
            a_highest = score
    a_avg = round(a_total / a_count, 2) if a_count > 0 else 0.0
    # ... exact same 9 lines copy-pasted for beta_scores ...
    # ... exact same 9 lines copy-pasted for gamma_scores ...
```

**After (`after_team_stats`):**
```python
def compute_group_stats(scores):
    """Return count, rounded average, and highest score for one team."""
    if not scores:
        return {"count": 0, "average": 0.0, "highest": 0}
    total = 0
    highest = scores[0]
    for score in scores:
        total += score
        if score > highest:
            highest = score
    return {
        "count": len(scores),
        "average": round(total / len(scores), 2),
        "highest": highest,
    }


def after_team_stats(alpha_scores, beta_scores, gamma_scores):
    """Summarize tournament statistics for all three teams."""
    return {
        "alpha": compute_group_stats(alpha_scores),
        "beta": compute_group_stats(beta_scores),
        "gamma": compute_group_stats(gamma_scores),
    }
```

One bug fix in `compute_group_stats` now fixes all three teams automatically!

## Your Refactoring Mission

Edit `messy_code.py` while respecting these rules:

1. **Preserve the exact function signature:**
   `summarize_workout_week(morning_reps, afternoon_reps, evening_reps)`
2. **Extract a reusable helper function** (e.g. `summarize_session(reps)`) that computes `{"total": ..., "best": ..., "active_days": ...}` for any single list of daily reps, and call it from `summarize_workout_week`.
3. **Reduce loops in `summarize_workout_week` to at most 1** (down from 3 duplicated loops — ideally 0 loops inside `summarize_workout_week`, or 1 loop iterating over the 3 sessions!).
4. **Slim down `summarize_workout_week`** so it clearly reads as high-level orchestration rather than 45 lines of repetition.
5. **Keep `TestBehaviorSafetyNet` green** on every edge case (empty lists, all-zero rest weeks, single-day lists, huge rep counts)!

## Running the Tests

From inside the `ExamPrep/` folder:

```bash
python -m unittest refactoring_projects.refactor_05_copy_paste_loops.test_refactor -v
```

Or run directly from this folder:

```bash
python test_refactor.py
```

Goal: turn `TestRefactorGoals` from **RED** to **GREEN** while keeping `TestWorkedExample` and `TestBehaviorSafetyNet` **GREEN**!
