"""Automated tests for Checkpoint 09: Music Streaming Queue Engine."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_09_playlist_queue_engine import (  # noqa: E402
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Verify the Print-Shop Job Queue Manager reference works."""

    def test_enqueue_jobs_dedup_and_immutability(self) -> None:
        base = ["J1", "J2"]
        incoming = ["J2", "J3", "J3", "J4"]
        deduped = worked_example.enqueue_jobs(base, incoming, allow_duplicates=False)
        self.assertEqual(deduped, ["J1", "J2", "J3", "J4"])

        with_dups = worked_example.enqueue_jobs(base, incoming, allow_duplicates=True)
        self.assertEqual(with_dups, ["J1", "J2", "J2", "J3", "J3", "J4"])
        self.assertEqual(base, ["J1", "J2"])

    def test_deduplicate_jobs_preserves_order(self) -> None:
        raw = ["J3", "J1", "J3", "J2", "J1"]
        self.assertEqual(worked_example.deduplicate_jobs(raw), ["J3", "J1", "J2"])
        self.assertEqual(raw, ["J3", "J1", "J3", "J2", "J1"])

    def test_bump_job_to_front_and_missing_raises(self) -> None:
        queue = ["J1", "J2", "J3"]
        self.assertEqual(
            worked_example.bump_job_to_front(queue, "J3"),
            ["J3", "J1", "J2"],
        )
        self.assertEqual(queue, ["J1", "J2", "J3"])
        with self.assertRaises(ValueError):
            worked_example.bump_job_to_front(queue, "J999")

    def test_cancel_job_and_missing_raises(self) -> None:
        queue = ["J1", "J2", "J3", "J2"]
        self.assertEqual(worked_example.cancel_job(queue, "J2"), ["J1", "J3", "J2"])
        self.assertEqual(queue, ["J1", "J2", "J3", "J2"])
        with self.assertRaises(ValueError):
            worked_example.cancel_job(queue, "J404")

    def test_rotate_batch_positive_negative_and_wrap(self) -> None:
        queue = ["J1", "J2", "J3", "J4"]
        self.assertEqual(worked_example.rotate_batch(queue, 1), ["J2", "J3", "J4", "J1"])
        self.assertEqual(worked_example.rotate_batch(queue, -1), ["J4", "J1", "J2", "J3"])
        self.assertEqual(worked_example.rotate_batch(queue, 6), ["J3", "J4", "J1", "J2"])
        self.assertEqual(worked_example.rotate_batch([], 3), [])


class TestMasterProject(unittest.TestCase):
    """TDD test suite for the student's Music Streaming Queue Engine."""

    def test_add_tracks_with_and_without_duplicates_pure(self) -> None:
        queue = ["Song A", "Song B"]
        incoming = ["Song B", "Song C", "Song C", "Song D"]

        unique_q = project.add_tracks(queue, incoming, allow_duplicates=False)
        self.assertEqual(unique_q, ["Song A", "Song B", "Song C", "Song D"])

        full_q = project.add_tracks(queue, incoming, allow_duplicates=True)
        self.assertEqual(
            full_q,
            ["Song A", "Song B", "Song B", "Song C", "Song C", "Song D"],
        )
        self.assertEqual(queue, ["Song A", "Song B"])
        self.assertEqual(incoming, ["Song B", "Song C", "Song C", "Song D"])

    def test_deduplicate_queue_preserves_first_occurrence_order(self) -> None:
        raw = ["Track 3", "Track 1", "Track 3", "Track 2", "Track 1", "Track 4"]
        result = project.deduplicate_queue(raw)
        self.assertEqual(result, ["Track 3", "Track 1", "Track 2", "Track 4"])
        self.assertEqual(
            raw,
            ["Track 3", "Track 1", "Track 3", "Track 2", "Track 1", "Track 4"],
        )
        self.assertEqual(project.deduplicate_queue([]), [])

    def test_move_track_forward_backward_and_bounds_errors(self) -> None:
        queue = ["A", "B", "C", "D"]
        self.assertEqual(project.move_track(queue, 3, 1), ["A", "D", "B", "C"])
        self.assertEqual(project.move_track(queue, 0, 2), ["B", "C", "A", "D"])
        self.assertEqual(project.move_track(queue, 2, 2), ["A", "B", "C", "D"])
        self.assertEqual(queue, ["A", "B", "C", "D"])

        for old_i, new_i in [(-1, 0), (0, -1), (4, 0), (0, 4)]:
            with self.subTest(old_i=old_i, new_i=new_i):
                with self.assertRaises(IndexError):
                    project.move_track(queue, old_i, new_i)

        with self.assertRaises(IndexError):
            project.move_track([], 0, 0)

    def test_rotate_queue_left_right_large_and_empty(self) -> None:
        queue = ["A", "B", "C", "D"]
        self.assertEqual(project.rotate_queue(queue, 1), ["B", "C", "D", "A"])
        self.assertEqual(project.rotate_queue(queue, -1), ["D", "A", "B", "C"])
        self.assertEqual(project.rotate_queue(queue, 6), ["C", "D", "A", "B"])
        self.assertEqual(project.rotate_queue(queue, 0), ["A", "B", "C", "D"])
        self.assertEqual(project.rotate_queue([], 5), [])
        self.assertEqual(queue, ["A", "B", "C", "D"])

    def test_play_next_non_empty_and_empty_pure(self) -> None:
        queue = ["Intro", "Chorus", "Outro"]
        self.assertEqual(
            project.play_next(queue),
            ("Intro", ["Chorus", "Outro"]),
        )
        self.assertEqual(project.play_next(["Solo"]), ("Solo", []))
        self.assertEqual(project.play_next([]), (None, []))
        self.assertEqual(queue, ["Intro", "Chorus", "Outro"])

    def test_interleave_queues_equal_unequal_and_empty(self) -> None:
        q1 = ["A1", "A2"]
        q2 = ["B1", "B2", "B3", "B4"]
        self.assertEqual(
            project.interleave_queues(q1, q2),
            ["A1", "B1", "A2", "B2", "B3", "B4"],
        )
        self.assertEqual(
            project.interleave_queues(["X1", "X2", "X3"], ["Y1"]),
            ["X1", "Y1", "X2", "X3"],
        )
        self.assertEqual(project.interleave_queues([], ["Z1"]), ["Z1"])
        self.assertEqual(project.interleave_queues([], []), [])

    def test_all_operations_never_mutate_inputs(self) -> None:
        base = ["T1", "T2", "T3", "T2"]
        extra = ["T4", "T1"]
        snapshot_base = list(base)
        snapshot_extra = list(extra)

        cleaned = project.deduplicate_queue(base)
        self.assertEqual(cleaned, ["T1", "T2", "T3"])
        merged = project.add_tracks(cleaned, extra)
        self.assertEqual(merged, ["T1", "T2", "T3", "T4"])
        moved = project.move_track(merged, 3, 0)
        self.assertEqual(moved, ["T4", "T1", "T2", "T3"])
        rotated = project.rotate_queue(moved, 2)
        self.assertEqual(rotated, ["T2", "T3", "T4", "T1"])
        self.assertEqual(project.play_next(rotated), ("T2", ["T3", "T4", "T1"]))
        self.assertEqual(
            project.interleave_queues(cleaned, extra),
            ["T1", "T4", "T2", "T1", "T3"],
        )

        # Originals must still match snapshots identically
        self.assertEqual(base, snapshot_base)
        self.assertEqual(extra, snapshot_extra)


if __name__ == "__main__":
    unittest.main()
