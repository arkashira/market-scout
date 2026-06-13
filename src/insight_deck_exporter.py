import json
import os
from dataclasses import dataclass
from typing import Dict, List, Optional
import argparse

@dataclass
class Competitor:
    name: str
    market_share: float

@dataclass
class MarketSizing:
    total_market: float
    growth_rate: float

@dataclass
class OpportunityScore:
    score: int
    description: str

@dataclass
class Insight:
    title: str
    competitors: List[Competitor]
    market_sizing: MarketSizing
    opportunity_score: OpportunityScore
    language: str = "English"
    branding_colors: Dict[str, str] = None

class InsightDeckExporter:
    def __init__(self, insight: Insight):
        self.insight = insight
        self.branding_colors = insight.branding_colors or {
            "primary": "#007BFF",
            "secondary": "#6C757D",
            "success": "#28A745",
            "danger": "#DC3545"
        }

    def export(self, output_path: str):
        insight_data = {
            "title": self.insight.title,
            "competitors": [{"name": c.name, "market_share": c.market_share} for c in self.insight.competitors],
            "market_sizing": {"total_market": self.insight.market_sizing.total_market, "growth_rate": self.insight.market_sizing.growth_rate},
            "opportunity_score": {"score": self.insight.opportunity_score.score, "description": self.insight.opportunity_score.description}
        }
        with open(output_path, 'w') as f:
            json.dump(insight_data, f, indent=4)

def main():
    parser = argparse.ArgumentParser(description="Export Insight Deck")
    parser.add_argument("--output", type=str, required=True, help="Path to output JSON file")
    parser.add_argument("--input", type=str, required=True, help="Path to input JSON file")
    args = parser.parse_args()
    with open(args.input, 'r') as f:
        insight_data = json.load(f)
    insight = Insight(
        title=insight_data["title"],
        competitors=[Competitor(**c) for c in insight_data["competitors"]],
        market_sizing=MarketSizing(**insight_data["market_sizing"]),
        opportunity_score=OpportunityScore(**insight_data["opportunity_score"]),
        language=insight_data.get("language", "English"),
        branding_colors=insight_data.get("branding_colors")
    )
    exporter = InsightDeckExporter(insight)
    exporter.export(args.output)

if __name__ == "__main__":
    main()
