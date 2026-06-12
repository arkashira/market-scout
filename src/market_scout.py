import datetime
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass
class Insight:
    """Represents a market insight with optional hypothesis and validation status."""
    id: int
    owner: str
    hypothesis: str = ""
    status: str = "unvalidated"
    validated_at: Optional[datetime.datetime] = None

    def set_hypothesis(self, text: str) -> None:
        """Set or update the hypothesis text, enforcing a 300 character limit."""
        if len(text) > 300:
            raise ValueError("Hypothesis exceeds 300 characters")
        self.hypothesis = text

    def validate(self, user: str, logger: "EventLogger") -> None:
        """Mark the insight as validated if the user is authorized."""
        if user != self.owner and user != "admin":
            raise PermissionError("User not authorized to validate this insight")
        if self.status == "validated":
            # Already validated; no action needed
            return
        self.status = "validated"
        self.validated_at = datetime.datetime.utcnow()
        logger.log_event(
            event_type="insight_validated",
            insight_id=self.id,
            user=user,
            timestamp=self.validated_at,
        )


class InsightStore:
    """In-memory store for insights."""

    def __init__(self) -> None:
        self._insights: Dict[int, Insight] = {}
        self._next_id: int = 1

    def create_insight(self, owner: str) -> Insight:
        """Create a new insight with a unique ID."""
        insight = Insight(id=self._next_id, owner=owner)
        self._insights[self._next_id] = insight
        self._next_id += 1
        return insight

    def get_insight(self, insight_id: int) -> Insight:
        """Retrieve an insight by ID."""
        try:
            return self._insights[insight_id]
        except KeyError as exc:
            raise KeyError(f"Insight {insight_id} not found") from exc

    def update_insight(self, insight: Insight) -> None:
        """Persist changes to an existing insight."""
        if insight.id not in self._insights:
            raise KeyError(f"Insight {insight.id} not found")
        self._insights[insight.id] = insight

    def list_insights(self) -> List[Insight]:
        """Return all insights."""
        return list(self._insights.values())


class EventLogger:
    """Simple in-memory event logger."""

    def __init__(self) -> None:
        self.events: List[Dict] = []

    def log_event(self, event_type: str, **data) -> None:
        """Record an event with a timestamp."""
        event = {"type": event_type, "timestamp": datetime.datetime.utcnow()}
        event.update(data)
        self.events.append(event)


def get_validated_insights(store: InsightStore) -> List[Insight]:
    """Return all insights that have been validated."""
    return [insight for insight in store.list_insights() if insight.status == "validated"]
