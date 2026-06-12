import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.opportunity_scoring import OpportunityScore

def test_calculate_score_both_values():
    opportunity = OpportunityScore(market_size=80, competitor_density=20)
    assert opportunity.calculate_score() == 60

def test_calculate_score_market_size_only():
    opportunity = OpportunityScore(market_size=80)
    assert opportunity.calculate_score() == 80

def test_calculate_score_competitor_density_only():
    opportunity = OpportunityScore(competitor_density=20)
    assert opportunity.calculate_score() == 80

def test_calculate_score_no_values():
    opportunity = OpportunityScore()
    assert opportunity.calculate_score() == 50

def test_get_justification_high_score():
    opportunity = OpportunityScore(market_size=80, competitor_density=20)
    assert "High opportunity score" in opportunity.get_justification()

def test_get_justification_low_score():
    opportunity = OpportunityScore(market_size=20, competitor_density=80)
    assert "Low opportunity score" in opportunity.get_justification()

def test_get_justification_neutral_score():
    opportunity = OpportunityScore()
    assert "Neutral score" in opportunity.get_justification()
