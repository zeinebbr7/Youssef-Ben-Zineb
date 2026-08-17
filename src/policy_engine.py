"""Fictional policy checks for the ECHO narrative."""


CORE_FIELDS = {
    "event_id",
    "timestamp",
    "source",
    "event_type",
    "indicator",
    "severity",
}


def validate_collection_fields(requested_fields: set[str]) -> tuple[bool, list[str]]:
    """Reject undocumented fields and return an explanation."""
    unexpected = sorted(requested_fields - CORE_FIELDS)
    if unexpected:
        return False, [
            "Fields outside the documented security scope: " + ", ".join(unexpected)
        ]
    return True, ["Requested fields match the documented core schema."]
