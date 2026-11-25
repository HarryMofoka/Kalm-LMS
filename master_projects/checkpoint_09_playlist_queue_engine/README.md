# Checkpoint 09 — Music Streaming Queue Engine

- **Unlocked After:** Activity 054 *(Lists, Slicing, Dedup & Rotation)*
- **Difficulty:** ★★★☆☆ (Intermediate)
- **Core Concepts:** Pure / non-mutating list transformations, order-preserving deduplication, slicing, modulo rotation, queue interleaving

---

## Real-World Value

Think about what happens every time you tap **"Add to Queue"**, **drag a song up in "Up Next"**, **skip ahead**, or blend your playlist with a friend's on **Spotify, YouTube Music, or Apple Music** — or when a backend worker schedules tasks in a **job queue**:

- Duplicate tracks shouldn't pile up unintentionally.
- Reordering tracks by drag-and-drop must validate indices cleanly.
- Skipping or cycling through tracks wraps around like a ring buffer.
- Most importantly, in modern reactive UI architectures (Redux, React state, undo/redo stacks) and testable Python backends, **queue transformations must be pure (non-mutating)** — returning a *brand-new list* so previous snapshots are never corrupted by hidden side effects!

In this checkpoint, you will build a pure, immutable-style Music Streaming Queue Engine.

---

## Problem Statement

Design and implement six pure list-transformation functions for a music streaming queue (`list[str]` of track titles/IDs): adding tracks with optional deduplication, order-preserving deduplication, index-based track moving, left/right cyclic rotation, playing the next track, and interleaving two queues like a smart radio mixer. **No function may mutate its input list(s)!**

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study [`worked_example.py`](worked_example.py) — a **Print-Shop Job Queue Manager**.

A busy print shop manages print jobs (`"JOB-101"`, `"JOB-102"`, ...) where staff can append new jobs, deduplicate accidental double-submissions, bump rush orders to the front, cancel jobs, and rotate batches across shifts — all **without mutating** any caller's list!

### Key Architectural Patterns in `worked_example.py`

1. **Copy-Before-Transform Discipline:**
   Every function builds a fresh list (`list(queue)`, comprehensions, or slice concatenation `queue[k:] + queue[:k]`) so the original list passed by the caller is guaranteed unchanged.
2. **Order-Preserving Deduplication (`deduplicate_jobs`):**
   Using `list(set(queue))` destroys playback order! Instead, keep a `seen: set[str]` alongside a `result: list[str]` to filter duplicates in `O(n)` time while preserving first-seen order.
3. **Modulo Wrap-Around Rotation (`rotate_batch`):**
   Normalizing `shift = shift % len(queue)` handles shifts larger than the queue length AND negative shifts (Python's `%` always yields `0 <= k < len(queue)` for positive `len(queue)`!), letting `queue[k:] + queue[:k]` handle both left and right rotations cleanly!

Run the reference demo:

```bash
python master_projects/checkpoint_09_playlist_queue_engine/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the six **pure, non-mutating** functions in [`project.py`](project.py).

> **Golden Rule:** None of your functions may mutate `queue`, `new_tracks`, `q1`, or `q2` in place!

### 1. `add_tracks(queue: list[str], new_tracks: list[str], allow_duplicates: bool = False) -> list[str]`
- Return a **new** list containing `queue` followed by tracks from `new_tracks`.
- If `allow_duplicates=False`: skip any track from `new_tracks` that is already in `queue` OR already added from earlier in `new_tracks` (preserving order).
- If `allow_duplicates=True`: append all tracks from `new_tracks` as-is.

### 2. `deduplicate_queue(queue: list[str]) -> list[str]`
- Return a **new** list containing only the **first** occurrence of each track in `queue`, preserving original order.

### 3. `move_track(queue: list[str], old_index: int, new_index: int) -> list[str]`
- Return a **new** list where the track at `old_index` is removed and inserted at `new_index`.
- **Strict bounds validation:** Both `old_index` and `new_index` must satisfy `0 <= index < len(queue)`. Raise `IndexError` if either index is negative, `>= len(queue)`, or if `queue` is empty.
- Examples:
  - `move_track(["A", "B", "C", "D"], 3, 1)` -> `["A", "D", "B", "C"]`
  - `move_track(["A", "B", "C", "D"], 0, 2)` -> `["B", "C", "A", "D"]`

### 4. `rotate_queue(queue: list[str], steps: int) -> list[str]`
- Rotate `queue` **left** by `steps` positions (e.g. skipping forward `steps` tracks and moving skipped tracks to the end).
- Negative `steps` rotates **right** (bringing tracks from the back to the front).
- Wrap `steps` cleanly when `abs(steps) >= len(queue)`.
- If `queue` is empty, return a new empty list `[]`.
- Examples:
  - `rotate_queue(["A", "B", "C", "D"], 1)` -> `["B", "C", "D", "A"]`
  - `rotate_queue(["A", "B", "C", "D"], -1)` -> `["D", "A", "B", "C"]`

### 5. `play_next(queue: list[str]) -> tuple[str | None, list[str]]`
- Return `(current_track, remaining_queue)`.
- If `queue` is empty, return `(None, [])`.
- Otherwise return `(queue[0], queue[1:])`.

### 6. `interleave_queues(q1: list[str], q2: list[str]) -> list[str]`
- Return a **new** list alternating tracks from `q1` and `q2`: `[q1[0], q2[0], q1[1], q2[1], ...]`.
- If one queue is longer, append its remaining tracks in order at the end.

---

## Running Tests

From the `ExamPrep/` directory:

```bash
python -m unittest master_projects/checkpoint_09_playlist_queue_engine/test_project.py -v
```
