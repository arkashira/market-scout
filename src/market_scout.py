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
        return self.competitors.get(product_idea, [])

    def display_competitor_landscape(self, product_idea: str):
        competitors = self.generate_competitor_landscape(product_idea)
        print(f"Competitor Landscape for {product_idea}:")
        for i, competitor in enumerate(competitors):
            print(f"{i+1}. {competitor.name} - {competitor.description}")

def main():
    market_scout = MarketScout()
    market_scout.add_competitor("Product A", Competitor("Competitor 1", "Description 1"))
    market_scout.add_competitor("Product A", Competitor("Competitor 2", "Description 2"))
    market_scout.add_competitor("Product B", Competitor("Competitor 3", "Description 3"))
    product_idea = input("Enter a product idea: ")
    market_scout.display_competitor_landscape(product_idea)

if __name__ == "__main__":
    main()
