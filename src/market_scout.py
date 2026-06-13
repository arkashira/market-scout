"""market_scout – simple SVG chart generator for go‑to‑market opportunities.
The module provides:
* `Opportunity` – a dataclass describing a market opportunity.
* `generate_svg(opportunities)` – returns an SVG string visualising the data.
* `save_chart(opportunities, path)` – writes the SVG to *path* (supports `.svg` and `.pdf` extensions; the same SVG content is written for both).
* A tiny CLI (`python -m market_scout`) that writes a demo chart to a file.
"""
from __future__ import annotations
import argparse
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import List

@dataclass
class Opportunity:
    """Dataclass for market opportunities."""
    name: str
    size: int
    growth: int

def generate_svg(opportunities: List[Opportunity]) -> str:
    """Generate an SVG string representing the opportunities."""
    svg = "<svg width='100%' height='100%'>\n"
    for i, opp in enumerate(opportunities):
        svg += f"<rect x='{i*100}' y='0' width='100' height='{opp.size}' fill='blue'/>\n"
        svg += f"<rect x='{i*100}' y='{opp.size}' width='100' height='{opp.growth}' fill='green'/>\n"
        svg += f"<text x='{i*100+50}' y='{opp.size+opp.growth+20}' text-anchor='middle'>{opp.name}</text>\n"
        svg += f"<title>{opp.name}: size={opp.size}, growth={opp.growth}</title>\n"
    svg += "</svg>"  # Removed the newline character here
    return svg

def save_chart(opportunities: List[Opportunity], path: Path) -> None:
    """Save the SVG chart to a file."""
    svg = generate_svg(opportunities)
    with open(path, "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a simple SVG chart of go‑to‑market opportunities.")
    parser.add_argument("output", help="Path to output file")
    args = parser.parse_args()
    opportunities = [
        Opportunity("Alpha", 100, 20),
        Opportunity("Beta", 50, 40),
    ]
    save_chart(opportunities, Path(args.output))
