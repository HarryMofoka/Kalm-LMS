# Refactor 15 — Replace Ad-Hoc Bracket Counters with a Clean Stack

## Backstory & Problem Statement

Your team built a spreadsheet formula checker (`validate_formula_brackets(expr)`) to catch missing parentheses, brackets, and braces before running calculations.

The original author thought: *"Easy! I'll just keep three counters: `round_cnt`, `square_cnt`, and `curly_cnt`!"*

All the basic tests passed — balanced formulas like `"({[]})"` returned `True`, and unclosed formulas like `"(([]"` returned `False`. Then a user typed `"([)]"` and `"{[}]"`... and the validator happily said **`True`**!

Why? Because **independent counters forget nesting order (LIFO)**. When `)` closes before `]`, the counters still reach zero even though the brackets are illegally interleaved!

## Code Smells Checklist

- [ ] **Wrong data structure (counters instead of a stack)**: Separate integer counters cannot enforce Last-In, First-Out nesting order.
- [ ] **Silent correctness bug on interleaved brackets**: `"([)]"` and `"{[}]"` slip right through!
- [ ] **Repetitive `if/elif` chains**: Copy-pasted increment/decrement/negative-check branches for every bracket type.
- [ ] **Hard to extend**: Adding another delimiter pair (like `< >`) means adding yet another counter variable and two more `elif` branches.

## Worked Refactoring Walkthrough (Before -> After)

Open `worked_example.py` to compare `before_check_parens(expr)` and `after_check_parens(expr)`:

- **Before (`before_check_parens`)**: Juggles `open_cnt`, `close_cnt`, and an `error_flag` inside noisy conditional checks.
- **After (`after_check_parens`)**: Uses a Python list as a **stack** (`stack.append("(")` on open, `if not stack: return False; stack.pop()` on close, `return not stack` at the end).
  - For a single bracket type `()`, both behave identically — **but the stack pattern generalizes cleanly to `()`, `[]`, and `{}` using a single lookup dictionary!**

## Your Refactoring Mission

Refactor `validate_formula_brackets(expr)` in `messy_code.py`:

1. Define a dictionary mapping bracket pairs (for example, `CLOSING_TO_OPENING = {")": "(", "]": "[", "}": "{"}` or opening-to-closing).
2. Replace `round_cnt`, `square_cnt`, and `curly_cnt` with a single **stack** (`stack = []` using `.append(...)` and `.pop()`).
3. Reject illegally interleaved brackets such as `"([)]"`, `"{[}]"`, and `"[({)}]"` while keeping all existing safety-net tests green!

## Run the Tests

From the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_15_brittle_manual_parser/test_refactor.py -v
```

Or run the test file directly:

```bash
python ExamPrep/refactoring_projects/refactor_15_brittle_manual_parser/test_refactor.py -v
```

Confirm `TestWorkedExample` and `TestBehaviorSafetyNet` are **GREEN** and `TestRefactorGoals` is **RED**, then refactor `messy_code.py` until all three classes pass!
