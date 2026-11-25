# Legacy SkyHop flight schedule formatter.
# Warning: contains dangerous levels of copy-pasted time math and manual zero-padding!


def format_flight_schedule(dep_h, dep_m, dur_mins):
    # Manually pad departure time
    if dep_h < 10:
        dep_h_str = "0" + str(dep_h)
    else:
        dep_h_str = str(dep_h)

    if dep_m < 10:
        dep_m_str = "0" + str(dep_m)
    else:
        dep_m_str = str(dep_m)

    # Manually break down and pad duration
    dur_h = dur_mins // 60
    dur_m = dur_mins % 60
    if dur_h < 10:
        dur_h_str = "0" + str(dur_h)
    else:
        dur_h_str = str(dur_h)

    if dur_m < 10:
        dur_m_str = "0" + str(dur_m)
    else:
        dur_m_str = str(dur_m)

    # Recompute total arrival minutes over and over with hardcoded 60, 1440, 24
    days = (dep_h * 60 + dep_m + dur_mins) // 1440
    arr_h = (((dep_h * 60 + dep_m + dur_mins) % 1440) // 60) % 24
    arr_m = ((dep_h * 60 + dep_m + dur_mins) % 1440) % 60

    # Manually pad arrival time too
    if arr_h < 10:
        arr_h_str = "0" + str(arr_h)
    else:
        arr_h_str = str(arr_h)

    if arr_m < 10:
        arr_m_str = "0" + str(arr_m)
    else:
        arr_m_str = str(arr_m)

    day_suffix = ""
    if days > 0:
        day_suffix = " (+" + str(days) + "d)"

    return (
        "Depart "
        + dep_h_str
        + ":"
        + dep_m_str
        + " | Duration "
        + dur_h_str
        + "h "
        + dur_m_str
        + "m | Arrive "
        + arr_h_str
        + ":"
        + arr_m_str
        + day_suffix
    )
