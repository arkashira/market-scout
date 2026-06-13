import pytest
from market_scout import MarketScout, Competitor
import json
import time

def test_get_competitors():
    market_scout = MarketScout()
    product_description = "Test product description"
    competitors = market_scout.get_competitors(product_description)
    assert len(competitors) == 10
    for competitor in competitors:
        assert isinstance(competitor, Competitor)
        assert competitor.relevance_score >= 0.0 and competitor.relevance_score <= 100.0

def test_product_description_length():
    market_scout = MarketScout()
    product_description = "a" * 251
    competitors = market_scout.get_competitors(product_description)
    assert len(competitors) == 10

def test_response_time():
    market_scout = MarketScout()
    product_description = "Test product description"
    start_time = time.time()
    market_scout.get_competitors(product_description)
    end_time = time.time()
    assert end_time - start_time <= 1.5

def test_reproducibility():
    market_scout = MarketScout()
    product_description = "Test product description"
    competitors1 = market_scout.get_competitors(product_description)
    competitors2 = market_scout.get_competitors(product_description)
    assert len(competitors1) == len(competitors2)
    for competitor1, competitor2 in zip(competitors1, competitors2):
        assert competitor1.name == competitor2.name
        assert competitor1.tagline == competitor2.tagline
        assert competitor1.pricing_model == competitor2.pricing_model
        assert competitor1.market_share_estimate == competitor2.market_share_estimate
        assert abs(competitor1.relevance_score - competitor2.relevance_score) <= 5.0

def test_json_output():
    market_scout = MarketScout()
    product_description = "Test product description"
    competitors = market_scout.get_competitors(product_description)
    json_output = json.dumps([{
        "name": competitor.name,
        "tagline": competitor.tagline,
        "pricing_model": competitor.pricing_model,
        "market_share_estimate": competitor.market_share_estimate,
        "relevance_score": competitor.relevance_score
    } for competitor in competitors], indent=4)
    assert json_output is not None
