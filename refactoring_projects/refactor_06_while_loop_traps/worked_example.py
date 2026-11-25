"""Worked Example for RF 06: Sensor Spike Finder (manual while -> for + enumerate)."""


def before_find_spikes(readings, threshold):
    """Messy version: uses a fragile manual-index while loop."""
    spikes = []
    i = 0
    while i < len(readings):
        val = readings[i]
        if val > threshold:
            spikes.append((i, val))
        i = i + 1
    return spikes


def after_find_spikes(readings, threshold):
    """Clean version: uses Pythonic for + enumerate."""
    spikes = []
    for index, value in enumerate(readings):
        if value > threshold:
            spikes.append((index, value))
    return spikes


if __name__ == "__main__":
    sample_readings = [18.5, 22.0, 27.4, 21.9, 31.2, 25.0]
    limit = 25.0
    print("Readings:", sample_readings, "| Threshold:", limit)
    print("Before:", before_find_spikes(sample_readings, limit))
    print("After: ", after_find_spikes(sample_readings, limit))
