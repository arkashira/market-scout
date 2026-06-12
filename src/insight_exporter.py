import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class Competitor:
    name: str
    market_share: float

@dataclass
class MarketSizing:
    size: float
    growth_rate: float

@dataclass
class Insight:
    title: str
    competitors: List[Competitor]
    market_sizing: MarketSizing
    sources: List[str]

class InsightExporter:
    def __init__(self, insight: Insight):
        self.insight = insight

    def export_to_pptx(self) -> bytes:
        # Simulate generating a PPTX file
        pptx_content = f"Title: {self.insight.title}\n"
        pptx_content += "Competitors:\n"
        for competitor in self.insight.competitors:
            pptx_content += f"- {competitor.name}: {competitor.market_share}%\n"
        pptx_content += f"Market Sizing: {self.insight.market_sizing.size} ({self.insight.market_sizing.growth_rate}% growth rate)\n"
        pptx_content += "Sources:\n"
        for source in self.insight.sources:
            pptx_content += f"- {source}\n"
        return pptx_content.encode()

    def export_to_pdf(self) -> bytes:
        # Simulate generating a PDF file
        pdf_content = f"Title: {self.insight.title}\n"
        pdf_content += "Competitors:\n"
        for competitor in self.insight.competitors:
            pdf_content += f"- {competitor.name}: {competitor.market_share}%\n"
        pdf_content += f"Market Sizing: {self.insight.market_sizing.size} ({self.insight.market_sizing.growth_rate}% growth rate)\n"
        pdf_content += "Sources:\n"
        for source in self.insight.sources:
            pdf_content += f"- {source}\n"
        return pdf_content.encode()

    def log_telemetry(self, format_type: str):
        # Simulate logging a telemetry event
        print(f"insight_exported: {format_type}")
