import pytest
from market_scout import Insight, Competitor, MarketSizing, export_insight

def test_generate_pptx():
    insight = Insight(
        title='Market Insight',
        competitors=[Competitor('Competitor 1', 0.2), Competitor('Competitor 2', 0.3)],
        market_sizings=[MarketSizing('Market Sizing 1', 100.0), MarketSizing('Market Sizing 2', 200.0)],
        sources=['Source 1', 'Source 2']
    )
    content = export_insight(insight, 'pptx')
    assert len(content) < 5 * 1024 * 1024  # 5 MB

def test_generate_pdf():
    insight = Insight(
        title='Market Insight',
        competitors=[Competitor('Competitor 1', 0.2), Competitor('Competitor 2', 0.3)],
        market_sizings=[MarketSizing('Market Sizing 1', 100.0), MarketSizing('Market Sizing 2', 200.0)],
        sources=['Source 1', 'Source 2']
    )
    content = export_insight(insight, 'pdf')
    assert len(content) < 5 * 1024 * 1024  # 5 MB

def test_export_insight():
    insight = Insight(
        title='Market Insight',
        competitors=[Competitor('Competitor 1', 0.2), Competitor('Competitor 2', 0.3)],
        market_sizings=[MarketSizing('Market Sizing 1', 100.0), MarketSizing('Market Sizing 2', 200.0)],
        sources=['Source 1', 'Source 2']
    )
    content = export_insight(insight, 'pptx')
    assert content is not None

def test_invalid_format():
    insight = Insight(
        title='Market Insight',
        competitors=[Competitor('Competitor 1', 0.2), Competitor('Competitor 2', 0.3)],
        market_sizings=[MarketSizing('Market Sizing 1', 100.0), MarketSizing('Market Sizing 2', 200.0)],
        sources=['Source 1', 'Source 2']
    )
    with pytest.raises(ValueError):
        export_insight(insight, 'invalid')
