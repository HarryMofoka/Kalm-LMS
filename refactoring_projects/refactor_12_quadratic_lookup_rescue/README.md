# Refactor 12 — Rescue Sluggish `O(n^2)` Scans with `O(n)` Sets & Dicts

## Backstory & Problem Statement

Security Ops relies on `audit_access_logs(allowed_users, seen_users)` to inspect daily badge swipes and report:

1. **`unauthorized`**: users who swiped in but are not on the allowed list,
2. **`duplicates`**: users who swiped in 2 or more times, and
3. **`active_allowed`**: allowed users who actually showed up.

It worked fine during testing with 10 mock employees. The moment it ran on a real building log with thousands of swipes, CPU usage spiked and the audit stalled!

Inspecting `messy_code.py` reveals pure **`O(n^2)` quadratic bottlenecks** everywhere:
- `if user not in allowed_users` inside a loop (linear list scan!),
- `seen_users.count(user) > 1` inside a loop (re-scans the entire list for every entry!), and
- A nested double `for` loop comparing every `allowed_user` against every `seen_user`!

## Code Smells Checklist

- [ ] **Linear membership tests on lists inside loops**: `x in some_list` is `O(n)`; inside a loop of size `n`, it becomes `O(n^2)`.
- [ ] **Repeated `.count()` inside a loop**: Calling `seen_users.count(u)` for each item scans the whole list `n` times!
- [ ] **Nested double `for` loops for set intersection**: Manually comparing every pair of items instead of using `set_a & set_b`.
- [ ] **Manual list deduplication**: Repeatedly checking `if u not in result: result.append(u)` instead of using a `set`.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to compare `before_common_users` and `after_common_users`:

- **Before (`before_common_users`)**: Uses a nested `for` loop (`O(n * m)`) plus `user not in common` deduplication.
- **After (`after_common_users`)**: Converts both lists to `set`s and computes `sorted(set(group_a) & set(group_b))` in `O(n + m)` time!

## Your Refactoring Mission

Refactor `audit_access_logs(allowed_users, seen_users)` in `messy_code.py` to run in **`O(n)` linear time** while keeping identical outputs:

1. Convert `allowed_users` into a `set` for `O(1)` membership and set operations (`-`, `&`).
2. Count occurrences of `seen_users` in a single pass using a dictionary (or `collections.Counter` / a `seen_once` + `duplicates` set pair).
3. Eliminate all nested loops and `.count(...)` calls inside loops so auditing thousands of entries finishes in **under 0.05 seconds**!

## Run the Tests

From the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_12_quadratic_lookup_rescue/test_refactor.py -v
```

Or run the test file directly:

```bash
python ExamPrep/refactoring_projects/refactor_12_quadratic_lookup_rescue/test_refactor.py -v
```

Confirm `TestWorkedExample` and `TestBehaviorSafetyNet` are **GREEN** and `TestRefactorGoals` is **RED**, then refactor `messy_code.py` until all three classes are **GREEN**!
