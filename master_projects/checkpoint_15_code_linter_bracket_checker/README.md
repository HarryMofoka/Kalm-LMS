# Checkpoint 15 — Source Code Bracket & Quote Linter

- **Unlocked After:** Activity 090 — Stacks & Scanning Algorithms
- **Difficulty:** Advanced
- **Core Concepts:** LIFO stacks, single-pass lexical scanning, string/escape/comment state machines, 1-indexed line & column diagnostics

---

## Real-World Value

Every time **VS Code**, **Ruff**, **ESLint**, or a compiler puts a red squiggly underline on line 42, column 17 telling you `Mismatched bracket: expected ')', got ']'`, you are watching a **stack-driven lexical scanner** at work.

Naive bracket checkers break immediately on real source code because strings (`"hello )"`), escaped quotes (`"say \"(\""`), and comments (`# TODO: fix [`) contain bracket characters that are *not* syntax delimiters. Building a quote- and comment-aware linter teaches you the exact foundation of real lexers, syntax highlighters, and IDE bracket-pair colorizers.

---

## Problem Statement

You are building a **Source Code Bracket & Quote Linter** for Python-like source files. Your engine must:

1. Scan multi-line source code character by character (`lint_brackets`), tracking **1-indexed** `line` and `col` numbers.
2. Balance `()`, `[]`, and `{}` using a LIFO stack while properly ignoring brackets inside `'...'` / `"..."` string literals (including backslash escapes like `\"`, `\'`, `\\`) and `# ...` end-of-line comments.
3. Report the **first** syntax error with exact `(line, col)` coordinates and a clear message (mismatched closing bracket, unexpected closing bracket, unterminated string literal, or unclosed opening bracket).
4. Compute sorted `(open_idx, close_idx)` match coordinates for single-line IDE bracket-pair highlighting (`find_matching_pairs`).

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Explore and run the sibling system in [`worked_example.py`](./worked_example.py): an **HTML/XML Tag Balance Checker**.

Run it from `ExamPrep/`:

```bash
python master_projects/checkpoint_15_code_linter_bracket_checker/worked_example.py
```

### Architecture & Key Patterns Demonstrated

1. **Two-Stage Scanning (`parse_tags` → `check_markup_balance`)**:
   - Stage 1 (`parse_tags`) skips `<!-- ... -->` comments and self-closing tags (`<br/>`, `<img src="a.png" />`), emitting normalized open/close tag tokens with their exact 1-indexed `line`.
   - Stage 2 (`check_markup_balance`) maintains a LIFO stack of `(tag_name, line)`. Every opening tag pushes onto the stack; every closing tag pops and verifies it matches the top of the stack.
2. **Exact First-Error Reporting**:
   - Stops on the first mismatch or unexpected closing tag, returning `{"valid": False, "error": {"line": ..., "message": ...}}`.
   - After EOF, if the stack is non-empty, reports the innermost unclosed opening tag (`stack[-1]`) at its opening line.

---

## Your Project Brief (`project.py`)

Implement the two functions in [`project.py`](./project.py):

### 1. `lint_brackets(source_code: str) -> dict`
Scans `source_code` character by character with **1-indexed** `line` and `col` counters (a `\n` increments `line` by 1 and resets `col` to 1 for the next character).

Rules:
- **Opening brackets:** `(`, `[`, `{` → push `(char, line, col)` onto the stack.
- **Closing brackets:** `)`, `]`, `}`:
  - If stack is empty → return immediately:
    `{"valid": False, "error": {"line": line, "col": col, "message": f"Unexpected closing bracket '{ch}'"}}`
  - Pop top `(open_ch, _, _)`. If `ch` does not match `open_ch` → return immediately:
    `{"valid": False, "error": {"line": line, "col": col, "message": f"Mismatched bracket: expected '{expected}', got '{ch}'"}}`
- **String literals (`'...'` and `"..."`):**
  - When outside a string/comment, encountering `'` or `"` enters string mode, recording `(quote_char, quote_line, quote_col)`.
  - Inside a string, brackets and `#` are **ignored**.
  - Backslash escapes (`\x`, e.g., `\"`, `\'`, `\\`) skip the escaped character so an escaped quote does **not** close the string.
  - If a newline (`\n`) or end of input is reached while still inside a string → return immediately with the opening quote's coordinates:
    `{"valid": False, "error": {"line": quote_line, "col": quote_col, "message": f"Unterminated string literal starting with {quote_char}"}}`
- **Line comments (`#`):**
  - When outside a string, `#` ignores all remaining characters on the current line until `\n` (or EOF).
- **End of file (EOF):**
  - If the stack is non-empty, pop the top `(open_ch, open_line, open_col)` and return:
    `{"valid": False, "error": {"line": open_line, "col": open_col, "message": f"Unclosed bracket '{open_ch}'"}}`
  - Otherwise return:
    `{"valid": True, "error": None}`

### 2. `find_matching_pairs(line: str) -> list[tuple[int, int]]`
Scans a single line of code using **0-indexed** character positions, ignoring brackets inside `'...'` / `"..."` strings (respecting backslash escapes) and `#` comments.

- Matches `()`, `[]`, `{}` with a stack, recording `(open_idx, close_idx)` whenever a closing bracket matches its opening bracket.
- Returns all matched pairs **sorted by `open_idx` ascending**.
- Raises `ValueError` if any bracket is mismatched, unexpected, unclosed, or if a string literal is unterminated.

```python
find_matching_pairs("fn(a[0], {1: (2)})")
# -> [(2, 17), (4, 6), (9, 16), (13, 15)]

find_matching_pairs("msg = '(not a bracket)' # [comment]")
# -> []
```

---

## Running the Tests

From inside the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_15_code_linter_bracket_checker/test_project.py -v
```

- `TestWorkedExample` passes immediately.
- `TestMasterProject` starts red and turns green as you build `project.py`.
