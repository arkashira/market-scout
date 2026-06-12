import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Insight:
    id: int
    validated_at: datetime = None

class InsightManager:
    def __init__(self):
        self.insights = []
        self.audit_log = []
        self.nsm_counter = 0

    def add_insight(self, insight):
        self.insights.append(insight)

    def validate_insight(self, insight_id, user_id):
        for insight in self.insights:
            if insight.id == insight_id:
                insight.validated_at = datetime.now()
                self.audit_log.append({
                    'user_id': user_id,
                    'insight_id': insight_id,
                    'timestamp': datetime.now().isoformat()
                })
                self.nsm_counter += 1
                return

    def get_validated_insights(self):
        return [insight for insight in self.insights if insight.validated_at]

    def get_audit_log(self):
        return self.audit_log

    def get_nsm_counter(self):
        return self.nsm_counter
