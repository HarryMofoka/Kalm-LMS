"""Messy checkout cart preparer — rescue this file!

It returns the expected list on simple happy-path tests, BUT it secretly
mutates both `items` and `blacklist` in place, returns the same aliased
list object, and fails to remove duplicate blacklisted items!
"""


def prepare_checkout_cart(items, promo_item, blacklist):
    """Prepare a sorted checkout list excluding blacklisted items and adding an eligible promo.

    Rules:
        - Exclude all occurrences of any item in `blacklist`.
        - Keep legitimate duplicate non-blacklisted items.
        - If `promo_item` is non-empty, not blacklisted, and not already in the
          filtered cart, include one `promo_item`.
        - Return a new alphabetically sorted list without mutating inputs.
    """
    # Bug 1: mutates caller's blacklist in place!
    blacklist.sort()

    # Bug 2: mutates caller's items in place AND only removes the first match!
    for banned in blacklist:
        if banned in items:
            items.remove(banned)

    # Bug 3: appends directly into caller's list!
    if promo_item and promo_item not in blacklist and promo_item not in items:
        items.append(promo_item)

    # Bug 4: sorts in place and returns the caller's original list object!
    items.sort()
    return items
