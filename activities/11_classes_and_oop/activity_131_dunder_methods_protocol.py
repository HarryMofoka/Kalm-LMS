"""
Activity 131: Dunder Methods (__len__, __eq__, __contains__, __iter__)
Difficulty: 131 / 132

Why do Python's built-in functions `len(x)`, `item in x`, `x == y`, and
`for item in x:` feel so natural?
Because Python delegates them directly to **dunder ("double underscore") methods**
on your class — the Python Data Model!

  - `len(obj)`      -> `obj.__len__()`
  - `item in obj`   -> `obj.__contains__(item)`
  - `a == b`        -> `a.__eq__(b)`
  - `for x in obj:` -> `obj.__iter__()`

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleBag (Multiset Container)
===============================================================================
Problem:
    Build `ExampleBag` storing item counts in a dict and implementing:
      - `add(item, qty=1)`: adds `qty > 0` copies of `item`.
      - `__len__() -> int`: total number of items across all quantities.
      - `__contains__(item) -> bool`: True if `item` has count > 0.
      - `__eq__(other) -> bool`: True if `other` is an `ExampleBag` with identical counts.
      - `__iter__()`: yields unique item names in sorted alphabetical order.

Step-by-Step Breakdown:
    1. In `__eq__`, check `if not isinstance(other, ExampleBag): return NotImplemented`
       so comparing with another type (like `bag == "hello"`) safely returns `False`.
    2. Implementing `__iter__` lets your object work seamlessly with `for`,
       `list(bag)`, `enumerate(bag)`, and comprehensions!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Scoreboard
===============================================================================
Problem:
    Implement a `Scoreboard` class for a competitive game leaderboard:
      - `__init__(self, initial_scores: dict[str, int] | None = None) -> None`
        * Stores a copy of `initial_scores` if provided, else an empty dict `{}`.
      - `record(self, player: str, points: int) -> int`
        * Adds `points` (may be positive, zero, or negative penalty!) to
          `player`'s score (defaulting from `0` if new) and returns the new score.
      - `score_of(self, player: str) -> int`
        * Returns `player`'s current score, or `0` if not on the scoreboard.
      - `top(self, n: int) -> list[tuple[str, int]]`
        * Returns the top `n` `(player, score)` pairs sorted by:
            1. Highest score FIRST (`-score`)
            2. Alphabetically by player name ASCENDING (`player`) on ties!
        * Returns `[]` if `n <= 0`.
      - `__len__(self) -> int`
        * Returns the number of players on the scoreboard.
      - `__contains__(self, player: object) -> bool`
        * Returns `True` iff `player` has been recorded on the scoreboard.
      - `__eq__(self, other: object) -> bool`
        * Returns `True` if `other` is a `Scoreboard` with identical player->score
          entries; returns `NotImplemented` if `other` is not a `Scoreboard`.
      - `__iter__(self)`
        * Yields player names (strings!) in leaderboard order (highest score
          first, tie-break alphabetically ascending!).

    Examples:
        sb = Scoreboard({"Zara": 100, "Alex": 100, "Maya": 150})
        len(sb)             -> 3
        "Maya" in sb        -> True
        "Ghost" in sb       -> False
        sb.top(2)           -> [("Maya", 150), ("Alex", 100)]
        list(sb)            -> ["Maya", "Alex", "Zara"]
        sb.record("Alex", 50) -> 150
        sb.top(2)           -> [("Alex", 150), ("Maya", 150)]

    Edge-case hints:
        - Sort key for `(player, score)` is `key=lambda pair: (-pair[1], pair[0])`!
        - Don't mutate the caller's `initial_scores` dictionary!
        - Two `Scoreboard`s inserted in DIFFERENT orders with the SAME scores
          MUST compare equal (`sb1 == sb2` is `True`).
"""
from __future__ import annotations

from collections.abc import Iterator


class ExampleBag:
    """A multiset container implementing __len__, __contains__, __eq__, and __iter__."""

    def __init__(self) -> None:
        self._counts: dict[str, int] = {}

    def add(self, item: str, qty: int = 1) -> None:
        """Add `qty` copies of `item` (qty must be positive)."""
        if qty <= 0:
            raise ValueError("qty must be positive")
        self._counts[item] = self._counts.get(item, 0) + qty

    def __len__(self) -> int:
        return sum(self._counts.values())

    def __contains__(self, item: object) -> bool:
        return isinstance(item, str) and self._counts.get(item, 0) > 0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, ExampleBag):
            return NotImplemented
        return self._counts == other._counts

    def __iter__(self) -> Iterator[str]:
        return iter(sorted(self._counts))


class Scoreboard:
    """A game leaderboard implementing Python container dunder methods + top(n)."""

    def __init__(self, initial_scores: dict[str, int] | None = None) -> None:
        """Initialize scoreboard with an optional copy of initial_scores."""
        pass

    def record(self, player: str, points: int) -> int:
        """Add `points` to `player`'s score and return their updated score."""
        pass

    def score_of(self, player: str) -> int:
        """Return `player`'s current score, or 0 if not present."""
        pass

    def top(self, n: int) -> list[tuple[str, int]]:
        """Return top `n` (player, score) pairs sorted by (-score, player)."""
        pass

    def __len__(self) -> int:
        """Return the number of players on the scoreboard."""
        pass

    def __contains__(self, player: object) -> bool:
        """Return True if `player` is on the scoreboard."""
        pass

    def __eq__(self, other: object) -> bool:
        """Return True if `other` is a Scoreboard with identical scores."""
        pass

    def __iter__(self) -> Iterator[str]:
        """Yield player names in leaderboard order (-score, player)."""
        pass


if __name__ == "__main__":
    bag = ExampleBag()
    bag.add("apple", 2)
    bag.add("banana", 3)
    print("Total items:", len(bag))
    print("Has apple? ", "apple" in bag)
    print("Sorted keys:", list(bag))
