"""Legacy procedural bug/task tracker — raw nested dicts, magic codes, zero validation.

TODO (Mission 20):
- Introduce clean encapsulated `Task` and `TaskBoard` classes with `__repr__`,
  duplicate-ID checks, and priority validation (`"low"`, `"medium"`, `"high"`).
- Refactor the 5 top-level facade functions to delegate cleanly to `TaskBoard`
  so all existing callers keep working seamlessly.
"""


def create_board():
    """Create and return a brand-new task board."""
    # SMELL: raw unstructured dictionary passed into every function!
    return {"items": []}


def add_task(board, task_id, title, priority):
    """Add a task to the board."""
    # SMELL: cryptic keys ("t", "p", "st"), magic status "O", zero validation!
    board["items"].append({
        "id": task_id,
        "t": title,
        "p": priority,
        "st": "O",
    })


def complete_task(board, task_id):
    """Mark the matching task done; return True if found, else False."""
    # SMELL: duplicated linear scan + magic string "D"!
    for item in board["items"]:
        if item["id"] == task_id:
            item["st"] = "D"
            return True
    return False


def get_open_tasks(board):
    """Return a list of open task dicts with keys 'id', 'title', 'priority'."""
    result = []
    for item in board["items"]:
        if item["st"] == "O":
            result.append({
                "id": item["id"],
                "title": item["t"],
                "priority": item["p"],
            })
    return result


def board_summary(board):
    """Return a count summary dict: {'total': ..., 'open': ..., 'done': ...}."""
    total = 0
    open_cnt = 0
    done_cnt = 0
    for item in board["items"]:
        total += 1
        if item["st"] == "O":
            open_cnt += 1
        elif item["st"] == "D":
            done_cnt += 1
    return {"total": total, "open": open_cnt, "done": done_cnt}
