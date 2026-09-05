#!/usr/bin/env python3
"""Exact certificate for a shallow mixed-radix checkpoint meet in the s=1 branch.

At the renewal checkpoint Z we know 2^72 < Z < 2^73.
- The first 28 parity bits of the tail determine Z mod 2^28.
- The last 28 odd-ordinal correction digits of the prefix determine Z mod 3^28.
Because 2^28*3^28 > 2^72, one such residue pair admits at most one ordinary
checkpoint in the allowed interval.

The script also certifies the exact necessary tail-ballot prefix language at
28 steps and counts its residues: 16,956,950, less than 1/15 of all 2^28
residues.  No claim is made that every such necessary prefix extends to the
full first-passage tail.  This is an exact pruning/interface theorem, not a
proof of Collatz.
"""

from collections import defaultdict
from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670
t0 = 10 * J0
j0 = 10 * R0 + 1
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# Exact values of ceil(alpha*(t0+k))-j0, alpha=ln2/ln3, for k=1..28.
req = [
    0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8,
    9, 10, 10, 11, 11, 12, 13, 13, 14, 15, 15, 16, 17, 17,
]
assert len(req) == 28

# Certify each ceiling with directed rational log bounds:
#   j0+r-1 < alpha*(t0+k) < j0+r.
for k, r in enumerate(req, start=1):
    assert (t0 + k) * l2 > (j0 + r - 1) * u3
    assert (t0 + k) * u2 < (j0 + r) * l3

# Necessary tail ballot condition: after k tail time steps the number q of
# tail odd steps must satisfy q >= req[k-1].  Parity words are in bijection
# with start residues modulo 2^28 for the accelerated Collatz map, so this
# word count is also the count of necessary low-28-bit start residues.
states = {0: 1}
for r in req:
    nxt = defaultdict(int)
    for q, count in states.items():
        for bit in (0, 1):
            q2 = q + bit
            if q2 >= r:
                nxt[q2] += count
    states = dict(nxt)

tail_prefix_count = sum(states.values())
assert tail_prefix_count == 16_956_950
assert 15 * tail_prefix_count < (1 << 28)

# Mixed-radix singleton threshold for Z in (2^72,2^73), interval width 2^72.
M = (1 << 28) * (3 ** 28)
W = 1 << 72
assert M == 6 ** 28
assert M > W
assert 3 ** 28 > (1 << 44)

# Since gcd(2^28,3^28)=1, every pair of residues has one CRT class mod M.
# Any interval of width <M contains at most one representative of that class.
from math import gcd
assert gcd(1 << 28, 3 ** 28) == 1

print("PASS A0 s=1 mixed-radix 28x28 checkpoint certificate")
print("tail_28bit_necessary_residues", tail_prefix_count)
print("tail_fraction_lt_1_over_15", True)
print("CRT_modulus", M)
print("checkpoint_interval_width", W)
print("CRT_modulus_over_width", float(Fraction(M, W)))
print("candidate_per_residue_pair_at_most", 1)
