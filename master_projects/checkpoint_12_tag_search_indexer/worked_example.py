"""Worked Example (Checkpoint 12): Recipe Ingredient Matcher.

A sibling reference system showing how inverted indexes (dict[str, set[str]])
power instant exact-match filtering and relevance-ranked partial matching.
"""

from __future__ import annotations

import re


def normalize_ingredients(raw_text: str) -> set[str]:
    """Extract unique lowercase alphanumeric ingredient tokens from text."""
    return set(re.findall(r"[a-z0-9]+", raw_text.lower()))


def build_ingredient_index(recipes: dict[str, str]) -> dict[str, set[str]]:
    """Build an inverted index mapping each ingredient token to recipe IDs."""
    index: dict[str, set[str]] = {}
    for recipe_id, ingredient_text in recipes.items():
        for token in normalize_ingredients(ingredient_text):
            index.setdefault(token, set()).add(recipe_id)
    return index


def find_exact_recipes(
    index: dict[str, set[str]],
    required: list[str],
) -> list[str]:
    """Return sorted recipe IDs that contain ALL required ingredients."""
    normalized: set[str] = set()
    for entry in required:
        normalized.update(normalize_ingredients(entry))

    if not normalized:
        return []

    posting_sets: list[set[str]] = []
    for ingredient in normalized:
        if ingredient not in index:
            return []
        posting_sets.append(index[ingredient])

    matched = set.intersection(*posting_sets)
    return sorted(matched)


def rank_recipes_by_pantry(
    index: dict[str, set[str]],
    pantry: list[str],
) -> list[tuple[str, int]]:
    """Rank recipes by how many distinct pantry ingredients they use.

    Returns a list of ``(recipe_id, match_count)`` tuples sorted by
    ``match_count`` descending, then ``recipe_id`` ascending.
    """
    pantry_tokens: set[str] = set()
    for entry in pantry:
        pantry_tokens.update(normalize_ingredients(entry))

    hit_counts: dict[str, int] = {}
    for token in pantry_tokens:
        for recipe_id in index.get(token, set()):
            hit_counts[recipe_id] = hit_counts.get(recipe_id, 0) + 1

    return sorted(hit_counts.items(), key=lambda pair: (-pair[1], pair[0]))


if __name__ == "__main__":
    recipe_book = {
        "aglio_e_olio": "spaghetti, garlic, olive-oil, chili, parsley",
        "shakshuka": "tomato, garlic, onion, egg, cumin, chili",
        "caprese_salad": "tomato, mozzarella, basil, olive-oil",
        "garlic_fried_rice": "rice, garlic, egg, soy, scallion",
    }

    ingredient_index = build_ingredient_index(recipe_book)
    print("=== Recipe Ingredient Matcher ===")
    print("Indexed terms:", len(ingredient_index))
    print(
        "Recipes with garlic AND chili:",
        find_exact_recipes(ingredient_index, ["Garlic", "Chili"]),
    )
    print(
        "Best matches for pantry [tomato, garlic, chili, egg]:",
        rank_recipes_by_pantry(
            ingredient_index, ["tomato", "garlic", "chili", "egg"]
        ),
    )
