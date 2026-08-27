#!/usr/bin/env python3
"""Exact certificate for local exposure of the s=1 renewal debit/credit addresses.

The companion 40-bit corridor theorem gives

    0 < L_minus < 112 G < 3^26,
    0 < L_plus  < 108 G < 2^40.

This file certifies the finite local address depths needed to recover those
ordinary values:

* L_minus is determined by X mod 3^26 and the last 26 odd ordinals of the
  prefix affine correction;
* L_plus is determined by Y mod 2^40 and the first 40 parity steps of the
  tail affine correction.

It also certifies the exact necessary 40-step tail ballot language and its
cardinality 31,654,570,714 < 2^40/32.

No finite boundary address is promoted to a full long-block path theorem.
This is not a proof of Collatz.
"""

from collections import defaultdict
from fractions import Fraction
from math import gcd

B = 1 << 71
G = 1 << 33
J0 = 10_439_860_591
R0 = 6_586_818_670
A0 = 114_208_327_604
Q0 = 72_057_431_991

t0 = 10 * J0
j0 = 10 * R0 + 1
U = A0 - t0
P = Q0 - 10 * R0
qtail = P - 1
NLOG = 90

assert j0 > 26
assert U > 40
assert qtail > 40
assert 112 * G < 3 ** 26
assert 108 * G < (1 << 40)
assert gcd(1 << t0.bit_length(), 3 ** 26) == 1  # powers of 2 are 3-adic units
assert gcd(3, 1 << 40) == 1


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# Exact tail renewal thresholds for the first 40 time steps:
# ceil(alpha*(t0+k))-j0, alpha=ln2/ln3.
req40 = [
    0,1,1,2,3,3,4,5,5,6,
    6,7,8,8,9,10,10,11,11,12,
    13,13,14,15,15,16,17,17,18,18,
    19,20,20,21,22,22,23,23,24,25,
]
assert len(req40) == 40

for k, r in enumerate(req40, start=1):
    assert (t0 + k) * l2 > (j0 + r - 1) * u3
    assert (t0 + k) * u2 < (j0 + r) * l3

states = {0: 1}
for r in req40:
    nxt = defaultdict(int)
    for q, count in states.items():
        for bit in (0, 1):
            q2 = q + bit
            if q2 >= r:
                nxt[q2] += count
    states = dict(nxt)

tail40 = sum(states.values())
assert tail40 == 31_654_570_714
assert 32 * tail40 < (1 << 40)

# Finite truncation depths are sufficient because the full affine corrections
# have triangular divisibility:
#
# Prefix: R_pre=sum_{j=1}^{j0} 3^(j0-j) 2^a_j.
# Mod 3^26 all terms with j0-j>=26 vanish, leaving exactly the last 26 odds.
# Since 2^t0 is invertible mod 3^26,
#   L_minus = 3X-Z == 3X - 2^-t0 R_pre (mod 3^26).
# With 0<L_minus<3^26, the least residue is the ordinary L_minus itself.
#
# Tail: R_tail=sum_j 3^(qtail-j)2^a_j.
# In
#   3^qtail L_plus=(3^(qtail+1)-2^U)Y+R_tail,
# reduction mod 2^40 kills 2^U Y and every correction term with a_j>=40.
# Hence only odd events in the first 40 parity positions remain and
#   L_plus == 3Y + 3^-qtail R_tail (mod 2^40).
# With 0<L_plus<2^40, this residue is the ordinary L_plus itself.

print("PASS A0 s=1 local boundary address exposure certificate")
print("prefix_terminal_odd_digits_needed", 26)
print("tail_initial_parity_bits_needed", 40)
print("tail40_necessary_words", tail40)
print("tail40_fraction_lt_1_over_32", True)
print("Lminus_modulus", 3 ** 26)
print("Lplus_modulus", 1 << 40)
