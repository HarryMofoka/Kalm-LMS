# Refactoring Mission 20 — Procedural to OOP Rescue (CP 20)

## Backstory & Problem Statement

A startup's internal bug/task tracker (`messy_code.py`) grew out of a quick procedural script. Every function passes around raw nested dictionaries with cryptic keys (`"id"`, `"t"`, `"p"`, `"st"`) and magic status codes (`"O"` for open, `"D"` for done).

Because there are no domain classes or invariants:
- Duplicate task IDs silently pile up in the list.
- Typo priorities like `"urgent"` or `"SUPERHIGH"` slip in unchecked.
- Every function repeats the exact same linear search loop over `board["items"]`.

Even trickier: **existing scripts already call the 5 procedural functions** (`create_board`, `add_task`, `complete_task`, `get_open_tasks`, `board_summary`). In real-world software engineering, you refactor safely using the **Strangler Fig / Facade pattern**: introduce clean OOP domain classes (`Task` and `TaskBoard`) and delegate the 5 top-level facade functions to them so zero callers break!

---

## Code Smells Checklist

- [ ] **Primitive obsession & sprawling raw dicts** (`{"id": ..., "t": ..., "p": ..., "st": "O"}`) passed into every function.
- [ ] **Magic status strings** (`"O"`, `"D"`) instead of a clear boolean `done` attribute on a `Task` object.
- [ ] **Zero validation** — silently accepts duplicate task IDs and invalid priorities.
- [ ] **Duplicated linear lookup loops** across `complete_task`, `get_open_tasks`, and `board_summary`.

---

## Worked Refactoring Walkthrough (`worked_example.py`)

In `worked_example.py`, we rescue a procedural dict-based library catalog into clean `Book` and `Library` classes while keeping a backwards-compatible facade:

### Before (raw dicts & magic status flags)
```python
def before_create_library():
    return {"books": []}

def before_add_book(lib, isbn, title):
    lib["books"].append({"isbn": isbn, "ttl": title, "avail": 1})

def before_checkout(lib, isbn):
    for b in lib["books"]:
        if b["isbn"] == isbn and b["avail"] == 1:
            b["avail"] = 0
            return True
    return False
```

### After (encapsulated `Book` & `Library` + thin facade)
```python
class Book:
    def __init__(self, isbn, title, available=True):
        self.isbn = isbn
        self.title = title
        self.available = available

    def __repr__(self):
        return f"Book({self.isbn!r}, {self.title!r}, available={self.available!r})"

class Library:
    def __init__(self):
        self._books = {}

    def add_book(self, isbn, title):
        if isbn in self._books:
            raise ValueError(f"Duplicate ISBN: {isbn}")
        book = Book(isbn, title)
        self._books[isbn] = book
        return book
```

---

## Your Refactoring Mission

Refactor `messy_code.py` so **all three test classes pass**:

1. **`class Task`**:
   - Constructor: `Task(task_id, title, priority="medium", done=False)`.
   - Valid priorities are `"low"`, `"medium"`, `"high"` — raise **`ValueError`** for any other priority!
   - Attributes: `task_id`, `title`, `priority`, `done` (`bool`).
   - Implement a clean `__repr__(self)` including `"Task"` and `self.task_id`.

2. **`class TaskBoard`**:
   - Constructor: `TaskBoard()` (no required arguments).
   - Implement `__repr__(self)` including `"TaskBoard"`.
   - `add_task(self, task_id, title, priority="medium") -> Task`:
     - Raises **`ValueError`** on duplicate `task_id` or invalid `priority`.
     - Stores and returns the new `Task`.
   - `complete_task(self, task_id) -> bool`:
     - Marks the matching `Task` done (`done = True`) and returns `True`; returns `False` if not found.
   - `open_tasks(self) -> list[Task]`:
     - Returns a list of open (`not task.done`) `Task` instances in insertion order.
   - `summary(self) -> dict`:
     - Returns `{"total": ..., "open": ..., "done": ...}`.

3. **Keep all 5 top-level Strangler Fig facade functions delegating to `TaskBoard`**:
   - `create_board()` -> returns a `TaskBoard()` instance.
   - `add_task(board, task_id, title, priority)` -> delegates to `board.add_task(...)`.
   - `complete_task(board, task_id)` -> delegates to `board.complete_task(...)`.
   - `get_open_tasks(board)` -> returns `[{"id": t.task_id, "title": t.title, "priority": t.priority} for t in board.open_tasks()]`.
   - `board_summary(board)` -> delegates to `board.summary()`.

---

## Run the Tests

```bash
python -m unittest ExamPrep/refactoring_projects/refactor_20_procedural_to_oop_rescue/test_refactor.py
```

When you start:
- `TestWorkedExample` -> **PASS**
- `TestBehaviorSafetyNet` -> **PASS** (your safety net!)
- `TestRefactorGoals` -> **FAIL** (your refactoring targets!)

When you finish, **all 3 test classes should be GREEN**!
