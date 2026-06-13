from insight_export import generate_insight_deck, export_insight_deck
import json

def test_generate_insight_deck():
    title = 'Test Deck'
    slides = ['Slide 1', 'Slide 2']
    deck = generate_insight_deck(title, slides)
    assert deck.title == title
    assert deck.slides == slides

def test_export_insight_deck_json():
    title = 'Test Deck'
    slides = ['Slide 1', 'Slide 2']
    deck = generate_insight_deck(title, slides)
    exported_deck = export_insight_deck(deck)
    expected_output = {'title': title, 'slides': slides}
    assert json.loads(exported_deck) == expected_output

def test_export_insight_deck_invalid_format():
    title = 'Test Deck'
    slides = ['Slide 1', 'Slide 2']
    deck = generate_insight_deck(title, slides)
    try:
        export_insight_deck(deck, 'invalid_format')
        assert False, 'Expected ValueError'
    except ValueError as e:
        assert str(e) == 'Unsupported format'
