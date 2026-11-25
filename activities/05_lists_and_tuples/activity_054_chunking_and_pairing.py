"""
Activity 054: Chunking & Pairing Tuples  [Unlocks Checkpoint 09!]
Difficulty: 54 / 132

Context:
    Pagination APIs split 100 search results into pages of 10; batch database
    loaders group records into chunks of 50; pairing routines zip student names
    with exam scores into immutable tuples. Both patterns rely on range steps
    and clean slicing.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Pair Two Lists Into Tuples
===============================================================================
Problem:
    Given two lists `first` and `second`, pair elements at matching indices into
    a list of 2-tuples `[(first[0], second[0]), ...]`, stopping when the shorter
    list runs out.

Step-by-Step Explanation:
    1. Determine `limit = min(len(first), len(second))`.
    2. Build `[(first[i], second[i]) for i in range(limit)]` (equivalent to
       `list(zip(first, second))`, shown explicitly so the index mechanics are
       transparent).
    3. If either list is empty, `limit` is `0` and the result is `[]`.

Edge Cases:
    - `(["a", "b"], [1, 2, 3])` -> `[("a", 1), ("b", 2)]`
    - `([], [1, 2])`            -> `[]`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Split List Into Fixed-Size Chunks
===============================================================================
Problem:
    Implement `solve_chunk_list(items: list[Any], size: int) -> list[list[Any]]`.
    Split `items` into consecutive sublists (chunks) each of length `size`.
      - If `len(items)` is not evenly divisible by `size`, the final chunk holds
        the remaining items (length `< size`).
      - If `size <= 0`, raise `ValueError("Chunk size must be positive")`.
      - If `items` is empty (and `size > 0`), return `[]`.
      - Do NOT mutate `items`.

Examples:
    - `([1, 2, 3, 4, 5], 2)` -> `[[1, 2], [3, 4], [5]]`
    - `([1, 2, 3, 4], 2)`    -> `[[1, 2], [3, 4]]`
    - `([1, 2], 5)`          -> `[[1, 2]]`
    - `(["a", "b", "c"], 1)` -> `[["a"], ["b"], ["c"]]`
    - `([], 3)`              -> `[]`
    - `([1, 2, 3], 0)`       -> raises `ValueError`
    - `([1, 2, 3], -2)`      -> raises `ValueError`

Edge-Case Hints:
    - Validate `if size <= 0: raise ValueError(...)` BEFORE anything else—even
      if `items` is empty!
    - `range(0, len(items), size)` generates every chunk's starting index `i`,
      and `items[i : i + size]` cleanly clamps at the end of the list without
      ever raising `IndexError`!
"""

from __future__ import annotations

from typing import Any


def example_pair_lists(first: list[Any], second: list[Any]) -> list[tuple[Any, Any]]:
    """Pair corresponding elements of `first` and `second`, stopping at the shorter."""
    limit = min(len(first), len(second))
    return [(first[i], second[i]) for i in range(limit)]


def solve_chunk_list(items: list[Any], size: int) -> list[list[Any]]:
    """Split `items` into consecutive chunks of length `size` (raises ValueError if size <= 0)."""
    pass


if __name__ == "__main__":
    names = ["Ada", "Grace", "Alan"]
    scores = [98, 95]
    print("Paired:", example_pair_lists(names, scores))
