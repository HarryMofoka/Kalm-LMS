# QuickBite Delivery discount calculator — affectionately known as "The Pyramid of Doom".
# Good luck matching the bottom `else:` to its `if:` without scrolling twice!


def evaluate_delivery_discount(is_member, cart_total, item_count, has_coupon, is_weekend):
    result = ""
    if item_count > 0:
        if cart_total >= 100:
            if is_member:
                if item_count >= 3:
                    if has_coupon:
                        if is_weekend:
                            result = "25% discount: weekend coupon VIP"
                        else:
                            result = "20% discount: weekday coupon member"
                    else:
                        if is_weekend:
                            result = "15% discount: weekend member"
                        else:
                            result = "10% discount: standard member"
                else:
                    result = "5% discount: small member order"
            else:
                result = "No discount: members only"
        else:
            result = "No discount: minimum order is R100"
    else:
        result = "No discount: cart is empty"
    return result
