from src.dashboard import Dashboard
import pytest
import json
from datetime import datetime

def test_load_insights():
    dashboard = Dashboard()
    data = '[{"title": "Test Insight", "creation_date": "2022-01-01", "status": "draft"}]'
    dashboard.load_insights(data)
    assert len(dashboard.dashboard.insights) == 1

def test_get_insights():
    dashboard = Dashboard()
    data = '[{"title": "Test Insight", "creation_date": "2022-01-01", "status": "draft"}]'
    dashboard.load_insights(data)
    insights = dashboard.get_insights(1, 20)
    assert len(insights) == 1

def test_delete_insight():
    dashboard = Dashboard()
    data = '[{"title": "Test Insight", "creation_date": "2022-01-01", "status": "draft"}]'
    dashboard.load_insights(data)
    dashboard.delete_insight("Test Insight")
    assert len(dashboard.dashboard.insights) == 0

def test_archive_insight():
    dashboard = Dashboard()
    data = '[{"title": "Test Insight", "creation_date": "2022-01-01", "status": "draft"}]'
    dashboard.load_insights(data)
    dashboard.archive_insight("Test Insight")
    assert dashboard.dashboard.insights[0].status == "archived"
