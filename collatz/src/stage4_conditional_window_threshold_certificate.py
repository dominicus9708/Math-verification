#!/usr/bin/env python3
"""Exact arithmetic certificate for the Stage-4 28-step conditional-window threshold.

This does not prove the missing renewal-conditioned transversality theorem.
It proves that a uniform conditional same-integer overlap amplification < 15
per 28-step renewal window is already strong enough to beat the current
L=7 deterministic language-exclusion rate 7/50.

It also records how much weaker this target is than the existing fresh-window
m=45 theorem Xi < 76/75.
"""

from fractions import Fraction

WINDOW = 28
K = 15

# log2(K)/WINDOW < 7/50 is equivalent to
# K^50 < 2^(28*7) = 2^196; divide both exponents by 2.
assert K**25 < 2**98

# Existing fresh-window theorem: Xi < 76/75 and log2(Xi) < 1/50 bit.
assert 76**50 < 2 * 75**50
assert Fraction(76, 75) < K

# The likelihood-ratio threshold is more than 14 times the fresh-window bound.
assert Fraction(K, 1) / Fraction(76, 75) == Fraction(1125, 76)
assert Fraction(1125, 76) > 14

# TV reformulation. If the baseline next-window hard fraction is u >= 3/64,
# then mu(H)/nu(H) <= 1 + TV/u. Therefore TV < 21/32 already implies
# amplification < 15.
u = Fraction(3, 64)
tv_threshold = Fraction(21, 32)
assert 1 + tv_threshold / u == K

# The current fresh-window TV theorem is TV < 1/1600, so the allowed
# conditional-TV threshold is exactly 1050 times larger.
assert tv_threshold / Fraction(1, 1600) == 1050

print("Stage-4 conditional-window threshold certificate: PASS")
print("window =", WINDOW)
print("target exclusion rate = 7/50")
print("sufficient conditional amplification K < 15 per 28 steps")
print("exact check: 15^25 < 2^98")
print("fresh-window bound: Xi < 76/75 < 15")
print("likelihood-ratio slack factor > 14")
print("if baseline hard fraction >= 3/64, sufficient conditional TV < 21/32")
print("fresh TV < 1/1600; allowable TV degradation factor = 1050")
