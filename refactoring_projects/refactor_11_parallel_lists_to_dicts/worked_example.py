"""Worked Example for CP 11: Fragile parallel lists -> clean dictionary lookup.

Compare:
- ``before_lookup_student``: explodes rows into 3 parallel lists and scans by index.
- ``after_lookup_student``: builds a dict keyed by name for clean O(1) lookup.
"""

from typing import Dict, List, Optional, Sequence, Tuple, Union

StudentRow = Tuple[str, int, str]
StudentRecord = Dict[str, Union[str, int]]


def before_lookup_student(
    records: Sequence[StudentRow], target_name: str
) -> Optional[StudentRecord]:
    """Messy parallel-list lookup scanning with range(len(...))."""
    names: List[str] = []
    scores: List[int] = []
    houses: List[str] = []

    for name, score, house in records:
        names.append(name)
        scores.append(score)
        houses.append(house)

    for i in range(len(names)):
        if names[i] == target_name:
            return {
                "name": names[i],
                "score": scores[i],
                "house": houses[i],
            }
    return None


def build_student_directory(
    records: Sequence[StudentRow],
) -> Dict[str, StudentRecord]:
    """Build a name -> student-record dictionary once for O(1) lookups."""
    return {
        name: {"name": name, "score": score, "house": house}
        for name, score, house in records
    }


def after_lookup_student(
    records: Sequence[StudentRow], target_name: str
) -> Optional[StudentRecord]:
    """Clean dictionary-based student lookup."""
    directory = build_student_directory(records)
    return directory.get(target_name)


if __name__ == "__main__":
    sample_records = [
        ("Amara", 88, "Falcon"),
        ("Bongani", 74, "Orion"),
        ("Chidi", 95, "Solar"),
    ]
    print("Before:", before_lookup_student(sample_records, "Chidi"))
    print("After: ", after_lookup_student(sample_records, "Chidi"))
    print("Missing:", after_lookup_student(sample_records, "Zara"))
