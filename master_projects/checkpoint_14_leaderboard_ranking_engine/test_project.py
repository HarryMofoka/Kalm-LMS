"""Unit tests for Checkpoint 14: Esports / Football Tournament Ranking Engine."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_14_leaderboard_ranking_engine import (
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Verify the Hackathon Judging & Tie-Breaker Scorer reference implementation."""

    def test_trimmed_average_drops_extremes_and_handles_small_lists(self) -> None:
        # Drops 1.0 and 10.0 -> mean of [7.0, 9.0] == 8.0
        self.assertEqual(worked_example.trimmed_average([10.0, 1.0, 7.0, 9.0]), 8.0)
        # Fewer than 3 scores: average all
        self.assertEqual(worked_example.trimmed_average([6.0, 8.0]), 7.0)
        with self.assertRaises(ValueError):
            worked_example.trimmed_average([])

    def test_score_team_computes_weighted_total(self) -> None:
        weights = {"innovation": 0.5, "execution": 0.5}
        scores = {"innovation": [6.0, 8.0, 10.0], "execution": [7.0, 9.0, 10.0]}
        summary = worked_example.score_team("TeamA", scores, weights)
        # Trimmed innovation=8.0, execution=9.0 -> total=8.5
        self.assertEqual(summary["execution"], 9.0)
        self.assertEqual(summary["total"], 8.5)

    def test_score_team_missing_category_raises_value_error(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.score_team("TeamA", {"innovation": [8.0]}, {"execution": 1.0})

    def test_rank_hackathon_teams_breaks_ties_on_execution_then_name(self) -> None:
        submissions = [
            {"team": "Zeta", "execution": 8.0, "total": 9.0},
            {"team": "Beta", "execution": 9.0, "total": 9.0},
            {"team": "Alpha", "execution": 9.0, "total": 9.0},
            {"team": "Gamma", "execution": 10.0, "total": 8.5},
        ]
        ranked = worked_example.rank_hackathon_teams(submissions)
        self.assertEqual([r["team"] for r in ranked], ["Alpha", "Beta", "Zeta", "Gamma"])
        self.assertEqual([r["rank"] for r in ranked], [1, 2, 3, 4])

    def test_format_podium_report_alignment_and_no_trailing_spaces(self) -> None:
        ranked = [
            {"rank": 1, "team": "CircuitBreakers", "execution": 9.25, "total": 9.10},
            {"rank": 2, "team": "Arc", "execution": 8.50, "total": 8.75},
        ]
        lines = worked_example.format_podium_report(ranked)
        self.assertEqual(len(lines), 4)
        self.assertTrue(all(line == line.rstrip() for line in lines))
        self.assertEqual(len({len(line) for line in lines}), 1)
        self.assertIn("CircuitBreakers", lines[2])


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Esports / Football Tournament Ranking Engine."""

    def test_record_match_win_draw_and_deep_immutability(self) -> None:
        initial = {
            "Apex": {
                "played": 1,
                "wins": 1,
                "draws": 0,
                "losses": 0,
                "goals_for": 2,
                "goals_against": 0,
                "points": 3,
            }
        }
        after_win = project.record_match(initial, "Apex", "Nova", 3, 1)
        self.assertIsInstance(after_win, dict)
        self.assertEqual(
            after_win["Apex"],
            {
                "played": 2,
                "wins": 2,
                "draws": 0,
                "losses": 0,
                "goals_for": 5,
                "goals_against": 1,
                "points": 6,
            },
        )
        self.assertEqual(
            after_win["Nova"],
            {
                "played": 1,
                "wins": 0,
                "draws": 0,
                "losses": 1,
                "goals_for": 1,
                "goals_against": 3,
                "points": 0,
            },
        )
        # Neither outer dict nor nested dict of initial may be mutated
        self.assertEqual(list(initial.keys()), ["Apex"])
        self.assertEqual(initial["Apex"]["played"], 1)
        self.assertEqual(initial["Apex"]["points"], 3)

        after_draw = project.record_match(after_win, "Nova", "Apex", 2, 2)
        self.assertEqual(after_draw["Apex"]["draws"], 1)
        self.assertEqual(after_draw["Apex"]["points"], 7)
        self.assertEqual(after_draw["Nova"]["draws"], 1)
        self.assertEqual(after_draw["Nova"]["points"], 1)

    def test_record_match_rejects_self_play_and_negative_scores(self) -> None:
        with self.assertRaises(ValueError):
            project.record_match({}, "Apex", "Apex", 1, 0)
        with self.assertRaises(ValueError):
            project.record_match({}, "Apex", "Nova", -1, 2)
        with self.assertRaises(ValueError):
            project.record_match({}, "Apex", "Nova", 1, -2)

    def test_build_standings_aggregates_season_and_empty_matches(self) -> None:
        self.assertEqual(project.build_standings([]), {})

        matches = [
            ("Lions", "Tigers", 2, 1),
            ("Tigers", "Bears", 1, 1),
            ("Bears", "Lions", 0, 3),
        ]
        standings = project.build_standings(matches)
        self.assertIsInstance(standings, dict)
        self.assertEqual(standings["Lions"]["points"], 6)
        self.assertEqual(standings["Lions"]["goals_for"], 5)
        self.assertEqual(standings["Tigers"]["points"], 1)
        self.assertEqual(standings["Bears"]["losses"], 1)

    def test_rank_teams_full_tie_breaker_cascade(self) -> None:
        # Crafted standings exercising every single tie-breaker level:
        # 1. Leader:  6 pts
        # 2. DiffWin: 4 pts, GD +3, GF 4
        # 3. GoalsHi: 4 pts, GD +1, GF 5
        # 4. Alpha:   4 pts, GD +1, GF 3  (beats Zebra alphabetically)
        # 5. Zebra:   4 pts, GD +1, GF 3
        standings = {
            "Zebra":   {"played": 2, "wins": 1, "draws": 1, "losses": 0, "goals_for": 3, "goals_against": 2, "points": 4},
            "Alpha":   {"played": 2, "wins": 1, "draws": 1, "losses": 0, "goals_for": 3, "goals_against": 2, "points": 4},
            "GoalsHi": {"played": 2, "wins": 1, "draws": 1, "losses": 0, "goals_for": 5, "goals_against": 4, "points": 4},
            "DiffWin": {"played": 2, "wins": 1, "draws": 1, "losses": 0, "goals_for": 4, "goals_against": 1, "points": 4},
            "Leader":  {"played": 2, "wins": 2, "draws": 0, "losses": 0, "goals_for": 2, "goals_against": 0, "points": 6},
        }
        ranked = project.rank_teams(standings)
        self.assertIsInstance(ranked, list)
        self.assertEqual(
            [r["team"] for r in ranked],
            ["Leader", "DiffWin", "GoalsHi", "Alpha", "Zebra"],
        )
        self.assertEqual([r["rank"] for r in ranked], [1, 2, 3, 4, 5])
        self.assertEqual([r["goal_diff"] for r in ranked], [2, 3, 1, 1, 1])

    def test_format_league_table_alignment_and_zero_trailing_spaces(self) -> None:
        matches = [
            ("Apex FC", "Byte City", 3, 0),
            ("Nova United", "Byte City", 2, 1),
            ("Apex FC", "Nova United", 2, 1),
        ]
        ranked = project.rank_teams(project.build_standings(matches))
        lines = project.format_league_table(ranked)

        self.assertIsInstance(lines, list)
        self.assertEqual(len(lines), 5)  # Header + separator + 3 teams
        # Zero trailing spaces on every line
        for line in lines:
            self.assertEqual(line, line.rstrip(), f"Trailing space found in: {line!r}")
        # All lines share identical width and separator is pure dashes
        expected_width = len(lines[0])
        self.assertTrue(all(len(line) == expected_width for line in lines))
        self.assertEqual(lines[1], "-" * expected_width)

        self.assertEqual(
            lines[0],
            "Pos  Team          P   W   D   L   GF   GA    GD  Pts",
        )
        self.assertEqual(
            lines[2],
            "  1  Apex FC       2   2   0   0    5    1    +4    6",
        )
        self.assertEqual(
            lines[3],
            "  2  Nova United   2   1   0   1    3    3     0    3",
        )
        self.assertEqual(
            lines[4],
            "  3  Byte City     2   0   0   2    1    5    -4    0",
        )

    def test_format_league_table_empty_returns_header_and_separator(self) -> None:
        lines = project.format_league_table([])
        self.assertEqual(
            lines,
            [
                "Pos  Team   P   W   D   L   GF   GA    GD  Pts",
                "----------------------------------------------",
            ],
        )


if __name__ == "__main__":
    unittest.main()
