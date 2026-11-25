"""Master Project (Checkpoint 12): Inverted Index & Mini Full-Text Search Engine.

Implement the five functions below according to the specification in README.md.
Run tests from ExamPrep/ with:
    python -m unittest master_projects/checkpoint_12_tag_search_indexer/test_project.py -v
"""

from __future__ import annotations


def tokenize(
    text: str,
    stop_words: set[str] | None = None,
) -> list[str]:
    """Split text into lowercase alphanumeric tokens, optionally filtering stop words.

    Extracts contiguous ``[a-z0-9]+`` tokens in order (preserving duplicates).
    When ``stop_words`` is provided, tokens matching any stop word
    (case-insensitively) are excluded.

    Args:
        text: Raw input text to tokenize.
        stop_words: Optional set of words to exclude.

    Returns:
        Ordered list of normalized tokens.
    """
    pass


def build_inverted_index(
    documents: dict[str, str],
    stop_words: set[str] | None = None,
) -> dict[str, set[str]]:
    """Build an inverted index mapping each term to the set of matching doc IDs.

    Args:
        documents: Mapping of ``doc_id -> text``.
        stop_words: Optional set of stop words to omit from indexing.

    Returns:
        Dictionary mapping ``term -> set[doc_id]``.
    """
    pass


def search_all(
    index: dict[str, set[str]],
    query: str,
    stop_words: set[str] | None = None,
) -> list[str]:
    """Return sorted doc IDs containing EVERY term in ``query``.

    Args:
        index: Inverted index mapping ``term -> set[doc_id]``.
        query: Search query string.
        stop_words: Optional set of stop words ignored in the query.

    Returns:
        Alphabetically sorted list of matching doc IDs, or ``[]`` if the
        query has no tokens or any token is absent from the index.
    """
    pass


def search_any(
    index: dict[str, set[str]],
    query: str,
    stop_words: set[str] | None = None,
) -> list[str]:
    """Return doc IDs containing AT LEAST ONE term in ``query``, ranked by hits.

    Each distinct query term counts at most once per document. Results are
    sorted by number of distinct matching terms descending, then ``doc_id``
    ascending for ties.

    Args:
        index: Inverted index mapping ``term -> set[doc_id]``.
        query: Search query string.
        stop_words: Optional set of stop words ignored in the query.

    Returns:
        Ranked list of matching doc IDs.
    """
    pass


def suggest_related_docs(
    documents: dict[str, str],
    doc_id: str,
    top_k: int = 3,
    stop_words: set[str] | None = None,
) -> list[tuple[str, float]]:
    """Recommend up to ``top_k`` related documents using Jaccard similarity.

    Computes ``|A & B| / |A | B|`` between the unique token set of ``doc_id``
    and every other document. Excludes ``doc_id`` itself and documents with
    zero similarity. Scores are rounded to 4 decimal places and sorted by
    similarity descending, then ``other_doc_id`` ascending.

    Args:
        documents: Mapping of ``doc_id -> text``.
        doc_id: Reference document ID to find neighbors for.
        top_k: Maximum number of recommendations to return.
        stop_words: Optional set of stop words excluded before similarity.

    Returns:
        List of ``(other_doc_id, similarity)`` tuples.

    Raises:
        KeyError: If ``doc_id`` does not exist in ``documents``.
    """
    pass
