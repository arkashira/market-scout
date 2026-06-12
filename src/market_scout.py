import json
from dataclasses import dataclass
from typing import List, Dict, Optional

@dataclass
class MarketOpportunity:
    name: str
    market_size: float
    growth_rate: float

class MarketScout:
    def __init__(self, data_file: Optional[str] = None):
        self.opportunities: List[MarketOpportunity] = []
        if data_file:
            self.load_data(data_file)

    def load_data(self, data_file: str) -> None:
        with open(data_file, 'r') as f:
            data = json.load(f)
        for item in data:
            self.opportunities.append(MarketOpportunity(**item))

    def visualize_opportunities(self) -> None:
        if not self.opportunities:
            raise ValueError("No market opportunities data loaded.")
        names = [op.name for op in self.opportunities]
        market_sizes = [op.market_size for op in self.opportunities]
        growth_rates = [op.growth_rate for op in self.opportunities]
        print("Market Opportunities:")
        for name, market_size, growth_rate in zip(names, market_sizes, growth_rates):
            print(f"{name}: Market Size = {market_size:.1f}, Growth Rate = {growth_rate:.1f}")

    def save_visualization(self, format: str = 'txt') -> str:
        if not self.opportunities:
            raise ValueError("No market opportunities data loaded.")
        buf = ""
        for op in self.opportunities:
            buf += f"{op.name}: Market Size = {op.market_size:.1f}, Growth Rate = {op.growth_rate:.1f}\n"
        return buf
