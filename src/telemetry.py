"""Synthetic telemetry schema for the fictional ECHO investigation."""

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class SecurityEvent:
    event_id: str
    timestamp: datetime
    source: str
    event_type: str
    indicator: str
    severity: int


def validate_event(event: SecurityEvent) -> bool:
    """Accept only basic, synthetic security-event records."""
    return (
        bool(event.event_id)
        and bool(event.source)
        and bool(event.event_type)
        and 0 <= event.severity <= 10
    )
