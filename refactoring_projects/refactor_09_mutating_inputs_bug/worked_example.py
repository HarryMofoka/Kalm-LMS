"""Worked Example for RF 09: Playlist Top Tracks (in-place mutation -> pure copy)."""


def before_top_tracks(tracks, limit):
    """Messy version: mutates the caller's playlist in place and returns the alias."""
    tracks.sort(key=lambda track: (-track[1], track[0]))
    keep = max(0, limit)
    while len(tracks) > keep:
        tracks.pop()
    return tracks


def after_top_tracks(tracks, limit):
    """Clean version: returns a new sorted slice without touching caller's list."""
    if limit <= 0:
        return []
    return sorted(tracks, key=lambda track: (-track[1], track[0]))[:limit]


if __name__ == "__main__":
    original_a = [("Sunset", 42), ("Neon Drive", 115), ("Lo-Fi Rain", 88)]
    original_b = list(original_a)

    top_before = before_top_tracks(original_a, 2)
    print("Before returned:", top_before)
    print("Caller list AFTER before_top_tracks (MUTATED!):", original_a)

    top_after = after_top_tracks(original_b, 2)
    print("After returned: ", top_after)
    print("Caller list AFTER after_top_tracks (SAFE!):    ", original_b)
