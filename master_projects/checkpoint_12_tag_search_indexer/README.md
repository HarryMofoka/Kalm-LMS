# Checkpoint 12 — Inverted Index & Mini Full-Text Search Engine

- **Unlocked After:** Activity 072 — Dictionaries, Sets & Inverted Indexes
- **Difficulty:** Intermediate
- **Core Concepts:** Dictionaries of sets, inverted indexes, set intersections, frequency ranking, Jaccard similarity

---

## Real-World Value

How does **GitHub** search millions of issues in milliseconds, or **Elasticsearch** / **Apache Lucene** power instant documentation search? They do **not** scan every document line by line on every keystroke.

Instead, search engines build an **inverted index**: a dictionary mapping each normalized term to the `set` of document IDs that contain it. Once indexed:
- An **AND query** (`search_all`) becomes a fast set intersection ($O(\min |S_i|)$).
- An **OR ranked query** (`search_any`) counts matching postings across query terms.
- **"Related Articles / Similar Issues"** recommendations use **Jaccard similarity** on document term sets.

---

## Problem Statement

You are building a lightweight, pure-Python full-text search & recommendation engine for a technical documentation portal. Given a dictionary of documents `{doc_id: text}`, your engine must:

1. Tokenize raw text into clean lowercase alphanumeric terms with optional stop-word removal.
2. Construct an inverted index mapping `term -> set[doc_id]`.
3. Execute strict `AND` queries (`search_all`) returning sorted matching document IDs.
4. Execute ranked `OR` queries (`search_any`) ordered by number of distinct matching query terms descending, then `doc_id` ascending.
5. Recommend related documents (`suggest_related_docs`) ranked by **Jaccard similarity**.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study and run the sibling system in [`worked_example.py`](./worked_example.py): a **Recipe Ingredient Matcher**.

Run it from `ExamPrep/`:

```bash
python master_projects/checkpoint_12_tag_search_indexer/worked_example.py
```

### Architecture & Key Patterns Demonstrated

1. **Normalization First (`normalize_ingredients`)**:
   - Uses `re.findall(r"[a-z0-9]+", raw_text.lower())` so `"Garlic, Olive-Oil!"` cleanly splits into `{"garlic", "olive", "oil"}`.
2. **Inverted Index Construction (`build_ingredient_index`)**:
   - Uses `index.setdefault(term, set()).add(recipe_id)` to map each ingredient directly to the set of recipes using it.
3. **Set Intersection for Exact Matching (`find_exact_recipes`)**:
   - Looks up each required ingredient's posting set. If *any* ingredient is missing, returns `[]` immediately; otherwise computes `set.intersection(*posting_sets)` and sorts alphabetically.
4. **Hit-Count Ranking for Partial Matches (`rank_recipes_by_pantry`)**:
   - Deduplicates pantry ingredients before counting so repeating `"tomato"` twice in the query cannot artificially inflate a recipe's score.
   - Sorts by `(-match_count, recipe_id)` for deterministic tie-breaking.

---

## Your Project Brief (`project.py`)

Implement the five functions in [`project.py`](./project.py):

### 1. `tokenize(text: str, stop_words: set[str] | None = None) -> list[str]`
- Lowercases `text` and extracts all contiguous alphanumeric tokens (`[a-z0-9]+`), preserving order and duplicates.
- If `stop_words` is provided, filters out any token whose lowercase form appears in `stop_words` (treat `stop_words` case-insensitively).

```python
tokenize("Fast, 24/7 API-Search & fast indexing!", stop_words={"API"})
# -> ["fast", "24", "7", "search", "fast", "indexing"]
```

### 2. `build_inverted_index(documents: dict[str, str], stop_words: set[str] | None = None) -> dict[str, set[str]]`
- Tokenizes each document's text via `tokenize(text, stop_words=stop_words)`.
- Returns a dictionary mapping each unique term to the `set` of `doc_id`s containing that term.
- Does **not** mutate `documents`.

```python
build_inverted_index({"doc1": "Python sets", "doc2": "Python dicts"})
# -> {"python": {"doc1", "doc2"}, "sets": {"doc1"}, "dicts": {"doc2"}}
```

### 3. `search_all(index: dict[str, set[str]], query: str, stop_words: set[str] | None = None) -> list[str]`
- Tokenizes `query` (passing `stop_words`).
- Returns `[]` if the query yields no tokens or if any query token is missing from `index`.
- Otherwise returns a **sorted** `list[str]` of `doc_id`s containing **every** unique query token.

### 4. `search_any(index: dict[str, set[str]], query: str, stop_words: set[str] | None = None) -> list[str]`
- Tokenizes `query` (passing `stop_words`) and deduplicates the query terms.
- Returns `[]` if the query yields no tokens.
- Counts how many **distinct** query terms match each candidate `doc_id`.
- Returns matching `doc_id`s sorted by:
  1. Number of distinct matching terms **descending**
  2. `doc_id` **ascending** (lexicographical tie-breaker)

### 5. `suggest_related_docs(documents: dict[str, str], doc_id: str, top_k: int = 3, stop_words: set[str] | None = None) -> list[tuple[str, float]]`
- Raises `KeyError` if `doc_id` is not present in `documents`.
- Returns `[]` if `top_k <= 0`.
- Converts each document into its unique token set using `set(tokenize(text, stop_words=stop_words))`.
- Computes **Jaccard similarity** between target document set $A$ and every *other* document set $B$:
  $$\text{Jaccard}(A, B) = \frac{|A \cap B|}{|A \cup B|}$$
  (If $A \cup B$ is empty, similarity is `0.0`.)
- Excludes `doc_id` itself and excludes any document with `similarity == 0.0`.
- Rounds each similarity score to **4 decimal places** (`round(score, 4)`).
- Sorts by similarity **descending**, then `other_doc_id` **ascending**, and returns at most `top_k` tuples `(other_doc_id, rounded_similarity)`.

---

## Running the Tests

From inside the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_12_tag_search_indexer/test_project.py -v
```

- `TestWorkedExample` passes immediately.
- `TestMasterProject` starts red and passes once you complete `project.py`.
