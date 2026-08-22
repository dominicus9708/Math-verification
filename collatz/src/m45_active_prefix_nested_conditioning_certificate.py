#!/usr/bin/env python3
"""Exact algebraic consequence of the certified m=45 selector histogram.

The NTT certificate proves that every free-selector residue modulo 2^26 has
multiplicity c(r) in [260110, 264167].  This script certifies that arbitrary
nested conditioning by events measurable in the same active residue space
cannot accumulate cross-base repair: for A subset E,

    [mu(A|E) / nu(A|E)] = avg_A(c) / avg_E(c)
                         <= max(c)/min(c) < 65/64.

Thus any number of nested filters inside the same active 28-bit prefix has a
total prefix-normalized repair budget below 1/40 bit.

This does not control conditions depending on higher binary digits beyond the
active 2^26 residue coordinate and is not a proof of Collatz.
"""

from fractions import Fraction

CMIN = 260_110
CMAX = 264_167

ratio = Fraction(CMAX, CMIN)

# Exact pointwise dynamic-range bound.
assert 64 * CMAX < 65 * CMIN
assert ratio < Fraction(65, 64)

# Exact bit-budget bound log2(65/64) < 1/40.
assert 65**40 < 2 * 64**40

# The new Stage-4 sufficient per-28-step threshold is vastly weaker.
assert ratio < 15

print("m45 active-prefix nested-conditioning certificate: PASS")
print("selector multiplicity range:", CMIN, CMAX)
print("max/min = %d/%d" % (CMAX, CMIN))
print("exact dynamic range: max/min < 65/64")
print("arbitrary nested active-prefix amplification < 65/64")
print("total nested active-prefix repair budget < 1/40 bit")
print("scope: events measurable modulo 2^26 in Y, equivalently through binary depth 28 in N=4Y+3")
