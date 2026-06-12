from insight_export import InsightExportModule, InsightDeck
import json

def test_generate_insight_deck():
    insight_export_module = InsightExportModule({'format': 'json'})
    insight_deck = insight_export_module.generate_insight_deck('Test Title', 'Test Content')
    assert isinstance(insight_deck, InsightDeck)
    assert insight_deck.title == 'Test Title'
    assert insight_deck.content == 'Test Content'

def test_export_insight_deck_json():
    insight_export_module = InsightExportModule({'format': 'json'})
    insight_deck = InsightDeck('Test Title', 'Test Content')
    exported_deck = insight_export_module.export_insight_deck(insight_deck)
    assert json.loads(exported_deck) == {'title': 'Test Title', 'content': 'Test Content'}

def test_export_insight_deck_invalid_format():
    insight_export_module = InsightExportModule({'format': 'invalid'})
    insight_deck = InsightDeck('Test Title', 'Test Content')
    try:
        insight_export_module.export_insight_deck(insight_deck)
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert str(e) == 'Unsupported export format'
