from onboarding import OnboardingTour, Step

def test_onboarding_tour():
    tour = OnboardingTour()
    assert len(tour.steps) == 3
    assert tour.get_current_step().text == "Welcome to the platform! Click on the 'Generate Insight' button to start."
    tour.next_step()
    assert tour.get_current_step().text == "Select a data source and click 'Next' to proceed."
    tour.next_step()
    assert tour.get_current_step().text == "Review your insight and click 'Validate' to complete the tour."
    assert tour.is_tour_completed()
    tour.trigger_tour_completed_event()

def test_skip_tour():
    tour = OnboardingTour()
    tour.skip_tour()
    assert tour.is_tour_completed()

def test_replay_tour():
    tour = OnboardingTour()
    tour.next_step()
    tour.replay_tour()
    assert tour.get_current_step().text == "Welcome to the platform! Click on the 'Generate Insight' button to start."
