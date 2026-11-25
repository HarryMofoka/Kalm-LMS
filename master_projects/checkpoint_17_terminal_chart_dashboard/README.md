# Checkpoint 17 — Terminal Metrics & Bar-Chart Dashboard Renderer

- **Unlocked After:** Activity 102 — ASCII Patterns, Layout & Zero Trailing Spaces
- **Difficulty:** Medium-Hard (Tier 4 — Precision String Layout & Rendering)
- **Core Concepts:** Dynamic column alignment, proportional scaling, framed ASCII boxes, pure string-list composition, **zero trailing spaces**

---

## Real-World Value

When you SSH into a production Linux server or watch a GitHub Actions CI run, there is no browser GUI — everything happens in a terminal. Tools like `htop`, `rich`, `pytest`, `cargo bench`, and `docker stats` turn raw telemetry into crisp, aligned ASCII tables, progress meters, and horizontal bar charts.

In automated CLI testing and snapshot verification, **trailing whitespace is a classic bug**: one stray space at the end of a line breaks diff assertions, wraps awkwardly on narrow terminals, and fails strict linters. Building pure functions that return `list[str]` (never calling `print()` inside the engine) with **zero trailing spaces on every line** is how real terminal rendering libraries stay rock-solid and 100% unit-testable.

---

## Problem Statement

Build a pure-Python **Terminal Metrics Dashboard Renderer** capable of drawing:
1. A clamped ASCII progress bar with percentage readout.
2. A proportionally scaled horizontal `#` bar chart with cleanly aligned labels and numeric values.
3. A framed `+---+` / `| ... |` KPI summary box that automatically sizes itself to its widest line.
4. A full observability dashboard combining a KPI summary box and a bar chart — with **zero trailing spaces** on every single line.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Inspect **`worked_example.py`** — a complete **CLI Build Status Box & Progress Bar Renderer** used to render CI/CD pipeline summaries.

### Design Walkthrough

1. **Pure Rendering (`list[str]`)**:
   - Every renderer returns a `str` or `list[str]` instead of calling `print()`. Only the `if __name__ == "__main__":` demo joins and prints them.
2. **Dynamic Width Computation**:
   - In `render_kv_panel`, we first compute `key_width = max(len(k) for k, _ in pairs)` so all colons line up vertically, then compute `inner_width = max(len(title), *(len(row) for row in body_rows))` so the box frame hugs the widest line cleanly.
3. **Zero Trailing Spaces Guarantee**:
   - Framed lines always end in `+` or `|`, and empty separator lines are `""` (never `"   "`). Unframed lines omit redundant padding spaces when bars are empty.

Run the reference demo anytime:
```bash
python master_projects/checkpoint_17_terminal_chart_dashboard/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the following four functions in `project.py`:

1. **`render_progress_bar(value: int | float, total: int | float, width: int = 20) -> str`**
   - Raise `ValueError` if `total <= 0` or `width <= 0`.
   - Clamp `value` into `[0, total]`.
   - Compute `filled = round((clamped / total) * width)` and `pct = round((clamped / total) * 100)`.
   - Return `f"[{'#' * filled}{'-' * (width - filled)}] {pct}%"` (e.g. `"[##########----------] 50%"`).

2. **`render_bar_chart(data: list[tuple[str, int | float]], max_bar_width: int = 20) -> list[str]`**
   - Raise `ValueError` if `max_bar_width <= 0` or any metric value is `< 0`.
   - Return `[]` if `data` is empty.
   - Left-align all labels to `max_label_len = max(len(label) for label, _ in data)`.
   - Scale each bar proportionally against `max_val = max(v for _, v in data)`:
     - If `max_val == 0`, `bar_len = 0` for all entries; otherwise `bar_len = round((value / max_val) * max_bar_width)`.
   - Format each row with **zero trailing spaces**:
     - When `bar_len > 0`: `f"{label:<{max_label_len}} | {'#' * bar_len} {value}"`
     - When `bar_len == 0`: `f"{label:<{max_label_len}} | {value}"`

3. **`render_kpi_box(title: str, lines: list[str]) -> list[str]`**
   - Compute `inner_width = max([len(title)] + [len(line) for line in lines])`.
   - Let `border = "+" + "-" * (inner_width + 2) + "+"`.
   - Header line: `f"| {title:<{inner_width}} |"`.
   - If `lines` is non-empty, return:
     `[border, header, border] + [f"| {line:<{inner_width}} |" for line in lines] + [border]`.
   - If `lines` is empty, return `[border, header, border]`.

4. **`render_dashboard(title: str, metrics_dict: dict[str, int | float]) -> list[str]`**
   - If `metrics_dict` is empty, return `render_kpi_box(title, ["No metrics available"])`.
   - Otherwise, compute KPI lines:
     - `f"Metrics: {len(metrics_dict)}"`
     - `f"Total: {sum(metrics_dict.values())}"`
     - `f"Peak: {peak_key} ({metrics_dict[peak_key]})"` (where `peak_key` is the first key with maximum value)
   - Return `render_kpi_box(title, kpi_lines) + [""] + render_bar_chart(list(metrics_dict.items()))`.
   - **Strict invariant:** Every returned line must satisfy `line == line.rstrip()` (ZERO trailing spaces!).

---

## Running Tests

From the `ExamPrep/` root directory:

```bash
python -m unittest master_projects/checkpoint_17_terminal_chart_dashboard/test_project.py -v
```
