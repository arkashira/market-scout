import json
from dataclasses import dataclass
from typing import List

@dataclass
class Competitor:
    name: str
    tam: float
    sam: float
    som: float
    relevance_score: float

def estimate_market_size(competitors: List[Competitor]) -> List[dict]:
    """ Estimates market size for each competitor segment.
    
    Args:
    competitors (List[Competitor]): List of competitor segments.
    
    Returns:
    List[dict]: List of dictionaries containing TAM, SAM, and SOM estimates.
    """
    estimates = []
    for competitor in competitors:
        tam_estimate = competitor.tam
        sam_estimate = competitor.sam
        som_estimate = competitor.som
        confidence_interval = 0.2  # 20% confidence interval
        tam_ci = tam_estimate * confidence_interval
        sam_ci = sam_estimate * confidence_interval
        som_ci = som_estimate * confidence_interval
        estimates.append({
            "name": competitor.name,
            "tam": f"${tam_estimate:.2f}M ± ${tam_ci:.2f}M",
            "sam": f"${sam_estimate:.2f}M ± ${sam_ci:.2f}M",
            "som": f"${som_estimate:.2f}M ± ${som_ci:.2f}M",
            "relevance_score": competitor.relevance_score
        })
    return estimates

def prioritize_segments(estimates: List[dict]) -> List[dict]:
    """ Prioritizes competitor segments based on combined TAM and relevance score.
    
    Args:
    estimates (List[dict]): List of dictionaries containing market size estimates.
    
    Returns:
    List[dict]: List of dictionaries containing the top-3 prioritized segments.
    """
    def extract_tam_value(tam_str: str) -> float:
        return float(tam_str.split("±")[0].split("$")[1].replace("M", ""))

    estimates.sort(key=lambda x: (extract_tam_value(x["tam"]), x["relevance_score"]), reverse=True)
    return estimates

def main():
    competitors = [
        Competitor("Segment 1", 100, 50, 20, 0.8),
        Competitor("Segment 2", 50, 30, 15, 0.6),
        Competitor("Segment 3", 200, 100, 50, 0.9)
    ]
    estimates = estimate_market_size(competitors)
    prioritized_segments = prioritize_segments(estimates)
    print(json.dumps(prioritized_segments, indent=4))

if __name__ == "__main__":
    main()
