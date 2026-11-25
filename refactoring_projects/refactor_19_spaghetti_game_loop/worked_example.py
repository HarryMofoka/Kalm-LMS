"""Worked Example (RF 19): Global-variable rover game -> pure state transitions.

Compare `before_step_rover` / `before_run_rover` (mutating module globals)
with `after_step_rover` / `after_run_rover` (pure functions returning new state).
"""

ROVER_POS = 0
ROVER_STEPS = 0


def before_step_rover(command):
    """Messy version: mutates module-level globals directly."""
    global ROVER_POS, ROVER_STEPS
    if command == "R":
        ROVER_POS += 1
    elif command == "L":
        ROVER_POS = max(0, ROVER_POS - 1)
    ROVER_STEPS += 1


def before_run_rover(commands):
    """Resets globals and runs commands through the global-mutating helper."""
    global ROVER_POS, ROVER_STEPS
    ROVER_POS = 0
    ROVER_STEPS = 0
    for cmd in commands:
        before_step_rover(cmd)
    return {"pos": ROVER_POS, "steps": ROVER_STEPS}


def after_step_rover(state, command):
    """Clean pure transition: returns a fresh state dict without mutating inputs or globals."""
    pos = state["pos"]
    if command == "R":
        pos += 1
    elif command == "L":
        pos = max(0, pos - 1)
    return {"pos": pos, "steps": state["steps"] + 1}


def after_run_rover(commands):
    """Clean runner built by threading pure state through `after_step_rover`."""
    state = {"pos": 0, "steps": 0}
    for cmd in commands:
        state = after_step_rover(state, cmd)
    return state


if __name__ == "__main__":
    cmds = ["R", "R", "L", "R"]
    print("Before:", before_run_rover(cmds))
    print("After: ", after_run_rover(cmds))

    # Two independent rovers interleaved cleanly using pure state transitions:
    rover_a = {"pos": 0, "steps": 0}
    rover_b = {"pos": 10, "steps": 0}
    rover_a = after_step_rover(rover_a, "R")
    rover_b = after_step_rover(rover_b, "L")
    rover_a = after_step_rover(rover_a, "R")
    print("Interleaved Rover A:", rover_a)
    print("Interleaved Rover B:", rover_b)
