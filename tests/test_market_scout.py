import pytest
from market_scout import MarketScout, Competitor, FeatureCategory

def test_generate_heatmap():
    competitors = [
        Competitor("Competitor A", {"Feature 1": 80, "Feature 2": 20, "Feature 3": 0}),
        Competitor("Competitor B", {"Feature 1": 0, "Feature 2": 100, "Feature 3": 50}),
        Competitor("Competitor C", {"Feature 1": 50, "Feature 2": 0, "Feature 3": 100})
    ]

    feature_categories = [
        FeatureCategory("Feature 1", competitors),
        FeatureCategory("Feature 2", competitors),
        FeatureCategory("Feature 3", competitors)
    ]

    market_scout = MarketScout(competitors, feature_categories)
    heatmap = market_scout.generate_heatmap()
    assert len(heatmap) == len(competitors)
    assert len(heatmap[0]) == len(feature_categories)

def test_generate_tooltip():
    competitor = Competitor("Competitor A", {"Feature 1": 80, "Feature 2": 20, "Feature 3": 0})
    feature_category = FeatureCategory("Feature 1", [competitor])
    market_scout = MarketScout([competitor], [feature_category])
    tooltip = market_scout.generate_tooltip(competitor, feature_category)
    assert "Feature 1: 80%" in tooltip

def test_main():
    import io
    import sys
    capturedOutput = io.StringIO()
    sys.stdout = capturedOutput
    from market_scout import main
    main()
    sys.stdout = sys.__stdout__
    assert capturedOutput.getvalue() != ""
