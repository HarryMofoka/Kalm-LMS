# Module 04: Strings & Text (Activities 037–048)

Master Python's immutable string superpowers—from indexing, slicing, and character filtering to URL slugs, palindromes, run-length encoding, Caesar ciphers, data masking, and multi-key template rendering.

## Learning Goals

- Index and slice strings cleanly (including negative indices and reverse steps) without `IndexError`.
- Count, filter, and transform characters while respecting case sensitivity and immutability.
- Split, clean, and join words reliably using whitespace handling and accumulator lists (`"".join(...)`).
- Solve classic exam text-processing algorithms: palindromes, tie-breaking word searches, RLE compression/decompression, modular Caesar shifting, sensitive-data masking, and single-pass template rendering.
- Handle empty strings, punctuation, multi-digit counts, and Unicode/ASCII edge cases cleanly.

## Activities Roadmap

| Activity | File | Worked Example ("I Do") | Your Turn ("You Do") | Difficulty |
| :---: | :--- | :--- | :--- | :---: |
| **037** | `activity_037_indexing_and_slicing.py` | First & last character tuple | Reverse string & extract middle slice | `37 / 132` |
| **038** | `activity_038_char_counting.py` | Count exact character occurrences | Count vowels case-insensitively | `38 / 132` |
| **039** | `activity_039_filtering_characters.py` | Remove English vowels | Keep only alphanumeric characters | `39 / 132` |
| **040** | `activity_040_case_transformations.py` | Capitalize each word safely | Swap case + reverse if non-letter/space present | `40 / 132` |
| **041** | `activity_041_word_splitting_joining.py` | Split text into clean word list | Reverse each word preserving word order | `41 / 132` |
| **042** | `activity_042_cleaning_and_slugs.py` | Trim & collapse whitespace | URL slug generator (`hello-world`) | `42 / 132` |
| **043** | `activity_043_palindrome_detection.py` | Exact palindrome check | Phrase palindrome (ignore case/spaces/punctuation) | `43 / 132` |
| **044** | `activity_044_word_extremes.py` | Shortest word (first tie wins) | Longest word ignoring punctuation (last tie wins) | `44 / 132` |
| **045** | `activity_045_run_length_encoding.py` | RLE compress (`"aaabbc"` → `"a3b2c1"`) | RLE decompress (`"a3b2c1"` → `"aaabbc"`) | `45 / 132` |
| **046** | `activity_046_caesar_cipher.py` | Caesar shift lowercase letters | Caesar cipher preserving case & punctuation | `46 / 132` |
| **047** | `activity_047_substring_scanning_masking.py` | Count non-overlapping substrings | Mask emails & card numbers keeping last 4 | `47 / 132` |
| **048** | `activity_048_template_replacement.py` | Single `{name}` placeholder fill | Multi-key `{{var}}` template renderer | `48 / 132` |

## Checkpoints

> **Checkpoint 07 Unlocked after Activity 042!**
> Once Activities 037–042 pass, you have mastered string indexing, filtering, case manipulation, splitting/joining, and text normalization.

> **Checkpoint 08 Unlocked after Activity 048!**
> Once Activities 043–048 pass, you have conquered full exam-grade string algorithms—palindromes, RLE, ciphers, masking, and template engines!

## How to Run Tests

From inside the `ExamPrep/` directory:

```bash
# Run all tests in Module 04 with unittest
python -m unittest activities/04_strings_and_text/test_04_strings_and_text.py -v

# Run ONLY the worked examples (should all PASS right away)
python -m unittest activities.04_strings_and_text.test_04_strings_and_text.TestWorkedExamples -v

# Run ONLY your activities (starts red -> turn them green!)
python -m unittest activities.04_strings_and_text.test_04_strings_and_text.TestYourActivities -v

# Or using pytest
pytest activities/04_strings_and_text/test_04_strings_and_text.py -v
```
