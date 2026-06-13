import json
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List

@dataclass
class Competitor:
    name: str
    market_share: float

@dataclass
class MarketSizing:
    size: float
    growth_rate: float

@dataclass
class OpportunityScore:
    score: float
    description: str

class MarketScout:
    def __init__(self, title: str, competitors: List[Competitor], market_sizing: MarketSizing, opportunity_score: OpportunityScore, branding_colors: Dict[str, str], language: str = 'English'):
        self.title = title
        self.competitors = competitors
        self.market_sizing = market_sizing
        self.opportunity_score = opportunity_score
        self.branding_colors = branding_colors
        self.language = language

    def export_deck(self):
        # Generate title slide
        title_slide = f'Title: {self.title}\n'

        # Generate competitor table
        competitor_table = 'Competitors:\n'
        for competitor in self.competitors:
            competitor_table += f'- {competitor.name}: {competitor.market_share}%\n'

        # Generate market sizing chart
        market_sizing_chart = f'Market Size: {self.market_sizing.size}\nGrowth Rate: {self.market_sizing.growth_rate}%\n'

        # Generate opportunity score slide
        opportunity_score_slide = f'Opportunity Score: {self.opportunity_score.score}\nDescription: {self.opportunity_score.description}\n'

        # Generate deck
        deck = title_slide + competitor_table + market_sizing_chart + opportunity_score_slide

        # Save deck as PDF and PowerPoint
        with open('deck.pdf', 'w') as f:
            f.write(deck)
        with open('deck.pptx', 'w') as f:
            f.write(deck)

        return 'deck.pdf', 'deck.pptx'

    def get_branding_colors(self):
        return self.branding_colors

    def get_language(self):
        return self.language
