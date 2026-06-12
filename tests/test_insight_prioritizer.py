from insight_prioritizer import Insight, InsightPrioritizer

def test_prioritize_insights():
    insights = [
        Insight("Insight 1", 3, "Description 1"),
        Insight("Insight 2", 1, "Description 2"),
        Insight("Insight 3", 2, "Description 3")
    ]
    prioritizer = InsightPrioritizer(insights)
    prioritized_insights = prioritizer.prioritize_insights()
    assert prioritized_insights[0].name == "Insight 1"
    assert prioritized_insights[1].name == "Insight 3"
    assert prioritized_insights[2].name == "Insight 2"

def test_display_insights():
    insights = [
        Insight("Insight 1", 3, "Description 1"),
        Insight("Insight 2", 1, "Description 2"),
        Insight("Insight 3", 2, "Description 3")
    ]
    prioritizer = InsightPrioritizer(insights)
    prioritizer.display_insights(insights)

def test_filter_insights():
    insights = [
        Insight("Insight 1", 3, "Description 1"),
        Insight("Insight 2", 1, "Description 2"),
        Insight("Insight 3", 2, "Description 3")
    ]
    prioritizer = InsightPrioritizer(insights)
    filtered_insights = prioritizer.filter_insights(insights, 2)
    assert len(filtered_insights) == 2
    assert filtered_insights[0].name == "Insight 1"
    assert filtered_insights[1].name == "Insight 3"

def test_sort_insights():
    insights = [
        Insight("Insight 1", 3, "Description 1"),
        Insight("Insight 2", 1, "Description 2"),
        Insight("Insight 3", 2, "Description 3")
    ]
    prioritizer = InsightPrioritizer(insights)
    sorted_insights = prioritizer.sort_insights(insights, "name")
    assert sorted_insights[0].name == "Insight 1"
    assert sorted_insights[1].name == "Insight 2"
    assert sorted_insights[2].name == "Insight 3"
