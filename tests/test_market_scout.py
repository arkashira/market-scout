import os
import json
import shutil
from datetime import datetime, timedelta

import pytest

from market_scout import InsightTracker, Feedback


@pytest.fixture
def tmp_tracker(tmp_path):
    storage = tmp_path / "data.json"
    tracker = InsightTracker(storage_path=str(storage))
    yield tracker
    # cleanup
    if storage.exists():
        storage.unlink()


def test_record_and_load(tmp_tracker):
    tracker = tmp_tracker
    tracker.record_feedback("r1", True)
    tracker.record_feedback("r2", False)

    # Reload from disk to ensure persistence
    new_tracker = InsightTracker(storage_path=tracker.storage_path)
    all_fb = new_tracker.get_all_feedback()
    assert len(all_fb) == 2
    ids = {fb[0] for fb in all_fb}
    assert ids == {"r1", "r2"}
    vals = {fb[0]: fb[1] for fb in all_fb}
    assert vals["r1"] is True
    assert vals["r2"] is False


def test_monthly_counts(tmp_tracker):
    tracker = tmp_tracker

    # Create feedback with controlled timestamps
    base = datetime.utcnow().replace(day=1, hour=12, minute=0, second=0, microsecond=0)
    # two in current month, one in previous month
    for delta_days, validated in [(0, True), (5, True), (-30, True)]:
        ts = (base + timedelta(days=delta_days)).isoformat()
        fb = Feedback(report_id=f"id{delta_days}", validated=validated, timestamp=ts)
        tracker.feedback.append(fb)
    tracker._save()

    now = datetime.utcnow()
    cur_count = tracker.monthly_validated_counts(now.year, now.month)
    prev_month = (now.replace(day=1) - timedelta(days=1)).month
    prev_year = now.year if prev_month != 12 else now.year - 1
    prev_count = tracker.monthly_validated_counts(prev_year, prev_month)

    assert cur_count == 2
    assert prev_count == 1


def test_export_daily(tmp_tracker, tmp_path):
    tracker = tmp_tracker
    # feedback from today and yesterday
    today_iso = datetime.utcnow().isoformat()
    yesterday_iso = (datetime.utcnow() - timedelta(days=1)).isoformat()
    tracker.feedback.append(Feedback("today", True, today_iso))
    tracker.feedback.append(Feedback("yesterday", True, yesterday_iso))
    tracker._save()

    export_dir = tmp_path / "exports"
    out_file = tracker.export_daily(str(export_dir))

    # Verify file exists and contains only today's record
    assert os.path.isfile(out_file)
    with open(out_file, "r", encoding="utf-8") as f:
        lines = [json.loads(l) for l in f if l.strip()]
    assert len(lines) == 1
    assert lines[0]["report_id"] == "today"
    assert lines[0]["validated"] is True
