import pytest
from market_scout import MarketScout, Insight
import json
import os
import tempfile

def test_load_insights():
    with tempfile.TemporaryDirectory() as data_dir:
        market_scout = MarketScout(data_dir)
        market_scout.insights = {'report1': Insight('report1', True)}
        market_scout.save_insights()
        new_market_scout = MarketScout(data_dir)
        assert new_market_scout.insights['report1'].validated

def test_ask_for_validation(monkeypatch):
    with tempfile.TemporaryDirectory() as data_dir:
        market_scout = MarketScout(data_dir)
        monkeypatch.setattr('builtins.input', lambda: 'yes')
        market_scout.ask_for_validation('report1')
        assert market_scout.insights['report1'].validated

def test_get_validated_insights():
    with tempfile.TemporaryDirectory() as data_dir:
        market_scout = MarketScout(data_dir)
        market_scout.insights = {'report1': Insight('report1', True), 'report2': Insight('report2', False)}
        assert market_scout.get_validated_insights() == 1

def test_export_to_brain():
    with tempfile.TemporaryDirectory() as data_dir:
        market_scout = MarketScout(data_dir)
        market_scout.insights = {'report1': Insight('report1', True)}
        market_scout.export_to_brain()
        with open(os.path.join(data_dir, 'export.json'), 'r') as f:
            data = json.load(f)
        assert data['report1']

def test_display_privacy_notice(capsys):
    with tempfile.TemporaryDirectory() as data_dir:
        market_scout = MarketScout(data_dir)
        market_scout.display_privacy_notice()
        captured = capsys.readouterr()
        assert "Your feedback will be collected and stored for future use." in captured.out

def test_get_dashboard_metric():
    with tempfile.TemporaryDirectory() as data_dir:
        market_scout = MarketScout(data_dir)
        market_scout.insights = {'report1': Insight('report1', True), 'report2': Insight('report2', False)}
        assert market_scout.get_dashboard_metric() == "Total validated insights: 1"
