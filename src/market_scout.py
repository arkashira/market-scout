import json
from dataclasses import dataclass
from typing import List

@dataclass
class Competitor:
    name: str
    description: str
    funding: int
    employee_count: int
    product_focus: str
    relevance_score: float

class MarketScout:
    def __init__(self, keyword: str):
        if keyword is None:
            raise AttributeError("Keyword cannot be None")
        self.keyword = keyword
        self.competitors = self.generate_competitors()

    def generate_competitors(self) -> List[Competitor]:
        # Simulate competitor data generation
        competitors = [
            Competitor("Company A", "Description A", 1000000, 50, "Product A", 0.8),
            Competitor("Company B", "Description B", 500000, 20, "Product B", 0.6),
            Competitor("Company C", "Description C", 2000000, 100, "Product C", 0.9),
            Competitor("Company D", "Description D", 800000, 30, "Product D", 0.7),
            Competitor("Company E", "Description E", 1500000, 60, "Product E", 0.85),
            Competitor("Company F", "Description F", 1200000, 40, "Product F", 0.75),
            Competitor("Company G", "Description G", 2500000, 120, "Product G", 0.95),
            Competitor("Company H", "Description H", 900000, 35, "Product H", 0.65),
            Competitor("Company I", "Description I", 1800000, 70, "Product I", 0.8),
            Competitor("Company J", "Description J", 2200000, 90, "Product J", 0.9),
        ]
        return sorted(competitors, key=lambda x: x.relevance_score, reverse=True)

    def get_competitors(self) -> List[dict]:
        return [
            {
                "name": competitor.name,
                "description": competitor.description,
                "funding": competitor.funding,
                "employee_count": competitor.employee_count,
                "product_focus": competitor.product_focus,
                "relevance_score": competitor.relevance_score,
                "source": "https://example.com/source",
            }
            for competitor in self.competitors
        ]

    def main(self):
        import argparse
        parser = argparse.ArgumentParser()
        parser.add_argument("keyword", help="Target market keyword")
        args = parser.parse_args()
        market_scout = MarketScout(args.keyword)
        competitors = market_scout.get_competitors()
        print(json.dumps(competitors, indent=4))

if __name__ == "__main__":
    MarketScout("test_keyword").main()
