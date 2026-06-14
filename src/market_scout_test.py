import pytest
from src import market_scout

def test_load_competitors():
    data = '[{"name": "Competitor 1", "market_share": 0.3, "growth_rate": 0.05}, {"name": "Competitor 2", "market_share": 0.2, "growth_rate": 0.03}]'
    competitors = market_scout.load_competitors(data)
    assert len(competitors) == 2
    assert competitors[0].name == 'Competitor 1'
    assert competitors[0].market_share == 0.3
    assert competitors[0].growth_rate == 0.05

def test_plot_competitors():
    data = '[{"name": "Competitor 1", "market_share": 0.3, "growth_rate": 0.05}, {"name": "Competitor 2", "market_share": 0.2, "growth_rate": 0.03}]'
    competitors = market_scout.load_competitors(data)
    market_scout.plot_competitors(competitors)

def test_main():
    data = '[{"name": "Competitor 1", "market_share": 0.3, "growth_rate": 0.05}, {"name": "Competitor 2", "market_share": 0.2, "growth_rate": 0.03}]'
    with pytest.raises(SystemExit):
        market_scout.main()
