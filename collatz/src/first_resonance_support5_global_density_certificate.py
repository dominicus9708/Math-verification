#!/usr/bin/env python3
"""Exact global counting consequence of the support<=5 local exclusion."""
Q = 72_057_431_991
WINDOW = 49
MIN_POS = 6
BOUNDARY = WINDOW - 1

num = MIN_POS * (Q - BOUNDARY)
den = WINDOW + MIN_POS
RMIN = (num + den - 1) // den

assert RMIN == 7_860_810_758
assert MIN_POS * (Q - RMIN - BOUNDARY) <= WINDOW * RMIN
assert MIN_POS * (Q - (RMIN - 1) - BOUNDARY) > WINDOW * (RMIN - 1)

print("PASS global density from support-5 local rule")
print("Q", Q)
print("positive_displacements_at_least", RMIN)
print("density_lower", RMIN / Q)
print("normalized_defect_strictly_greater_than", RMIN / 12)
