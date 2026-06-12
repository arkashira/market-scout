from market_sizer import MarketParameters, estimate_market_size

def test_estimate_market_size():
    parameters = MarketParameters(
        market_growth_rate=0.1,
        market_size_last_year=100,
        years_to_estimate=2,
    )
    estimated_size = estimate_market_size(parameters)
    assert estimated_size == 121

def test_main():
    # This test is a bit tricky since it involves argparse and stdout
    # We'll just test that it doesn't crash
    import sys
    import io
    from unittest.mock import patch
    with patch.object(sys, "argv", ["market_sizer.py", "--growth-rate", "0.1", "--last-year-size", "100", "--years-to-estimate", "2"]):
        with patch("sys.stdout", new=io.StringIO()) as fake_stdout:
            from market_sizer import main
            main()
    assert fake_stdout.getvalue().startswith("Estimated market size: ")
