"""Test suite for Refactoring Mission 20: Procedural to OOP Rescue."""

import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

from refactoring_projects.refactor_20_procedural_to_oop_rescue import (  # noqa: E402
    messy_code,
    worked_example,
)


class TestWorkedExample(unittest.TestCase):
    """Verifies the worked example procedural vs OOP library implementations match."""

    def test_before_and_after_library_match(self):
        old_lib = worked_example.before_create_library()
        new_lib = worked_example.after_create_library()

        for isbn, title in [("A1", "Python Basics"), ("A2", "Clean Architecture")]:
            worked_example.before_add_book(old_lib, isbn, title)
            worked_example.after_add_book(new_lib, isbn, title)

        self.assertEqual(
            worked_example.before_checkout(old_lib, "A1"),
            worked_example.after_checkout(new_lib, "A1"),
        )
        self.assertEqual(
            worked_example.before_checkout(old_lib, "A1"),
            worked_example.after_checkout(new_lib, "A1"),
        )
        self.assertEqual(
            worked_example.before_available_titles(old_lib),
            worked_example.after_available_titles(new_lib),
        )

    def test_oop_library_rejects_duplicate_isbn(self):
        lib = worked_example.Library()
        lib.add_book("X1", "Algorithms")
        with self.assertRaises(ValueError):
            lib.add_book("X1", "Duplicate")


class TestBehaviorSafetyNet(unittest.TestCase):
    """Behavioral safety net — all 5 procedural facade functions must stay 100% GREEN."""

    def test_full_procedural_board_lifecycle(self):
        board = messy_code.create_board()
        self.assertEqual(
            messy_code.board_summary(board),
            {"total": 0, "open": 0, "done": 0},
        )
        self.assertEqual(messy_code.get_open_tasks(board), [])

        messy_code.add_task(board, "BUG-1", "Fix login crash", "high")
        messy_code.add_task(board, "BUG-2", "Refresh docs", "low")
        messy_code.add_task(board, "BUG-3", "Add unit tests", "medium")

        self.assertEqual(
            messy_code.get_open_tasks(board),
            [
                {"id": "BUG-1", "title": "Fix login crash", "priority": "high"},
                {"id": "BUG-2", "title": "Refresh docs", "priority": "low"},
                {"id": "BUG-3", "title": "Add unit tests", "priority": "medium"},
            ],
        )

        self.assertTrue(messy_code.complete_task(board, "BUG-1"))
        self.assertFalse(messy_code.complete_task(board, "MISSING"))

        self.assertEqual(
            messy_code.get_open_tasks(board),
            [
                {"id": "BUG-2", "title": "Refresh docs", "priority": "low"},
                {"id": "BUG-3", "title": "Add unit tests", "priority": "medium"},
            ],
        )
        self.assertEqual(
            messy_code.board_summary(board),
            {"total": 3, "open": 2, "done": 1},
        )


class TestRefactorGoals(unittest.TestCase):
    """Refactoring goals — RED on baseline, GREEN once refactored to clean OOP."""

    def test_task_class_exists_with_repr_and_priority_validation(self):
        self.assertTrue(
            hasattr(messy_code, "Task"),
            "Expected domain class `Task` in messy_code.py.",
        )
        Task = getattr(messy_code, "Task")
        self.assertIsInstance(Task, type, "`Task` must be a class.")

        task = Task("BUG-10", "Fix parser", "high")
        self.assertEqual(task.task_id, "BUG-10")
        self.assertEqual(task.title, "Fix parser")
        self.assertEqual(task.priority, "high")
        self.assertFalse(task.done)

        self.assertIsNot(
            Task.__repr__,
            object.__repr__,
            "`Task` should define a readable `__repr__` method.",
        )
        text = repr(task)
        self.assertIn("Task", text)
        self.assertIn("BUG-10", text)

        with self.assertRaises(ValueError):
            Task("BUG-11", "Bad priority", "urgent")

    def test_task_board_class_methods_and_repr(self):
        self.assertTrue(
            hasattr(messy_code, "TaskBoard"),
            "Expected domain class `TaskBoard` in messy_code.py.",
        )
        self.assertTrue(
            hasattr(messy_code, "Task"),
            "Expected domain class `Task` in messy_code.py.",
        )
        TaskBoard = getattr(messy_code, "TaskBoard")
        Task = getattr(messy_code, "Task")
        self.assertIsInstance(TaskBoard, type, "`TaskBoard` must be a class.")

        board = TaskBoard()
        self.assertIsNot(
            TaskBoard.__repr__,
            object.__repr__,
            "`TaskBoard` should define a readable `__repr__` method.",
        )
        self.assertIn("TaskBoard", repr(board))

        t1 = board.add_task("T-1", "Write spec", "medium")
        t2 = board.add_task("T-2", "Ship release", "high")
        self.assertIsInstance(t1, Task)
        self.assertIsInstance(t2, Task)

        open_list = board.open_tasks()
        self.assertEqual(len(open_list), 2)
        self.assertTrue(all(isinstance(t, Task) for t in open_list))

        self.assertTrue(board.complete_task("T-1"))
        self.assertFalse(board.complete_task("UNKNOWN"))
        self.assertEqual([t.task_id for t in board.open_tasks()], ["T-2"])
        self.assertEqual(board.summary(), {"total": 2, "open": 1, "done": 1})

    def test_task_board_rejects_duplicate_id_and_invalid_priority(self):
        self.assertTrue(
            hasattr(messy_code, "TaskBoard"),
            "Expected domain class `TaskBoard` in messy_code.py.",
        )
        TaskBoard = getattr(messy_code, "TaskBoard")
        board = TaskBoard()
        board.add_task("T-1", "Initial task", "low")

        with self.assertRaises(ValueError):
            board.add_task("T-1", "Duplicate ID task", "high")

        with self.assertRaises(ValueError):
            board.add_task("T-2", "Invalid priority task", "critical")

    def test_facade_functions_delegate_to_task_board(self):
        self.assertTrue(
            hasattr(messy_code, "TaskBoard"),
            "Expected `create_board()` to return a `TaskBoard` instance.",
        )
        TaskBoard = getattr(messy_code, "TaskBoard")

        board = messy_code.create_board()
        self.assertIsInstance(
            board,
            TaskBoard,
            "`create_board()` should return a `TaskBoard` instance.",
        )

        messy_code.add_task(board, "F-1", "Facade task", "high")
        with self.assertRaises(ValueError):
            messy_code.add_task(board, "F-1", "Duplicate via facade", "low")
        with self.assertRaises(ValueError):
            messy_code.add_task(board, "F-2", "Bad priority via facade", "p0")

        self.assertEqual(
            messy_code.get_open_tasks(board),
            [{"id": "F-1", "title": "Facade task", "priority": "high"}],
        )
        self.assertTrue(messy_code.complete_task(board, "F-1"))
        self.assertEqual(
            messy_code.board_summary(board),
            {"total": 1, "open": 0, "done": 1},
        )


if __name__ == "__main__":
    unittest.main()
