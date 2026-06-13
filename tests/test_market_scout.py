import pytest
from market_scout import MarketScout, CompetitorData, DataSource

def test_get_competitor_data():
    market_scout = MarketScout({})
    competitor_data = market_scout.get_competitor_data("company1")
    assert competitor_data.name == "Company 1"
    assert competitor_data.description == "Description 1"
    assert competitor_data.source == DataSource.INTERNAL

def test_get_competitor_landscape():
    market_scout = MarketScout({})
    company_ids = ["company1", "company2"]
    competitor_data = market_scout.get_competitor_landscape(company_ids)
    assert len(competitor_data) == 2
    assert competitor_data[0].name == "Company 1"
    assert competitor_data[0].description == "Description 1"
    assert competitor_data[0].source == DataSource.INTERNAL
    assert competitor_data[1].name == "Company 2"
    assert competitor_data[1].description == "Description 2"
    assert competitor_data[1].source == DataSource.INTERNAL

def test_error_handling():
    market_scout = MarketScout({})
    competitor_data = market_scout.get_competitor_data("unknown_company")
    assert competitor_data.name == "Unknown"
    assert competitor_data.description == "Unknown"
    assert competitor_data.source == DataSource.INTERNAL
