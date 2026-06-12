# ECHO Architecture Overview

**Document ID:** ECHO-DOC-001  
**Status:** Historical design note  
**Project:** ECHO

## Original purpose

ECHO was proposed as an analyst-assistance platform for correlating network events,
flagging unusual activity, and helping a security team prioritize investigation.
It was not originally described as a system for evaluating individual character
or predicting personal behavior.

## High-level flow

1. Collect security telemetry from approved sources.
2. Normalize events into a common schema.
3. Correlate events against known technical indicators.
4. Calculate an explainable incident-priority score.
5. Present findings to a human analyst.
6. Record the analyst's decision and supporting evidence.

## Design boundaries

- A score is a triage signal, not proof of wrongdoing.
- Personal profiling is outside the original scope.
- Data collection must have a documented purpose and retention period.
- Access to raw telemetry should be restricted and auditable.
- Human review is required before consequential action.

## Unresolved question

A later implementation introduced a `behavioral_context` field in risk profiles.
The available documentation does not clearly explain who approved that change or
how long the resulting data was retained.

See `../reviews/review_notes.md` and the commit history for related records.
