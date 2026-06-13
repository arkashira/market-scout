def calculate_demand_score(outcomes, go_count, no_go_count):
    """
    Calculate the demand score based on the number of GO and NO-GO outcomes.

    Parameters:
    - outcomes: The total number of outcomes (go + no_go).
    - go_count: Number of GO outcomes.
    - no_go_count: Number of NO-GO outcomes.

    Returns:
    A float representing the demand score as a percentage.
    """
    if outcomes == 0:
        return 0.0
    return (go_count / outcomes) * 100.0
