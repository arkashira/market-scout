import pytest
from insight import Insight, InsightStore
import os
import json
import hashlib

@pytest.fixture
def temp_dir():
    dir = "temp"
    os.mkdir(dir)
    yield dir
    import shutil
    shutil.rmtree(dir)

def test_save_insight(temp_dir):
    store = InsightStore(temp_dir)
    insight = Insight("Test Insight", "2022-01-01", "2022-01-01", {"key": "value"})
    store.save_insight(insight)
    assert os.path.exists(os.path.join(temp_dir, f"{hashlib.sha256((insight.title + insight.creation_date).encode()).hexdigest()}.json"))

def test_load_insights(temp_dir):
    store = InsightStore(temp_dir)
    insight1 = Insight("Test Insight 1", "2022-01-01", "2022-01-01", {"key": "value"})
    insight2 = Insight("Test Insight 2", "2022-01-02", "2022-01-02", {"key": "value"})
    store.save_insight(insight1)
    store.save_insight(insight2)
    insights = store.load_insights()
    assert len(insights) == 2

def test_delete_insight(temp_dir):
    store = InsightStore(temp_dir)
    insight = Insight("Test Insight", "2022-01-01", "2022-01-01", {"key": "value"})
    store.save_insight(insight)
    insight_id = hashlib.sha256((insight.title + insight.creation_date).encode()).hexdigest()
    store.delete_insight(insight_id)
    assert not os.path.exists(os.path.join(temp_dir, f"{insight_id}.json"))

def test_duplicate_insight(temp_dir):
    store = InsightStore(temp_dir)
    insight = Insight("Test Insight", "2022-01-01", "2022-01-01", {"key": "value"})
    store.save_insight(insight)
    insight_id = hashlib.sha256((insight.title + insight.creation_date).encode()).hexdigest()
    store.duplicate_insight(insight_id)
    assert len(os.listdir(temp_dir)) == 2
