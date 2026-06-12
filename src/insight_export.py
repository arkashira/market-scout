import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class InsightDeck:
    title: str
    content: str

class InsightExportModule:
    def __init__(self, export_settings):
        self.export_settings = export_settings

    def generate_insight_deck(self, title, content):
        return InsightDeck(title, content)

    def export_insight_deck(self, insight_deck):
        if self.export_settings['format'] == 'json':
            return json.dumps({'title': insight_deck.title, 'content': insight_deck.content})
        else:
            raise ValueError('Unsupported export format')

def main():
    parser = ArgumentParser(description='Insight Export Module')
    parser.add_argument('--title', help='Insight deck title')
    parser.add_argument('--content', help='Insight deck content')
    parser.add_argument('--format', help='Export format (json)')
    args = parser.parse_args()

    export_settings = {'format': args.format}
    insight_export_module = InsightExportModule(export_settings)
    insight_deck = insight_export_module.generate_insight_deck(args.title, args.content)
    exported_deck = insight_export_module.export_insight_deck(insight_deck)
    print(exported_deck)

if __name__ == '__main__':
    main()
