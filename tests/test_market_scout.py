from market_scout import MarketScout, Insight
import pytest
from unittest.mock import patch
from io import StringIO
import sys

def test_generate_insight():
    market_scout = MarketScout({"primary": "#000000", "secondary": "#FFFFFF"})
    insight = market_scout.generate_insight("Test Insight", ["Competitor 1", "Competitor 2"], 100, 50)
    assert insight.title == "Test Insight"
    assert insight.competitors == ["Competitor 1", "Competitor 2"]
    assert insight.market_size == 100
    assert insight.opportunity_score == 50

def test_export_insight():
    market_scout = MarketScout({"primary": "#000000", "secondary": "#FFFFFF"})
    insight = market_scout.generate_insight("Test Insight", ["Competitor 1", "Competitor 2"], 100, 50)
    with patch('sys.stdout', new=StringIO()) as fake_stdout:
        market_scout.export_insight(insight)
        assert "Exporting Test Insight to PDF..." in fake_stdout.getvalue()
        assert "Exporting Test Insight to PPTX..." in fake_stdout.getvalue()

def test_get_branding_colors():
    market_scout = MarketScout({"primary": "#000000", "secondary": "#FFFFFF"})
    branding_colors = market_scout.get_branding_colors()
    assert branding_colors == {"primary": "#000000", "secondary": "#FFFFFF"}

def test_get_language():
    market_scout = MarketScout({"primary": "#000000", "secondary": "#FFFFFF"}, "Spanish")
    language = market_scout.get_language()
    assert language == "Spanish"

def test_main():
    with patch('sys.argv', ['market_scout.py', '--branding_colors', '{"primary": "#000000", "secondary": "#FFFFFF"}', '--language', 'English']):
        with patch('sys.stdout', new=StringIO()) as fake_stdout:
            from market_scout import main
            main()
            assert "Exporting Test Insight to PDF..." in fake_stdout.getvalue()
            assert "Exporting Test Insight to PPTX..." in fake_stdout.getvalue()
