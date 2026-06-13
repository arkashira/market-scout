import os
import pathlib
import re
import pytest
from market_scout import Opportunity, generate_svg, save_chart

def test_generate_svg_contains_opportunity_data():
    data = [
        Opportunity(name="Alpha", size=100, growth=20),
        Opportunity(name="Beta", size=50, growth=40),
    ]
    svg = generate_svg(data)
    # Basic sanity checks
    assert svg.startswith("<svg")
    assert svg.endswith("</svg>")  # This assertion should now pass
    # Ensure each name appears as a label
    for opp in data:
        assert re.search(rf">{opp.name}<", svg), f"Label {opp.name} missing"
    # Ensure size and growth values appear in <title> elements (used for tooltip)
    for opp in data:
        title_snippet = f"{opp.name}: size={opp.size}, growth={opp.growth}"
        assert title_snippet in svg

def test_save_chart_creates_svg_file(tmp_path: pathlib.Path):
    data = [
        Opportunity(name="Gamma", size=80, growth=15),
    ]
    out_file = tmp_path / "chart.svg"
    save_chart(data, out_file)
    assert out_file.is_file()
    content = out_file.read_text(encoding="utf-8")
    assert "<svg" in content
    assert "Gamma" in content

def test_save_chart_creates_pdf_file(tmp_path: pathlib.Path):
    """Even though we write SVG, the function must accept a .pdf path."""
    data = [
        Opportunity(name="Delta", size=70, growth=30),
    ]
    out_file = tmp_path / "chart.pdf"
    save_chart(data, out_file)
    assert out_file.is_file()
    content = out_file.read_text(encoding="utf-8")
    # Simple check that the content is still SVG
    assert content.lstrip().startswith("<svg")
    # Ensure the filename extension does not affect the content
    assert "Delta" in content
