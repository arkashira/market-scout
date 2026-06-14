import json
from dataclasses import dataclass
from datetime import datetime
import os

@dataclass
class Insight:
    id: str
    validated: bool

class MarketScout:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)
        self.insights = self.load_insights()

    def load_insights(self):
        insights = {}
        insights_path = os.path.join(self.data_dir, 'insights.json')
        if os.path.exists(insights_path):
            with open(insights_path, 'r') as f:
                data = json.load(f)
            for id, validated in data.items():
                insights[id] = Insight(id, validated)
        return insights

    def save_insights(self):
        data = {id: insight.validated for id, insight in self.insights.items()}
        insights_path = os.path.join(self.data_dir, 'insights.json')
        with open(insights_path, 'w') as f:
            json.dump(data, f)

    def ask_for_validation(self, report_id):
        print("Did this insight inform a product hypothesis? (Yes/No)")
        response = input()
        if response.lower() == 'yes':
            self.insights[report_id] = Insight(report_id, True)
        else:
            self.insights[report_id] = Insight(report_id, False)
        self.save_insights()

    def get_validated_insights(self):
        return sum(1 for insight in self.insights.values() if insight.validated)

    def export_to_brain(self):
        data = {id: insight.validated for id, insight in self.insights.items()}
        export_path = os.path.join(self.data_dir, 'export.json')
        with open(export_path, 'w') as f:
            json.dump(data, f)

    def display_privacy_notice(self):
        print("Your feedback will be collected and stored for future use.")

    def get_dashboard_metric(self):
        validated_insights = self.get_validated_insights()
        return f"Total validated insights: {validated_insights}"

    def main(self):
        self.display_privacy_notice()
        self.ask_for_validation('report1')
        print(self.get_dashboard_metric())
        self.export_to_brain()

if __name__ == '__main__':
    market_scout = MarketScout('data')
    market_scout.main()
