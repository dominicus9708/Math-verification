#!/usr/bin/env python3
from fractions import Fraction

G = 1 << 33
M20 = 3**20
M21 = 3**21
M22 = 3**22

# Physical Hensel boundary normalization:
# K_R=-Y, K_L=-2^{-A}X, hence 2^A K_L-K_R = Y-X.
# This file certifies only the finite-resolution interval arithmetic needed
# to expose that ordinary difference from a residue.

# First global resonance: 0 < g < G.  20 trits are insufficient by interval
# width, while 21 trits are sufficient.
assert M20 < G < M21

# Post-A0,A0,J0 reset strip:
# 0 <= d < 0.478 G and d'-d < a_A < 0.5023 G.
# Since d' >= 0, delta=d'-d lies in (-0.478 G, 0.5023 G).
reset_lo = -Fraction(478, 1000) * G
reset_hi = Fraction(5023, 10000) * G
reset_width = reset_hi - reset_lo
assert M20 < reset_width < M21
# In fact the whole interval lies in the centered representatives mod 3^21.
assert -Fraction(M21, 2) < reset_lo
assert reset_hi < Fraction(M21, 2)

# Promoted strip: 0 <= d < 2G and one A0 return has d'-d < 0.51 G.
# The interval width is 2.51G, so 22 trits are sufficient while 21 are not.
promoted_lo = -2 * G
promoted_hi = Fraction(51, 100) * G
promoted_width = promoted_hi - promoted_lo
assert M21 < promoted_width < M22

print("PASS A0 physical boundary gap resolution certificate")
print("G", G)
print("3^20", M20)
print("3^21", M21)
print("3^22", M22)
print("first_global_min_resolution", 21)
print("reset_interval_over_G", float(reset_lo / G), float(reset_hi / G))
print("reset_width_over_G", float(reset_width / G), "min_resolution", 21)
print("promoted_interval_over_G", float(promoted_lo / G), float(promoted_hi / G))
print("promoted_width_over_G", float(promoted_width / G), "min_resolution", 22)
