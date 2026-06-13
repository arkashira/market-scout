import pytest
from market_scout import MarketScout, Competitor, MarketSizing, OpportunityScore

def test_export_deck():
    title = 'Test Title'
    competitors = [Competitor('Competitor 1', 20.0), Competitor('Competitor 2', 30.0)]
    market_sizing = MarketSizing(100.0, 10.0)
    opportunity_score = OpportunityScore(8.0, 'Test Description')
    branding_colors = {'primary': 'blue', 'secondary': 'green'}
    language = 'English'

    market_scout = MarketScout(title, competitors, market_sizing, opportunity_score, branding_colors, language)
    pdf_file, pptx_file = market_scout.export_deck()

    assert pdf_file == 'deck.pdf'
    assert pptx_file == 'deck.pptx'

def test_get_branding_colors():
    title = 'Test Title'
    competitors = [Competitor('Competitor 1', 20.0), Competitor('Competitor 2', 30.0)]
    market_sizing = MarketSizing(100.0, 10.0)
    opportunity_score = OpportunityScore(8.0, 'Test Description')
    branding_colors = {'primary': 'blue', 'secondary': 'green'}
    language = 'English'

    market_scout = MarketScout(title, competitors, market_sizing, opportunity_score, branding_colors, language)
    assert market_scout.get_branding_colors() == branding_colors

def test_get_language():
    title = 'Test Title'
    competitors = [Competitor('Competitor 1', 20.0), Competitor('Competitor 2', 30.0)]
    market_sizing = MarketSizing(100.0, 10.0)
    opportunity_score = OpportunityScore(8.0, 'Test Description')
    branding_colors = {'primary': 'blue', 'secondary': 'green'}
    language = 'English'

    market_scout = MarketScout(title, competitors, market_sizing, opportunity_score, branding_colors, language)
    assert market_scout.get_language() == language
