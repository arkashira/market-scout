import json
import os
import dataclasses
from datetime import datetime
from typing import List

@dataclasses.dataclass
class Insight:
    title: str
    creation_date: str
    last_modified: str
    competitor_list: List[str]
    heatmap: str
    scores: str

class InsightStore:
    def __init__(self, storage_dir):
        self.storage_dir = storage_dir

    def save_insight(self, insight: Insight):
        insight_dict = dataclasses.asdict(insight)
        with open(os.path.join(self.storage_dir, f"{insight.title}.json"), "w") as f:
            json.dump(insight_dict, f)

    def load_insights(self):
        insights = []
        for filename in os.listdir(self.storage_dir):
            if filename.endswith(".json"):
                with open(os.path.join(self.storage_dir, filename), "r") as f:
                    insight_dict = json.load(f)
                    insight = Insight(
                        title=insight_dict["title"],
                        creation_date=insight_dict["creation_date"],
                        last_modified=insight_dict["last_modified"],
                        competitor_list=insight_dict["competitor_list"],
                        heatmap=insight_dict["heatmap"],
                        scores=insight_dict["scores"],
                    )
                    insights.append(insight)
        # Sort the insights by title
        insights.sort(key=lambda x: x.title)
        return insights

    def delete_insight(self, title: str):
        os.remove(os.path.join(self.storage_dir, f"{title}.json"))

    def duplicate_insight(self, title: str):
        with open(os.path.join(self.storage_dir, f"{title}.json"), "r") as f:
            insight_dict = json.load(f)
            new_title = f"{title} (copy)"
            insight_dict["title"] = new_title
            with open(os.path.join(self.storage_dir, f"{new_title}.json"), "w") as f:
                json.dump(insight_dict, f)
