"""
Activity 080 — Multi-Criteria Leaderboard Sorting
Difficulty: 80 / 132

Context:
    What happens when you need to sort one field DESCENDING (highest score
    first) and a tie-breaker field ASCENDING (A before Z)? You cannot just set
    `reverse=True`, because that flips BOTH fields! The idiomatic Python trick
    is negating numeric fields inside a tuple key: `(-score, name)`.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO")
===============================================================================
Problem:
    Implement `example_rank_students(students)` where `students` is a list of
    `(name, score)` tuples. Return a NEW list sorted by:
      1. `score` DESCENDING (higher scores first)
      2. `name` ASCENDING (alphabetical tie-break)

Step-by-Step Explanation:
    1. If Alice has 95 and Bob has 95:
       - Key for Alice: `(-95, "Alice")`
       - Key for Bob:   `(-95, "Bob")`
       Because `-95 == -95`, Python compares `"Alice" < "Bob"` -> Alice first!
    2. If Cara has 98:
       - Key for Cara: `(-98, "Cara")`
       Because `-98 < -95`, Cara sorts BEFORE both Alice and Bob!
    3. `sorted(students, key=lambda s: (-s[1], s[0]))` handles both directions
       in a single clean pass without mutating `students`.

Edge Cases:
    - Empty list `[]` -> `[]`
    - Negative scores (e.g., `-5` vs `-10`): `-(-5) = 5 < -(-10) = 10`, so `-5`
      still ranks higher than `-10`!

===============================================================================
PART 2: YOUR TURN ("YOU DO")
===============================================================================
Problem:
    Implement `solve_rank_teams(teams)` for a football league standings table.
    Each element of `teams` is a dictionary with keys:
      - `"name"` (`str`)
      - `"points"` (`int`)
      - `"goal_diff"` (`int`)

    Return a list of team NAMES (`list[str]`) ordered by:
      1. `"points"` DESCENDING
      2. `"goal_diff"` DESCENDING
      3. `"name"` ASCENDING

Rules & Edge Cases:
    - Return ONLY the team names as a `list[str]`, not the dicts.
    - Do NOT mutate the `teams` list or any team dictionary inside it.
    - Empty list `[]` -> `[]`.
    - Works properly with negative `goal_diff` values (e.g., `-2` beats `-7`).

Examples:
    teams = [
        {"name": "Lions", "points": 12, "goal_diff": 4},
        {"name": "Eagles", "points": 12, "goal_diff": 7},
        {"name": "Bears", "points": 12, "goal_diff": 4},
        {"name": "Sharks", "points": 15, "goal_diff": 2},
    ]
    solve_rank_teams(teams) -> ["Sharks", "Eagles", "Bears", "Lions"]
"""

from __future__ import annotations


def example_rank_students(
    students: list[tuple[str, int]],
) -> list[tuple[str, int]]:
    """Return a new list of (name, score) sorted by score desc, then name asc."""
    return sorted(students, key=lambda student: (-student[1], student[0]))


def solve_rank_teams(teams: list[dict]) -> list[str]:
    """Return team names sorted by points desc, goal_diff desc, name asc."""
    pass


if __name__ == "__main__":
    roster = [("Zoe", 88), ("Alice", 95), ("Ben", 95), ("Mia", 72)]
    print("Ranked students:", example_rank_students(roster))
