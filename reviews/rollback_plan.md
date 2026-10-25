# Proposed Scope Rollback

**Author:** Y. Ben Zineb  
**Status:** Proposal only — completion not verified

## Proposed actions

- Disable persistence of `behavioral_context`.
- Keep incident-level indicators required for core detection.
- Remove profile fields from analyst summaries.
- Audit stored synthetic profile records and define a deletion process.
- Run regression tests to confirm that core incident detection remains available.

## Limitation

This document records an intention, not proof that every action was completed.
A source-control rollback cannot erase deployed copies, exported data, or records
already collected elsewhere. The deployment state is unknown from this repository.
