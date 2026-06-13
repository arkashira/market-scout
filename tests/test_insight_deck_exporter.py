import os
import json
from src.insight_deck_exporter import Insight, Competitor, MarketSizing, OpportunityScore, InsightDeckExporter

def test_insight_deck_exporter():
    insight = Insight(
        title="Test Insight",
        competitors=[Competitor(name="Competitor 1", market_share=0.5), Competitor(name="Competitor 2", market_share=0.3)],
        market_sizing=MarketSizing(total_market=100, growth_rate=10),
        opportunity_score=OpportunityScore(score=8, description="High opportunity")
    )
    exporter = InsightDeckExporter(insight)
    output_path = "test_output.json"
    exporter.export(output_path)
    with open(output_path, 'r') as f:
        output_data = json.load(f)
    assert output_data["title"] == insight.title
    assert len(output_data["competitors"]) == len(insight.competitors)
    for i, competitor in enumerate(insight.competitors):
        assert output_data["competitors"][i]["name"] == competitor.name
        assert output_data["competitors"][i]["market_share"] == competitor.market_share
    assert output_data["market_sizing"]["total_market"] == insight.market_sizing.total_market
    assert output_data["market_sizing"]["growth_rate"] == insight.market_sizing.growth_rate
    assert output_data["opportunity_score"]["score"] == insight.opportunity_score.score
    assert output_data["opportunity_score"]["description"] == insight.opportunity_score.description
    os.remove(output_path)
