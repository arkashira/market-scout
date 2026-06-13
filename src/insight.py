import json
from dataclasses import dataclass
from datetime import datetime
import os
import hashlib

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
        insight_id = hashlib.sha256((insight.title + insight.creation_date).encode()).hexdigest()
        with open(os.path.join(self.storage_dir, f"{insight_id}.json"), "w") as f:
            json.dump({
                "title": insight.title,
                "creation_date": insight.creation_date,
                "last_modified": insight.last_modified,
                "data": insight.data
            }, f)

    def load_insights(self):
        insights = []
        for filename in os.listdir(self.storage_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.storage_dir, filename), "r") as f:
                    data = json.load(f)
                    insights.append(Insight(
                        title=data["title"],
                        creation_date=data["creation_date"],
                        last_modified=data["last_modified"],
                        data=data["data"]
                    ))
        return insights

    def delete_insight(self, insight_id):
        os.remove(os.path.join(self.storage_dir, f"{insight_id}.json"))

    def duplicate_insight(self, insight_id):
        with open(os.path.join(self.storage_dir, f"{insight_id}.json"), "r") as f:
            data = json.load(f)
            new_insight_id = hashlib.sha256((data["title"] + str(datetime.now())).encode()).hexdigest()
            with open(os.path.join(self.storage_dir, f"{new_insight_id}.json"), "w") as new_f:
                json.dump(data, new_f)
