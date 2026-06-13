import pytest
from market_scout import MarketScout, Competitor

def test_get_competitors():
    market_scout = MarketScout()
    competitors = market_scout.get_competitors("Test product description")
    assert len(competitors) == 10
    assert all(isinstance(competitor, Competitor) for competitor in competitors)
    assert competitors[0].relevance_score == 90.0

def test_get_competitors_product_description_too_long():
    market_scout = MarketScout()
    with pytest.raises(ValueError):
        market_scout.get_competitors("a" * 251)

def test_to_json():
    market_scout = MarketScout()
    competitors = market_scout.get_competitors("Test product description")
    json_string = market_scout.to_json(competitors)
    assert json_string.startswith("[")
    assert json_string.endswith("]")
    competitor_names = [competitor.name for competitor in competitors]
    assert all(name in json_string for name in competitor_names)
