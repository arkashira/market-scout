import json
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Competitor:
    name: str
    tagline: str
    pricing_model: str
    market_share_estimate: float
    relevance_score: float

class MarketScout:
    def __init__(self):
        self.competitors = [
            Competitor("Competitor 1", "Tagline 1", "Pricing Model 1", 10.0, 90.0),
            Competitor("Competitor 2", "Tagline 2", "Pricing Model 2", 20.0, 80.0),
            Competitor("Competitor 3", "Tagline 3", "Pricing Model 3", 30.0, 70.0),
            Competitor("Competitor 4", "Tagline 4", "Pricing Model 4", 40.0, 60.0),
            Competitor("Competitor 5", "Tagline 5", "Pricing Model 5", 50.0, 50.0),
            Competitor("Competitor 6", "Tagline 6", "Pricing Model 6", 60.0, 40.0),
            Competitor("Competitor 7", "Tagline 7", "Pricing Model 7", 70.0, 30.0),
            Competitor("Competitor 8", "Tagline 8", "Pricing Model 8", 80.0, 20.0),
            Competitor("Competitor 9", "Tagline 9", "Pricing Model 9", 90.0, 10.0),
            Competitor("Competitor 10", "Tagline 10", "Pricing Model 10", 100.0, 0.0),
        ]

    def get_competitors(self, product_description: str) -> List[Competitor]:
        if len(product_description) > 250:
            raise ValueError("Product description must be 250 characters or less")
        return sorted(self.competitors, key=lambda x: x.relevance_score, reverse=True)

    def to_json(self, competitors: List[Competitor]) -> str:
        return json.dumps([asdict(competitor) for competitor in competitors])
