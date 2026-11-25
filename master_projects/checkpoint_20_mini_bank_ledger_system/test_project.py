"""Unit tests for Checkpoint 20: Mini Bank Ledger System."""

from __future__ import annotations

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from master_projects.checkpoint_20_mini_bank_ledger_system import (
    project,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Tests verifying the Object-Oriented Library Lending System worked example."""

    def test_borrow_and_return_lifecycle(self) -> None:
        lib = worked_example.Library()
        book = lib.add_book("ISBN-1", "Clean Architecture", "R. Martin")
        member = lib.register_member("M1", "Grace Hopper", max_loans=2)

        due = lib.borrow_book("M1", "ISBN-1", loan_days=10)
        self.assertEqual(due, 10)
        self.assertFalse(book.is_available)
        self.assertEqual(member.borrowed_isbns, ["ISBN-1"])

        lib.advance_day(5)
        was_overdue = lib.return_book("M1", "ISBN-1")
        self.assertFalse(was_overdue)
        self.assertTrue(book.is_available)
        self.assertEqual(member.borrowed_isbns, [])

    def test_invariants_prevent_double_checkout_and_limit_breach(self) -> None:
        lib = worked_example.Library()
        lib.add_book("B1", "Book One", "Author A")
        lib.add_book("B2", "Book Two", "Author B")
        lib.register_member("M1", "Alice", max_loans=1)
        lib.register_member("M2", "Bob", max_loans=2)

        lib.borrow_book("M1", "B1")
        with self.assertRaises(ValueError):
            lib.borrow_book("M2", "B1")  # Already checked out
        with self.assertRaises(ValueError):
            lib.borrow_book("M1", "B2")  # Over loan limit
        with self.assertRaises(ValueError):
            lib.return_book("M2", "B1")  # Bob does not hold B1

    def test_overdue_tracking_and_audit_log_immutability(self) -> None:
        lib = worked_example.Library()
        lib.add_book("B1", "Algorithms", "CLRS")
        lib.register_member("M1", "Linus")
        lib.borrow_book("M1", "B1", loan_days=7)

        lib.advance_day(10)
        self.assertEqual(lib.overdue_loans(), [("M1", "B1", 3)])
        self.assertTrue(lib.return_book("M1", "B1"))
        self.assertEqual(lib.overdue_loans(), [])
        self.assertIsInstance(lib.audit_log, tuple)
        self.assertEqual(len(lib.audit_log), 4)

    def test_repr_includes_key_identifiers(self) -> None:
        book = worked_example.Book("X1", "SICP", "Abelson")
        member = worked_example.Member("U1", "Ken")
        self.assertIn("X1", repr(book))
        self.assertIn("U1", repr(member))


class TestMasterProject(unittest.TestCase):
    """Tests for the student's Digital Wallet & Double-Entry Ledger in project.py."""

    def test_transaction_attributes_and_repr(self) -> None:
        tx = project.Transaction("TX-1", "DEPOSIT", 5000, "Paycheck", 5000)
        self.assertEqual(tx.tx_id, "TX-1")
        self.assertEqual(tx.kind, "DEPOSIT")
        self.assertEqual(tx.amount_cents, 5000)
        self.assertEqual(tx.description, "Paycheck")
        self.assertEqual(tx.balance_after_cents, 5000)
        rendered = repr(tx)
        self.assertIsInstance(rendered, str)
        self.assertIn("TX-1", rendered)
        self.assertIn("5000", rendered)

    def test_account_deposit_withdraw_and_overdraft(self) -> None:
        acc = project.Account(
            "ACC-1", "Ada", balance_cents=1000, overdraft_limit_cents=500
        )
        d_tx = acc.deposit(2500, "Bonus")
        self.assertEqual(acc.balance_cents, 3500)
        self.assertEqual(d_tx.kind, "DEPOSIT")
        self.assertEqual(d_tx.balance_after_cents, 3500)

        w_tx = acc.withdraw(4000, "Rent")
        self.assertEqual(acc.balance_cents, -500)  # Exactly at overdraft limit
        self.assertEqual(w_tx.kind, "WITHDRAWAL")
        self.assertEqual(len(acc.transactions), 2)

        # Exceeding overdraft must fail without mutating balance or history
        with self.assertRaises(ValueError):
            acc.withdraw(1, "Over the line")
        self.assertEqual(acc.balance_cents, -500)
        self.assertEqual(len(acc.transactions), 2)

    def test_account_rejects_invalid_amounts_and_init_params(self) -> None:
        with self.assertRaises(ValueError):
            project.Account("", "Ada")
        with self.assertRaises(ValueError):
            project.Account("A1", "Ada", balance_cents=-100, overdraft_limit_cents=0)
        with self.assertRaises(ValueError):
            project.Account("A1", "Ada", overdraft_limit_cents=-50)

        acc = project.Account("A1", "Ada", balance_cents=1000)
        with self.assertRaises(ValueError):
            acc.deposit(0)
        with self.assertRaises(ValueError):
            acc.deposit(-100)
        with self.assertRaises(ValueError):
            acc.deposit(True)  # bool must not be accepted as 1 cent
        with self.assertRaises(ValueError):
            acc.withdraw(0)
        with self.assertRaises(ValueError):
            acc.withdraw(-50)

    def test_account_statement_formatting_and_zero_trailing_spaces(self) -> None:
        acc = project.Account("ACC-9", "Grace", balance_cents=0)
        acc.deposit(10050, "Salary")
        acc.withdraw(2525, "Groceries")
        lines = acc.statement()
        self.assertIsInstance(lines, list)
        self.assertTrue(len(lines) >= 4)
        self.assertTrue(all(line == line.rstrip() for line in lines))
        joined = "\n".join(lines)
        self.assertIn("ACC-9", joined)
        self.assertIn("Grace", joined)
        self.assertIn("Salary", joined)
        self.assertIn("Groceries", joined)
        self.assertIn("$75.25", joined)

    def test_ledger_create_get_and_conservation_on_transfer(self) -> None:
        ledger = project.BankLedger()
        alice = ledger.create_account("A1", "Alice", initial_balance_cents=10000)
        bob = ledger.create_account("B1", "Bob", initial_balance_cents=2500)
        self.assertIs(ledger.get_account("A1"), alice)
        self.assertEqual(ledger.total_deposits_cents(), 12500)

        debit_tx, credit_tx = ledger.transfer("A1", "B1", 3000, "Dinner split")
        self.assertEqual(alice.balance_cents, 7000)
        self.assertEqual(bob.balance_cents, 5500)
        self.assertEqual(debit_tx.kind, "WITHDRAWAL")
        self.assertEqual(credit_tx.kind, "DEPOSIT")
        # Double-entry conservation: total deposits unchanged!
        self.assertEqual(ledger.total_deposits_cents(), 12500)
        self.assertTrue(len(ledger.audit_log) >= 3)

    def test_ledger_atomic_failure_preserves_all_balances_and_audit_log(self) -> None:
        ledger = project.BankLedger()
        alice = ledger.create_account("A1", "Alice", initial_balance_cents=500)
        bob = ledger.create_account("B1", "Bob", initial_balance_cents=1000)
        audit_before = len(ledger.audit_log)

        # Insufficient funds: neither account nor audit_log may change
        with self.assertRaises(ValueError):
            ledger.transfer("A1", "B1", 600, "Too much")
        self.assertEqual(alice.balance_cents, 500)
        self.assertEqual(bob.balance_cents, 1000)
        self.assertEqual(len(alice.transactions), 0)
        self.assertEqual(len(bob.transactions), 0)
        self.assertEqual(len(ledger.audit_log), audit_before)

        # Missing destination account: source must NOT be debited!
        with self.assertRaises(KeyError):
            ledger.transfer("A1", "GHOST", 100, "Into the void")
        self.assertEqual(alice.balance_cents, 500)
        self.assertEqual(len(alice.transactions), 0)
        self.assertEqual(len(ledger.audit_log), audit_before)

    def test_ledger_edge_cases_duplicate_and_self_transfer(self) -> None:
        ledger = project.BankLedger()
        ledger.create_account("A1", "Alice", initial_balance_cents=1000)
        with self.assertRaises(ValueError):
            ledger.create_account("A1", "Alice Clone")
        with self.assertRaises(KeyError):
            ledger.get_account("NOPE")
        with self.assertRaises(ValueError):
            ledger.transfer("A1", "A1", 100, "Self loop")
        with self.assertRaises(ValueError):
            ledger.transfer("A1", "A1", -50, "Negative")


if __name__ == "__main__":
    unittest.main()
