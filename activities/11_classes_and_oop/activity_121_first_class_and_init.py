"""
Activity 121: Your First Class & __init__
Difficulty: 121 / 132

Welcome to Module 11: Classes & Object-Oriented Programming!
A **class** is a blueprint that bundles DATA (attributes like `self.title`)
together with BEHAVIOR (methods like `summary()`). Every time you call
`ExampleBook(...)`, Python creates a brand-new object and runs `__init__` to
set up its starting attributes.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleBook
===============================================================================
Problem:
    Build `ExampleBook(title, author, pages)` with:
      - Attributes `self.title`, `self.author`, `self.pages`
      - `summary() -> str`: returns `f"'{self.title}' by {self.author} ({self.pages} pages)"`
      - `is_long() -> bool`: returns `True` if `self.pages >= 300`, else `False`

Step-by-Step Breakdown:
    1. `self` is always the first parameter of every instance method — it refers
       to the specific object being created or called.
    2. Inside `__init__`, assigning `self.title = title` saves `title` on that
       instance so other methods can read it later.
    3. Methods like `summary(self)` read `self.title`, `self.author`, `self.pages`
       without needing those values passed again!

===============================================================================
PART 2: YOUR TURN ("YOU DO") — MovieTicket
===============================================================================
Problem:
    Implement the `MovieTicket` class for a cinema booking system:
      - `__init__(self, movie: str, price: float) -> None`
        * Raises `ValueError` if `price < 0`.
        * Stores `self.movie = movie` and `self.price = float(price)`.
      - `apply_discount(self, pct: float) -> float`
        * Raises `ValueError` if `pct < 0` or `pct > 100`.
        * Reduces `self.price` by `pct` percent, rounded to 2 decimal places:
              self.price = round(self.price * (1 - pct / 100), 2)
        * Returns the updated `self.price`.
      - `label(self) -> str`
        * Returns `f"{self.movie} - ${self.price:.2f}"`.

    Examples:
        ticket = MovieTicket("Dune", 120.0)
        ticket.movie                -> "Dune"
        ticket.price                -> 120.0
        ticket.label()              -> "Dune - $120.00"
        ticket.apply_discount(25)   -> 90.0
        ticket.price                -> 90.0
        ticket.label()              -> "Dune - $90.00"
        ticket.apply_discount(100)  -> 0.0

    Edge-case hints:
        - `pct == 0` leaves price unchanged; `pct == 100` sets price to `0.0`.
        - Negative `price` in `__init__` or `pct < 0` / `pct > 100` in
          `apply_discount` MUST raise `ValueError`.
        - Calling `apply_discount` twice compounds on the updated `self.price`!
"""
from __future__ import annotations


class ExampleBook:
    """A simple book record demonstrating __init__ and instance methods."""

    def __init__(self, title: str, author: str, pages: int) -> None:
        self.title = title
        self.author = author
        self.pages = pages

    def summary(self) -> str:
        """Return a human-friendly description of the book."""
        return f"'{self.title}' by {self.author} ({self.pages} pages)"

    def is_long(self) -> bool:
        """Return True if the book has at least 300 pages."""
        return self.pages >= 300


class MovieTicket:
    """A cinema ticket with movie title, price, and percentage discounts."""

    def __init__(self, movie: str, price: float) -> None:
        """Initialize the ticket, rejecting negative prices with ValueError."""
        pass

    def apply_discount(self, pct: float) -> float:
        """Apply a 0..100 percentage discount, update self.price, and return it."""
        pass

    def label(self) -> str:
        """Return formatted label '<movie> - $<price:.2f>'."""
        pass


if __name__ == "__main__":
    book = ExampleBook("Clean Code", "Robert C. Martin", 464)
    print(book.summary())
    print("Long book?", book.is_long())
