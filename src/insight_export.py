import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class InsightDeck:
    title: str
    slides: list

def generate_insight_deck(title: str, slides: list) -> InsightDeck:
    return InsightDeck(title, slides)

def export_insight_deck(deck: InsightDeck, format: str = 'json') -> str:
    if format == 'json':
        return json.dumps({'title': deck.title, 'slides': deck.slides})
    else:
        raise ValueError('Unsupported format')

def main():
    parser = ArgumentParser()
    parser.add_argument('--title', required=True)
    parser.add_argument('--slides', nargs='+', required=True)
    parser.add_argument('--format', default='json')
    args = parser.parse_args()

    deck = generate_insight_deck(args.title, args.slides)
    exported_deck = export_insight_deck(deck, args.format)
    print(exported_deck)

if __name__ == '__main__':
    main()
