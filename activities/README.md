# Progressive Python Activities — 132 Guided Challenges

This folder is **Layer 1** of Kalm-LMS: **11 progressive modules × 12 activities = 132 activities**, carefully ranked from absolute beginner (`001`) up to **Halo Patterns & Grid Walks (`120`)** and **Classes & OOP (`132`)**.

## How Every Activity File Works

Open any `activity_NNN_*.py` file and you will see two clear sections:
1. **PART 1: WORKED EXAMPLE ("I DO")** — A complete, idiomatic solution to a sibling problem, explained line by line. Run the file (`python activity_001_fstring_greeting.py`) to see it live!
2. **PART 2: YOUR TURN ("YOU DO")** — A companion problem with a stub (`pass`) for you to solve, paired with automated unit tests in that module's `test_*.py` file.

## All 11 Modules (Click Any Module to Start)

| # | Module | Activities | What You Master | Unlocks |
|---|---|---|---|---|
| **01** | [01_variables_and_math](./01_variables_and_math/README.md) | `001 – 012` | f-strings, arithmetic, `//` & `%`, clock wrap, rounding, formatted receipts | CP 01, CP 02 |
| **02** | [02_conditionals_and_logic](./02_conditionals_and_logic/README.md) | `013 – 024` | Booleans, `if/elif/else`, guard clauses, tiered brackets, raising `TypeError`/`ValueError` | CP 03, CP 04 |
| **03** | [03_loops_fundamentals](./03_loops_fundamentals/README.md) | `025 – 036` | `for`/`while` loops, accumulators, digit loops, Fibonacci, primes, GCD/LCM, nested loops | CP 05, CP 06 |
| **04** | [04_strings_and_text](./04_strings_and_text/README.md) | `037 – 048` | Indexing, slicing, filtering, palindromes, RLE compression, Caesar cipher, templates | CP 07, CP 08 |
| **05** | [05_lists_and_tuples](./05_lists_and_tuples/README.md) | `049 – 060` | Min/max, deduplication, rotation, prefix sums, sliding windows, 2D grids without aliasing | CP 09, CP 10 |
| **06** | [06_dictionaries_and_sets](./06_dictionaries_and_sets/README.md) | `061 – 072` | Frequency maps, safe merges, sets, anagram groups, hash-map two-sum, inverted indexes | CP 11, CP 12 |
| **07** | [07_functions_validation_and_tdd](./07_functions_validation_and_tdd/README.md) | `073 – 084` | Pure return vs print, helper decomposition, validation contracts, custom sort keys, recursion | CP 13, CP 14 |
| **08** | [08_algorithms_and_problem_solving](./08_algorithms_and_problem_solving/README.md) | `085 – 096` | Binary search, two pointers, stacks, Kadane's algorithm, Pascal, spirals, merge sort, DP/LCS | CP 15, CP 16 |
| **09** | [09_shapes_and_ascii_patterns](./09_shapes_and_ascii_patterns/README.md) | `097 – 108` | Solid/hollow squares, pyramids, diamonds, hourglasses, alphabet diamonds, number spirals | CP 17 |
| **10** | [10_halo_patterns_and_grid_walks](./10_halo_patterns_and_grid_walks/README.md) | `109 – 120` | `(row, col)` indexing, border rules, clockwise/CCW walks, thin-shape guards, modulo runners | CP 18, CP 19 |
| **11** | [11_classes_and_oop](./11_classes_and_oop/README.md) | `121 – 132` | `__init__`, `__str__`/`__repr__`, invariants, composition, inheritance, dunders, state machines | CP 20 |

## Running Tests

From the repository root (`Kalm-LMS/`):

```bash
# Check progress across all 11 modules
python progress.py

# Run all tests for one module
python -m unittest activities/01_variables_and_math/test_01_variables_and_math.py -v
```
