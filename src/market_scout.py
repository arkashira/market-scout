import json
from dataclasses import dataclass
from typing import List
import time
import random

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
            Competitor("Competitor 1", "Tagline 1", "Pricing Model 1", 10.0, 0.0),
            Competitor("Competitor 2", "Tagline 2", "Pricing Model 2", 20.0, 0.0),
            Competitor("Competitor 3", "Tagline 3", "Pricing Model 3", 30.0, 0.0),
            Competitor("Competitor 4", "Tagline 4", "Pricing Model 4", 40.0, 0.0),
            Competitor("Competitor 5", "Tagline 5", "Pricing Model 5", 50.0, 0.0),
            Competitor("Competitor 6", "Tagline 6", "Pricing Model 6", 60.0, 0.0),
            Competitor("Competitor 7", "Tagline 7", "Pricing Model 7", 70.0, 0.0),
            Competitor("Competitor 8", "Tagline 8", "Pricing Model 8", 80.0, 0.0),
            Competitor("Competitor 9", "Tagline 9", "Pricing Model 9", 90.0, 0.0),
            Competitor("Competitor 10", "Tagline 10", "Pricing Model 10", 100.0, 0.0),
        ]

    def get_competitors(self, product_description: str) -> List[Competitor]:
        # Simulate AI model computation
        time.sleep(random.uniform(0.1, 1.5))
        for competitor in self.competitors:
            competitor.relevance_score = random.uniform(0.0, 100.0)
        self.competitors.sort(key=lambda x: x.relevance_score, reverse=True)
        return self.competitors

def main():
    market_scout = MarketScout()
    product_description = input("Enter a product description: ")
    if len(product_description) > 250:
        print("Product description too long. Please enter a description of up to 250 characters.")
        return
    competitors = market_scout.get_competitors(product_description)
    print(json.dumps([{
        "name": competitor.name,
        "tagline": competitor.tagline,
        "pricing_model": competitor.pricing_model,
        "market_share_estimate": competitor.market_share_estimate,
        "relevance_score": competitor.relevance_score
    } for competitor in competitors], indent=4))

if __name__ == "__main__":
    main()
