"""
Activity 125: Validation & @property Encapsulation
Difficulty: 125 / 132

What stops someone from writing `account.balance = -999999`?
**Properties (`@property`)**!
A `@property` lets callers read `obj.balance` like a clean attribute while
allowing the class to:
  1. Make an attribute READ-ONLY (no setter -> `AttributeError` on direct assignment), OR
  2. Run validation logic inside `@attr.setter` before accepting a new value!

===============================================================================
PART 1: WORKED EXAMPLE ("I DO") — ExampleProduct
===============================================================================
Problem:
    Build `ExampleProduct(name, price)` using `@property` and `@price.setter`:
      - Rejects blank `name` or negative `price` with `ValueError` — BOTH at
        construction AND if someone later assigns `product.price = -5`!
      - `price_with_tax(tax_rate) -> float`: validates `tax_rate >= 0` and
        returns `round(self.price * (1 + tax_rate), 2)`.

Step-by-Step Breakdown:
    1. Store internal data in a leading-underscore attribute (`self._price`).
    2. In `__init__`, assign `self.price = price` so it runs through the
       setter's validation automatically (zero duplicated checks!).

===============================================================================
PART 2: YOUR TURN ("YOU DO") — BankAccount
===============================================================================
Problem:
    Implement `BankAccount` with read-only properties, overdraft protection,
    and a protected transaction ledger:
      - `__init__(self, owner: str, initial_balance: float = 0.0) -> None`
        * Raises `ValueError` if `not owner.strip()` or `initial_balance < 0`.
        * Stores `self.owner = owner.strip()`, `self._balance = float(initial_balance)`,
          and `self._transactions: list[tuple[str, float]] = []`.
      - `@property def balance(self) -> float`
        * Read-only property returning `self._balance`.
      - `@property def transactions(self) -> list[tuple[str, float]]`
        * Returns a COPY `list(self._transactions)` so external callers cannot
          accidentally corrupt the ledger with `.append()` or `.clear()`!
      - `deposit(self, amount: float) -> float`
        * Raises `ValueError` if `amount <= 0`.
        * Adds `amount` to `self._balance`, appends `("DEPOSIT", float(amount))`
          to `self._transactions`, and returns the updated balance.
      - `withdraw(self, amount: float) -> float`
        * Raises `ValueError` if `amount <= 0` or `amount > self._balance` (overdraft guard!).
        * Subtracts `amount` from `self._balance`, appends `("WITHDRAW", float(amount))`
          to `self._transactions`, and returns the updated balance.

    Examples:
        acct = BankAccount("  Ada  ", 100.0)
        acct.owner              -> "Ada"
        acct.balance            -> 100.0
        acct.deposit(50)        -> 150.0
        acct.withdraw(40)       -> 110.0
        acct.transactions       -> [("DEPOSIT", 50.0), ("WITHDRAW", 40.0)]
        acct.withdraw(200)      -> raises ValueError (overdraft!); balance stays 110.0!

    Edge-case hints:
        - Attempting `acct.balance = 999` raises `AttributeError` because
          `balance` has a `@property` getter and NO setter!
        - Modifying the list returned by `acct.transactions` MUST NOT affect
          the account's internal `self._transactions`.
"""
from __future__ import annotations


class ExampleProduct:
    """A store product validating non-empty name and non-negative price via @property."""

    def __init__(self, name: str, price: float) -> None:
        if not name.strip():
            raise ValueError("product name must not be blank")
        self.name = name.strip()
        self._price: float = 0.0
        self.price = price  # delegates to @price.setter

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float) -> None:
        if value < 0:
            raise ValueError("price cannot be negative")
        self._price = float(value)

    def price_with_tax(self, tax_rate: float) -> float:
        """Return price including tax_rate (e.g. 0.15 for 15%), rounded to 2 decimals."""
        if tax_rate < 0:
            raise ValueError("tax_rate cannot be negative")
        return round(self._price * (1 + tax_rate), 2)


class BankAccount:
    """A bank account with read-only balance, overdraft guard, and transaction log."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        """Initialize account, validating non-blank owner and non-negative balance."""
        pass

    @property
    def balance(self) -> float:
        """Return the current account balance (read-only)."""
        pass

    @property
    def transactions(self) -> list[tuple[str, float]]:
        """Return a defensive copy of the ('DEPOSIT'|'WITHDRAW', amount) history."""
        pass

    def deposit(self, amount: float) -> float:
        """Deposit a strictly positive amount, record it, and return new balance."""
        pass

    def withdraw(self, amount: float) -> float:
        """Withdraw a strictly positive amount <= balance, record it, and return balance."""
        pass


if __name__ == "__main__":
    item = ExampleProduct("Mechanical Keyboard", 129.99)
    print(f"{item.name}: ${item.price:.2f} -> with 15% tax: ${item.price_with_tax(0.15):.2f}")
