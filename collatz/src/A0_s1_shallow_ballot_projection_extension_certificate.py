#!/usr/bin/env python3
"""Exact boundary arithmetic for the s=1 shallow ballot projection theorem.

The symbolic theorem is recorded in the companion note:

* every 37-step pre prefix satisfying the first-crossing ballot barrier extends
  combinatorially to some full nonnegative 0->0 ballot bridge at t0;
* every 40-step tail prefix satisfying the renewal barrier extends
  combinatorially to some full first-passage 0->-1 ballot bridge at U.

This certificate checks the exact endpoint ceiling identities and reproduces
both shallow prefix counts.  It does NOT assert arithmetic Collatz same-address
extension of those ballot words.
"""

from collections import defaultdict
from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670
A0 = 114_208_327_604
Q0 = 72_057_431_991

t0 = 10 * J0
j0 = 10 * R0 + 1
U = A0 - t0
P = Q0 - 10 * R0
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# ceil(alpha*t0)=j0.
assert t0 * l2 > (j0 - 1) * u3
assert t0 * u2 < j0 * l3

# At A0-1 the coefficient barrier is Q0; at A0 it jumps to Q0+1.
assert (A0 - 1) * l2 > (Q0 - 1) * u3
assert (A0 - 1) * u2 < Q0 * l3
assert A0 * l2 > Q0 * u3
assert A0 * u2 < (Q0 + 1) * l3

# Therefore for the tail renewal barrier c(k)=ceil(alpha(t0+k))-j0,
# c(U-1)=P-1 and c(U)=P.
assert Q0 - j0 == P - 1
assert (Q0 + 1) - j0 == P

# Reproduce exact shallow projection counts.
pre_req = [
    1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,12,13,
    14,14,15,16,16,17,18,18,19,19,20,21,21,22,23,23,24,
]
tail_req = [
    0,1,1,2,3,3,4,5,5,6,6,7,8,8,9,10,10,11,11,12,
    13,13,14,15,15,16,17,17,18,18,19,20,20,21,22,22,23,23,24,25,
]

for k, r in enumerate(pre_req, 1):
    assert k * l2 > (r - 1) * u3
    assert k * u2 < r * l3
for k, r in enumerate(tail_req, 1):
    assert (t0 + k) * l2 > (j0 + r - 1) * u3
    assert (t0 + k) * u2 < (j0 + r) * l3


def count_prefix(req):
    states = {0: 1}
    for r in req:
        nxt = defaultdict(int)
        for q, c in states.items():
            for bit in (0, 1):
                q2 = q + bit
                if q2 >= r:
                    nxt[q2] += c
        states = dict(nxt)
    return sum(states.values())


assert count_prefix(pre_req) == 967_378_591
assert count_prefix(tail_req) == 31_654_570_714
assert max(pre_req) < j0
assert max(tail_req) < P - 1

print("PASS A0 s=1 shallow ballot projection extension certificate")
print("pre37_projection_count", 967_378_591)
print("tail40_projection_count", 31_654_570_714)
print("pre_ballot_extension", "combinatorially complete")
print("tail_first_passage_extension", "combinatorially complete")
print("arithmetic_same_address_extension", "OPEN")
