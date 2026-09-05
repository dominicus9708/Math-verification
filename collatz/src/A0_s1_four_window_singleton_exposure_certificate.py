#!/usr/bin/env python3
"""Exact finite-address certificate for the s=1 four-window singleton reduction.

The companion results give:

1. Z in (2^72,2^73);
2. 28 tail parity bits + 28 prefix endpoint trits determine at most one Z;
3. renewal observables L_minus=3X-Z and L_plus=3Y-Z obey the safe coarse
   consistent corridors

       75G < L_minus < 109G,
       74G < L_plus  < 108G.

For a fixed checkpoint Z these corridors put X=(Z+L_minus)/3 and
Y=(Z+L_plus)/3 in intervals of width <34G/3.  The script proves

    34G/3 < 2^37 < 3^24.

Hence 37 dyadic start bits determine X uniquely inside its conditional
interval, and 24 ternary endpoint digits determine Y uniquely inside its
conditional interval.

The first 37 pre parity bits are also audited against the global coefficient
ballot barrier; exactly 967,378,591 necessary words survive, less than 1/128
of all 37-bit words.

This is a boundary-candidate singleton theorem, not an extension theorem for
the billion-step interiors and not a proof of Collatz.
"""

from collections import defaultdict
from fractions import Fraction

G = 1 << 33
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# Conditional X/Y interval widths once Z is fixed.
width = Fraction(34, 3) * G
assert width < (1 << 37)
assert (1 << 37) < 3 ** 24

# The checkpoint itself is singleton after the 28x28 mixed-radix join.
assert (1 << 28) * (3 ** 28) > (1 << 72)

# Exact global first-crossing ballot thresholds ceil(alpha*k), k=1..37.
req37 = [
    1,2,2,3,4,4,5,6,6,7,
    7,8,9,9,10,11,11,12,12,13,
    14,14,15,16,16,17,18,18,19,19,
    20,21,21,22,23,23,24,
]
assert len(req37) == 37

for k, r in enumerate(req37, start=1):
    assert k * l2 > (r - 1) * u3
    assert k * u2 < r * l3

states = {0: 1}
for r in req37:
    nxt = defaultdict(int)
    for q, count in states.items():
        for bit in (0, 1):
            q2 = q + bit
            if q2 >= r:
                nxt[q2] += count
    states = dict(nxt)

pre37 = sum(states.values())
assert pre37 == 967_378_591
assert 128 * pre37 < (1 << 37)

# Endpoint exposure: any affine block with at least 24 odd ordinals determines
# its endpoint mod 3^24 from the final 24 odd correction terms.  The tail has
# vastly more than 24 odd ordinals, and an interval of width <3^24 admits at
# most one representative of a fixed residue.

print("PASS A0 s=1 four-window singleton exposure certificate")
print("checkpoint_join", "tail first 28 bits + prefix last 28 odd trits")
print("X_exposure_bits_after_Z", 37)
print("Y_exposure_trits_after_Z", 24)
print("conditional_XY_width_lt", float(width))
print("pre37_necessary_words", pre37)
print("pre37_fraction_lt_1_over_128", True)
