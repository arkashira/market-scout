import json
from dataclasses import dataclass
from typing import List

@dataclass
class Competitor:
    name: str
    description: str
    market_share: float
    market_size: int
    growth_rate: float

class MarketScout:
    def __init__(self, competitors_data: List[Competitor]):
        self.competitors_data = competitors_data

    def get_competitors(self, product_idea: str) -> List[Competitor]:
        return [competitor for competitor in self.competitors_data if competitor.name.lower() == product_idea.lower()]

    def filter_competitors(self, competitors: List[Competitor], market_size: int = None, growth_rate: float = None) -> List[Competitor]:
        filtered_competitors = competitors
        if market_size:
            filtered_competitors = [competitor for competitor in filtered_competitors if competitor.market_size >= market_size]
        if growth_rate:
            filtered_competitors = [competitor for competitor in filtered_competitors if competitor.growth_rate >= growth_rate]
        return filtered_competitors

def load_competitors_data() -> List[Competitor]:
    competitors_data = [
        Competitor("Product A", "Description A", 0.2, 1000, 0.05),
        Competitor("Product B", "Description B", 0.3, 2000, 0.1),
        Competitor("Product C", "Description C", 0.1, 500, 0.02),
        Competitor("Product D", "Description D", 0.2, 1500, 0.07),
        Competitor("Product E", "Description E", 0.1, 800, 0.03),
    ]
    return competitors_data
