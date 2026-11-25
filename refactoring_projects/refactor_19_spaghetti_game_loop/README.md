# Refactoring Mission 19 — Spaghetti Game Loop (CP 19)

## Backstory & Problem Statement

An arcade robotics prototype simulates a robot navigating a 2D grid arena (`messy_code.py`). Whoever built the prototype stored the robot's entire world inside module-level global variables (`ROBOT_R`, `ROBOT_C`, `SCORE`, `GRID`) and scattered **five `global` statements** across tightly-coupled helper functions!

Right now, `run_commands(width, height, commands)` barely survives single-robot tests because it remembers to wipe the globals at the start of every call. The moment the game tries to track **two robots at once** — or run single step transitions cleanly — everything clobbers everything else!

Your mission: eliminate every `global` statement and mutable module-level state, extract a pure `step_robot(pos, command, width, height)` transition function, and rebuild `run_commands` on clean local state!

---

## Code Smells Checklist

- [ ] **Mutable module-level globals** (`ROBOT_R`, `ROBOT_C`, `SCORE`, `GRID`) acting as hidden shared state.
- [ ] **5 `global` statements** making helper functions unpredictable and untestable in isolation.
- [ ] **Impossible to interleave two simulations** without clobbering each other's coordinates and scores.
- [ ] **No pure transition function** (`(pos, command, width, height) -> new_pos`) that works independently of the game loop.

---

## Worked Refactoring Walkthrough (`worked_example.py`)

In `worked_example.py`, we refactor a 1D rover counter game from globals to pure state transitions:

### Before (mutates module globals!)
```python
ROVER_POS = 0
ROVER_STEPS = 0

def before_step_rover(command):
    global ROVER_POS, ROVER_STEPS
    if command == "R":
        ROVER_POS += 1
    elif command == "L":
        ROVER_POS = max(0, ROVER_POS - 1)
    ROVER_STEPS += 1
```

### After (pure state transition — zero globals!)
```python
def after_step_rover(state, command):
    pos = state["pos"]
    if command == "R":
        pos += 1
    elif command == "L":
        pos = max(0, pos - 1)
    return {"pos": pos, "steps": state["steps"] + 1}
```

With pure state transitions, you can run ten independent rovers side by side — each owns its own state value, and every helper is trivially testable!

---

## Your Refactoring Mission

Refactor `messy_code.py` so **all three test classes pass**:

1. **Zero `global` statements & zero mutable module-level state**:
   - Delete `ROBOT_R`, `ROBOT_C`, `SCORE`, `GRID` (module-level *immutable* constants like direction deltas are fine, as long as calling `run_commands` never mutates any module global!).
   - `messy_code.py` must contain **zero `global` statements**.

2. **`step_robot(pos, command, width, height)`**:
   - Pure helper taking `pos = (row, col)`, a command string (`"U"`, `"D"`, `"L"`, `"R"`), and grid dimensions `width`, `height`.
   - Returns a **new `(row, col)` tuple** clamped safely inside `0 <= row < height` and `0 <= col < width` (bumping into a wall keeps the robot in place; unknown commands leave `pos` unchanged).
   - Never mutates any globals.

3. **`run_commands(width, height, commands)`**:
   - Keep the exact behavioral contract using pure local variables (`pos = (0, 0)`, `visited = {(0, 0)}`) and calling `step_robot`:
     - If `width <= 0 or height <= 0`: return `{"position": None, "visited_count": 0}`.
     - Otherwise return `{"position": (row, col), "visited_count": len(visited)}`.

---

## Run the Tests

```bash
python -m unittest ExamPrep/refactoring_projects/refactor_19_spaghetti_game_loop/test_refactor.py
```

When you start:
- `TestWorkedExample` -> **PASS**
- `TestBehaviorSafetyNet` -> **PASS** (your safety net!)
- `TestRefactorGoals` -> **FAIL** (your refactoring targets!)

When you finish, **all 3 test classes should be GREEN**!
