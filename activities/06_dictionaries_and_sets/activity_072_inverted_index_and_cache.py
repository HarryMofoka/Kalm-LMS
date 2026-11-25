"""
Activity 072: Inverted Index & Tag Querying  [Unlocks Checkpoint 12!]
Difficulty: 72 / 132

Context:
    Welcome to the Module 06 capstone! How does Google or a documentation site
    instantly find every page containing BOTH `"python"` and `"exam"`? It builds
    an **inverted index** (`word -> doc_ids`) and intersects posting sets—a
    technique that combines dictionaries and sets at full power!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Build a `word -> doc_ids` Inverted Index
===============================================================================
Problem:
    Given `docs: dict[str, str]` mapping each `doc_id` to its text content,
    build and return an inverted index `dict[str, list[str]]` mapping every
    normalized word (whitespace-split, alphanumeric-only, lowercased) to a
    **sorted** list of unique `doc_id`s in which that word appears.

Step-by-Step Explanation:
    1. Build an intermediate `index: dict[str, set[str]] = {}` using sets so a
       word appearing 5 times in `"doc1"` only records `"doc1"` once!
    2. For each `doc_id, text` in `docs.items()`:
         - Extract normalized words and do `index.setdefault(word, set()).add(doc_id)`.
    3. Convert each value set to a sorted list:
       `{word: sorted(doc_ids) for word, doc_ids in index.items()}`.

Edge Cases:
    - Repeated words in the same doc produce only ONE entry for that `doc_id`.
    - Empty `docs` or punctuation-only text returns `{}`.

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Query Docs Containing ALL Required Tags
===============================================================================
Problem:
    Implement `solve_query_docs_with_all_tags(doc_tags: dict[str, set[str]], required_tags: list[str]) -> list[str]`.
    Given:
      - `doc_tags`: dictionary mapping each `doc_id` to a `set[str]` of tags
        (tags may have mixed casing like `"Python"`, `"EXAM"`),
      - `required_tags`: list of tags that a matching document MUST possess
        (also matched **case-insensitively**!).
    Return a **sorted** list of all `doc_id`s that contain EVERY tag listed in
    `required_tags`:
      - If `required_tags` is empty (`[]`), EVERY document matches—return
        `sorted(doc_tags.keys())`.
      - If `doc_tags` is empty, return `[]`.
      - Do NOT mutate `doc_tags` or any of its inner tag sets!

Examples:
    Given:
        doc_tags = {
            "d1": {"Python", "exam", "loops"},
            "d2": {"python", "dicts"},
            "d3": {"PYTHON", "exam", "dicts"},
        }
    - `required_tags = ["python", "exam"]`          -> `["d1", "d3"]`
    - `required_tags = ["PYTHON", "Dicts", "Exam"]` -> `["d3"]`
    - `required_tags = ["rust"]`                    -> `[]`
    - `required_tags = []`                          -> `["d1", "d2", "d3"]`

Edge-Case Hints:
    - Approach 1 (subset check): normalize `needed = {t.lower() for t in required_tags}`,
      then keep each `doc_id` whose `{t.lower() for t in tags}` satisfies
      `needed.issubset(normalized_tags)` (or `needed <= normalized_tags`).
    - Approach 2 (inverted index + intersection): build `tag_to_docs: dict[str, set[str]]`
      and intersect `tag_to_docs.get(tag, set())` across every tag in `needed`!
      In a real search service, you'd cache `tag_to_docs` (memoization) so
      thousands of tag queries run in microseconds!
"""

from __future__ import annotations


def example_build_inverted_index(docs: dict[str, str]) -> dict[str, list[str]]:
    """Build a `word -> sorted unique doc_ids` inverted index from `docs`."""
    index: dict[str, set[str]] = {}
    for doc_id, text in docs.items():
        for token in text.split():
            word = "".join(ch.lower() for ch in token if ch.isalnum())
            if word:
                index.setdefault(word, set()).add(doc_id)

    return {word: sorted(doc_ids) for word, doc_ids in index.items()}


def solve_query_docs_with_all_tags(
    doc_tags: dict[str, set[str]],
    required_tags: list[str],
) -> list[str]:
    """Return sorted `doc_id`s containing ALL `required_tags` (case-insensitive)."""
    pass


if __name__ == "__main__":
    sample_docs = {
        "doc2": "Python dicts and sets!",
        "doc1": "Python lists and Python loops.",
    }
    print(example_build_inverted_index(sample_docs))
