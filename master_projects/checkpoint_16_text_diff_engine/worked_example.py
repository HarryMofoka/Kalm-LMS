"""Worked Example for Checkpoint 16: Playlist Version Comparator (LCS DP).

Demonstrates building a 2D Longest Common Subsequence (LCS) table and
backtracking through it to find kept, dropped, and added songs between two
versions of a playlist.
"""

from __future__ import annotations


def build_playlist_lcs_table(
    old_songs: list[str], new_songs: list[str]
) -> list[list[int]]:
    """Return the (m+1) x (n+1) LCS dynamic programming table.

    ``dp[i][j]`` stores the LCS length of ``old_songs[:i]`` and ``new_songs[:j]``.
    """
    rows = len(old_songs)
    cols = len(new_songs)
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if old_songs[i - 1] == new_songs[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def compare_playlists(
    old_songs: list[str], new_songs: list[str]
) -> list[tuple[str, str]]:
    """Compare two playlists and return minimal KEEP/DROP/ADD operations."""
    dp = build_playlist_lcs_table(old_songs, new_songs)
    i = len(old_songs)
    j = len(new_songs)
    changes_reversed: list[tuple[str, str]] = []

    while i > 0 or j > 0:
        if i > 0 and j > 0 and old_songs[i - 1] == new_songs[j - 1]:
            changes_reversed.append(("KEEP", old_songs[i - 1]))
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j - 1] >= dp[i - 1][j]):
            # Prefer taking ADD while walking backward so DROP comes before ADD forward.
            changes_reversed.append(("ADD", new_songs[j - 1]))
            j -= 1
        else:
            changes_reversed.append(("DROP", old_songs[i - 1]))
            i -= 1

    changes_reversed.reverse()
    return changes_reversed


def summarize_playlist_changes(changes: list[tuple[str, str]]) -> dict[str, int]:
    """Count kept, dropped, and added songs from a change list."""
    counts = {"kept": 0, "dropped": 0, "added": 0}
    mapping = {"KEEP": "kept", "DROP": "dropped", "ADD": "added"}

    for action, _ in changes:
        if action not in mapping:
            raise ValueError(f"Unknown playlist action: {action!r}")
        counts[mapping[action]] += 1

    return counts


def format_playlist_report(
    old_songs: list[str], new_songs: list[str]
) -> list[str]:
    """Format a human-readable report comparing two playlists."""
    changes = compare_playlists(old_songs, new_songs)
    prefixes = {"KEEP": "  ", "DROP": "- ", "ADD": "+ "}
    return [f"{prefixes[action]}{song}" for action, song in changes]


if __name__ == "__main__":
    v1 = [
        "Midnight City",
        "Blinding Lights",
        "Electric Feel",
        "Starlight",
        "Take On Me",
    ]
    v2 = [
        "Midnight City",
        "Dreams",
        "Electric Feel",
        "Take On Me",
        "Time to Pretend",
    ]

    ops = compare_playlists(v1, v2)
    stats = summarize_playlist_changes(ops)
    print("=== Playlist Diff Demo ===")
    for line in format_playlist_report(v1, v2):
        print(line)
    print(f"Summary: {stats}")
