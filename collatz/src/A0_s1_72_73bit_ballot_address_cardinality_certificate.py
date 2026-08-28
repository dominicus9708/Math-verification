#!/usr/bin/env python3
"""Exact finite certificate for the s=1 72/73-bit ballot-address marginals.

This certificate counts two NECESSARY local address languages only:

1. the first 72 parity bits of the pre 0->0 renewal ballot bridge;
2. the first 73 parity bits after the renewal point t0.

The thresholds are certified by directed rational bounds for ln(2), ln(3),
and the word counts are exact integer dynamic programs.

The two counts are MARGINAL counts.  They must not be multiplied as if the
pre and tail/checkpoint addresses were probabilistically independent.
No finite local address count is promoted to a full long-block path theorem.
This is not a proof of Collatz.
"""

from collections import defaultdict
from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670

t0 = 10 * J0
j0 = 10 * R0 + 1
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    """Directed bounds for 2*atanh(z)."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))  # ln 2
l3, u3 = log_bounds(Fraction(1, 2))  # ln 3

# Exact requirements ceil(alpha*k), alpha=ln2/ln3, for k=1,...,72.
req_pre72 = [
    1,2,2,3,4,4,5,6,6,7,7,8,9,9,10,11,11,12,
    12,13,14,14,15,16,16,17,18,18,19,19,20,21,21,22,23,23,
    24,24,25,26,26,27,28,28,29,30,30,31,31,32,33,33,34,35,
    35,36,36,37,38,38,39,40,40,41,42,42,43,43,44,45,45,46,
]
assert len(req_pre72) == 72

# Exact requirements ceil(alpha*(t0+k))-j0 for k=1,...,73.
req_tail73 = [
    0,1,1,2,3,3,4,5,5,6,6,7,8,8,9,10,10,11,11,12,
    13,13,14,15,15,16,17,17,18,18,19,20,20,21,22,22,23,23,24,25,
    25,26,27,27,28,29,29,30,30,31,32,32,33,34,34,35,35,36,37,37,
    38,39,39,40,41,41,42,42,43,44,44,45,46,
]
assert len(req_tail73) == 73

# Directed proof of every ceiling value.
for k, r in enumerate(req_pre72, start=1):
    assert k * l2 > (r - 1) * u3
    assert k * u2 < r * l3

for k, r in enumerate(req_tail73, start=1):
    assert (t0 + k) * l2 > (j0 + r - 1) * u3
    assert (t0 + k) * u2 < (j0 + r) * l3


def count_ballot_words(req):
    """Count bit words whose running number of 1s stays above req[k]."""
    states = {0: 1}
    for threshold in req:
        nxt = defaultdict(int)
        for q, count in states.items():
            for bit in (0, 1):
                q2 = q + bit
                if q2 >= threshold:
                    nxt[q2] += count
        states = dict(nxt)
    return sum(states.values()), states


pre72, pre_terminal_counts = count_ballot_words(req_pre72)
tail73, tail_terminal_counts = count_ballot_words(req_tail73)

assert pre72 == 4_650_657_914_809_371_340
assert tail73 == 42_553_228_731_364_551_533

# Sharp integer reciprocal-density brackets relative to the physical shells
# used by the current Route-B audit.  These are marginal upper-density facts,
# not intersection estimates.
assert 507 * pre72 < (1 << 71)
assert not (508 * pre72 < (1 << 71))
assert 110 * tail73 < (1 << 72)
assert not (111 * tail73 < (1 << 72))

# Explicitly do not form a product estimate for the joint same-address event.

print("PASS A0 s=1 72/73-bit ballot address cardinality certificate")
print("pre72_necessary_words", pre72)
print("pre72_reciprocal_density_floor", 507)
print("tail73_necessary_words", tail73)
print("tail73_reciprocal_density_floor", 110)
print("independence_product_used", False)
