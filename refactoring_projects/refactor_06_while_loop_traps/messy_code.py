"""Messy greenhouse temperature analyzer — rescue this file!

It currently works and passes TestBehaviorSafetyNet, but relies on three
clunky manual-index `while` loops that are hard to read and easy to break.
"""


def analyze_temperature_readings(readings, high_threshold):
    """Return summary metrics for a sequence of temperature readings.

    Returns a dict with:
        - "count": number of readings
        - "average": mean temperature rounded to 2 decimals (0.0 if empty)
        - "max_temp": highest reading (None if empty)
        - "min_temp": lowest reading (None if empty)
        - "high_indices": list of indices where reading >= high_threshold
        - "deltas": consecutive differences readings[k] - readings[k - 1]
                    rounded to 2 decimals
    """
    n = len(readings)
    if n == 0:
        return {
            "count": 0,
            "average": 0.0,
            "max_temp": None,
            "min_temp": None,
            "high_indices": [],
            "deltas": [],
        }

    # Loop 1: manual-index while loop for total, min, and max
    total = 0.0
    max_temp = readings[0]
    min_temp = readings[0]
    i = 0
    while i < n:
        curr = readings[i]
        total = total + curr
        if curr > max_temp:
            max_temp = curr
        if curr < min_temp:
            min_temp = curr
        i = i + 1

    # Loop 2: manual-index while loop for threshold indices
    high_indices = []
    j = 0
    while j < n:
        temp_val = readings[j]
        if temp_val >= high_threshold:
            high_indices.append(j)
        j = j + 1

    # Loop 3: manual-index while loop for consecutive temperature deltas
    deltas = []
    k = 1
    while k < n:
        prev_val = readings[k - 1]
        next_val = readings[k]
        diff = round(next_val - prev_val, 2)
        deltas.append(diff)
        k = k + 1

    avg = round(total / n, 2)
    return {
        "count": n,
        "average": avg,
        "max_temp": max_temp,
        "min_temp": min_temp,
        "high_indices": high_indices,
        "deltas": deltas,
    }
