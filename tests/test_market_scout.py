from market_scout import MarketScout, Competitor, load_competitors_data

def test_get_competitors():
    competitors_data = load_competitors_data()
    market_scout = MarketScout(competitors_data)
    product_idea = "Product A"
    competitors = market_scout.get_competitors(product_idea)
    assert len(competitors) == 1
    assert competitors[0].name == product_idea

def test_filter_competitors():
    competitors_data = load_competitors_data()
    market_scout = MarketScout(competitors_data)
    product_idea = "Product A"
    competitors = market_scout.get_competitors(product_idea)
    filtered_competitors = market_scout.filter_competitors(competitors, market_size=1000)
    assert len(filtered_competitors) == 1
    assert filtered_competitors[0].market_size >= 1000

def test_filter_competitors_growth_rate():
    competitors_data = load_competitors_data()
    market_scout = MarketScout(competitors_data)
    product_idea = "Product A"
    competitors = market_scout.get_competitors(product_idea)
    filtered_competitors = market_scout.filter_competitors(competitors, growth_rate=0.05)
    assert len(filtered_competitors) == 1
    assert filtered_competitors[0].growth_rate >= 0.05

def test_get_competitors_empty():
    competitors_data = []
    market_scout = MarketScout(competitors_data)
    product_idea = "Product A"
    competitors = market_scout.get_competitors(product_idea)
    assert len(competitors) == 0
