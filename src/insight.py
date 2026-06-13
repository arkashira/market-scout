import json
import os
import hashlib
from dataclasses import dataclass
from datetime import datetime

@dataclass
class Insight:
    title: str
    creation_date: str
    last_modified: str
    data: dict

class InsightStore:
    def __init__(self, storage_dir):
        self.storage_dir = storage_dir

    def save_insight(self, insight):
        insight_id = hashlib.sha256(insight.title.encode()).hexdigest()
        insight_data = {
            "title": insight.title,
            "creation_date": insight.creation_date,
            "last_modified": insight.last_modified,
            "data": insight.data
        }
        with open(os.path.join(self.storage_dir, f"{insight_id}.json"), "w") as f:
            json.dump(insight_data, f)

    def load_insights(self):
        insights = []
        for filename in os.listdir(self.storage_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.storage_dir, filename), "r") as f:
                    insight_data = json.load(f)
                    insight = Insight(
                        title=insight_data["title"],
                        creation_date=insight_data["creation_date"],
                        last_modified=insight_data["last_modified"],
                        data=insight_data["data"]
                    )
                    insights.append(insight)
        return insights

    def delete_insight(self, insight_id):
        filename = f"{insight_id}.json"
        if os.path.exists(os.path.join(self.storage_dir, filename)):
            os.remove(os.path.join(self.storage_dir, filename))

    def duplicate_insight(self, insight_id):
        filename = f"{insight_id}.json"
        if os.path.exists(os.path.join(self.storage_dir, filename)):
            with open(os.path.join(self.storage_dir, filename), "r") as f:
                insight_data = json.load(f)
                new_insight_id = hashlib.sha256((insight_data["title"] + " copy").encode()).hexdigest()
                new_insight_data = {
                    "title": insight_data["title"] + " copy",
                    "creation_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "last_modified": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "data": insight_data["data"]
                }
                with open(os.path.join(self.storage_dir, f"{new_insight_id}.json"), "w") as f:
                    json.dump(new_insight_data, f)
