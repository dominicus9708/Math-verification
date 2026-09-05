#!/usr/bin/env python3
"""Exact counting consequence of the support<=4 base-shell local exclusion.

Local input already certified separately:
  every full 49-odd-state window whose first displacement is zero contains
  at least five positive displacement states.

This script derives the global lower bound on the number r_* of positive
mechanical displacements in the first resonance by deterministic double
counting.  No orbit enumeration occurs here.
"""

Q = 72_057_431_991
WINDOW = 49
MIN_POS = 5
BOUNDARY = WINDOW - 1

# Let R be the number of positive displacement positions and Z=Q-R the zeros.
# At most BOUNDARY zero positions occur too near the terminal end to start a
# full 49-state window.  Hence Z_int >= Q-R-BOUNDARY.
# Every such zero-start window contains >= MIN_POS positive positions.
# A fixed positive position lies in at most WINDOW such windows.  Therefore
#   MIN_POS * (Q-R-BOUNDARY) <= WINDOW * R.
# Equivalently
#   MIN_POS*(Q-BOUNDARY) <= (WINDOW+MIN_POS) R.
num = MIN_POS * (Q - BOUNDARY)
den = WINDOW + MIN_POS
RMIN = (num + den - 1) // den

assert RMIN == 6_671_984_440
assert MIN_POS * (Q - RMIN - BOUNDARY) <= WINDOW * RMIN
assert MIN_POS * (Q - (RMIN - 1) - BOUNDARY) > WINDOW * (RMIN - 1)

# Every positive displacement has normalized Christoffel charge > 1/12.
# Keep the exact integer inequality 12 * defect > RMIN rather than using a
# floating-point decimal.
print("PASS global density from support-4 local rule")
print("Q", Q)
print("positive_displacements_at_least", RMIN)
print("density_lower", RMIN / Q)
print("normalized_defect_strictly_greater_than", RMIN / 12)
