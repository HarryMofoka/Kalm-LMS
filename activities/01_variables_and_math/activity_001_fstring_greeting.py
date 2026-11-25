"""
Activity 001: Greeting & String Interpolation (f-strings)
Difficulty: 1 / 132 (Rank 1 - Absolute Beginner)

Context:
Every great piece of software starts by talking to its user! Whether you are
building a coding bootcamp welcome screen or an RPG multiplayer lobby, Python
f-strings (formatted string literals) let you drop variables straight into text
without clunky string concatenation (`+`) or manual `str(...)` calls.

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write a function `example_welcome_banner(name, language)` that returns a warm
welcome message formatted exactly as:
    "Hello, <name>! Welcome to <language> programming."

Step-by-step walkthrough:
1. Prefix the string literal with the letter `f`: `f"..."`.
2. Inside the string, place variable names inside curly braces `{name}` and
   `{language}`. Python automatically evaluates each expression and converts
   it to text.
3. Return the resulting string directly — no need to store it in a temporary
   variable unless it improves clarity, and NEVER use `print()` instead of
   `return` when a function is expected to hand back a value!

Edge cases:
- Multi-word names (e.g., `"Ada Lovelace"`) work automatically because `{name}`
  inserts the exact string unchanged.
- Empty strings (e.g., `""`) still produce a valid formatted string without
  crashing.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
You are building the lobby HUD for an indie fantasy RPG. Write a function
`solve_gamer_badge(username, level, guild)` that returns a formatted player
badge string with the exact format:
    "Player <username> (Lv.<level>) - Guild: <guild>"

Rules:
- `username` is a string (e.g., `"ShadowFox"`).
- `level` is an integer (e.g., `42`). Notice f-strings convert ints for you!
- `guild` is a string (e.g., `"Iron Owls"`).
- Pay close attention to capitalization, spaces, parentheses, dot, and hyphen.

Examples:
- `solve_gamer_badge("ShadowFox", 42, "Iron Owls")`
  -> `"Player ShadowFox (Lv.42) - Guild: Iron Owls"`
- `solve_gamer_badge("Nova", 1, "Wanderers")`
  -> `"Player Nova (Lv.1) - Guild: Wanderers"`

Hints:
- Remember: return the string; do not print it.
- Watch the period right after `Lv` with NO space before the number: `(Lv.42)`.
"""

from __future__ import annotations


def example_welcome_banner(name: str, language: str) -> str:
    """Return a formatted welcome banner for a learner."""
    # Prefixing the string with `f` lets Python interpolate {name} and {language}.
    return f"Hello, {name}! Welcome to {language} programming."


def solve_gamer_badge(username: str, level: int, guild: str) -> str:
    """Return a formatted RPG badge: 'Player <username> (Lv.<level>) - Guild: <guild>'."""
    pass


if __name__ == "__main__":
    print(example_welcome_banner("Ada", "Python"))
    print(example_welcome_banner("Grace Hopper", "COBOL"))
