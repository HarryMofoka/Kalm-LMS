"""Master Project (Checkpoint 14): Esports / Football Tournament Ranking Engine.

Implement the four functions below according to the specification in README.md.
Run tests from ExamPrep/ with:
    python -m unittest master_projects/checkpoint_14_leaderboard_ranking_engine/test_project.py -v
"""

from __future__ import annotations


def record_match(
    standings: dict[str, dict[str, int]],
    home: str,
    away: str,
    home_score: int,
    away_score: int,
) -> dict[str, dict[str, int]]:
    """Record a single match result and return a NEW standings dictionary.

    Neither ``standings`` nor any nested team dictionary inside it may be
    mutated. Points follow 3 for a win, 1 for a draw, and 0 for a loss.

    Each team record tracks:
        ``played``, ``wins``, ``draws``, ``losses``, ``goals_for``,
        ``goals_against``, ``points``.

    Args:
        standings: Existing mapping of team name -> stat dictionary.
        home: Home team name.
        away: Away team name.
        home_score: Non-negative goals/points scored by the home team.
        away_score: Non-negative goals/points scored by the away team.

    Returns:
        A new standings dictionary with updated records for ``home`` and ``away``.

    Raises:
        ValueError: If ``home == away`` or either score is negative.
    """
    pass


def build_standings(
    matches: list[tuple[str, str, int, int]],
) -> dict[str, dict[str, int]]:
    """Aggregate standings from a sequence of ``(home, away, home_score, away_score)`` tuples.

    Args:
        matches: List of match result tuples.

    Returns:
        Standings dictionary (``{}`` when ``matches`` is empty).
    """
    pass


def rank_teams(standings: dict[str, dict[str, int]]) -> list[dict]:
    """Sort teams deterministically and attach ``rank`` (1-based) and ``goal_diff``.

    Sort order:
        1. ``points`` descending
        2. ``goal_diff`` (``goals_for - goals_against``) descending
        3. ``goals_for`` descending
        4. ``team`` name ascending

    Does not mutate ``standings``.

    Args:
        standings: Mapping of team name -> stat dictionary.

    Returns:
        Ordered list of row dictionaries containing ``rank``, ``team``,
        ``played``, ``wins``, ``draws``, ``losses``, ``goals_for``,
        ``goals_against``, ``goal_diff``, and ``points``.
    """
    pass


def format_league_table(ranked: list[dict]) -> list[str]:
    """Format ranked league rows as cleanly aligned ASCII table lines.

    Every line MUST have zero trailing whitespace.
    Columns: ``Pos``, ``Team``, ``P``, ``W``, ``D``, ``L``, ``GF``, ``GA``,
    ``GD`` (positive values prefixed with ``+``), ``Pts``.
    See README.md for the exact column widths and separator line format.

    Args:
        ranked: List of ranked team row dictionaries from ``rank_teams``.

    Returns:
        List of formatted lines starting with header and dashed separator.
    """
    pass
