"""Worked Example (RF 20): Procedural library dicts -> clean Book & Library classes.

Shows how to replace raw dict-passing procedures with encapsulated domain classes
while optionally keeping a thin backwards-compatible facade.
"""


# ---------------------------------------------------------------------------
# BEFORE: Sprawling procedural dict manipulation with magic flags
# ---------------------------------------------------------------------------
def before_create_library():
    return {"books": []}


def before_add_book(lib, isbn, title):
    lib["books"].append({"isbn": isbn, "ttl": title, "avail": 1})


def before_checkout(lib, isbn):
    for b in lib["books"]:
        if b["isbn"] == isbn and b["avail"] == 1:
            b["avail"] = 0
            return True
    return False


def before_available_titles(lib):
    out = []
    for b in lib["books"]:
        if b["avail"] == 1:
            out.append(b["ttl"])
    return out


# ---------------------------------------------------------------------------
# AFTER: Encapsulated OOP classes (`Book`, `Library`) + thin facade wrappers
# ---------------------------------------------------------------------------
class Book:
    """Represents a single cataloged book and its checkout status."""

    def __init__(self, isbn, title, available=True):
        self.isbn = isbn
        self.title = title
        self.available = available

    def __repr__(self):
        return f"Book({self.isbn!r}, {self.title!r}, available={self.available!r})"


class Library:
    """Manages unique books by ISBN with clean validation and lookup."""

    def __init__(self):
        self._books = {}

    def __repr__(self):
        return f"Library(total={len(self._books)})"

    def add_book(self, isbn, title):
        if isbn in self._books:
            raise ValueError(f"Duplicate ISBN: {isbn}")
        book = Book(isbn, title)
        self._books[isbn] = book
        return book

    def checkout(self, isbn):
        book = self._books.get(isbn)
        if book is None or not book.available:
            return False
        book.available = False
        return True

    def available_titles(self):
        return [b.title for b in self._books.values() if b.available]


def after_create_library():
    return Library()


def after_add_book(lib, isbn, title):
    return lib.add_book(isbn, title)


def after_checkout(lib, isbn):
    return lib.checkout(isbn)


def after_available_titles(lib):
    return lib.available_titles()


if __name__ == "__main__":
    old_lib = before_create_library()
    before_add_book(old_lib, "978-1", "Clean Code")
    before_add_book(old_lib, "978-2", "Refactoring")
    before_checkout(old_lib, "978-1")
    print("Before available:", before_available_titles(old_lib))

    new_lib = after_create_library()
    after_add_book(new_lib, "978-1", "Clean Code")
    after_add_book(new_lib, "978-2", "Refactoring")
    after_checkout(new_lib, "978-1")
    print("After available: ", after_available_titles(new_lib))
    print("Library repr:    ", repr(new_lib))
