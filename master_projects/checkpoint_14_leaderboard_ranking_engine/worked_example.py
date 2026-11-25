"""Worked Example (Checkpoint 14): Hackathon Judging & Tie-Breaker Scorer.

A sibling reference system demonstrating trimmed judge scoring, deterministic
multi-key tie-breaker sorting, and cleanly aligned ASCII report generation
with zero trailing spaces.
"""

from __future__ import annotations


def trimmed_average(scores: list[float]) -> float:
    """Compute the mean of ``scores``, dropping one min and one max if len >= 3.

    Raises:
        ValueError: If ``scores`` is empty.
    """
    if not scores:
        raise ValueError("Cannot compute average of an empty score list")

    ordered = sorted(scores)
    if len(ordered) >= 3:
        ordered = ordered[1:-1]
    return round(sum(ordered) / len(ordered), 2)


def score_team(
    team: str,
    judge_scores: dict[str, list[float]],
    weights: dict[str, float],
) -> dict:
    """Aggregate weighted category scores for a hackathon team.

    Raises:
        ValueError: If a weighted category is missing from ``judge_scores``.
    """
    category_means: dict[str, float] = {}
    weighted_total = 0.0

    for category, weight in weights.items():
        if category not in judge_scores:
            raise ValueError(f"Missing category '{category}' for team '{team}'")
        mean = trimmed_average(judge_scores[category])
        category_means[category] = mean
        weighted_total += mean * weight

    return {
        "team": team,
        "categories": category_means,
        "execution": category_means.get("execution", 0.0),
        "total": round(weighted_total, 2),
    }


def rank_hackathon_teams(submissions: list[dict]) -> list[dict]:
    """Rank scored hackathon teams deterministically.

    Tie-breaker order:
        1. ``total`` descending
        2. ``execution`` descending
        3. ``team`` name ascending
    """
    ordered = sorted(
        submissions,
        key=lambda item: (-item["total"], -item["execution"], item["team"]),
    )
    ranked: list[dict] = []
    for position, entry in enumerate(ordered, start=1):
        row = dict(entry)
        row["rank"] = position
        ranked.append(row)
    return ranked


def format_podium_report(ranked: list[dict]) -> list[str]:
    """Render ranked hackathon teams as aligned ASCII lines (no trailing spaces)."""
    name_width = max([len("Team")] + [len(row["team"]) for row in ranked])
    header = f"{'Rank':>4}  {'Team':<{name_width}}  {'Exec':>6}  {'Total':>6}"
    separator = "-" * len(header)
    lines = [header, separator]

    for row in ranked:
        line = (
            f"{row['rank']:>4}  "
            f"{row['team']:<{name_width}}  "
            f"{row['execution']:>6.2f}  "
            f"{row['total']:>6.2f}"
        )
        lines.append(line.rstrip())
    return lines


if __name__ == "__main__":
    judging_weights = {"innovation": 0.4, "execution": 0.4, "design": 0.2}
    raw_entries = {
        "CircuitBreakers": {
            "innovation": [8.0, 9.0, 9.5, 10.0],
            "execution": [7.5, 8.5, 9.0, 9.0],
            "design": [8.0, 8.5, 9.0],
        },
        "ByteBenders": {
            "innovation": [8.0, 8.5, 9.0, 9.0],
            "execution": [8.5, 9.0, 9.5, 10.0],
            "design": [8.0, 8.5, 9.0],
        },
        "NullPointers": {
            "innovation": [7.0, 8.0, 8.0, 9.0],
            "execution": [7.0, 7.5, 8.0, 8.5],
            "design": [9.0, 9.5, 10.0],
        },
    }

    scored = [
        score_team(team, scores, judging_weights)
        for team, scores in raw_entries.items()
    ]
    leaderboard = rank_hackathon_teams(scored)

    print("=== Hackathon Final Leaderboard ===")
    for output_line in format_podium_report(leaderboard):
        print(output_line)
