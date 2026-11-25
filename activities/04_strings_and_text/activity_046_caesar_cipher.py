"""
Activity 046: Caesar Cipher Encryption & Decryption
Difficulty: 46 / 132

Context:
    Julius Caesar shifted alphabet letters to hide military messages. Shifting
    characters with `ord()`, `chr()`, and modulo `% 26` is a classic test of
    ASCII arithmetic and wrap-around logic.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — Lowercase Caesar Shift
===============================================================================
Problem:
    Shift every lowercase ASCII letter (`'a'`–`'z'`) in `text` forward by `shift`
    positions in the alphabet, wrapping around from `'z'` back to `'a'`. Leave
    all other characters unchanged. Support positive, zero, negative, and large
    (`abs(shift) > 26`) shifts.

Step-by-Step Explanation:
    1. Convert a lowercase letter `ch` to a 0–25 index: `pos = ord(ch) - ord('a')`.
    2. Add `shift` and wrap with `% 26`: `new_pos = (pos + shift) % 26`.
       Because Python's `%` always returns a non-negative remainder in `0..25`
       even for negative numbers (e.g. `(-1) % 26 == 25`), negative shifts
       automatically decrypt cleanly!
    3. Convert back to a character: `chr(ord('a') + new_pos)`.

Edge Cases:
    - `("xyz", 3)`    -> `"abc"`  (wraps past `'z'`)
    - `("abc", -3)`   -> `"xyz"`  (negative shift decrypts cleanly)
    - `("abc", 29)`   -> `"def"`  (`29 % 26 == 3`)
    - `("hi 123", 1)` -> `"ij 123"`

===============================================================================
PART 2: YOUR TURN ("YOU DO") — Case-Preserving Caesar Cipher
===============================================================================
Problem:
    Implement `solve_caesar_cipher(text: str, shift: int) -> str`.
    Shift BOTH lowercase ASCII letters (`'a'`–`'z'`) AND uppercase ASCII letters
    (`'A'`–`'Z'`) by `shift` positions, preserving original letter case!
    All non-letter characters (spaces, digits, punctuation) must remain unchanged.
    Negative shifts decrypt, and arbitrary large shifts wrap modulo 26.

Examples:
    - `("Hello, World!", 3)`   -> `"Khoor, Zruog!"`
    - `("Khoor, Zruog!", -3)`  -> `"Hello, World!"`
    - `("Zoo 2026!", 1)`       -> `"App 2026!"`
    - `("AbC", 26)`            -> `"AbC"`
    - `("AbC", 27)`            -> `"BcD"`
    - `("AbC", -27)`           -> `"ZaB"`
    - `("", 5)`                -> `""`

Edge-Case Hints:
    - Use `base = ord("a")` for `'a' <= ch <= 'z'` and `base = ord("A")` for
      `'A' <= ch <= 'Z'`.
    - Check ASCII ranges (`'a' <= ch <= 'z'`) rather than `.islower()` if you
      want to be 100% immune to accented non-ASCII letters, or verify carefully.
"""

from __future__ import annotations


def example_caesar_lowercase(text: str, shift: int) -> str:
    """Shift lowercase ASCII letters in `text` by `shift` positions (mod 26)."""
    offset = shift % 26
    result: list[str] = []

    for ch in text:
        if "a" <= ch <= "z":
            shifted_pos = (ord(ch) - ord("a") + offset) % 26
            result.append(chr(ord("a") + shifted_pos))
        else:
            result.append(ch)
    return "".join(result)


def solve_caesar_cipher(text: str, shift: int) -> str:
    """Shift ASCII letters by `shift`, preserving uppercase/lowercase and punctuation."""
    pass


if __name__ == "__main__":
    secret = example_caesar_lowercase("attack at dawn! 09:00", 5)
    print("Encrypted:", secret)
    print("Decrypted:", example_caesar_lowercase(secret, -5))
