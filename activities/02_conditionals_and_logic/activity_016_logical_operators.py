"""
Activity 016: Logical Operators (`and`, `or`, `not`)
Difficulty: 16 / 132 (Rank 2 - Decision Maker)

Context:
Business rules almost always blend multiple conditions together: "must NOT be
banned, AND must be either a student OR a senior." Knowing how `not`, `and`,
and `or` interact — and using parentheses so readers never have to guess
precedence — prevents subtle security and eligibility bugs!

================================================================================
PART 1: WORKED EXAMPLE ("I DO")
================================================================================
Problem:
Write `example_can_ride_coaster(height_cm, has_adult, has_heart_condition)` for
a theme park safety gate:
- Nobody with a heart condition may ride (`has_heart_condition` MUST be `False`).
- Otherwise, a rider is allowed if:
  * their height is at least `140` cm (can ride solo), OR
  * their height is at least `110` cm AND they have an accompanying adult.

Step-by-step walkthrough:
1. Remember Python's operator precedence: `not` > `and` > `or`.
   Even though you might remember precedence, ALWAYS use parentheses when
   mixing `and` and `or` so the intent is unmistakable!
2. Break the rule into readable pieces:
   - `tall_enough_solo = height_cm >= 140`
   - `tall_enough_with_adult = height_cm >= 110 and has_adult`
   - `return (not has_heart_condition) and (tall_enough_solo or tall_enough_with_adult)`
3. Named intermediate booleans make complex policies read like plain English!

Edge cases:
- Tall rider (`180` cm) WITH heart condition -> `False` (safety veto wins!).
- Child `110` cm with adult, no heart condition -> `True` (exact boundary!).
- Child `109` cm with adult, no heart condition -> `False`.

================================================================================
PART 2: YOUR TURN ("YOU DO")
================================================================================
Problem:
A movie theater awards a discounted ticket if ALL of the following hold:
1. The customer is **NOT** banned from promotions (`is_vip_banned` is `False`).
2. AND **at least one** of these discount triggers applies:
   - Child rate: `age < 12`
   - Senior rate: `age >= 65`
   - Student rate: `is_student` is `True`
   - Bargain Tuesday: `is_tuesday` is `True`

Write `solve_movie_discount(age, is_student, is_tuesday, is_vip_banned)` that
returns `True` if eligible for a discount and `False` otherwise.

Rules:
- If `is_vip_banned` is `True`, ALWAYS return `False` regardless of age,
  student status, or day of the week!
- Watch the exact age boundaries:
  * `age == 11` -> qualifies as child (`< 12`).
  * `age == 12` -> does NOT qualify as child.
  * `age == 64` -> does NOT qualify as senior.
  * `age == 65` -> qualifies as senior (`>= 65`).

Examples:
- `solve_movie_discount(10, False, False, False)` -> `True`   (child)
- `solve_movie_discount(12, False, False, False)` -> `False`  (not < 12)
- `solve_movie_discount(65, False, False, False)` -> `True`   (senior)
- `solve_movie_discount(30, True, False, False)` -> `True`    (student)
- `solve_movie_discount(30, False, True, False)` -> `True`    (Tuesday)
- `solve_movie_discount(10, True, True, True)` -> `False`     (banned overrides all!)

Hints:
- Group all four qualifying conditions inside parentheses separated by `or`,
  then combine with `(not is_vip_banned) and (...)`.
"""

from __future__ import annotations


def example_can_ride_coaster(
    height_cm: int, has_adult: bool, has_heart_condition: bool
) -> bool:
    """Return True if the rider satisfies all theme-park roller coaster safety rules."""
    # Named boolean sub-expressions make multi-clause rules effortless to read.
    tall_enough_solo = height_cm >= 140
    tall_enough_with_adult = height_cm >= 110 and has_adult
    return (not has_heart_condition) and (tall_enough_solo or tall_enough_with_adult)


def solve_movie_discount(
    age: int, is_student: bool, is_tuesday: bool, is_vip_banned: bool
) -> bool:
    """Return True if customer qualifies for a movie discount and is not banned."""
    pass


if __name__ == "__main__":
    print("145cm solo, healthy:", example_can_ride_coaster(145, False, False))
    print("120cm + adult, healthy:", example_can_ride_coaster(120, True, False))
    print("180cm, heart condition:", example_can_ride_coaster(180, False, True))
