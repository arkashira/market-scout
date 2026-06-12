import json
from dataclasses import dataclass

@dataclass
class Step:
    text: str
    ui_element: str

class OnboardingTour:
    def __init__(self):
        self.steps = [
            Step("Welcome to the platform! Click on the 'Generate Insight' button to start.", "generate_insight_button"),
            Step("Select a data source and click 'Next' to proceed.", "data_source_selector"),
            Step("Review your insight and click 'Validate' to complete the tour.", "validate_insight_button")
        ]
        self.current_step = 0

    def get_current_step(self):
        return self.steps[self.current_step]

    def next_step(self):
        self.current_step += 1
        if self.current_step >= len(self.steps):
            self.current_step = len(self.steps) - 1

    def skip_tour(self):
        self.current_step = len(self.steps) - 1

    def replay_tour(self):
        self.current_step = 0

    def is_tour_completed(self):
        return self.current_step == len(self.steps) - 1

    def trigger_tour_completed_event(self):
        print("Tour completed event triggered")
