import pytest
from market_scout import MarketScout, MarketOpportunity
import json
import os
import tempfile

def test_market_scout_initialization():
    scout = MarketScout()
    assert isinstance(scout, MarketScout)
    assert len(scout.opportunities) == 0

def test_load_data():
    data = [
        {"name": "Opportunity 1", "market_size": 100, "growth_rate": 5},
        {"name": "Opportunity 2", "market_size": 200, "growth_rate": 3}
    ]
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        json.dump(data, f)
        f.flush()
        scout = MarketScout(f.name)
        assert len(scout.opportunities) == 2
        assert scout.opportunities[0].name == "Opportunity 1"
        assert scout.opportunities[0].market_size == 100
        assert scout.opportunities[0].growth_rate == 5
        assert scout.opportunities[1].name == "Opportunity 2"
        assert scout.opportunities[1].market_size == 200
        assert scout.opportunities[1].growth_rate == 3
    os.unlink(f.name)

def test_visualize_opportunities(capsys):
    data = [
        {"name": "Opportunity 1", "market_size": 100, "growth_rate": 5},
        {"name": "Opportunity 2", "market_size": 200, "growth_rate": 3}
    ]
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        json.dump(data, f)
        f.flush()
        scout = MarketScout(f.name)
        scout.visualize_opportunities()
        captured = capsys.readouterr()
        assert "Opportunity 1: Market Size = 100.0, Growth Rate = 5.0" in captured.out
        assert "Opportunity 2: Market Size = 200.0, Growth Rate = 3.0" in captured.out
    os.unlink(f.name)

def test_save_visualization():
    data = [
        {"name": "Opportunity 1", "market_size": 100, "growth_rate": 5},
        {"name": "Opportunity 2", "market_size": 200, "growth_rate": 3}
    ]
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        json.dump(data, f)
        f.flush()
        scout = MarketScout(f.name)
        result = scout.save_visualization()
        assert isinstance(result, str)
        assert "Opportunity 1: Market Size = 100.0, Growth Rate = 5.0" in result
        assert "Opportunity 2: Market Size = 200.0, Growth Rate = 3.0" in result
    os.unlink(f.name)
