# Module 06: Dictionaries & Sets (Activities 061–072)

Unlock $O(1)$ lookups, frequency maps, set algebra, and hash-map problem solving—from square-number maps and case-insensitive counters to safe merging, grouped inversion, nested inventory math, anagram clustering, disjoint Two-Sum pairs, and inverted-index tag queries.

## Learning Goals

- Build, traverse, filter, merge, and invert dictionaries cleanly without mutating caller inputs.
- Use frequency dictionaries to solve counting, tie-breaking, anagram, and palindrome-permutation tasks in linear time.
- Leverage Python sets for $O(1)$ membership, intersections, symmetric differences, missing-element detection, and ordered duplicate tracking.
- Manage nested dictionaries (copying inner dicts safely to avoid aliasing) and multi-value hash-map groupings.
- Combine hash maps and sets for exam-favorite algorithms: anagram grouping, disjoint Two-Sum pairs, and inverted indices.

## Activities Roadmap

| Activity | File | Worked Example ("I Do") | Your Turn ("You Do") | Difficulty |
| :---: | :--- | :--- | :--- | :---: |
| **061** | `activity_061_dict_creation_squares.py` | Squares map `1..n` | `generate_squared_dict` (positive, zero & negative `n`) | `61 / 132` |
| **062** | `activity_062_char_frequency_map.py` | Count each character | Full 26-letter `'a'..'z'` case-insensitive frequency map | `62 / 132` |
| **063** | `activity_063_word_frequency_topk.py` | Word counts dictionary | Most frequent word with alphabetical tie-break | `63 / 132` |
| **064** | `activity_064_merging_dicts_safely.py` | Override merge (non-mutating) | Sum overlapping values without mutating inputs | `64 / 132` |
| **065** | `activity_065_inverting_filtering_dicts.py` | Filter entries above threshold | Invert dict grouping equal-value keys into lists | `65 / 132` |
| **066** | `activity_066_nested_dicts_inventory.py` | Total shopping cart value | Apply stock updates & report out-of-stock items | `66 / 132` |
| **067** | `activity_067_set_operations.py` | Common elements in two lists | Sorted symmetric difference (unique to each) | `67 / 132` |
| **068** | `activity_068_fast_membership_missing.py` | Find missing number in `1..n` | Find all duplicates preserving first-duplicate order | `68 / 132` |
| **069** | `activity_069_anagram_checking.py` | `is_anagram` (ignore case & spaces) | Check if string can permute into a palindrome | `69 / 132` |
| **070** | `activity_070_grouping_by_key.py` | Group words by first letter | `find_anagram_groups` preserving first-seen group order | `70 / 132` |
| **071** | `activity_071_two_sum_and_pairs.py` | Single Two-Sum index pair | All disjoint index pairs summing to target | `71 / 132` |
| **072** | `activity_072_inverted_index_and_cache.py` | Build `word -> doc_ids` inverted index | Query docs containing ALL required tags | `72 / 132` |

## Checkpoints

> **Checkpoint 11 Unlocked after Activity 066!**
> Once Activities 061–066 pass, you have mastered dictionary construction, frequency counting, safe merging, value-grouped inversion, and nested inventory updates.

> **Checkpoint 12 Unlocked after Activity 072!**
> Once Activities 067–072 pass, you can solve set-algebra, anagram-grouping, disjoint Two-Sum, and inverted-index search questions at exam speed!

## How to Run Tests

From inside the `ExamPrep/` directory:

```bash
# Run all tests in Module 06 with unittest
python -m unittest activities/06_dictionaries_and_sets/test_06_dictionaries_and_sets.py -v

# Run ONLY the worked examples (should all PASS right away)
python -m unittest activities.06_dictionaries_and_sets.test_06_dictionaries_and_sets.TestWorkedExamples -v

# Run ONLY your activities (starts red -> turn them green!)
python -m unittest activities.06_dictionaries_and_sets.test_06_dictionaries_and_sets.TestYourActivities -v

# Or using pytest
pytest activities/06_dictionaries_and_sets/test_06_dictionaries_and_sets.py -v
```
