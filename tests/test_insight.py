from insight import Insight, InsightManager
import pytest
from datetime import datetime

def test_add_insight():
    manager = InsightManager()
    insight = Insight(1)
    manager.add_insight(insight)
    assert len(manager.insights) == 1

def test_validate_insight():
    manager = InsightManager()
    insight = Insight(1)
    manager.add_insight(insight)
    manager.validate_insight(1, 1)
    assert insight.validated_at is not None
    assert len(manager.audit_log) == 1
    assert manager.nsm_counter == 1

def test_get_validated_insights():
    manager = InsightManager()
    insight1 = Insight(1)
    insight2 = Insight(2)
    manager.add_insight(insight1)
    manager.add_insight(insight2)
    manager.validate_insight(1, 1)
    validated_insights = manager.get_validated_insights()
    assert len(validated_insights) == 1
    assert validated_insights[0].id == 1

def test_get_audit_log():
    manager = InsightManager()
    insight = Insight(1)
    manager.add_insight(insight)
    manager.validate_insight(1, 1)
    audit_log = manager.get_audit_log()
    assert len(audit_log) == 1
    assert audit_log[0]['user_id'] == 1
    assert audit_log[0]['insight_id'] == 1

def test_get_nsm_counter():
    manager = InsightManager()
    insight = Insight(1)
    manager.add_insight(insight)
    manager.validate_insight(1, 1)
    assert manager.get_nsm_counter() == 1
