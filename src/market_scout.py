import json
from dataclasses import dataclass
from typing import List
import argparse

@dataclass
class Competitor:
    name: str
    market_share: float

@dataclass
class MarketSizing:
    title: str
    value: float

@dataclass
class Insight:
    title: str
    competitors: List[Competitor]
    market_sizings: List[MarketSizing]
    sources: List[str]

def generate_pptx(insight: Insight) -> bytes:
    # Generate PPTX content
    content = f"""
    {insight.title}
    Competitors:
    {', '.join([c.name for c in insight.competitors])}
    Market Sizing:
    {', '.join([ms.title for ms in insight.market_sizings])}
    Sources:
    {', '.join(insight.sources)}
    """
    return content.encode('utf-8')

def generate_pdf(insight: Insight) -> bytes:
    # Generate PDF content
    content = f"""
    {insight.title}
    Competitors:
    {', '.join([c.name for c in insight.competitors])}
    Market Sizing:
    {', '.join([ms.title for ms in insight.market_sizings])}
    Sources:
    {', '. join(insight.sources)}
    """
    return content.encode('utf-8')

def export_insight(insight: Insight, format: str) -> bytes:
    if format == 'pptx':
        return generate_pptx(insight)
    elif format == 'pdf':
        return generate_pdf(insight)
    else:
        raise ValueError('Invalid format')

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--format', choices=['pptx', 'pdf'], required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()

    insight = Insight(
        title='Market Insight',
        competitors=[Competitor('Competitor 1', 0.2), Competitor('Competitor 2', 0.3)],
        market_sizings=[MarketSizing('Market Sizing 1', 100.0), MarketSizing('Market Sizing 2', 200.0)],
        sources=['Source 1', 'Source 2']
    )

    content = export_insight(insight, args.format)

    with open(args.output, 'wb') as f:
        f.write(content)

if __name__ == '__main__':
    main()
