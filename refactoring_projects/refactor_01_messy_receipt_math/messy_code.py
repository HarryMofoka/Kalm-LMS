# Legacy shipping calculator written in a rush before a long weekend.
# It passes all billing checks, but good luck figuring out what any number means!


def calculate_shipping_total(w, d, e):
    # dont touch this finance already approved it lol
    a = 15.0
    b = w * 2.5
    c = d * 0.5
    x1 = 45.0 if e else 0.0
    x2 = a + b + c + x1
    z = x2 + (x2 * 0.15)
    return round(z, 2)
