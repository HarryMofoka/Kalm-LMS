# Legacy FitTrack weekly workout summarizer.
# Note from previous intern: "If we change how active_days works, remember to edit ALL THREE loops!"


def summarize_workout_week(morning_reps, afternoon_reps, evening_reps):
    # Morning session stats
    m_total = 0
    m_best = 0
    m_active = 0
    for rep in morning_reps:
        m_total = m_total + rep
        if rep > m_best:
            m_best = rep
        if rep > 0:
            m_active = m_active + 1
    m_summary = {
        "total": m_total,
        "best": m_best,
        "active_days": m_active,
    }

    # Afternoon session stats (definitely not copy-pasted from above...)
    a_total = 0
    a_best = 0
    a_active = 0
    for rep in afternoon_reps:
        a_total = a_total + rep
        if rep > a_best:
            a_best = rep
        if rep > 0:
            a_active = a_active + 1
    a_summary = {
        "total": a_total,
        "best": a_best,
        "active_days": a_active,
    }

    # Evening session stats (third time's the charm!)
    e_total = 0
    e_best = 0
    e_active = 0
    for rep in evening_reps:
        e_total = e_total + rep
        if rep > e_best:
            e_best = rep
        if rep > 0:
            e_active = e_active + 1
    e_summary = {
        "total": e_total,
        "best": e_best,
        "active_days": e_active,
    }

    return {
        "morning": m_summary,
        "afternoon": a_summary,
        "evening": e_summary,
    }
