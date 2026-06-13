from axentx_product import calculate_demand_score

def test_demand_score_all_go():
    """Test with all GO outcomes."""
    score = calculate_demand_score(4, 4, 0)
    assert score == 100.0

def test_demand_score_half_go():
    """Test with half GO and half NO-GO."""
    score = calculate_demand_score(4, 2, 2)
    assert score == 50.0

def test_demand_score_no_outcomes():
    """Test with no outcomes."""
    score = calculate_demand_score(0, 0, 0)
    assert score == 0.0
