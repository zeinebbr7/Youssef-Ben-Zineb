# System Scope and Change Record

**Document ID:** ECHO-SCOPE-004  
**Status:** Incomplete extract

## Approved scope — initial phase

ECHO could identify suspicious authentication patterns, unusual network connections,
repeated failed logins, and known malicious indicators. The output was intended to
help analysts decide which technical incidents needed attention.

## Expanded scope — later phase

Subsequent records refer to:
- Aggregating activity across multiple sessions.
- Assigning persistent behavioral risk scores.
- Inferring patterns beyond a single technical incident.
- Retaining contextual records for longer periods.

The available extract does not include the complete approval trail for these changes.

## Open review items

1. What is the documented purpose for each collected field?
2. Can a person challenge or correct an inferred profile?
3. What prevents a security score from being reused for unrelated decisions?
4. Who authorized the broader scope?
5. Can the expanded collection be disabled without breaking core threat detection?

A separate file named `echo_scope_review_final_v3` is referenced in the project index,
but its contents are not present in this repository snapshot.
