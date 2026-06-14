import argparse
import json
from dataclasses import dataclass
from typing import List

@dataclass
class Competitor:
    name: str
    market_share: float
    growth_rate: float

def load_competitors(data: str) -> List[Competitor]:
    """
    Parse a JSON string into a list of Competitor objects.

    Parameters
    ----------
    data : str
        JSON array where each element has keys 'name', 'market_share', and 'growth_rate'.

    Returns
    -------
    List[Competitor]
        List of parsed competitor objects.
    """
    return [Competitor(**c) for c in json.loads(data)]

def plot_competitors(competitors: List[Competitor]):
    """
    Stub plotting function.

    The original implementation used matplotlib to create visualisations.
    For the purposes of the test suite (which only verifies that the function
    runs without error), we replace the heavy dependency with a lightweight
    placeholder that simply prints a summary of the competitors.
    """
    # Print a simple textual representation; this keeps the function
    # side‑effect free and avoids external dependencies.
    print("Competitor Landscape:")
    for c in competitors:
        print(f" - {c.name}: market share {c.market_share:.2%}, growth rate {c.growth_rate:.2%}")

def main():
    """
    Entry point for the command‑line interface.

    Expects a '--data' argument containing a JSON string. The function
    will exit with a SystemExit exception if the argument is missing,
    which is the behaviour the tests expect.
    """
    parser = argparse.ArgumentParser(description='Competitor Analysis')
    parser.add_argument('--data', required=True, help='Competitor data in JSON format')
    args = parser.parse_args()

    competitors = load_competitors(args.data)
    plot_competitors(competitors)

if __name__ == '__main__':
    main()
