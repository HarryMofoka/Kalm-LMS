# Refactoring Mission 09 — Mutating Inputs Bug (CP 09)

## Backstory & Problem Statement

An e-commerce checkout helper (`prepare_checkout_cart`) seemed fine during quick smoke tests: given a shopper's cart, a promo item, and a recall blacklist, it returned a sorted checkout list.

Then customers started reporting bizarre bugs in production:
1. Previewing a checkout cart **secretly reordered, deleted from, and appended to** the shopper's saved wishlist/cart in place — AND scrambled the store's `blacklist` list!
2. Because it returned the exact same list object (`result is items`), changing the returned checkout preview also mutated the original cart!
3. If a customer had **two or more** copies of a blacklisted item in their cart, `.remove(banned)` only removed the *first* one and let the duplicates slip through to checkout!

Your mission: refactor `prepare_checkout_cart` into a clean, side-effect-free function that leaves caller inputs completely untouched and removes **all** occurrences of blacklisted items!

## Code Smells Checklist

- [ ] **In-place input mutation** via `items.remove(...)`, `items.append(...)`, `items.sort()`, and `blacklist.sort()`.
- [ ] **Aliased return value** (`return items`) — caller gets a reference to their own mutated list instead of a fresh list.
- [ ] **Incomplete removal bug** — `if banned in items: items.remove(banned)` only deletes the first matching occurrence, missing duplicates!

## Worked Refactoring Walkthrough (Before -> After)

Open [`worked_example.py`](worked_example.py) to compare a playlist top-tracks helper before and after fixing in-place mutation:

### Before (`before_top_tracks`)
```python
def before_top_tracks(tracks, limit):
    tracks.sort(key=lambda t: (-t[1], t[0]))
    while len(tracks) > max(0, limit):
        tracks.pop()
    return tracks
```
Calling `before_top_tracks(my_playlist, 2)` **destroys** `my_playlist` in place!

### After (`after_top_tracks`)
```python
def after_top_tracks(tracks, limit):
    if limit <= 0:
        return []
    return sorted(tracks, key=lambda t: (-t[1], t[0]))[:limit]
```
`sorted(...)` creates a brand-new list, leaving `my_playlist` 100% intact and unaliased!

## Your Refactoring Mission

Refactor [`messy_code.py`](messy_code.py) so that `prepare_checkout_cart(items, promo_item, blacklist)`:

1. **Never mutates `items`** (the caller's list stays identical in content and order).
2. **Never mutates `blacklist`** (no `blacklist.sort()` or other in-place changes).
3. **Always returns a brand-new list object** (`result is not items`).
4. **Removes ALL duplicate occurrences** of every blacklisted item (while preserving legitimate duplicates of non-blacklisted items!).
5. **Keeps all `TestBehaviorSafetyNet` tests 100% GREEN!**

## Run the Tests

Run from the `ExamPrep` directory:

```bash
python -m unittest refactoring_projects/refactor_09_mutating_inputs_bug/test_refactor.py -v
```
