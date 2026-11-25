"""Worked Example for Refactor 02: Multi-Leg Distance Formatter.

Demonstrates replacing repeated `// 1000`, `% 1000`, and manual zero-padding
with a named constant, a small helper function, and clean f-string formatting.
"""

# ---------------------------------------------------------------------------
# BEFORE: Repeated conversion math and manual zero-padding everywhere
# ---------------------------------------------------------------------------


def before_convert(meters_leg_a, meters_leg_b):
    a_km = meters_leg_a // 1000
    a_m = meters_leg_a % 1000
    if a_m < 10:
        a_m_str = "00" + str(a_m)
    elif a_m < 100:
        a_m_str = "0" + str(a_m)
    else:
        a_m_str = str(a_m)

    b_km = meters_leg_b // 1000
    b_m = meters_leg_b % 1000
    if b_m < 10:
        b_m_str = "00" + str(b_m)
    elif b_m < 100:
        b_m_str = "0" + str(b_m)
    else:
        b_m_str = str(b_m)

    t_km = (meters_leg_a + meters_leg_b) // 1000
    t_m = (meters_leg_a + meters_leg_b) % 1000
    if t_m < 10:
        t_m_str = "00" + str(t_m)
    elif t_m < 100:
        t_m_str = "0" + str(t_m)
    else:
        t_m_str = str(t_m)

    return (
        "Leg A: " + str(a_km) + " km " + a_m_str + " m | "
        "Leg B: " + str(b_km) + " km " + b_m_str + " m | "
        "Total: " + str(t_km) + " km " + t_m_str + " m"
    )


# ---------------------------------------------------------------------------
# AFTER: Named constant + reusable helper + clean f-string `:03d` padding
# ---------------------------------------------------------------------------

METERS_PER_KM = 1000


def format_distance(total_meters):
    """Format a distance in meters as '<km> km <mmm> m' with zero-padded meters."""
    kilometers = total_meters // METERS_PER_KM
    remaining_meters = total_meters % METERS_PER_KM
    return f"{kilometers} km {remaining_meters:03d} m"


def after_convert_distance(meters_leg_a, meters_leg_b):
    """Format two hiking legs and their combined distance cleanly."""
    total_meters = meters_leg_a + meters_leg_b
    return (
        f"Leg A: {format_distance(meters_leg_a)} | "
        f"Leg B: {format_distance(meters_leg_b)} | "
        f"Total: {format_distance(total_meters)}"
    )


if __name__ == "__main__":
    samples = [
        (1250, 3050),
        (500, 505),
        (0, 9),
    ]
    for leg_a, leg_b in samples:
        print("BEFORE:", before_convert(leg_a, leg_b))
        print("AFTER: ", after_convert_distance(leg_a, leg_b))
        print()
