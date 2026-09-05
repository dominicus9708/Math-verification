#!/usr/bin/env python3
"""Exact arithmetic consequence of the support<=6 local certificate.

Combinatorial lemma used in the note:
If every full length-L window whose first symbol is zero contains at least m
ones, then every full length-L window contains at least m ones.

For the first resonance L=49, m=7.  Summing all Q-L+1 windows then gives
    m (Q-L+1) <= L R,
where R is the total number of positive-displacement positions.
"""

Q = 72_057_431_991
L = 49
M = 7

RMIN = (M * (Q - L + 1) + L - 1) // L
assert RMIN == 10_293_918_849

# Sharp integer check for the counting inequality.
assert M * (Q - L + 1) <= L * RMIN
assert M * (Q - L + 1) > L * (RMIN - 1)

print("PASS all-window density consequence")
print("Q", Q)
print("window_length", L)
print("minimum_positive_per_window", M)
print("positive_displacements_at_least", RMIN)
print("density_lower", RMIN / Q)
print("normalized_defect_strictly_greater_than", RMIN / 12)
