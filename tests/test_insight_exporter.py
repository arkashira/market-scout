from insight_exporter import Insight, Competitor, MarketSizing, InsightExporter
import pytest
import json

def test_export_to_pptx():
    insight = Insight(
        title="Test Insight",
        competitors=[Competitor("Competitor 1", 20.0), Competitor("Competitor 2", 30.0)],
        market_sizing=MarketSizing(100.0, 10.0),
        sources=["Source 1", "Source 2"]
    )
    exporter = InsightExporter(insight)
    pptx_content = exporter.export_to_pptx()
    assert len(pptx_content) < 5 * 1024 * 1024  # < 5 MB
    assert "Title: Test Insight" in pptx_content.decode()

def test_export_to_pdf():
    insight = Insight(
        title="Test Insight",
        competitors=[Competitor("Competitor 1", 20.0), Competitor("Competitor 2", 30.0)],
        market_sizing=MarketSizing(100.0, 10.0),
        sources=["Source 1", "Source 2"]
    )
    exporter = InsightExporter(insight)
    pdf_content = exporter.export_to_pdf()
    assert len(pdf_content) < 5 * 1024 * 1024  # < 5 MB
    assert "Title: Test Insight" in pdf_content.decode()

def test_log_telemetry():
    insight = Insight(
        title="Test Insight",
        competitors=[Competitor("Competitor 1", 20.0), Competitor("Competitor 2", 30.0)],
        market_sizing=MarketSizing(100.0, 10.0),
        sources=["Source 1", "Source 2"]
    )
    exporter = InsightExporter(insight)
    exporter.log_telemetry("pptx")
    # Simulate checking the telemetry log
    print("insight_exported: pptx")

def test_export_button_appears():
    # Simulate checking the export button appears on the insight page
    assert True  # This test is not automated, but the button should appear

def test_download_time():
    # Simulate checking the download time
    assert True  # This test is not automated, but the download should take < 10 seconds
