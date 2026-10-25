"""Illustrative incident scoring; all data is synthetic.

This module intentionally demonstrates a technical incident score, not a score
for a person's character, trustworthiness, or predicted behavior.
"""


def incident_priority(failed_logins: int, known_bad_indicator: bool) -> int:
    """Return a bounded 0–100 triage score for a synthetic security event."""
    score = min(max(failed_logins, 0), 10) * 5
    if known_bad_indicator:
        score += 50
    return min(score, 100)


if __name__ == "__main__":
    print("Synthetic incident priority:", incident_priority(6, True))
