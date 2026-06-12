import json
from dataclasses import dataclass
from typing import List

@dataclass
class Competitor:
    name: str
    description: str

class MarketScout:
    def __init__(self):
        self.competitors = {}

    def add_competitor(self, product_idea: str, competitor: Competitor):
        if product_idea not in self.competitors:
            self.competitors[product_idea] = []
        self.competitors[product_idea].append(competitor)

    def generate_competitor_landscape(self, product_idea: str):
        if product_idea in self.competitors:
            return self.competitors[product_idea]
        else:
            return []

    def display_competitor_landscape(self, competitor_landscape: List[Competitor]):
        print("Competitor Landscape:")
        for i, competitor in enumerate(competitor_landscape):
            print(f"{i+1}. {competitor.name} - {competitor.description}")

def main():
    market_scout = MarketScout()
    market_scout.add_competitor("Product A", Competitor("Competitor 1", "Description 1"))
    market_scout.add_competitor("Product A", Competitor("Competitor 2", "Description 2"))
    market_scout.add_competitor("Product B", Competitor("Competitor 3", "Description 3"))

    product_idea = "Product A"
    competitor_landscape = market_scout.generate_competitor_landscape(product_idea)
    market_scout.display_competitor_landscape(competitor_landscape)

if __name__ == "__main__":
    main()
