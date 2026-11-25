# Checkpoint 16 — Mini `git diff` Line-Comparison Engine

- **Unlocked After:** Activity 096 — Dynamic Programming & Longest Common Subsequence (LCS)
- **Difficulty:** Hard (Tier 4 — Algorithms & Dynamic Programming)
- **Core Concepts:** 2D dynamic programming tables, Longest Common Subsequence (LCS), backtracking, edit scripts

---

## Real-World Value

Every time you run `git diff`, review a GitHub Pull Request, inspect Terraform plan drift, or compare two versions of a legal contract, an **LCS-based diff engine** is doing the heavy lifting underneath.

Naive line-by-line comparison breaks the moment someone inserts a single line at the top of a file — suddenly every line below looks "changed." By computing the **Longest Common Subsequence (LCS)** with dynamic programming, a real diff engine anchors on the largest ordered set of unchanged lines and isolates the minimal deletions (`-`) and insertions (`+`).

---

## Problem Statement

Given two versions of a text document represented as lists of lines (`old_lines` and `new_lines`), build a clean, deterministic diff engine that:
1. Constructs the `(m + 1) x (n + 1)` LCS dynamic programming table.
2. Backtracks through that table to emit a minimal sequence of `(" ", line)`, `("-", line)`, and `("+", line)` operations.
3. Formats the diff into human-readable unified diff lines.
4. Summarizes diff statistics (`added`, `removed`, `unchanged`).

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Before tackling the diff engine, study **`worked_example.py`** — a complete **Playlist Version Comparator** that compares two snapshots of a streaming playlist (`old_songs` vs `new_songs`) to report which tracks were kept, dropped, or added.

### Design Walkthrough

1. **Bottom-Up LCS Table (`build_playlist_lcs_table`)**:
   - Allocates a 2D list `dp` of size `(len(old_songs) + 1) x (len(new_songs) + 1)` filled with `0`.
   - `dp[i][j]` represents the LCS length of `old_songs[:i]` and `new_songs[:j]`.
   - Recurrence:
     - If `old_songs[i - 1] == new_songs[j - 1]`: `dp[i][j] = dp[i - 1][j - 1] + 1`
     - Else: `dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])`
2. **Backtracking (`compare_playlists`)**:
   - Walks backward from `(len(old_songs), len(new_songs))` to `(0, 0)`:
     - Matching songs emit `("KEEP", song)` and step diagonally `(i - 1, j - 1)`.
     - Otherwise, prefer stepping left `(i, j - 1)` with `("ADD", song)` when `dp[i][j - 1] >= dp[i - 1][j]`, and step up `(i - 1, j)` with `("DROP", song)` otherwise.
   - Reversing the collected list restores top-to-bottom order with **drops listed cleanly before adds** (just like `git diff`!).
3. **Reporting & Aggregation (`summarize_playlist_changes`, `format_playlist_report`)**:
   - Keeps presentation and counting decoupled from the DP algorithm.

Run the reference demo anytime:
```bash
python master_projects/checkpoint_16_text_diff_engine/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the following four functions in `project.py`:

1. **`lcs_table(old_lines: list[str], new_lines: list[str]) -> list[list[int]]`**
   - Build and return the `(len(old_lines) + 1) x (len(new_lines) + 1)` prefix LCS DP table where `table[i][j]` is the length of the longest common subsequence of `old_lines[:i]` and `new_lines[:j]`.
   - Row `0` and column `0` must all be `0`.

2. **`compute_diff(old_lines: list[str], new_lines: list[str]) -> list[tuple[str, str]]`**
   - Use `lcs_table` + backtracking to return a minimal edit script as a list of `(op, line)` tuples:
     - `(" ", line)` — line is unchanged (part of the LCS)
     - `("-", line)` — line was removed from `old_lines`
     - `("+", line)` — line was added in `new_lines`
   - **Tie-breaking preference:** When backtracking from `(m, n)` to `(0, 0)` and `dp[i][j - 1] >= dp[i - 1][j]`, emit `("+", new_lines[j - 1])` first so that after reversing, removals (`-`) appear before additions (`+`) in replacement hunks.
   - **Invariant:** Filtering for `" "` and `"-"` must reconstruct `old_lines` exactly; filtering for `" "` and `"+"` must reconstruct `new_lines` exactly; the number of `" "` entries must equal `lcs_table(old_lines, new_lines)[-1][-1]`.

3. **`format_unified_diff(old_lines: list[str], new_lines: list[str]) -> list[str]`**
   - Compute the diff and format each `(op, line)` as a readable string:
     - `(" ", line)` -> `f"  {line}"` (or `""` if `line == ""` to avoid trailing spaces)
     - `("-", line)` -> `f"- {line}"` (or `"-"` if `line == ""`)
     - `("+", line)` -> `f"+ {line}"` (or `"+"` if `line == ""`)

4. **`diff_stats(diff_ops: list[tuple[str, str]]) -> dict[str, int]`**
   - Count operations and return `{"added": int, "removed": int, "unchanged": int}`.
   - Raise `ValueError` if an operation tuple has an unrecognized op code (anything other than `" "`, `"-"`, `"+"`).

---

## Running Tests

From the `ExamPrep/` root directory:

```bash
python -m unittest master_projects/checkpoint_16_text_diff_engine/test_project.py -v
```

- `TestWorkedExample` should pass 100% right away.
- `TestMasterProject` starts red and turns green as you build `project.py`!
