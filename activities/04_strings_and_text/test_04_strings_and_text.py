"""Test suite for Module 04: Strings & Text (Activities 037-048)."""

from __future__ import annotations

import importlib
import sys
import unittest
from pathlib import Path

EXAMPREP_ROOT = Path(__file__).resolve().parents[2]
if str(EXAMPREP_ROOT) not in sys.path:
    sys.path.insert(0, str(EXAMPREP_ROOT))

_m037 = importlib.import_module("activities.04_strings_and_text.activity_037_indexing_and_slicing")
_m038 = importlib.import_module("activities.04_strings_and_text.activity_038_char_counting")
_m039 = importlib.import_module("activities.04_strings_and_text.activity_039_filtering_characters")
_m040 = importlib.import_module("activities.04_strings_and_text.activity_040_case_transformations")
_m041 = importlib.import_module("activities.04_strings_and_text.activity_041_word_splitting_joining")
_m042 = importlib.import_module("activities.04_strings_and_text.activity_042_cleaning_and_slugs")
_m043 = importlib.import_module("activities.04_strings_and_text.activity_043_palindrome_detection")
_m044 = importlib.import_module("activities.04_strings_and_text.activity_044_word_extremes")
_m045 = importlib.import_module("activities.04_strings_and_text.activity_045_run_length_encoding")
_m046 = importlib.import_module("activities.04_strings_and_text.activity_046_caesar_cipher")
_m047 = importlib.import_module("activities.04_strings_and_text.activity_047_substring_scanning_masking")
_m048 = importlib.import_module("activities.04_strings_and_text.activity_048_template_replacement")

example_first_and_last = _m037.example_first_and_last
solve_reverse_and_middle = _m037.solve_reverse_and_middle
example_count_char = _m038.example_count_char
solve_count_vowels = _m038.solve_count_vowels
example_remove_vowels = _m039.example_remove_vowels
solve_keep_alphanumeric = _m039.solve_keep_alphanumeric
example_capitalize_words = _m040.example_capitalize_words
solve_smart_swap_case = _m040.solve_smart_swap_case
example_split_words = _m041.example_split_words
solve_reverse_each_word = _m041.solve_reverse_each_word
example_clean_spaces = _m042.example_clean_spaces
solve_slugify = _m042.solve_slugify
example_is_simple_palindrome = _m043.example_is_simple_palindrome
solve_is_phrase_palindrome = _m043.solve_is_phrase_palindrome
example_shortest_word = _m044.example_shortest_word
solve_longest_word = _m044.solve_longest_word
example_rle_compress = _m045.example_rle_compress
solve_rle_decompress = _m045.solve_rle_decompress
example_caesar_lowercase = _m046.example_caesar_lowercase
solve_caesar_cipher = _m046.solve_caesar_cipher
example_count_substring = _m047.example_count_substring
solve_mask_sensitive = _m047.solve_mask_sensitive
example_fill_name = _m048.example_fill_name
solve_render_template = _m048.solve_render_template


class TestWorkedExamples(unittest.TestCase):
    """Verify all 12 worked examples in Module 04 pass out of the box."""

    def test_example_037(self) -> None:
        self.assertEqual(example_first_and_last("python"), ("p", "n"))
        self.assertEqual(example_first_and_last("X"), ("X", "X"))
        self.assertEqual(example_first_and_last(""), ("", ""))

    def test_example_038(self) -> None:
        self.assertEqual(example_count_char("Banana", "a"), 3)
        self.assertEqual(example_count_char("Banana", "B"), 1)
        self.assertEqual(example_count_char("Banana", "b"), 0)
        self.assertEqual(example_count_char("hello", ""), 0)
        self.assertEqual(example_count_char("hello", "ll"), 0)

    def test_example_039(self) -> None:
        self.assertEqual(example_remove_vowels("Hello, World!"), "Hll, Wrld!")
        self.assertEqual(example_remove_vowels("AEIOUaeiou"), "")
        self.assertEqual(example_remove_vowels("123!@#"), "123!@#")
        self.assertEqual(example_remove_vowels(""), "")

    def test_example_040(self) -> None:
        self.assertEqual(example_capitalize_words("hello world"), "Hello World")
        self.assertEqual(
            example_capitalize_words("  don't   STOP believing  "),
            "Don't Stop Believing",
        )
        self.assertEqual(example_capitalize_words("   "), "")

    def test_example_041(self) -> None:
        self.assertEqual(
            example_split_words("  Hello   world\tfrom\nPython  "),
            ["Hello", "world", "from", "Python"],
        )
        self.assertEqual(example_split_words("   "), [])
        self.assertEqual(example_split_words(""), [])

    def test_example_042(self) -> None:
        self.assertEqual(example_clean_spaces("   hello  \t world \n "), "hello world")
        self.assertEqual(example_clean_spaces("clean"), "clean")
        self.assertEqual(example_clean_spaces("   "), "")

    def test_example_043(self) -> None:
        self.assertTrue(example_is_simple_palindrome("racecar"))
        self.assertFalse(example_is_simple_palindrome("Racecar"))
        self.assertTrue(example_is_simple_palindrome("a"))
        self.assertTrue(example_is_simple_palindrome(""))
        self.assertFalse(example_is_simple_palindrome("python"))

    def test_example_044(self) -> None:
        self.assertEqual(example_shortest_word("The quick brown fox"), "The")
        self.assertEqual(example_shortest_word("cat dog ox an"), "ox")
        self.assertEqual(example_shortest_word("   "), "")

    def test_example_045(self) -> None:
        self.assertEqual(example_rle_compress("aaabbc"), "a3b2c1")
        self.assertEqual(example_rle_compress("aabaa"), "a2b1a2")
        self.assertEqual(example_rle_compress("a" * 12), "a12")
        self.assertEqual(example_rle_compress("x"), "x1")
        self.assertEqual(example_rle_compress(""), "")

    def test_example_046(self) -> None:
        self.assertEqual(example_caesar_lowercase("xyz", 3), "abc")
        self.assertEqual(example_caesar_lowercase("abc", -3), "xyz")
        self.assertEqual(example_caesar_lowercase("abc", 29), "def")
        self.assertEqual(example_caesar_lowercase("Hi 123!", 1), "Hj 123!")

    def test_example_047(self) -> None:
        self.assertEqual(example_count_substring("aaaa", "aa"), 2)
        self.assertEqual(example_count_substring("ababa", "aba"), 1)
        self.assertEqual(example_count_substring("ababab", "ab"), 3)
        self.assertEqual(example_count_substring("hello", ""), 0)
        self.assertEqual(example_count_substring("hi", "hello"), 0)

    def test_example_048(self) -> None:
        self.assertEqual(example_fill_name("Hello, {name}!", "Ada"), "Hello, Ada!")
        self.assertEqual(
            example_fill_name("{name} meets {name}", "Bo"),
            "Bo meets Bo",
        )
        self.assertEqual(
            example_fill_name("No placeholder", "Ada"),
            "No placeholder",
        )
        self.assertEqual(example_fill_name("", "Ada"), "")


class TestYourActivities(unittest.TestCase):
    """Test suite for student implementations in Module 04 (Activities 037-048)."""

    def test_activity_037(self) -> None:
        self.assertEqual(solve_reverse_and_middle("hello"), ("olleh", "l"))
        self.assertEqual(solve_reverse_and_middle("python"), ("nohtyp", "th"))
        self.assertEqual(solve_reverse_and_middle("code"), ("edoc", "od"))
        self.assertEqual(solve_reverse_and_middle("a"), ("a", "a"))
        self.assertEqual(solve_reverse_and_middle("ab"), ("ba", "ab"))
        self.assertEqual(solve_reverse_and_middle(""), ("", ""))

    def test_activity_038(self) -> None:
        self.assertEqual(solve_count_vowels("Hello World"), 3)
        self.assertEqual(solve_count_vowels("AEIOUaeiou"), 10)
        self.assertEqual(solve_count_vowels("Rhythm"), 0)
        self.assertEqual(solve_count_vowels("PyThOn 3.12!"), 1)
        self.assertEqual(solve_count_vowels(""), 0)

    def test_activity_039(self) -> None:
        self.assertEqual(
            solve_keep_alphanumeric("Hello, World! 2026"),
            "HelloWorld2026",
        )
        self.assertEqual(
            solve_keep_alphanumeric("user_name-01@mail"),
            "username01mail",
        )
        self.assertEqual(solve_keep_alphanumeric("!!!   ---"), "")
        self.assertEqual(solve_keep_alphanumeric("Python3"), "Python3")
        self.assertEqual(solve_keep_alphanumeric(""), "")

    def test_activity_040(self) -> None:
        self.assertEqual(solve_smart_swap_case("Hello World"), "hELLO wORLD")
        self.assertEqual(solve_smart_swap_case("Hi 2026!"), "!6202 Ih")
        self.assertEqual(solve_smart_swap_case("PyThOn3"), "3NoHtYp")
        self.assertEqual(solve_smart_swap_case("abc"), "ABC")
        self.assertEqual(solve_smart_swap_case("   "), "   ")
        self.assertEqual(solve_smart_swap_case(""), "")

    def test_activity_041(self) -> None:
        self.assertEqual(solve_reverse_each_word("Hello World"), "olleH dlroW")
        self.assertEqual(
            solve_reverse_each_word("  Python   is  fun! "),
            "nohtyP si !nuf",
        )
        self.assertEqual(solve_reverse_each_word("racecar level"), "racecar level")
        self.assertEqual(solve_reverse_each_word("single"), "elgnis")
        self.assertEqual(solve_reverse_each_word("   "), "")
        self.assertEqual(solve_reverse_each_word(""), "")

    def test_activity_042(self) -> None:
        self.assertEqual(solve_slugify("Hello, World!"), "hello-world")
        self.assertEqual(
            solve_slugify("  Learn   Python 101!  "),
            "learn-python-101",
        )
        self.assertEqual(solve_slugify("Don't Panic!"), "dont-panic")
        self.assertEqual(
            solve_slugify("snake_case--and---kebab"),
            "snake-case-and-kebab",
        )
        self.assertEqual(solve_slugify("C++ & Python: A Guide"), "c-python-a-guide")
        self.assertEqual(solve_slugify("!!! --- ___"), "")
        self.assertEqual(solve_slugify(""), "")

    def test_activity_043(self) -> None:
        self.assertIs(solve_is_phrase_palindrome("A man, a plan, a canal: Panama!"), True)
        self.assertIs(solve_is_phrase_palindrome("Was it a car or a cat I saw?"), True)
        self.assertIs(solve_is_phrase_palindrome("No 'x' in Nixon"), True)
        self.assertIs(solve_is_phrase_palindrome("12321"), True)
        self.assertIs(solve_is_phrase_palindrome("race a car"), False)
        self.assertIs(solve_is_phrase_palindrome("0P"), False)
        self.assertIs(solve_is_phrase_palindrome("   !!!"), True)

    def test_activity_044(self) -> None:
        self.assertEqual(solve_longest_word("The quick, brown fox!"), "brown")
        self.assertEqual(solve_longest_word("Hello, world!!!"), "world")
        self.assertEqual(solve_longest_word("cat dog bat"), "bat")
        self.assertEqual(solve_longest_word("one!!! two"), "two")
        self.assertEqual(solve_longest_word("extraordinary"), "extraordinary")
        self.assertEqual(solve_longest_word("!!! ... ???"), "")
        self.assertEqual(solve_longest_word(""), "")

    def test_activity_045(self) -> None:
        self.assertEqual(solve_rle_decompress("a3b2c1"), "aaabbc")
        self.assertEqual(solve_rle_decompress("a12b2"), "aaaaaaaaaaaabb")
        self.assertEqual(solve_rle_decompress("a2b1a2"), "aabaa")
        self.assertEqual(solve_rle_decompress(" 3!2"), "   !!")
        self.assertEqual(solve_rle_decompress("x1"), "x")
        self.assertEqual(solve_rle_decompress(""), "")

    def test_activity_046(self) -> None:
        self.assertEqual(solve_caesar_cipher("Hello, World!", 3), "Khoor, Zruog!")
        self.assertEqual(solve_caesar_cipher("Khoor, Zruog!", -3), "Hello, World!")
        self.assertEqual(solve_caesar_cipher("Zoo 2026!", 1), "App 2026!")
        self.assertEqual(solve_caesar_cipher("AbC", 26), "AbC")
        self.assertEqual(solve_caesar_cipher("AbC", 27), "BcD")
        self.assertEqual(solve_caesar_cipher("AbC", -27), "ZaB")
        self.assertEqual(solve_caesar_cipher("", 5), "")

    def test_activity_047(self) -> None:
        self.assertEqual(
            solve_mask_sensitive("4111-2222-3333-4444"),
            "****-****-****-4444",
        )
        self.assertEqual(
            solve_mask_sensitive("1234 5678 9012 3456"),
            "**** **** **** 3456",
        )
        self.assertEqual(solve_mask_sensitive("9876543210"), "******3210")
        self.assertEqual(solve_mask_sensitive("1234"), "1234")
        self.assertEqual(
            solve_mask_sensitive("student2026@uni.edu"),
            "*******2026@uni.edu",
        )
        self.assertEqual(
            solve_mask_sensitive("alice.smith@example.com"),
            "*******mith@example.com",
        )
        self.assertEqual(solve_mask_sensitive("amy@uni.edu"), "***@uni.edu")
        self.assertEqual(solve_mask_sensitive(""), "")

    def test_activity_048(self) -> None:
        self.assertEqual(
            solve_render_template(
                "Hi {{name}}, score: {{score}}!",
                {"name": "Ada", "score": "98"},
            ),
            "Hi Ada, score: 98!",
        )
        self.assertEqual(
            solve_render_template("Welcome {{ name }}!", {"name": "Kai"}),
            "Welcome Kai!",
        )
        self.assertEqual(
            solve_render_template("{{x}} + {{x}} = 2*{{x}}", {"x": "5"}),
            "5 + 5 = 2*5",
        )
        self.assertEqual(
            solve_render_template("Hello {{user}}, role={{role}}", {"user": "Sam"}),
            "Hello Sam, role={{role}}",
        )
        self.assertEqual(
            solve_render_template("{{a}}", {"a": "{{b}}", "b": "WRONG"}),
            "{{b}}",
        )
        self.assertEqual(
            solve_render_template("Price: {{unclosed", {"unclosed": "10"}),
            "Price: {{unclosed",
        )
        self.assertEqual(solve_render_template("", {"a": "1"}), "")


if __name__ == "__main__":
    unittest.main()
