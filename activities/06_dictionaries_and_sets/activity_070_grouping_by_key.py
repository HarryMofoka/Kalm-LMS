"""
Activity 070: Grouping Items by Key
Difficulty: 70 / 132

Context:
    Grouping records into buckets by a computed "signature" key is one of the
    highest-leverage patterns in Python: group transactions by month, group
    students by campus, or group words into anagram families!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Group Words by First Letter
===============================================================================
Problem:
    Given a list of strings `words`, return a dictionary mapping each lowercase
    first letter to the list of words starting with that letter (preserving
    original word casing and order). Ignore empty strings `""`.

Step-by-Step Explanation:
    1. Initialize `groups: dict[str, list[str]] = {}`.
    2. For each `word` in `words`: skip if `not word`.
    3. Compute the bucket key `key = word[0].lower()`.
    4. Append to the bucket via `groups.setdefault(key, []).append(word)`.

Edge Cases:
    - `["Apple", "ant", "Bear", ""]` -> `{"a": ["Apple", "ant"], "b": ["Bear"]}`
    - `[]`                           -> `{}`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — `find_anagram_groups` Preserving First-Seen Order
===============================================================================
Problem:
    Implement `solve_find_anagram_groups(words: list[str]) -> list[list[str]]`.
    Group strings in `words` that are anagrams of each other (ignoring letter
    case and spaces):
      - Two words belong to the same group iff they have the same canonical
        signature: `"".join(sorted(word.replace(" ", "").lower()))`.
      - Groups MUST appear in the order their FIRST member appears in `words`.
      - Words inside each group MUST preserve their original order and spelling.
      - Return `[]` for an empty list.

Examples:
    - `["eat", "tea", "tan", "ate", "nat", "bat"]`
      -> `[["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]`
    - `["Listen", "Silent", "Dormitory", "Dirty room"]`
      -> `[["Listen", "Silent"], ["Dormitory", "Dirty room"]]`
    - `["solo"]`
      -> `[["solo"]]`
    - `[]`
      -> `[]`

Edge-Case Hints:
    - Because Python dictionaries remember insertion order, doing
      `groups.setdefault(signature, []).append(word)` and returning
      `list(groups.values())` AUTOMATICALLY preserves both first-seen group
      order AND within-group word order!
    - Keep the original `word` inside the group list—only normalize it when
      computing `signature`!
"""

from __future__ import annotations


def example_group_by_first_letter(words: list[str]) -> dict[str, list[str]]:
    """Group non-empty words by their lowercase first letter, preserving order."""
    groups: dict[str, list[str]] = {}
    for word in words:
        if not word:
            continue
        key = word[0].lower()
        groups.setdefault(key, []).append(word)
    return groups


def solve_find_anagram_groups(words: list[str]) -> list[list[str]]:
    """Group anagram words (ignoring case & spaces), preserving first-seen group order."""
    pass


if __name__ == "__main__":
    sample = ["Apple", "banana", "Apricot", "blueberry", "", "cherry"]
    print(example_group_by_first_letter(sample))
