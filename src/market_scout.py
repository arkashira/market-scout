import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, date
from typing import Dict, List, Optional, Tuple


@dataclass
class Feedback:
    report_id: str
    validated: bool
    timestamp: str  # ISO format


class InsightTracker:
    """
    Tracks insight validation feedback and provides simple analytics.
    """

    def __init__(self, storage_path: str = "insight_data.json"):
        self.storage_path = storage_path
        self._load()

    # ------------------------------------------------------------------ storage
    def _load(self) -> None:
        if os.path.exists(self.storage_path):
            with open(self.storage_path, "r", encoding="utf-8") as f:
                raw = json.load(f)
                self.feedback: List[Feedback] = [
                    Feedback(**item) for item in raw
                ]
        else:
            self.feedback = []

    def _save(self) -> None:
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump([asdict(fb) for fb in self.feedback], f, indent=2)

    # ----------------------------------------------------------------- public API
    def view_report(self, report_id: str) -> None:
        """
        Simulate a user viewing a report. In a real UI this would trigger a modal.
        Here we just ensure the report_id is known (no-op).
        """
        # No operation needed for the stub; method exists for completeness.
        pass

    def record_feedback(self, report_id: str, validated: bool) -> None:
        """
        Record the user's answer to the validation modal.
        """
        fb = Feedback(
            report_id=report_id,
            validated=validated,
            timestamp=datetime.utcnow().isoformat(),
        )
        self.feedback.append(fb)
        self._save()

    def monthly_validated_counts(self, year: int, month: int) -> int:
        """
        Return the number of insights marked as validated (Yes) in the given month.
        """
        count = 0
        for fb in self.feedback:
            if not fb.validated:
                continue
            ts = datetime.fromisoformat(fb.timestamp)
            if ts.year == year and ts.month == month:
                count += 1
        return count

    def export_daily(self, export_dir: str) -> str:
        """
        Export all feedback collected today to a JSON Lines file in `export_dir`.
        Returns the path of the created file.
        """
        today = date.today()
        filename = f"insights_{today.isoformat()}.jsonl"
        os.makedirs(export_dir, exist_ok=True)
        out_path = os.path.join(export_dir, filename)

        with open(out_path, "w", encoding="utf-8") as f:
            for fb in self.feedback:
                ts = datetime.fromisoformat(fb.timestamp).date()
                if ts == today:
                    f.write(json.dumps(asdict(fb)) + "\n")
        return out_path

    # ----------------------------------------------------------------- helper
    def get_all_feedback(self) -> List[Tuple[str, bool, str]]:
        """Utility for tests: returns list of (report_id, validated, timestamp)."""
        return [(fb.report_id, fb.validated, fb.timestamp) for fb in self.feedback]
