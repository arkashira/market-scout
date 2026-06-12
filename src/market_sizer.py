import argparse
import json
from dataclasses import dataclass

@dataclass
class MarketParameters:
    """Market parameters for sizing"""
    market_growth_rate: float
    market_size_last_year: float
    years_to_estimate: int

def estimate_market_size(parameters: MarketParameters) -> float:
    """Estimate market size based on given parameters"""
    estimated_size = parameters.market_size_last_year
    for _ in range(parameters.years_to_estimate):
        estimated_size *= (1 + parameters.market_growth_rate)
    return round(estimated_size, 0)  # Round to the nearest whole number

def main():
    parser = argparse.ArgumentParser(description="Market Sizer")
    parser.add_argument("--growth-rate", type=float, help="Market growth rate")
    parser.add_argument("--last-year-size", type=float, help="Market size last year")
    parser.add_argument("--years-to-estimate", type=int, help="Years to estimate")
    args = parser.parse_args()
    parameters = MarketParameters(
        market_growth_rate=args.growth_rate,
        market_size_last_year=args.last_year_size,
        years_to_estimate=args.years_to_estimate,
    )
    estimated_size = estimate_market_size(parameters)
    print(f"Estimated market size: {estimated_size}")

if __name__ == "__main__":
    main()
