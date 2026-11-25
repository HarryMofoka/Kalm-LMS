"""
Activity 127: Composition — Objects Holding Other Objects
Difficulty: 127 / 132

Real software is built from small, focused objects working together!
**Composition** ("has-a") means one class holds a collection of instances of
another class — for example, a `Playlist` *has* `Song` objects, and a
`ShoppingCart` *has* `CartItem` objects.

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExamplePlaylist holding ExampleSong Objects
===============================================================================
Problem:
    Build two collaborating classes:
      - `ExampleSong(title, artist, duration_sec)`: validates `duration_sec > 0`.
      - `ExamplePlaylist(name)`: holds a list of `ExampleSong` objects with
        `add_song(song)`, `total_duration()`, `titles()`, and
        `remove_by_title(title) -> bool`.

Step-by-Step Breakdown:
    1. Each class owns ONE clear responsibility: `ExampleSong` knows song details;
       `ExamplePlaylist` manages the collection and aggregates durations.
    2. Notice `remove_by_title`: iterating with `enumerate` lets us pop the first
       matching song cleanly and return `True` (or `False` if not found).

===============================================================================
PART 2: YOUR TURN ("YOU DO") — ShoppingCart holding CartItem Objects
===============================================================================
Problem:
    Implement `CartItem` and `ShoppingCart`:

    1. `CartItem`:
       - `__init__(self, name: str, unit_price: float, quantity: int = 1) -> None`
         * Raises `ValueError` if `not name.strip()`, `unit_price < 0`, or `quantity <= 0`.
         * Stores `self.name = name.strip()`, `self.unit_price = float(unit_price)`,
           `self.quantity = quantity`.
       - `line_total(self) -> float`
         * Returns `round(self.unit_price * self.quantity, 2)`.

    2. `ShoppingCart`:
       - `__init__(self, tax_rate: float = 0.0) -> None`
         * Raises `ValueError` if `tax_rate < 0` or `tax_rate > 1`.
         * Stores `self.tax_rate = float(tax_rate)` and `self.items: list[CartItem] = []`.
       - `add_item(self, item: CartItem) -> None`
         * Appends `item` to `self.items`.
       - `remove_by_name(self, name: str) -> bool`
         * Removes the FIRST `CartItem` whose `item.name == name` and returns
           `True`; returns `False` if no item matches.
       - `subtotal(self) -> float`
         * Returns `round(sum(item.line_total() for item in self.items), 2)`.
       - `tax_amount(self) -> float`
         * Returns `round(self.subtotal() * self.tax_rate, 2)`.
       - `total(self) -> float`
         * Returns `round(self.subtotal() + self.tax_amount(), 2)`.

    Examples:
        cart = ShoppingCart(tax_rate=0.15)
        cart.add_item(CartItem("Notebook", 25.0, quantity=2))  # 50.0
        cart.add_item(CartItem("Pen", 5.0, quantity=4))        # 20.0
        cart.subtotal()            -> 70.0
        cart.tax_amount()          -> 10.5
        cart.total()               -> 80.5
        cart.remove_by_name("Pen") -> True
        cart.subtotal()            -> 50.0
        cart.remove_by_name("Pen") -> False

    Edge-case hints:
        - Empty cart has `subtotal() == 0.0`, `tax_amount() == 0.0`, `total() == 0.0`.
        - Free promotional items (`unit_price == 0`) are allowed (`unit_price < 0` is not).
"""
from __future__ import annotations


class ExampleSong:
    """A single song track with title, artist, and duration in seconds."""

    def __init__(self, title: str, artist: str, duration_sec: int) -> None:
        if not title.strip() or not artist.strip() or duration_sec <= 0:
            raise ValueError("invalid song attributes")
        self.title = title.strip()
        self.artist = artist.strip()
        self.duration_sec = duration_sec


class ExamplePlaylist:
    """A playlist composed of ExampleSong instances."""

    def __init__(self, name: str) -> None:
        if not name.strip():
            raise ValueError("playlist name must not be blank")
        self.name = name.strip()
        self.songs: list[ExampleSong] = []

    def add_song(self, song: ExampleSong) -> None:
        """Append a song to the playlist."""
        self.songs.append(song)

    def total_duration(self) -> int:
        """Return combined duration of all songs in seconds."""
        return sum(song.duration_sec for song in self.songs)

    def titles(self) -> list[str]:
        """Return list of song titles in playlist order."""
        return [song.title for song in self.songs]

    def remove_by_title(self, title: str) -> bool:
        """Remove the first song matching `title`; return True if removed."""
        for index, song in enumerate(self.songs):
            if song.title == title:
                self.songs.pop(index)
                return True
        return False


class CartItem:
    """One line item inside a shopping cart."""

    def __init__(self, name: str, unit_price: float, quantity: int = 1) -> None:
        """Validate and store item name, unit_price, and quantity."""
        pass

    def line_total(self) -> float:
        """Return unit_price * quantity rounded to 2 decimal places."""
        pass


class ShoppingCart:
    """A shopping cart composed of CartItem instances with subtotal, tax, and removal."""

    def __init__(self, tax_rate: float = 0.0) -> None:
        """Initialize empty cart with 0 <= tax_rate <= 1."""
        pass

    def add_item(self, item: CartItem) -> None:
        """Add a CartItem to the cart."""
        pass

    def remove_by_name(self, name: str) -> bool:
        """Remove the first item with matching name; return True if found, else False."""
        pass

    def subtotal(self) -> float:
        """Return sum of item line totals rounded to 2 decimals."""
        pass

    def tax_amount(self) -> float:
        """Return subtotal * tax_rate rounded to 2 decimals."""
        pass

    def total(self) -> float:
        """Return subtotal + tax_amount rounded to 2 decimals."""
        pass


if __name__ == "__main__":
    pl = ExamplePlaylist("Study Beats")
    pl.add_song(ExampleSong("Focus Flow", "LoFi Lab", 180))
    pl.add_song(ExampleSong("Night Code", "Synth Club", 240))
    print(f"{pl.name}: {pl.titles()} ({pl.total_duration()}s)")
