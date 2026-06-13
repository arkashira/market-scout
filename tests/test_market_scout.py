import pytest
from market_scout import Competitor, estimate_market_size, prioritize_segments

def test_estimate_market_size():
    competitors = [
        Competitor("Segment 1", 100, 50, 20, 0.8),
        Competitor("Segment 2", 50, 30, 15, 0.6)
    ]
    estimates = estimate_market_size(competitors)
    assert len(estimates) == 2
    assert estimates[0]["name"] == "Segment 1"
    assert estimates[0]["tam"] == "$100.00M ± $20.00M"
    assert estimates[1]["name"] == "Segment 2"
    assert estimates[1]["tam"] == "$50.00M ± $10.00M"

def test_prioritize_segments():
    estimates = [
        {"name": "Segment 1", "tam": "$100.00M ± $20.00M", "relevance_score": 0.8},
        {"name": "Segment 2", "tam": "$50.00M ± $10.00M", "relevance_score": 0.6},
        {"name": "Segment 3", "tam": "$200.00M ± $40.00M", "relevance_score": 0.9}
    ]
    prioritized_segments = prioritize_segments(estimates)
    assert len(prioritized_segments) == 3
    assert prioritized_segments[0]["name"] == "Segment 3"
    assert prioritized_segments[1]["name"] == "Segment 1"
    assert prioritized_segments[2]["name"] == "Segment 2"

def test_edge_case_empty_list():
    estimates = estimate_market_size([])
    assert estimates == []

def test_edge_case_single_segment():
    competitors = [Competitor("Segment 1", 100, 50, 20, 0.8)]
    estimates = estimate_market_size(competitors)
    assert len(estimates) == 1
    assert estimates[0]["name"] == "Segment 1"
    assert estimates[0]["tam"] == "$100.00M ± $20.00M"
