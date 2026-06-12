import html
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Competitor:
    name: str

@dataclass
class Category:
    name: str

@dataclass
class CellData:
    percentage: float  # 0-100
    description: str

def _clamp(value: float, min_value: float = 0.0, max_value: float = 100.0) -> float:
    """Clamp a numeric value between min_value and max_value."""
    return max(min_value, min(max_value, value))

def _pct_to_color(percentage: float) -> str:
    """
    Convert a percentage (0-100) to a red‑intensity RGB color string.
    0% -> rgb(255,255,255) (white)
    100% -> rgb(255,0,0) (red)
    """
    pct = _clamp(percentage)
    intensity = int(255 * pct / 100)
    # Red stays at 255, green and blue decrease with intensity
    return f"rgb(255,{255 - intensity},{255 - intensity})"

def generate_heatmap_html(
    competitors: List[Competitor],
    categories: List[Category],
    data: Dict[str, Dict[str, CellData]],
) -> str:
    """
    Generate an HTML string containing a responsive heatmap table.

    Parameters
    ----------
    competitors : list of Competitor
        List of competitors to display as rows.
    categories : list of Category
        List of top feature categories to display as columns.
    data : dict
        Mapping from competitor name to a mapping of category name to CellData.
        Missing entries are treated as 0% with an empty description.

    Returns
    -------
    str
        An HTML snippet that can be embedded in a page.
    """
    # Start building the HTML
    html_parts = [
        '<table style="width:100%; table-layout:fixed; border-collapse:collapse;">',
        "  <thead>",
        "    <tr>",
        "      <th></th>",  # Top-left empty corner
    ]

    # Header row with category names
    for cat in categories:
        html_parts.append(f"      <th>{html.escape(cat.name)}</th>")
    html_parts.append("    </tr>")
    html_parts.append("  </thead>")
    html_parts.append("  <tbody>")

    # Rows for each competitor
    for comp in competitors:
        html_parts.append("    <tr>")
        html_parts.append(f"      <th>{html.escape(comp.name)}</th>")
        for cat in categories:
            cell = data.get(comp.name, {}).get(cat.name, CellData(0.0, ""))
            pct = _clamp(cell.percentage)
            color = _pct_to_color(pct)
            title = html.escape(cell.description) if cell.description else ""
            style = f"background-color:{color}; text-align:center; padding:4px; border:1px solid #ccc;"
            html_parts.append(
                f'      <td style="{style}" title="{title}">{pct:.0f}%</td>'
            )
        html_parts.append("    </tr>")

    html_parts.append("  </tbody>")
    html_parts.append("</table>")

    # Add a simple responsive rule (optional but ensures width:100% works)
    html_parts.append(
        """
<style>
@media (max-width: 600px) {
  table, th, td { font-size: 12px; }
}
</style>
"""
    )

    return "\n".join(html_parts)
