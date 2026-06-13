import json
from dataclasses import dataclass
from typing import List
import time
from urllib.parse import urlparse
from collections import defaultdict

@dataclass
class Competitor:
    name: str
    website_url: str
    core_feature_summary: str
    funding_stage: str
    relevance_score: float

class MarketScout:
    def __init__(self):
        self.competitors = [
            Competitor("Company A", "https://companya.com", "AI-powered marketing", "Series A", 0.8),
            Competitor("Company B", "https://companyb.com", "Data analytics platform", "Series B", 0.7),
            Competitor("Company C", "https://companyc.com", "Cloud-based CRM", "Series C", 0.6),
            Competitor("Company D", "https://companyd.com", "Cybersecurity solutions", "Series D", 0.5),
            Competitor("Company E", "https://companye.com", "E-commerce platform", "Series E", 0.4),
            Competitor("Company F", "https://companyf.com", "Financial services", "Series F", 0.3),
            Competitor("Company G", "https://companyg.com", "Gaming platform", "Series G", 0.2),
            Competitor("Company H", "https://companyh.com", "Healthcare services", "Series H", 0.1),
            Competitor("Company I", "https://companyi.com", "Insurance platform", "Series I", 0.05),
            Competitor("Company J", "https://companyj.com", "IT services", "Series J", 0.01),
        ]

    def get_competitors(self, product_idea: str) -> List[Competitor]:
        start_time = time.time()
        competitors = self.competitors.copy()
        competitors.sort(key=lambda x: self.calculate_relevance_score(x, product_idea), reverse=True)
        end_time = time.time()
        print(f"Response time: {end_time - start_time} seconds")
        return competitors[:10]

    def calculate_relevance_score(self, competitor: Competitor, product_idea: str) -> float:
        keyword_match = self.keyword_match(competitor.core_feature_summary, product_idea)
        funding_stage = self.funding_stage(competitor.funding_stage)
        market_segment = self.market_segment(competitor.name)
        return (keyword_match + funding_stage + market_segment) / 3

    def keyword_match(self, core_feature_summary: str, product_idea: str) -> float:
        keywords = product_idea.split()
        matches = sum(1 for keyword in keywords if keyword in core_feature_summary)
        return matches / len(keywords)

    def funding_stage(self, funding_stage: str) -> float:
        funding_stages = ["Series A", "Series B", "Series C", "Series D", "Series E", "Series F", "Series G", "Series H", "Series I", "Series J"]
        return 1 - (funding_stages.index(funding_stage) / len(funding_stages))

    def market_segment(self, name: str) -> float:
        market_segments = ["AI", "Data", "Cloud", "Cybersecurity", "E-commerce", "Financial", "Gaming", "Healthcare", "Insurance", "IT"]
        for segment in market_segments:
            if segment in name:
                return 1
        return 0

    def main(self):
        product_idea = input("Enter a product idea (max 200 chars): ")
        competitors = self.get_competitors(product_idea)
        for competitor in competitors:
            print(f"Name: {competitor.name}")
            print(f"Website URL: {competitor.website_url}")
            print(f"Core Feature Summary: {competitor.core_feature_summary}")
            print(f"Funding Stage: {competitor.funding_stage}")
            print(f"Relevance Score: {competitor.relevance_score}")
            print("")

if __name__ == "__main__":
    market_scout = MarketScout()
    market_scout.main()
