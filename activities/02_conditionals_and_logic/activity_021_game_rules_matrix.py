"""
Activity 021: Game Rules Matrix (RPS & RPS-Lizard-Spock)
Difficulty: 21 / 132 (Rank 3 - Logic Architect)

Context:
When a game has 5 moves, there are 5 x 5 = 25 possible matchups! Writing 25
nested `if/elif` branches is tedious and error-prone. Instead, clean Python
developers normalize inputs, check invalid moves and ties early, and encode
winning matchups concisely in a lookup structure (a dictionary or set of
winning pairs)!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_rps_winner(player1, player2)` for Rock-Paper-Scissors:
- Valid moves (case-insensitive, ignoring leading/trailing spaces):
  `"rock"`, `"paper"`, `"scissors"`.
- If either move is invalid -> return `"invalid"`.
- If both players chose the same move -> return `"tie"`.
- Otherwise return `"player1"` or `"player2"` according to classic rules:
  rock beats scissors, scissors beats paper, paper beats rock.

Step-by-step walkthrough:
1. Normalize both strings: `p1 = player1.strip().lower()`, `p2 = player2.strip().lower()`.
2. Store the winning map `beats = {"rock": "scissors", "scissors": "paper", "paper": "rock"}`.
   Notice its keys are ALSO the complete set of valid moves!
3. Guard clause: `if p1 not in beats or p2 not in beats: return "invalid"`.
4. Tie check: `if p1 == p2: return "tie"`.
5. Winner check: `if beats[p1] == p2: return "player1"`, else `return "player2"`.
   Only 10 lines of code cover all 9 valid matchups + every invalid input!

Edge cases:
- Mixed casing / whitespace like `"  Rock "` vs `"SCISSORS"` -> `"player1"`.
- Unknown move like `"gun"` -> `"invalid"` (even if both players type `"gun"`!).

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
Upgrade the referee to **Rock-Paper-Scissors-Lizard-Spock**! Write
`solve_rpsls_winner(player1, player2)` returning `"player1"`, `"player2"`,
`"tie"`, or `"invalid"`.

Valid moves (case-insensitive, strip leading/trailing whitespace):
`"rock"`, `"paper"`, `"scissors"`, `"lizard"`, `"spock"`

Complete Winning Rules (each move beats EXACTLY two other moves!):
- `"scissors"` beats `"paper"` and `"lizard"`
- `"paper"`    beats `"rock"` and `"spock"`
- `"rock"`     beats `"lizard"` and `"scissors"`
- `"lizard"`   beats `"spock"` and `"paper"`
- `"spock"`    beats `"scissors"` and `"rock"`

Rules:
- Normalize with `.strip().lower()`.
- Check validity BEFORE checking for a tie! (So `("laser", "laser")` returns
  `"invalid"`, NOT `"tie"`!)
- Return exact lowercase strings: `"player1"`, `"player2"`, `"tie"`, or `"invalid"`.

Examples:
- `solve_rpsls_winner("rock", "lizard")` -> `"player1"`
- `solve_rpsls_winner("lizard", "rock")` -> `"player2"`
- `solve_rpsls_winner("Spock", "  SPOCK ")` -> `"tie"`
- `solve_rpsls_winner("paper", "spock")` -> `"player1"`
- `solve_rpsls_winner("rock", "fire")` -> `"invalid"`

Hints:
- Map each move to a tuple or set of the TWO moves it beats:
      `beats = {"rock": ("lizard", "scissors"), ...}`
  Then `if p2 in beats[p1]: return "player1"`!
"""

from __future__ import annotations


def example_rps_winner(player1: str, player2: str) -> str:
    """Return 'player1', 'player2', 'tie', or 'invalid' for Rock-Paper-Scissors."""
    beats = {
        "rock": "scissors",
        "scissors": "paper",
        "paper": "rock",
    }
    p1 = player1.strip().lower()
    p2 = player2.strip().lower()

    # Validate before tie-checking so two identical bogus moves return 'invalid'.
    if p1 not in beats or p2 not in beats:
        return "invalid"
    if p1 == p2:
        return "tie"
    if beats[p1] == p2:
        return "player1"
    return "player2"


def solve_rpsls_winner(player1: str, player2: str) -> str:
    """Return 'player1', 'player2', 'tie', or 'invalid' for RPS-Lizard-Spock."""
    pass


if __name__ == "__main__":
    print("Rock vs Scissors ->", example_rps_winner("Rock", "scissors"))
    print("Paper vs Paper   ->", example_rps_winner("paper", "  PAPER "))
    print("Rock vs Laser    ->", example_rps_winner("rock", "laser"))
