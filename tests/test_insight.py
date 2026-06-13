import os
import pytest
import hashlib
from insight import Insight, InsightStore

@pytest.fixture
def insight_store(tmp_path):
    return InsightStore(tmp_path)

def test_save_insight(insight_store):
    insight = Insight(
        title="Test Insight",
        creation_date="2022-01-01 12:00:00",
        last_modified="2022-01-01 12:00:00",
        data={"competitor_list": ["Competitor 1", "Competitor 2"], "heatmap": {}, "scores": {}}
    )
    insight_store.save_insight(insight)
    assert os.path.exists(os.path.join(insight_store.storage_dir, f"{hashlib.sha256(insight.title.encode()).hexdigest()}.json"))

def test_load_insights(insight_store):
    insight = Insight(
        title="Test Insight",
        creation_date="2022-01-01 12:00:00",
        last_modified="2022-01-01 12:00:00",
        data={"competitor_list": ["Competitor 1", "Competitor 2"], "heatmap": {}, "scores": {}}
    )
    insight_store.save_insight(insight)
    insights = insight_store.load_insights()
    assert len(insights) == 1
    assert insights[0].title == insight.title

def test_delete_insight(insight_store):
    insight = Insight(
        title="Test Insight",
        creation_date="2022-01-01 12:00:00",
        last_modified="2022-01-01 12:00:00",
        data={"competitor_list": ["Competitor 1", "Competitor 2"], "heatmap": {}, "scores": {}}
    )
    insight_store.save_insight(insight)
    insight_id = hashlib.sha256(insight.title.encode()).hexdigest()
    insight_store.delete_insight(insight_id)
    assert not os.path.exists(os.path.join(insight_store.storage_dir, f"{insight_id}.json"))

def test_duplicate_insight(insight_store):
    insight = Insight(
        title="Test Insight",
        creation_date="2022-01-01 12:00:00",
        last_modified="2022-01-01 12:00:00",
        data={"competitor_list": ["Competitor 1", "Competitor 2"], "heatmap": {}, "scores": {}}
    )
    insight_store.save_insight(insight)
    insight_id = hashlib.sha256(insight.title.encode()).hexdigest()
    insight_store.duplicate_insight(insight_id)
    insights = insight_store.load_insights()
    assert len(insights) == 2
    assert insights[0].title == insight.title
    assert insights[1].title == insight.title + " copy"
