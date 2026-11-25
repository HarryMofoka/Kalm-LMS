"""Worked Example for Checkpoint 20: Object-Oriented Library Lending System.

Demonstrates OOP domain modeling (Book, Member, Library), strict invariant
enforcement, overdue tracking, clean ``__repr__``, and structured audit logs.
"""

from __future__ import annotations


class Book:
    """A cataloged library book that can be checked out by at most one member."""

    def __init__(self, isbn: str, title: str, author: str) -> None:
        if not isbn.strip() or not title.strip() or not author.strip():
            raise ValueError("isbn, title, and author must be non-empty")
        self.isbn = isbn
        self.title = title
        self.author = author
        self.checked_out_by: str | None = None
        self.due_day: int | None = None

    @property
    def is_available(self) -> bool:
        return self.checked_out_by is None

    def __repr__(self) -> str:
        status = "available" if self.is_available else f"loaned to {self.checked_out_by}"
        return f"Book(isbn={self.isbn!r}, title={self.title!r}, status={status!r})"


class Member:
    """A registered library member with a maximum active loan limit."""

    def __init__(self, member_id: str, name: str, max_loans: int = 3) -> None:
        if not member_id.strip() or not name.strip():
            raise ValueError("member_id and name must be non-empty")
        if max_loans < 1:
            raise ValueError("max_loans must be at least 1")
        self.member_id = member_id
        self.name = name
        self.max_loans = max_loans
        self.borrowed_isbns: list[str] = []

    def __repr__(self) -> str:
        return (
            f"Member(member_id={self.member_id!r}, name={self.name!r}, "
            f"loans={len(self.borrowed_isbns)}/{self.max_loans})"
        )


class Library:
    """Manages books, members, borrow/return invariants, overdues, and audits."""

    def __init__(self) -> None:
        self.current_day: int = 0
        self.books: dict[str, Book] = {}
        self.members: dict[str, Member] = {}
        self._audit_log: list[dict] = []

    @property
    def audit_log(self) -> tuple[dict, ...]:
        """Return an immutable snapshot of all library audit events."""
        return tuple(dict(entry) for entry in self._audit_log)

    def add_book(self, isbn: str, title: str, author: str) -> Book:
        if isbn in self.books:
            raise ValueError(f"Duplicate ISBN: {isbn!r}")
        book = Book(isbn, title, author)
        self.books[isbn] = book
        self._audit_log.append(
            {"day": self.current_day, "event": "ADD_BOOK", "isbn": isbn}
        )
        return book

    def register_member(
        self, member_id: str, name: str, max_loans: int = 3
    ) -> Member:
        if member_id in self.members:
            raise ValueError(f"Duplicate member_id: {member_id!r}")
        member = Member(member_id, name, max_loans=max_loans)
        self.members[member_id] = member
        self._audit_log.append(
            {"day": self.current_day, "event": "REGISTER_MEMBER", "member_id": member_id}
        )
        return member

    def borrow_book(
        self, member_id: str, isbn: str, loan_days: int = 14
    ) -> int:
        """Check out a book atomically; returns the due day."""
        if loan_days < 1:
            raise ValueError("loan_days must be positive")
        if member_id not in self.members:
            raise KeyError(f"Unknown member: {member_id!r}")
        if isbn not in self.books:
            raise KeyError(f"Unknown book: {isbn!r}")

        member = self.members[member_id]
        book = self.books[isbn]

        if not book.is_available:
            raise ValueError(f"Book {isbn!r} is already checked out")
        if len(member.borrowed_isbns) >= member.max_loans:
            raise ValueError(f"Member {member_id!r} reached loan limit")

        due_day = self.current_day + loan_days
        book.checked_out_by = member_id
        book.due_day = due_day
        member.borrowed_isbns.append(isbn)
        self._audit_log.append(
            {
                "day": self.current_day,
                "event": "BORROW",
                "member_id": member_id,
                "isbn": isbn,
                "due_day": due_day,
            }
        )
        return due_day

    def return_book(self, member_id: str, isbn: str) -> bool:
        """Return a checked-out book; returns True if it was overdue."""
        if member_id not in self.members:
            raise KeyError(f"Unknown member: {member_id!r}")
        if isbn not in self.books:
            raise KeyError(f"Unknown book: {isbn!r}")

        member = self.members[member_id]
        book = self.books[isbn]
        if book.checked_out_by != member_id:
            raise ValueError(f"Member {member_id!r} does not hold book {isbn!r}")

        was_overdue = book.due_day is not None and self.current_day > book.due_day
        book.checked_out_by = None
        book.due_day = None
        member.borrowed_isbns.remove(isbn)
        self._audit_log.append(
            {
                "day": self.current_day,
                "event": "RETURN",
                "member_id": member_id,
                "isbn": isbn,
                "overdue": was_overdue,
            }
        )
        return was_overdue

    def advance_day(self, days: int = 1) -> int:
        if days < 0:
            raise ValueError("days cannot be negative")
        self.current_day += days
        return self.current_day

    def overdue_loans(self) -> list[tuple[str, str, int]]:
        """Return ``(member_id, isbn, days_overdue)`` for all overdue books."""
        overdue: list[tuple[str, str, int]] = []
        for book in self.books.values():
            if (
                book.checked_out_by is not None
                and book.due_day is not None
                and self.current_day > book.due_day
            ):
                overdue.append(
                    (
                        book.checked_out_by,
                        book.isbn,
                        self.current_day - book.due_day,
                    )
                )
        return overdue


if __name__ == "__main__":
    lib = Library()
    b1 = lib.add_book("978-0134685991", "Effective Python", "Brett Slatkin")
    m1 = lib.register_member("M01", "Ada Lovelace", max_loans=2)
    due = lib.borrow_book("M01", b1.isbn, loan_days=7)
    print(b1)
    print(m1)
    lib.advance_day(10)
    print(f"Day {lib.current_day} overdue loans (due day {due}): {lib.overdue_loans()}")
    was_late = lib.return_book("M01", b1.isbn)
    print(f"Returned late? {was_late} | Audit entries: {len(lib.audit_log)}")
