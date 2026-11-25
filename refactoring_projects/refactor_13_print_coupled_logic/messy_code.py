"""Messy Grade Reporter — Refactoring Target for Mission 13.

PROBLEM:
All grade calculations, pass/fail checks, averages, highest-score tracking,
and text formatting happen directly inside ``print(...)`` calls!
Because everything is welded to console output, no other part of the program
can inspect the grade statistics or export the report lines to a file.

YOUR GOAL:
1. Extract pure ``compute_grade_stats(students)`` -> dict
2. Extract pure ``format_grade_report(students)`` -> list[str]
3. Make ``print_grade_report(students)`` a thin wrapper around ``format_grade_report``.
"""

from typing import Sequence, Tuple


def print_grade_report(students: Sequence[Tuple[str, int]]) -> None:
    """Print a formatted class grade report (currently tangled with I/O!)."""
    print("=== GRADE REPORT ===")
    if len(students) == 0:
        print("No students to report.")
        return

    passed = 0
    failed = 0
    total_score = 0
    highest_name = None
    highest_score = None

    for name, score in students:
        total_score = total_score + score
        if score >= 50:
            passed = passed + 1
            print(f"{name}: {score} (PASS)")
        else:
            failed = failed + 1
            print(f"{name}: {score} (FAIL)")
        if highest_score is None or score > highest_score:
            highest_score = score
            highest_name = name

    print("--------------------")
    print(f"Total Students: {len(students)}")
    print(f"Passed: {passed} | Failed: {failed}")
    print(f"Average Score: {total_score / len(students):.2f}")
    print(f"Highest: {highest_name} ({highest_score})")
