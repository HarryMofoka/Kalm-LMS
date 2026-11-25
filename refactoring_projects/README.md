# Refactoring Projects — 20 Progressive "Rescue Someone Else's Code" Missions

Welcome to **Layer 3** of Kalm-LMS! In real software engineering, you spend more time **reading and improving existing code** than writing brand-new files from scratch.

Each mission pairs with a Checkpoint (`01` → `20`) and hands you a realistic piece of messy "someone else's code" (`messy_code.py`) that **already runs and passes its behavioral safety net** — but suffers from classic code smells, subtle traps, slow loops, or tangled structure.

## The Golden Rule of Safe Refactoring

1. **Read `README.md`** and study the Before → After sibling refactoring in `worked_example.py`.
2. **Run `test_refactor.py` first**:
   - `TestWorkedExample` is **GREEN** (proves the example Before & After behave identically).
   - `TestBehaviorSafetyNet` is **GREEN** (your safety net! Never let this break while refactoring).
   - `TestRefactorGoals` is **RED** (lists the exact structural, safety, or performance goals your refactored code should hit).
3. **Refactor `messy_code.py` in small steps**, re-running tests after each change, until **all three test classes are GREEN**!

## All 20 Refactoring Missions (Click Any Mission to Open)

| Mission | Checkpoint | Mission Folder | Main Code Smell(s) You Will Fix |
|---|---|---|---|
| **RF 01** | CP 01 | [refactor_01_messy_receipt_math](./refactor_01_messy_receipt_math/README.md) | Cryptic 1-letter variable names (`a, b, c, x1`) & magic numbers |
| **RF 02** | CP 02 | [refactor_02_time_converter_spaghetti](./refactor_02_time_converter_spaghetti/README.md) | Repeated math formulas & hard-coded time constants |
| **RF 03** | CP 03 | [refactor_03_nested_if_pyramid](./refactor_03_nested_if_pyramid/README.md) | 6-level deep arrow anti-pattern → clean guard clauses |
| **RF 04** | CP 04 | [refactor_04_boolean_soup](./refactor_04_boolean_soup/README.md) | Redundant `if x == True: return True else: return False` & tangled logic |
| **RF 05** | CP 05 | [refactor_05_copy_paste_loops](./refactor_05_copy_paste_loops/README.md) | Copy-pasted identical loops → DRY parameterized helper |
| **RF 06** | CP 06 | [refactor_06_while_loop_traps](./refactor_06_while_loop_traps/README.md) | Fragile manual index `while` loops → clean `for` / `enumerate` |
| **RF 07** | CP 07 | [refactor_07_string_concat_chaos](./refactor_07_string_concat_chaos/README.md) | Brittle manual string slicing & `+` loops → `.join()` / clean methods |
| **RF 08** | CP 08 | [refactor_08_messy_text_cleaner](./refactor_08_messy_text_cleaner/README.md) | Giant tangled text sanitizer → focused single-purpose helpers |
| **RF 09** | CP 09 | [refactor_09_mutating_inputs_bug](./refactor_09_mutating_inputs_bug/README.md) | Silent in-place list mutation & side-effect bugs |
| **RF 10** | CP 10 | [refactor_10_grid_aliasing_disaster](./refactor_10_grid_aliasing_disaster/README.md) | Classic `[["."]*cols]*rows` aliasing trap & cryptic grid indexing |
| **RF 11** | CP 11 | [refactor_11_parallel_lists_to_dicts](./refactor_11_parallel_lists_to_dicts/README.md) | Fragile parallel lists (`names[]`, `prices[]`, `stocks[]`) → dictionaries |
| **RF 12** | CP 12 | [refactor_12_quadratic_lookup_rescue](./refactor_12_quadratic_lookup_rescue/README.md) | Sluggish `O(n²)` nested-list scans → `O(n)` sets & dicts |
| **RF 13** | CP 13 | [refactor_13_print_coupled_logic](./refactor_13_print_coupled_logic/README.md) | Business logic coupled to `print()` → pure functions + thin wrapper |
| **RF 14** | CP 14 | [refactor_14_god_function_breakup](./refactor_14_god_function_breakup/README.md) | 100-line monolithic invoice god-function → clean modular helpers |
| **RF 15** | CP 15 | [refactor_15_brittle_manual_parser](./refactor_15_brittle_manual_parser/README.md) | Ad-hoc bracket counter flags → clean stack-based validator |
| **RF 16** | CP 16 | [refactor_16_slow_naive_algorithms](./refactor_16_slow_naive_algorithms/README.md) | Brute-force `O(n²)` subarray/search code → Kadane + binary search |
| **RF 17** | CP 17 | [refactor_17_fragile_ascii_printer](./refactor_17_fragile_ascii_printer/README.md) | Trailing-space `print(..., end=" ")` loops → `format_row` & pure lines |
| **RF 18** | CP 18 | [refactor_18_double_corner_halo_mess](./refactor_18_double_corner_halo_mess/README.md) | Duplicate-corner & hardcoded halo patrol loops → clean legs & thin guards |
| **RF 19** | CP 19 | [refactor_19_spaghetti_game_loop](./refactor_19_spaghetti_game_loop/README.md) | Global-variable grid simulation → clean pure state transitions |
| **RF 20** | CP 20 | [refactor_20_procedural_to_oop_rescue](./refactor_20_procedural_to_oop_rescue/README.md) | Sprawling dict-passing procedural tracker → clean encapsulated classes |

## Running Tests

```bash
# From the repository root:
python progress.py

# Or run a single mission:
python -m unittest refactoring_projects/refactor_01_messy_receipt_math/test_refactor.py -v
```
