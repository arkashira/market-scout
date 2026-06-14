import pytest
from market_scout import generate_competitor_landscape, Competitor

def test_generate_competitor_landscape():
    keyword = "test_keyword"
    competitors = generate_competitor_landscape(keyword)
    assert len(competitors) == 10
    for competitor in competitors:
        assert isinstance(competitor, Competitor)
        assert competitor.name
        assert competitor.description
        assert competitor.funding
        assert competitor.employee_count
        assert competitor.product_focus
        assert competitor.relevance_score

def test_competitor_ranking():
    keyword = "test_keyword"
    competitors = generate_competitor_landscape(keyword)
    assert competitors[0].relevance_score >= competitors[1].relevance_score
    assert competitors[1].relevance_score >= competitors[2].relevance_score

def test_empty_keyword():
    keyword = ""
    competitors = generate_competitor_landscape(keyword)
    assert len(competitors) == 10

def test_none_keyword():
    keyword = None
    with pytest.raises(AttributeError):
        generate_competitor_landscape(keyword)
