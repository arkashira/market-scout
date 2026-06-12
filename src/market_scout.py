import json
from dataclasses import dataclass
from typing import Dict

@dataclass
class MarketScout:
    competitor_density: float
    tam: float
    funding_activity: float
    weightings: Dict[str, float]

    def calculate_score(self) -> float:
        score = (self.competitor_density * self.weightings['competitor_density'] +
                 self.tam * self.weightings['tam'] +
                 self.funding_activity * self.weightings['funding_activity'])
        return score / sum(self.weightings.values())

    def get_tier(self, score: float) -> str:
        if score < 33.33:
            return 'Low'
        elif score < 66.67:
            return 'Medium'
        else:
            return 'High'

    def adjust_weightings(self, new_weightings: Dict[str, float]) -> None:
        self.weightings = new_weightings

    def persist_score(self, score: float) -> Dict:
        return {'score': score, 'tier': self.get_tier(score)}

def main() -> None:
    market_scout = MarketScout(competitor_density=10, tam=100, funding_activity=5, weightings={'competitor_density': 0.2, 'tam': 0.5, 'funding_activity': 0.3})
    score = market_scout.calculate_score()
    print(f'Score: {score:.2f}, Tier: {market_scout.get_tier(score)}')
    new_weightings = {'competitor_density': 0.3, 'tam': 0.4, 'funding_activity': 0.3}
    market_scout.adjust_weightings(new_weightings)
    new_score = market_scout.calculate_score()
    print(f'New Score: {new_score:.2f}, Tier: {market_scout.get_tier(new_score)}')
    persisted_score = market_scout.persist_score(new_score)
    print(f'Persisted Score: {persisted_score}')

if __name__ == '__main__':
    main()
