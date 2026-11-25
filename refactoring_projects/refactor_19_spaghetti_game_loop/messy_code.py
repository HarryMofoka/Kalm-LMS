"""Legacy robot arena simulator — tangled module-level globals everywhere!

TODO (Mission 19):
- Remove all mutable module globals (`ROBOT_R`, `ROBOT_C`, `SCORE`, `GRID`)
  and every `global` statement.
- Extract pure helper `step_robot(pos, command, width, height)` returning a new
  `(row, col)` tuple clamped within bounds.
- Rebuild `run_commands(width, height, commands)` using pure local state.
"""

ROBOT_R = 0
ROBOT_C = 0
SCORE = 0
GRID = []


def _reset_arena(width, height):
    global ROBOT_R, ROBOT_C, SCORE, GRID
    ROBOT_R = 0
    ROBOT_C = 0
    SCORE = 0
    GRID = [[0 for _ in range(width)] for _ in range(height)]


def _mark_current_cell():
    global SCORE, GRID
    if GRID[ROBOT_R][ROBOT_C] == 0:
        GRID[ROBOT_R][ROBOT_C] = 1
        SCORE += 1


def _move_vertical(cmd, height):
    global ROBOT_R
    if cmd == "U":
        if ROBOT_R > 0:
            ROBOT_R -= 1
    elif cmd == "D":
        if ROBOT_R < height - 1:
            ROBOT_R += 1


def _move_horizontal(cmd, width):
    global ROBOT_C
    if cmd == "L":
        if ROBOT_C > 0:
            ROBOT_C -= 1
    elif cmd == "R":
        if ROBOT_C < width - 1:
            ROBOT_C += 1


def run_commands(width, height, commands):
    """Simulate a robot starting at (0, 0) executing U/D/L/R commands on a width x height grid."""
    global ROBOT_R, ROBOT_C, SCORE
    if width <= 0 or height <= 0:
        return {"position": None, "visited_count": 0}

    _reset_arena(width, height)
    _mark_current_cell()

    for cmd in commands:
        if cmd in ("U", "D"):
            _move_vertical(cmd, height)
        elif cmd in ("L", "R"):
            _move_horizontal(cmd, width)
        _mark_current_cell()

    return {"position": (ROBOT_R, ROBOT_C), "visited_count": SCORE}
