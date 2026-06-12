from market_scout import MarketScout, Competitor

def test_add_competitor():
    market_scout = MarketScout()
    market_scout.add_competitor("Product A", Competitor("Competitor 1", "Description 1"))
    assert len(market_scout.generate_competitor_landscape("Product A")) == 1

def test_generate_competitor_landscape():
    market_scout = MarketScout()
    market_scout.add_competitor("Product A", Competitor("Competitor 1", "Description 1"))
    market_scout.add_competitor("Product A", Competitor("Competitor 2", "Description 2"))
    competitor_landscape = market_scout.generate_competitor_landscape("Product A")
    assert len(competitor_landscape) == 2

def test_display_competitor_landscape(capsys):
    market_scout = MarketScout()
    market_scout.add_competitor("Product A", Competitor("Competitor 1", "Description 1"))
    market_scout.add_competitor("Product A", Competitor("Competitor 2", "Description 2"))
    competitor_landscape = market_scout.generate_competitor_landscape("Product A")
    market_scout.display_competitor_landscape(competitor_landscape)
    captured = capsys.readouterr()
    assert "Competitor Landscape:" in captured.out
    assert "1. Competitor 1 - Description 1" in captured.out
    assert "2. Competitor 2 - Description 2" in captured.out
