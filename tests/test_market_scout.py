import pytest
from market_scout import MarketScout, Competitor

def test_generate_competitors():
    market_scout = MarketScout("test_keyword")
    competitors = market_scout.generate_competitors()
    assert len(competitors) == 10
    assert all(isinstance(competitor, Competitor) for competitor in competitors)

def test_get_competitors():
    market_scout = MarketScout("test_keyword")
    competitors = market_scout.get_competitors()
    assert len(competitors) == 10
    assert all(isinstance(competitor, dict) for competitor in competitors)
    assert all(
        "name" in competitor
        and "description" in competitor
        and "funding" in competitor
        and "employee_count" in competitor
        and "product_focus" in competitor
        and "relevance_score" in competitor
        and "source" in competitor
        for competitor in competitors
    )

def test_competitor_ranking():
    market_scout = MarketScout("test_keyword")
    competitors = market_scout.generate_competitors()
    assert competitors[0].relevance_score >= competitors[1].relevance_score
    assert competitors[1].relevance_score >= competitors[2].relevance_score

def test_edge_case_empty_keyword():
    market_scout = MarketScout("")
    competitors = market_scout.generate_competitors()
    assert len(competitors) == 10

def test_edge_case_none_keyword():
    with pytest.raises(AttributeError):
        MarketScout(None)
