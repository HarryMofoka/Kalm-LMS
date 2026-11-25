"""Unit tests for Checkpoint 16: Text Diff Engine."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_16_text_diff_engine import project, worked_example


class TestWorkedExample(unittest.TestCase):
    """Tests verifying the Playlist Version Comparator worked example."""

    def test_lcs_table_dimensions_and_length(self) -> None:
        old_songs = ["A", "B", "C", "D"]
        new_songs = ["B", "D", "E"]
        dp = worked_example.build_playlist_lcs_table(old_songs, new_songs)
        self.assertEqual(len(dp), 5)
        self.assertEqual(len(dp[0]), 4)
        self.assertEqual(dp[4][3], 2)  # "B", "D"

    def test_compare_playlists_mixed_changes(self) -> None:
        v1 = ["Intro", "Old Track", "Chorus", "Outro"]
        v2 = ["Intro", "New Track", "Chorus", "Bonus", "Outro"]
        changes = worked_example.compare_playlists(v1, v2)
        self.assertEqual(
            changes,
            [
                ("KEEP", "Intro"),
                ("DROP", "Old Track"),
                ("ADD", "New Track"),
                ("KEEP", "Chorus"),
                ("ADD", "Bonus"),
                ("KEEP", "Outro"),
            ],
        )

    def test_compare_playlists_empty_inputs(self) -> None:
        self.assertEqual(worked_example.compare_playlists([], []), [])
        self.assertEqual(
            worked_example.compare_playlists([], ["Solo"]),
            [("ADD", "Solo")],
        )
        self.assertEqual(
            worked_example.compare_playlists(["Solo"], []),
            [("DROP", "Solo")],
        )

    def test_summarize_and_format_report(self) -> None:
        v1 = ["Song A", "Song B"]
        v2 = ["Song B", "Song C"]
        changes = worked_example.compare_playlists(v1, v2)
        self.assertEqual(
            worked_example.summarize_playlist_changes(changes),
            {"kept": 1, "dropped": 1, "added": 1},
        )
        self.assertEqual(
            worked_example.format_playlist_report(v1, v2),
            ["- Song A", "  Song B", "+ Song C"],
        )

    def test_summarize_rejects_unknown_action(self) -> None:
        with self.assertRaises(ValueError):
            worked_example.summarize_playlist_changes([("SWAP", "Track")])


class TestMasterProject(unittest.TestCase):
    """Tests for the student's mini `git diff` engine in project.py."""

    def test_lcs_table_values(self) -> None:
        old_lines = ["a", "b", "c", "d"]
        new_lines = ["a", "x", "c", "y", "d"]
        dp = project.lcs_table(old_lines, new_lines)
        self.assertIsInstance(dp, list)
        self.assertEqual(len(dp), 5)
        self.assertEqual(len(dp[0]), 6)
        self.assertEqual(dp[0], [0, 0, 0, 0, 0, 0])
        self.assertEqual(dp[4][5], 3)  # a, c, d

    def test_compute_diff_identical_files(self) -> None:
        lines = ["import os", "print('ok')"]
        ops = project.compute_diff(lines, lines)
        self.assertEqual(ops, [(" ", "import os"), (" ", "print('ok')")])

    def test_compute_diff_insertions_and_deletions(self) -> None:
        old_lines = ["def greet():", "    return 'hi'", "print(greet())"]
        new_lines = [
            "def greet(name):",
            "    return f'hi {name}'",
            "print(greet('Ada'))",
        ]
        # Replace middle + keep header/footer in a separate clear case:
        old_v1 = ["header", "legacy", "shared", "footer"]
        new_v2 = ["header", "modern", "shared", "extra", "footer"]
        ops = project.compute_diff(old_v1, new_v2)
        self.assertEqual(
            ops,
            [
                (" ", "header"),
                ("-", "legacy"),
                ("+", "modern"),
                (" ", "shared"),
                ("+", "extra"),
                (" ", "footer"),
            ],
        )
        # Also verify full replacement preserves reconstruction invariants
        rep_ops = project.compute_diff(old_lines, new_lines)
        reconstructed_old = [ln for op, ln in rep_ops if op in (" ", "-")]
        reconstructed_new = [ln for op, ln in rep_ops if op in (" ", "+")]
        self.assertEqual(reconstructed_old, old_lines)
        self.assertEqual(reconstructed_new, new_lines)

    def test_compute_diff_empty_edge_cases(self) -> None:
        self.assertEqual(project.compute_diff([], []), [])
        self.assertEqual(
            project.compute_diff([], ["new1", "new2"]),
            [("+", "new1"), ("+", "new2")],
        )
        self.assertEqual(
            project.compute_diff(["old1"], []),
            [("-", "old1")],
        )

    def test_format_unified_diff_output(self) -> None:
        old_lines = ["line1", "line2", "line3"]
        new_lines = ["line1", "line2_edited", "line3", "line4"]
        formatted = project.format_unified_diff(old_lines, new_lines)
        self.assertEqual(
            formatted,
            [
                "  line1",
                "- line2",
                "+ line2_edited",
                "  line3",
                "+ line4",
            ],
        )

    def test_diff_stats_counts_and_validation(self) -> None:
        ops = [
            (" ", "a"),
            ("-", "b"),
            ("+", "c"),
            ("+", "d"),
            (" ", "e"),
        ]
        self.assertEqual(
            project.diff_stats(ops),
            {"added": 2, "removed": 1, "unchanged": 2},
        )
        self.assertEqual(
            project.diff_stats([]),
            {"added": 0, "removed": 0, "unchanged": 0},
        )
        with self.assertRaises(ValueError):
            project.diff_stats([("~", "bad")])


if __name__ == "__main__":
    unittest.main()
