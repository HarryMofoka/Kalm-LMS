# Checkpoint 20 — Digital Wallet & Double-Entry Ledger System (Capstone)

- **Unlocked After:** Activity 132 — OOP Capstone & Double-Entry Accounting
- **Difficulty:** Hard / Capstone (Tier 5 — Object-Oriented Design, Invariants & Accounting)
- **Core Concepts:** Classes & encapsulation, integer-cent money representation, strict invariant enforcement, atomic transfers, double-entry conservation, immutable-style audit trails, `__repr__`

---

## Real-World Value

In FinTech core banking, payment processors (Stripe, PayPal, Wise), and digital wallets, **a single bug can create or destroy real money**. Production financial systems rely on three non-negotiable engineering principles:

1. **Integer Cents Only — Never Floats:** `0.1 + 0.2 == 0.30000000000000004` in IEEE-754 floating point! Real ledgers store amounts as integer cents (`$19.99 -> 1999`).
2. **Atomic Transfers:** If Alice tries to transfer `$500` to Bob but Alice only has `$100`, the transfer must fail **completely** — neither Alice's balance, Bob's balance, nor the audit log may change.
3. **Conservation & Auditability:** Internal transfers never change the total money inside the bank (`total_deposits_cents()` stays invariant), and every account creation and transfer leaves a verifiable audit log entry.

---

## Problem Statement

Build an object-oriented **Digital Wallet & Double-Entry Ledger System** composed of three cooperating classes:
1. `Transaction` — immutable-style record of a single balance change.
2. `Account` — tracks owner, integer-cent balance, overdraft limit, transaction history, strict validation, and printable statements.
3. `BankLedger` — manages accounts, executes **atomic** account-to-account transfers, computes total system deposits, and maintains an audit log.

---

## How a Similar Functioning System Was Done (`worked_example.py`)

Study **`worked_example.py`** — a complete **Object-Oriented Library Lending System** (`Book`, `Member`, `Library`) that applies the exact same OOP invariant & audit-trail patterns to book borrowing.

### Design Walkthrough

1. **Clean Domain Entities (`Book`, `Member`)**:
   - Each class validates its inputs in `__init__` and implements a readable `__repr__` for debugging.
2. **Fail-Fast Atomic Operations (`Library.borrow_book`, `Library.return_book`)**:
   - Every precondition (member exists, book exists, book is available, member hasn't hit `max_loans`) is checked **before** any object attribute is mutated. If any check fails, a `ValueError` or `KeyError` is raised and zero state changes happen.
3. **Audit Trail (`Library.audit_log`)**:
   - Every successful state transition appends a structured event dictionary so operations can be audited at any time.

Run the reference demo anytime:
```bash
python master_projects/checkpoint_20_mini_bank_ledger_system/worked_example.py
```

---

## Your Project Brief (`project.py`)

Implement the following three classes in `project.py`:

### 1. `Transaction`
- `__init__(self, tx_id: str, kind: str, amount_cents: int, description: str, balance_after_cents: int) -> None`
  - Stores `tx_id`, `kind`, `amount_cents`, `description`, `balance_after_cents`.
- `__repr__(self) -> str`
  - Clean debug string including `tx_id`, `kind`, `amount_cents`, and `balance_after_cents`.

### 2. `Account`
- `__init__(self, account_id: str, owner: str, balance_cents: int = 0, overdraft_limit_cents: int = 0) -> None`
  - Validate:
    - `account_id` and `owner` must be non-empty strings after `.strip()` (else raise `ValueError`).
    - `overdraft_limit_cents >= 0` (else raise `ValueError`).
    - `balance_cents >= -overdraft_limit_cents` (else raise `ValueError`).
  - Store `account_id`, `owner`, `balance_cents`, `overdraft_limit_cents`, and `transactions: list[Transaction] = []`.
- `deposit(self, amount_cents: int, desc: str = "Deposit") -> Transaction`
  - Raise `ValueError` if `amount_cents` is not a positive `int` (also reject `bool` since `isinstance(True, int)` is `True`!).
  - Increase `self.balance_cents += amount_cents`.
  - Create, append to `self.transactions`, and return a `Transaction` with `kind="DEPOSIT"`, unique `tx_id` (e.g. `f"{self.account_id}-TX-{len(self.transactions) + 1:04d}"`), `amount_cents`, `description=desc`, `balance_after_cents=self.balance_cents`.
- `withdraw(self, amount_cents: int, desc: str = "Withdrawal") -> Transaction`
  - Raise `ValueError` if `amount_cents` is not a positive `int` (reject `bool`).
  - Raise `ValueError` if `self.balance_cents - amount_cents < -self.overdraft_limit_cents` (without modifying `balance_cents` or `transactions`!).
  - Decrease `self.balance_cents -= amount_cents`.
  - Create, append to `self.transactions`, and return a `Transaction` with `kind="WITHDRAWAL"`, `amount_cents`, `description=desc`, `balance_after_cents=self.balance_cents`.
- `statement(self) -> list[str]`
  - Return formatted statement lines (with **zero trailing spaces**) including:
    - Account header containing `account_id` and `owner`
    - One line per transaction showing `tx_id`, `kind`, formatted dollar amount (e.g. `+$50.00` or `-$20.00`), `description`, and resulting balance
    - Closing balance line formatted in dollars (e.g. `Closing Balance: $30.00` or `Closing Balance: -$10.00`)
- `__repr__(self) -> str`
  - Clean debug string including `account_id`, `owner`, and `balance_cents`.

### 3. `BankLedger`
- `__init__(self) -> None`
  - Initialize internal accounts storage (`self.accounts: dict[str, Account] = {}`) and `self.audit_log: list[dict] = []`.
- `create_account(self, account_id: str, owner: str, initial_balance_cents: int = 0, overdraft_limit_cents: int = 0) -> Account`
  - Raise `ValueError` if `account_id` already exists.
  - Create and store the `Account`, append a `"CREATE_ACCOUNT"` entry to `self.audit_log`, and return the `Account`.
- `get_account(self, account_id: str) -> Account`
  - Return the `Account` for `account_id`, or raise `KeyError` if not found.
- `transfer(self, from_id: str, to_id: str, amount_cents: int, desc: str = "Transfer") -> tuple[Transaction, Transaction]`
  - **Atomic invariant:** Validate everything before mutating!
    - Raise `ValueError` if `from_id == to_id`.
    - Raise `ValueError` if `amount_cents` is not a positive `int` (reject `bool`).
    - Look up BOTH `source = self.get_account(from_id)` and `target = self.get_account(to_id)` first (raises `KeyError` if either is missing, without debiting `source`).
    - Call `debit_tx = source.withdraw(amount_cents, f"Transfer to {to_id}: {desc}")`. If this raises `ValueError` (insufficient funds / overdraft breach), `target` and `audit_log` remain completely untouched!
    - Call `credit_tx = target.deposit(amount_cents, f"Transfer from {from_id}: {desc}")`.
    - Append `{"type": "TRANSFER", "from_id": from_id, "to_id": to_id, "amount_cents": amount_cents, "description": desc}` to `self.audit_log`.
    - Return `(debit_tx, credit_tx)`.
- `total_deposits_cents(self) -> int`
  - Return the sum of `balance_cents` across all accounts in the ledger.

---

## Running Tests

From the `ExamPrep/` root directory:

```bash
python -m unittest master_projects/checkpoint_20_mini_bank_ledger_system/test_project.py -v
```
