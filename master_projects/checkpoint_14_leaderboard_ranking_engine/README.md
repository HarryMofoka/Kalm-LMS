# Checkpoint 14 — Esports / Football Tournament Ranking Engine

- **Unlocked After:** Activity 084 — Custom Sorting, Decomposition & TDD
- **Difficulty:** Intermediate–Advanced
- **Core Concepts:** Multi-key deterministic sorting, pure/immutable nested dictionary updates, modular decomposition, fixed-width ASCII table formatting with zero trailing spaces

---

## Real-World Value

Sports leagues (**Premier League**, **Rugby Championship**, **FIDE Chess**) and competitive esports circuits (**Valorant VCT**, **League of Legends**, **CS2 Majors**) depend on tournament engines that calculate standings accurately under strict tie-breaker rules.

A single off-by-one tie-breaker, an accidental mutation of a shared standings dictionary, or sloppy column spacing in a CLI/log dashboard causes disputed playoff seedings and broken automated tooling. Mastering **multi-key sort tuples**, **pure state updates**, and **clean terminal rendering** is core software craftsmanship.

---

## Problem Statement

You are building a pure-Python **Esports / Football Tournament Ranking Engine**. Given a sequence of match results `(home, away, home_score, away_score)`, your module must:

1. Record individual match outcomes without mutating caller standings (`record_match`), awarding **3 points** for a win, **1 point** for a draw, and **0 points** for a loss.
2. Build full tournament standings from a list of match tuples (`build_standings`).
3. Rank teams deterministically using the official tie-breaker cascade:
   **Points (desc) → Goal Difference (desc) → Goals For (desc) → Team Name (asc)** (`rank_teams`).
4. Render a cleanly aligned ASCII league table with **zero trailing spaces** on every line (`format_league_table`).

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study and run the sibling system in [`worked_example.py`](./worked_example.py): a **Hackathon Judging & Tie-Breaker Scorer**.

Run it from `ExamPrep/`:

```bash
python master_projects/checkpoint_14_leaderboard_ranking_engine/worked_example.py
```

### Architecture & Key Patterns Demonstrated

1. **Focused Helper Decomposition (`trimmed_average` → `score_team` → `rank_hackathon_teams` → `format_podium_report`)**:
   - Each function does one clear job and can be unit-tested independently.
2. **Olympic-Style Trimmed Scoring (`trimmed_average`)**:
   - Sorts a copy of the scores (`sorted(scores)`), drops the single lowest and single highest when there are 3+ judges, and averages the remaining scores.
3. **Deterministic Tuple Sort Key (`rank_hackathon_teams`)**:
   - Sorts by `(-entry["total"], -entry["execution"], entry["team"])` — negative numbers for descending numeric keys, plain strings for ascending tie-breaking.
4. **Dynamic-Width Table Formatting Without Trailing Spaces (`format_podium_report`)**:
   - Computes column widths dynamically from the longest team name and formats right-aligned numeric columns so no line ever ends with trailing whitespace.

---

## Your Project Brief (`project.py`)

Implement the four functions in [`project.py`](./project.py):

### 1. `record_match(standings: dict[str, dict[str, int]], home: str, away: str, home_score: int, away_score: int) -> dict[str, dict[str, int]]`
- **Pure / non-mutating:** Deep-copy all nested team dictionaries so neither `standings` nor any inner team stats dictionary inside it is ever mutated.
- Validation:
  - Raise `ValueError` if `home == away`.
  - Raise `ValueError` if `home_score < 0` or `away_score < 0`.
- Initialize any unseen team with:
  ```python
  {
      "played": 0,
      "wins": 0,
      "draws": 0,
      "losses": 0,
      "goals_for": 0,
      "goals_against": 0,
      "points": 0,
  }
  ```
- Update both teams:
  - Both increment `"played"` by `1`.
  - `home`: `"goals_for" += home_score`, `"goals_against" += away_score`.
  - `away`: `"goals_for" += away_score`, `"goals_against" += home_score`.
  - Winner gets `"wins" += 1` and `"points" += 3`; loser gets `"losses" += 1`.
  - On a draw, both get `"draws" += 1` and `"points" += 1`.
- Return the new standings dictionary.

### 2. `build_standings(matches: list[tuple[str, str, int, int]]) -> dict[str, dict[str, int]]`
- Applies every `(home, away, home_score, away_score)` match sequentially using `record_match`, starting from `{}`.
- Returns `{}` if `matches` is empty.

### 3. `rank_teams(standings: dict[str, dict[str, int]]) -> list[dict]`
- Converts `standings` into a sorted list of team row dictionaries, **without mutating `standings`**.
- Each returned row dictionary contains:
  ```python
  {
      "rank": int,          # 1-based position (1, 2, 3, ...)
      "team": str,
      "played": int,
      "wins": int,
      "draws": int,
      "losses": int,
      "goals_for": int,
      "goals_against": int,
      "goal_diff": int,     # goals_for - goals_against
      "points": int,
  }
  ```
- Deterministic sort order:
  1. `points` descending
  2. `goal_diff` descending
  3. `goals_for` descending
  4. `team` name ascending (lexicographical)

### 4. `format_league_table(ranked: list[dict]) -> list[str]`
- Renders `ranked` into cleanly aligned ASCII table lines (`list[str]`) with **zero trailing spaces** on every line.
- Exact layout specification:
  - `team_width = max([len("Team")] + [len(row["team"]) for row in ranked])`
  - Header line:
    `f"{'Pos':>3}  {'Team':<{team_width}}  {'P':>2}  {'W':>2}  {'D':>2}  {'L':>2}  {'GF':>3}  {'GA':>3}  {'GD':>4}  {'Pts':>3}"`
  - Separator line:
    `"-" * len(header)`
  - Data rows (one per team in `ranked`):
    - Format positive goal difference with a leading `+` (e.g., `+3`, `0`, `-2`).
    - `f"{row['rank']:>3}  {row['team']:<{team_width}}  {row['played']:>2}  {row['wins']:>2}  {row['draws']:>2}  {row['losses']:>2}  {row['goals_for']:>3}  {row['goals_against']:>3}  {gd_str:>4}  {row['points']:>3}"`
- When `ranked` is empty (`[]`), returns `[header, separator]` (2 lines, with `team_width = 4`).

Example output:

```text
Pos  Team         P   W   D   L   GF   GA    GD  Pts
----------------------------------------------------
  1  Apex FC      2   2   0   0    5    1    +4    6
  2  Nova United  2   1   0   1    3    3     0    3
  3  Byte City    2   0   0   2    1    5    -4    0
```

---

## Running the Tests

From inside the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_14_leaderboard_ranking_engine/test_project.py -v
```

- `TestWorkedExample` passes immediately.
- `TestMasterProject` starts red and turns green as you build `project.py`.
