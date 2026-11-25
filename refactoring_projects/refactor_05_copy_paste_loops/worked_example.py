"""Worked Example for Refactor 05: Three-Team Score Statistics.

Demonstrates replacing three copy-pasted averaging loops (`before_team_stats`)
with a single DRY helper function called by `after_team_stats`.
"""

# ---------------------------------------------------------------------------
# BEFORE: The exact same stat-averaging loop copy-pasted 3 times!
# ---------------------------------------------------------------------------


def before_team_stats(alpha_scores, beta_scores, gamma_scores):
    # Copy #1: Alpha team
    a_total = 0
    a_count = 0
    a_highest = 0
    for score in alpha_scores:
        a_total += score
        a_count += 1
        if score > a_highest:
            a_highest = score
    a_avg = round(a_total / a_count, 2) if a_count > 0 else 0.0
    alpha_result = {"count": a_count, "average": a_avg, "highest": a_highest}

    # Copy #2: Beta team (Ctrl+C, Ctrl+V, replace a_ with b_)
    b_total = 0
    b_count = 0
    b_highest = 0
    for score in beta_scores:
        b_total += score
        b_count += 1
        if score > b_highest:
            b_highest = score
    b_avg = round(b_total / b_count, 2) if b_count > 0 else 0.0
    beta_result = {"count": b_count, "average": b_avg, "highest": b_highest}

    # Copy #3: Gamma team (Ctrl+C, Ctrl+V, replace b_ with g_)
    g_total = 0
    g_count = 0
    g_highest = 0
    for score in gamma_scores:
        g_total += score
        g_count += 1
        if score > g_highest:
            g_highest = score
    g_avg = round(g_total / g_count, 2) if g_count > 0 else 0.0
    gamma_result = {"count": g_count, "average": g_avg, "highest": g_highest}

    return {
        "alpha": alpha_result,
        "beta": beta_result,
        "gamma": gamma_result,
    }


# ---------------------------------------------------------------------------
# AFTER: One DRY helper function reused for every team
# ---------------------------------------------------------------------------


def compute_group_stats(scores):
    """Compute count, rounded average, and highest non-negative score for one group."""
    if not scores:
        return {"count": 0, "average": 0.0, "highest": 0}

    total = 0
    highest = 0
    for score in scores:
        total += score
        if score > highest:
            highest = score

    return {
        "count": len(scores),
        "average": round(total / len(scores), 2),
        "highest": highest,
    }


def after_team_stats(alpha_scores, beta_scores, gamma_scores):
    """Summarize tournament statistics across Alpha, Beta, and Gamma teams."""
    return {
        "alpha": compute_group_stats(alpha_scores),
        "beta": compute_group_stats(beta_scores),
        "gamma": compute_group_stats(gamma_scores),
    }


if __name__ == "__main__":
    alpha = [10, 25, 18]
    beta = [40, 35, 38, 42]
    gamma = []
    print("BEFORE:", before_team_stats(alpha, beta, gamma))
    print("AFTER: ", after_team_stats(alpha, beta, gamma))
