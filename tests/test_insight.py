import pytest
from insight import Insight, InsightStore
import os
import json

@pytest.fixture
def insight_store(tmp_path):
    return InsightStore(tmp_path)

def test_save_insight(insight_store):
    insight = Insight(
        title="Test Insight",
        creation_date="2022-01-01",
        last_modified="2022-01-01",
        competitor_list=["Competitor 1", "Competitor 2"],
        heatmap="Heatmap data",
        scores="Score data",
    )
    insight_store.save_insight(insight)
    assert os.path.exists(os.path.join(insight_store.storage_dir, "Test Insight.json"))

def test_load_insights(insight_store):
    insight = Insight(
        title="Test Insight",
        creation_date="2022-01-01",
        last_modified="2022-01-01",
        competitor_list=["Competitor 1", "Competitor 2"],
        heatmap="Heatmap data",
        scores="Score data",
    )
    insight_store.save_insight(insight)
    insights = insight_store.load_insights()
    assert len(insights) == 1
    assert insights[0].title == "Test Insight"

def test_delete_insight(insight_store):
    insight = Insight(
        title="Test Insight",
        creation_date="2022-01-01",
        last_modified="2022-01-01",
        competitor_list=["Competitor 1", "Competitor 2"],
        heatmap="Heatmap data",
        scores="Score data",
    )
    insight_store.save_insight(insight)
    insight_store.delete_insight("Test Insight")
    assert not os.path.exists(os.path.join(insight_store.storage_dir, "Test Insight.json"))

def test_duplicate_insight(insight_store):
    insight = Insight(
        title="Test Insight",
        creation_date="2022-01-01",
        last_modified="2022-01-01",
        competitor_list=["Competitor 1", "Competitor 2"],
        heatmap="Heatmap data",
        scores="Score data",
    )
    insight_store.save_insight(insight)
    insight_store.duplicate_insight("Test Insight")
    insights = insight_store.load_insights()
    assert len(insights) == 2
    assert insights[0].title == "Test Insight"
    assert insights[1].title == "Test Insight (copy)"
