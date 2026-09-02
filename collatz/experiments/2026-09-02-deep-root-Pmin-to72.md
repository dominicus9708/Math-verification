# Deep-root `P_min` execution to ordinary-X exposure depth 72

Date: 2026-09-02

Status: **EXACT FINITE EXECUTION EVIDENCE / NOT A THEOREM**

## Purpose

Test whether the already-certified scalar physical Bellman predicate

\[
P=m_{W,lo}N+\delta_{lo}3^qX_{lo}
\]

closes the deepest retained Route-B source roots before ordinary `X` is fully exposed by 72 parity bits.

The execution reused the committed exact formulas and constants from:

- `../src/A0_s1_prefix_channel_transducer_certificate.py`;
- `../src/A0_s1_prefix_defect_membership_pruning_certificate.py`;
- `../src/A0_s1_14root_long_membership_forest_certificate.py`;
- `../src/A0_s1_radius7_defect_christoffel_real_envelope_certificate.py`;
- `../src/A0_s1_routeB_linear_physical_danger_score_certificate.py`.

No new theorem is inferred from the finite runs.

## Results

| first defect `f` | initial depth `h=f+1` | scanned extra bits | maximum Bellman states | states at `h=72` | physical-score closed children |
|---:|---:|---:|---:|---:|---:|
| 29 | 30 | 42 | 1,080,374 | 16 | 0 |
| 32 | 33 | 39 | 419,510 | 16 | 0 |
| 35 | 36 | 36 | 167,507 | 14 | 0 |
| 37 | 38 | 34 | 81,519 | 13 | 0 |

A run for `f=27` was attempted but did not complete within the execution limit. No partial state count from that timed-out run is retained as evidence.

## Interpretation

### Exact finite observation

For the four completed deep-root scans, the directed physical `P_min` predicate produced **zero whole-family physical closures** before or at ordinary-X exposure depth 72.

Bellman merging was substantial, but closure did not occur.

### What this does not prove

It does not prove that:

- these roots are realizable members of the full pre-bridge correction language;
- the physical predicate can never close them at a later stage;
- every shallower root behaves the same way;
- `P_min` is useless when combined with another exact predicate;
- any current root survives Route-B.

### State-sufficiency warning after `h=72`

At depth 72, ordinary `X` is exposed. Histories that were safely merged for the directed physical predicate need not remain interchangeable for arbitrary later membership/control predicates.

Therefore the existing `P_min` key must not be propagated beyond this point as a universal state unless the future-control coordinates required by the next predicate are restored or separately proved redundant.

## Search-engine audit conclusion

The finite runs do not justify making the directed physical Bellman scan the sole next strategy for the deep roots.

Together with the exact redundancy of the terminal target-dominance ternary gate, they move the principal bottleneck to

`source-controlled exact correction/checkpoint membership`.

The physical score remains a valid secondary pruning predicate and should be activated where a future source-conditioned family is still large.
