import json
from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Competitor:
    name: str
    features: Dict[str, int]

@dataclass
class FeatureCategory:
    name: str
    competitors: List[Competitor]

class MarketScout:
    def __init__(self, competitors: List[Competitor], feature_categories: List[FeatureCategory]):
        self.competitors = competitors
        self.feature_categories = feature_categories

    def generate_heatmap(self):
        heatmap = []
        for competitor in self.competitors:
            row = []
            for category in self.feature_categories:
                feature_presence = 0
                for feature, presence in competitor.features.items():
                    if feature in category.name:
                        feature_presence = presence
                row.append(feature_presence)
            heatmap.append(row)
        return heatmap

    def generate_tooltip(self, competitor: Competitor, feature_category: FeatureCategory):
        tooltip = ""
        for feature, presence in competitor.features.items():
            if feature in feature_category.name:
                tooltip += f"{feature}: {presence}%"
        return tooltip

def main():
    competitors = [
        Competitor("Competitor A", {"Feature 1": 80, "Feature 2": 20, "Feature 3": 0}),
        Competitor("Competitor B", {"Feature 1": 0, "Feature 2": 100, "Feature 3": 50}),
        Competitor("Competitor C", {"Feature 1": 50, "Feature 2": 0, "Feature 3": 100})
    ]

    feature_categories = [
        FeatureCategory("Feature 1", competitors),
        FeatureCategory("Feature 2", competitors),
        FeatureCategory("Feature 3", competitors)
    ]

    market_scout = MarketScout(competitors, feature_categories)
    heatmap = market_scout.generate_heatmap()
    print(json.dumps(heatmap))

if __name__ == "__main__":
    main()
