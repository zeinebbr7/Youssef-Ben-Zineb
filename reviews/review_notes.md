# Internal Review Notes

**Reference:** REV-17  
**Author:** Y. Ben Zineb  
**Status:** Open — no final approval attached

## Review observations

The current branch no longer appears limited to incident-level analysis. Several
changes combine events across sessions and assign persistent behavioral context.
The technical documentation does not establish a sufficiently narrow purpose for
all of these fields.

I initially assumed the additional context would help analysts distinguish
coordinated attacks from unrelated activity. I am no longer convinced that the
implementation stays within that boundary.

## Questions requiring an answer

- Which use cases require a persistent profile?
- Which fields are essential to detect a technical threat?
- Who can access the expanded data?
- Is there a tested deletion path?
- Has the change been reviewed by someone independent of the project team?

## Cross-reference

The project index references `echo_scope_review_final_v3`. I cannot find that
document in the current repository snapshot. The missing review is an unresolved
record, not proof of what it contained.
