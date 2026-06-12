import json
from dataclasses import dataclass
from typing import Optional

@dataclass
class OpportunityScore:
    market_size: Optional[float] = None
    competitor_density: Optional[float] = None

    def calculate_score(self) -> int:
        if self.market_size is None and self.competitor_density is None:
            return 50
        if self.market_size is None:
            return int(100 - self.competitor_density)
        if self.competitor_density is None:
            return int(self.market_size)
        score = int(self.market_size) - int(self.competitor_density)
        return max(0, score)

    def get_justification(self) -> str:
        score = self.calculate_score()
        if score == 50:
            return "Neutral score due to insufficient data."
        if score > 50:
            return "High opportunity score due to significant market size and/or low competitor density."
        else:
            return "Low opportunity score due to small market size and/or high competitor density."

    def main(self):
        import argparse
        parser = argparse.ArgumentParser(description='Calculate opportunity score.')
        parser.add_argument('--market-size', type=float, help='Market size (0-100)')
        parser.add_argument('--competitor-density', type=float, help='Competitor density (0-100)')
        parser.add_argument('--output', type=str, help='Output file to save the result')
        args = parser.parse_args()
        opportunity = OpportunityScore(
            market_size=args.market_size,
            competitor_density=args.competitor_density
        )
        score = opportunity.calculate_score()
        justification = opportunity.get_justification()
        result = {
            'score': score,
            'justification': justification
        }
        if args.output:
            with open(args.output, 'w') as f:
                json.dump(result, f)
        else:
            print(json.dumps(result, indent=2))

if __name__ == '__main__':
    from opportunity_scoring import OpportunityScore
    OpportunityScore().main()
