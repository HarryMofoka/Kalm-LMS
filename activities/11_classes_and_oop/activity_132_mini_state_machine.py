"""
Activity 132: Mini Finite-State Machine Class  [Unlocks Checkpoint 20 — FINAL!]
Difficulty: 132 / 132

CONGRATULATIONS ON REACHING ACTIVITY 132 OF 132!
In real production systems — checkout pipelines, game AI, network protocols,
approval engines — objects move through well-defined **states**, and only
specific **transitions** are legal! Modeling allowed transitions in a data table
makes bugs impossible and keeps your state machine crystal clear.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleTrafficLight
===============================================================================
Problem:
    Build `ExampleTrafficLight(initial="RED")` cycling through:
        RED -> GREEN -> YELLOW -> RED
      - Validates initial state is in `{"RED", "GREEN", "YELLOW"}` (else `ValueError`).
      - `advance() -> str`: moves to the next state, logs it in `self.history`,
        and returns the new state.
      - `can_go() -> bool`: True only when `self.state == "GREEN"`.

Step-by-Step Breakdown:
    1. Keep the transition table as a class constant `_NEXT_STATE = {...}` —
       no tangled chains of `if/elif`!
    2. Every state change updates BOTH `self.state` and `self.history` in one
       single place.

===============================================================================
PART 2: YOUR TURN ("YOU DO") — OrderWorkflow State Machine
===============================================================================
Problem:
    Implement `OrderWorkflow` modeling an e-commerce order lifecycle!

    VALID STATES & ALLOWED TRANSITIONS:
        "DRAFT"     -> {"PAID", "CANCELLED"}
        "PAID"      -> {"SHIPPED", "CANCELLED"}
        "SHIPPED"   -> {"DELIVERED"}          # Cannot cancel once shipped!
        "DELIVERED" -> set()                  # Terminal state!
        "CANCELLED" -> set()                  # Terminal state!

    Interface:
      - `__init__(self, order_id: str) -> None`
        * Raises `ValueError` if `not order_id.strip()`.
        * Stores `self.order_id = order_id.strip()`,
          `self.state = "DRAFT"`,
          and `self.history: list[str] = ["DRAFT"]`.
      - `can_transition_to(self, next_state: str) -> bool`
        * Returns `True` iff `next_state` is in the allowed next states for
          `self.state` (returns `False` for unknown states, self-transitions,
          or transitions from terminal states).
      - `transition_to(self, next_state: str) -> str`
        * If `not self.can_transition_to(next_state)`: raise `ValueError(...)`
          and leave `self.state` and `self.history` unchanged!
        * Otherwise set `self.state = next_state`, append `next_state` to
          `self.history`, and return `self.state`.
      - `is_terminal(self) -> bool`
        * Returns `True` iff `self.state in {"DELIVERED", "CANCELLED"}`.

    Examples:
        order = OrderWorkflow("ORD-1001")
        order.state                        -> "DRAFT"
        order.can_transition_to("PAID")    -> True
        order.can_transition_to("SHIPPED") -> False   # must pay first!
        order.transition_to("PAID")        -> "PAID"
        order.transition_to("SHIPPED")     -> "SHIPPED"
        order.transition_to("CANCELLED")   -> raises ValueError!
        order.transition_to("DELIVERED")   -> "DELIVERED"
        order.is_terminal()                -> True
        order.history                      -> ["DRAFT", "PAID", "SHIPPED", "DELIVERED"]

    Edge-case hints:
        - Check `can_transition_to` BEFORE mutating `self.state` or `self.history`.
        - Unknown states like `"REFUNDED"` must return `False` from
          `can_transition_to` and raise `ValueError` in `transition_to`.
        - Cancelling is valid from `"DRAFT"` or `"PAID"`, NEVER from
          `"SHIPPED"`, `"DELIVERED"`, or `"CANCELLED"`!
"""
from __future__ import annotations


class ExampleTrafficLight:
    """A cyclic traffic-light state machine: RED -> GREEN -> YELLOW -> RED."""

    _NEXT_STATE: dict[str, str] = {
        "RED": "GREEN",
        "GREEN": "YELLOW",
        "YELLOW": "RED",
    }

    def __init__(self, initial: str = "RED") -> None:
        if initial not in self._NEXT_STATE:
            raise ValueError(f"invalid initial light state: {initial!r}")
        self.state = initial
        self.history: list[str] = [initial]

    def advance(self) -> str:
        """Advance to the next light state, record it, and return it."""
        self.state = self._NEXT_STATE[self.state]
        self.history.append(self.state)
        return self.state

    def can_go(self) -> bool:
        """Return True iff traffic may proceed (state is GREEN)."""
        return self.state == "GREEN"


class OrderWorkflow:
    """Finite-state machine for e-commerce order transitions."""

    def __init__(self, order_id: str) -> None:
        """Validate non-blank order_id and start in state 'DRAFT'."""
        pass

    def can_transition_to(self, next_state: str) -> bool:
        """Return True iff transitioning from self.state to next_state is allowed."""
        pass

    def transition_to(self, next_state: str) -> str:
        """Move to next_state if allowed (updating history), else raise ValueError."""
        pass

    def is_terminal(self) -> bool:
        """Return True if order is in a terminal state ('DELIVERED' or 'CANCELLED')."""
        pass


if __name__ == "__main__":
    light = ExampleTrafficLight()
    for _ in range(4):
        print(f"State={light.state:6s} can_go={light.can_go()}")
        light.advance()
    print("History:", light.history)
