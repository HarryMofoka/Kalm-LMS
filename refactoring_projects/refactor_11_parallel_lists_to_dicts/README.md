# Refactor 11 — Replace Fragile Parallel Lists with Clean Dictionaries

## Backstory & Problem Statement

The school tuck-shop point-of-sale script (`process_tuckshop_orders`) was written by someone who hadn't learned Python dictionaries yet. Every time it runs, it explodes the product catalog into **three separate parallel lists**:

```python
names = []
prices = []
stocks = []
```

Then, for **every single order**, it linearly scans `for i in range(len(names)):` until `names[i] == item_name` so it can index into `prices[i]` and `stocks[i]`!

During morning break with a small menu, nobody noticed. Now the school canteen catalog has **2,000 items** and **2,000 orders** — and the parallel-list index scanner crawls, while keeping three separate lists synchronized by position is an off-by-one bug waiting to happen.

## Code Smells Checklist

- [ ] **Parallel lists**: Splitting one entity's attributes (`name`, `price`, `stock`) across `names[]`, `prices[]`, and `stocks[]` indexed by position `i`.
- [ ] **Linear `range(len(...))` lookup**: Scanning all items from index `0` to `len(names) - 1` on every single order (`O(M * N)`).
- [ ] **Fragile index coupling**: Sorting or deleting from one list without updating the others silently corrupts every product's price and stock.
- [ ] **Redundant rebuilding**: Reconstructing `remaining_stock` with another `range(len(names))` loop at the end.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to compare `before_lookup_student` and `after_lookup_student`:

- **Before (`before_lookup_student`)**: Unpacks rows into `names[]`, `scores[]`, and `houses[]`, then loops `for i in range(len(names)):` to find the matching index.
- **After (`after_lookup_student`)**: Uses `build_student_directory(records)` to create a dictionary keyed by student name, turning lookup into a single clean `O(1)` call: `directory.get(target_name)`.

## Your Refactoring Mission

Refactor `process_tuckshop_orders(catalog_items, orders)` in `messy_code.py` while keeping all order-processing rules and return values identical:

1. Replace the parallel `names`, `prices`, and `stocks` lists with a **dictionary** keyed by item name (e.g., `catalog = {name: {"price": price, "stock": stock} for ...}` or clean dict mapping).
2. Remove all `range(len(...))` linear index scans and look up items directly via dictionary access (`.get(...)` or `in`).
3. Make 2,000 catalog items × 2,000 orders finish in **under 0.08 seconds** (an `O(1)` dict refactor completes in ~0.002 seconds!).

## Run the Tests

From the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_11_parallel_lists_to_dicts/test_refactor.py -v
```

Or run the test file directly:

```bash
python ExamPrep/refactoring_projects/refactor_11_parallel_lists_to_dicts/test_refactor.py -v
```

Confirm `TestWorkedExample` and `TestBehaviorSafetyNet` are **GREEN** and `TestRefactorGoals` is **RED**, then refactor `messy_code.py` until all three classes pass!
