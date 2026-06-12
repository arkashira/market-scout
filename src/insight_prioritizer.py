import json
from dataclasses import dataclass
from typing import List

@dataclass
class Insight:
    name: str
    priority: int
    description: str

class InsightPrioritizer:
    def __init__(self, insights: List[Insight]):
        self.insights = insights

    def prioritize_insights(self):
        return sorted(self.insights, key=lambda x: x.priority, reverse=True)

    def display_insights(self, insights):
        for insight in insights:
            print(f"Name: {insight.name}, Priority: {insight.priority}, Description: {insight.description}")

    def filter_insights(self, insights, min_priority):
        return [insight for insight in insights if insight.priority >= min_priority]

    def sort_insights(self, insights, sort_by):
        if sort_by == "name":
            return sorted(insights, key=lambda x: x.name)
        elif sort_by == "priority":
            return sorted(insights, key=lambda x: x.priority, reverse=True)
        else:
            return insights
