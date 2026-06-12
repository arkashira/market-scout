import re
import pytest

from heatmap import (
    Competitor,
    Category,
    CellData,
    generate_heatmap_html,
)

def test_generate_heatmap_basic_structure():
    competitors = [Competitor("Alpha"), Competitor("Beta")]
    categories = [
        Category("UI"),
        Category("Performance"),
        Category("Security"),
        Category("Integration"),
        Category("Support"),
    ]
    data = {
        "Alpha": {
            "UI": CellData(80, "Excellent UI."),
            "Performance": CellData(60, "Fast."),
            "Security": CellData(90, "Strong."),
            "Integration": CellData(70, "API."),
            "Support": CellData(50, "Email."),
        },
        "Beta": {
            "UI": CellData(40, "Basic UI."),
            "Performance": CellData(30, "Slow."),
            "Security": CellData(70, "Standard."),
            "Integration": CellData(20, "Limited API."),
            "Support": CellData(80, "Chat."),
        },
    }

    html = generate_heatmap_html(competitors, categories, data)

    # Basic checks
    assert isinstance(html, str)
    assert "<table" in html
    assert "</table>" in html
    assert "<thead>" in html
    assert "<tbody>" in html

    # Header row contains all category names
    for cat in categories:
        assert f"<th>{cat.name}</th>" in html

    # Each competitor row has 5 cells plus header
    rows = re.findall(r"<tr>.*?</tr>", html, flags=re.S)
    # First row is header, so skip
    competitor_rows = rows[1:]
    assert len(competitor_rows) == len(competitors)
    for row in competitor_rows:
        cells = re.findall(r"<td[^>]*>", row)
        assert len(cells) == len(categories)

def test_color_intensity_and_tooltip():
    competitors = [Competitor("X")]
    categories = [Category("Feature")]
    data = {
        "X": {
            "Feature": CellData(75, "Feature description.")
        }
    }
    html = generate_heatmap_html(competitors, categories, data)

    # Extract the cell's style and title
    cell_match = re.search(r'<td style="([^"]+)" title="([^"]+)">', html)
    assert cell_match
    style, title = cell_match.groups()
    # Check title
    assert title == "Feature description."
    # Check color intensity: 75% -> intensity 191 (255*0.75)
    expected_color = "rgb(255,64,64)"  # 255-191=64
    assert f"background-color:{expected_color}" in style

def test_clamping_and_missing_data():
    competitors = [Competitor("A")]
    categories = [Category("Cat")]
    data = {
        "A": {
            # Missing Cat entry should default to 0%
        }
    }
    html = generate_heatmap_html(competitors, categories, data)
    # Cell should show 0% and no title
    assert "0%" in html
    assert 'title=""' in html

    # Test percentage >100 clamped to 100%
    data = {"A": {"Cat": CellData(150, "Too high")}}
    html = generate_heatmap_html(competitors, categories, data)
    assert "100%" in html
    # Color should be pure red
    assert "background-color:rgb(255,0,0)" in html

def test_responsive_css():
    competitors = [Competitor("A")]
    categories = [Category("Cat")]
    data = {"A": {"Cat": CellData(50, "")}}
    html = generate_heatmap_html(competitors, categories, data)
    # Check that table has width:100% style
    assert 'style="width:100%; table-layout:fixed;' in html
    # Check that a media query is present
    assert "@media (max-width: 600px)" in html
