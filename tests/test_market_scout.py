import pytest
from market_scout import MarketScout, Competitor
import time

def test_get_competitors():
    market_scout = MarketScout()
    product_idea = "AI-powered marketing"
    competitors = market_scout.get_competitors(product_idea)
    assert len(competitors) == 10
    for competitor in competitors:
        assert isinstance(competitor, Competitor)

def test_calculate_relevance_score():
    market_scout = MarketScout()
    competitor = Competitor("Company A", "https://companya.com", "AI-powered marketing", "Series A", 0.8)
    product_idea = "AI-powered marketing"
    relevance_score = market_scout.calculate_relevance_score(competitor, product_idea)
    assert 0 <= relevance_score <= 1

def test_keyword_match():
    market_scout = MarketScout()
    core_feature_summary = "AI-powered marketing"
    product_idea = "AI-powered marketing"
    keyword_match = market_scout.keyword_match(core_feature_summary, product_idea)
    assert 0 <= keyword_match <= 1

def test_funding_stage():
    market_scout = MarketScout()
    funding_stage = "Series A"
    funding_stage_score = market_scout.funding_stage(funding_stage)
    assert 0 <= funding_stage_score <= 1

def test_market_segment():
    market_scout = MarketScout()
    name = "Company A"
    market_segment_score = market_scout.market_segment(name)
    assert 0 <= market_segment_score <= 1

def test_response_time():
    market_scout = MarketScout()
    product_idea = "AI-powered marketing"
    start_time = time.time()
    market_scout.get_competitors(product_idea)
    end_time = time.time()
    response_time = end_time - start_time
    assert response_time <= 8
