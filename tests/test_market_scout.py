import pytest
from market_scout import MarketScout

def test_calculate_score() -> None:
    market_scout = MarketScout(competitor_density=10, tam=100, funding_activity=5, weightings={'competitor_density': 0.2, 'tam': 0.5, 'funding_activity': 0.3})
    score = market_scout.calculate_score()
    assert 0 <= score <= 100

def test_get_tier() -> None:
    market_scout = MarketScout(competitor_density=10, tam=100, funding_activity=5, weightings={'competitor_density': 0.2, 'tam': 0.5, 'funding_activity': 0.3})
    score = market_scout.calculate_score()
    tier = market_scout.get_tier(score)
    assert tier in ['Low', 'Medium', 'High']

def test_adjust_weightings() -> None:
    market_scout = MarketScout(competitor_density=10, tam=100, funding_activity=5, weightings={'competitor_density': 0.2, 'tam': 0.5, 'funding_activity': 0.3})
    new_weightings = {'competitor_density': 0.3, 'tam': 0.4, 'funding_activity': 0.3}
    market_scout.adjust_weightings(new_weightings)
    assert market_scout.weightings == new_weightings

def test_persist_score() -> None:
    market_scout = MarketScout(competitor_density=10, tam=100, funding_activity=5, weightings={'competitor_density': 0.2, 'tam': 0.5, 'funding_activity': 0.3})
    score = market_scout.calculate_score()
    persisted_score = market_scout.persist_score(score)
    assert 'score' in persisted_score and 'tier' in persisted_score

def test_main() -> None:
    # This test is just to ensure the main function runs without errors
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    from market_scout import main
    main()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() != ''
