import importlib
import os

import council


def test_load_coaching_framework_returns_string():
    s = council.load_coaching_framework()
    assert isinstance(s, str)
    assert len(s) > 0


def test_truncate_plan_for_review_truncates_long_text():
    long_text = "A" * 10000
    truncated = council.truncate_plan_for_review(long_text, max_chars=3000)
    assert len(truncated) < len(long_text)
    assert "[... middle sections abbreviated for length ...]" in truncated
