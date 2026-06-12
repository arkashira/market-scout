from src.insight import Insight, InsightDashboard
import json
from datetime import datetime

class Dashboard:
    def __init__(self):
        self.dashboard = InsightDashboard()

    def load_insights(self, data: str):
        insights_data = json.loads(data)
        for insight_data in insights_data:
            insight = Insight(
                title=insight_data["title"],
                creation_date=datetime.strptime(insight_data["creation_date"], "%Y-%m-%d"),
                status=insight_data["status"]
            )
            self.dashboard.add_insight(insight)

    def get_insights(self, page: int, per_page: int):
        return self.dashboard.get_insights(page, per_page)

    def delete_insight(self, title: str):
        self.dashboard.delete_insight(title)

    def archive_insight(self, title: str):
        self.dashboard.archive_insight(title)
