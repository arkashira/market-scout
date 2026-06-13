from market_scout import MarketScout, Competitor

def test_add_competitor():
    market_scout = MarketScout()
    market_scout.add_competitor("Product A", Competitor("Competitor 1", "Description 1"))
    assert len(market_scout.generate_competitor_landscape("Product A")) == 1

def test_generate_competitor_landscape():
    market_scout = MarketScout()
    market_scout.add_competitor("Product A", Competitor("Competitor 1", "Description 1"))
    market_scout.add_competitor("Product A", Competitor("Competitor 2", "Description 2"))
    assert len(market_scout.generate_competitor_landscape("Product A")) == 2

def test_display_competitor_landscape(capsys):
    market_scout = MarketScout()
    market_scout.add_competitor("Product A", Competitor("Competitor 1", "Description 1"))
    market_scout.add_competitor("Product A", Competitor("Competitor 2", "Description 2"))
    market_scout.display_competitor_landscape("Product A")
    captured = capsys.readouterr()
    assert "Competitor Landscape for Product A:" in captured.out
    assert "1. Competitor 1 - Description 1" in captured.out
    assert "2. Competitor 2 - Description 2" in captured.out
