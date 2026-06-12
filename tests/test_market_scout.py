import datetime
import pytest

from market_scout import (
    Insight,
    InsightStore,
    EventLogger,
    get_validated_insights,
)


@pytest.fixture
def store() -> InsightStore:
    return InsightStore()


@pytest.fixture
def logger() -> EventLogger:
    return EventLogger()


def test_add_and_edit_hypothesis(store: InsightStore) -> None:
    insight = store.create_insight(owner="alice")
    # Add hypothesis within limit
    insight.set_hypothesis("Short hypothesis")
    assert insight.hypothesis == "Short hypothesis"

    # Edit hypothesis
    insight.set_hypothesis("Updated hypothesis")
    assert insight.hypothesis == "Updated hypothesis"

    # Exceeding 300 characters should raise ValueError
    long_text = "a" * 301
    with pytest.raises(ValueError):
        insight.set_hypothesis(long_text)


def test_validate_permission_and_timestamp(store: InsightStore, logger: EventLogger) -> None:
    insight = store.create_insight(owner="bob")

    # Non-owner, non-admin should fail
    with pytest.raises(PermissionError):
        insight.validate(user="alice", logger=logger)

    # Owner can validate
    before = datetime.datetime.utcnow()
    insight.validate(user="bob", logger=logger)
    after = datetime.datetime.utcnow()
    assert insight.status == "validated"
    assert insight.validated_at is not None
    assert before <= insight.validated_at <= after

    # Admin can also validate (idempotent)
    insight.status = "unvalidated"
    insight.validated_at = None
    insight.validate(user="admin", logger=logger)
    assert insight.status == "validated"
    assert insight.validated_at is not None


def test_metrics_exposes_validated_insights(store: InsightStore, logger: EventLogger) -> None:
    insight1 = store.create_insight(owner="alice")
    insight2 = store.create_insight(owner="bob")

    insight1.validate(user="alice", logger=logger)
    # insight2 remains unvalidated

    validated = get_validated_insights(store)
    assert len(validated) == 1
    assert validated[0].id == insight1.id
    assert validated[0].status == "validated"


def test_event_logging_on_validation(store: InsightStore, logger: EventLogger) -> None:
    insight = store.create_insight(owner="alice")
    insight.validate(user="alice", logger=logger)

    assert len(logger.events) == 1
    event = logger.events[0]
    assert event["type"] == "insight_validated"
    assert event["insight_id"] == insight.id
    assert event["user"] == "alice"
    assert isinstance(event["timestamp"], datetime.datetime)
