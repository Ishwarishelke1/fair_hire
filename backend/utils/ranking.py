def calculate_final_score(match_score, skill_count):

    skill_score = min(skill_count * 10, 100)

    final_score = (
        0.7 * match_score +
        0.3 * skill_score
    )

    return round(final_score, 2)