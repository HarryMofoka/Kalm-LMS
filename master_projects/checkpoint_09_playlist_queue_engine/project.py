"""Master Project — Checkpoint 09: Music Streaming Queue Engine.

Implement all six pure (non-mutating) music queue operations according to README.md.
None of these functions may modify their input lists in place.
"""

from __future__ import annotations


def add_tracks(
    queue: list[str],
    new_tracks: list[str],
    allow_duplicates: bool = False,
) -> list[str]:
    """Return a new queue with new_tracks appended (non-mutating).

    Args:
        queue: Existing playback queue.
        new_tracks: Tracks to append.
        allow_duplicates: When False (default), skip any track already present
            in queue or already added earlier from new_tracks. When True,
            append every track in new_tracks as-is.

    Returns:
        A new list representing the updated queue.
    """
    pass


def deduplicate_queue(queue: list[str]) -> list[str]:
    """Return a new queue with duplicate tracks removed, preserving first-seen order.

    Args:
        queue: Input playback queue (must not be mutated).

    Returns:
        New list containing unique tracks in order of first appearance.
    """
    pass


def move_track(queue: list[str], old_index: int, new_index: int) -> list[str]:
    """Return a new queue with the track at old_index moved to new_index.

    Args:
        queue: Input playback queue (must not be mutated).
        old_index: Current 0-based index of the track to move.
        new_index: Target 0-based index where the track should be placed.

    Returns:
        New reordered queue list.

    Raises:
        IndexError: If queue is empty or either index is outside 0 <= i < len(queue).
    """
    pass


def rotate_queue(queue: list[str], steps: int) -> list[str]:
    """Return a new queue rotated left by `steps` positions (negative rotates right).

    Args:
        queue: Input playback queue (must not be mutated).
        steps: Number of positions to rotate left (or right if negative).
            Values larger than len(queue) wrap cleanly via modulo.

    Returns:
        New rotated queue list (or [] if queue is empty).
    """
    pass


def play_next(queue: list[str]) -> tuple[str | None, list[str]]:
    """Pop the front track non-destructively and return (current_track, remaining_queue).

    Args:
        queue: Input playback queue (must not be mutated).

    Returns:
        (queue[0], queue[1:]) if queue is non-empty, otherwise (None, []).
    """
    pass


def interleave_queues(q1: list[str], q2: list[str]) -> list[str]:
    """Return a new queue alternating tracks from q1 and q2, appending any tail.

    Args:
        q1: First playback queue (must not be mutated).
        q2: Second playback queue (must not be mutated).

    Returns:
        New interleaved queue list: [q1[0], q2[0], q1[1], q2[1], ...].
    """
    pass
