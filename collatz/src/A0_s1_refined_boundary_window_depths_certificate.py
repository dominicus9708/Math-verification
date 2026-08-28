#!/usr/bin/env python3
"""Refined A0 s=1 mixed-radix and local boundary exposure depths.

Inherited SAFE constants:
- X is an integer with X > 2^71.
- Z is an integer with Z < 2^73.
- L_minus = 3X-Z <= 934,928,480,993.
- radius-seven defect + Christoffel envelope gives
      L_minus >= 669,562,762,561.
- coarse tail credit corridor:
      74G < L_plus < 108G, G=2^33.

Consequences certified here:
1. checkpoint singleton improves from 28x28 to 27 dyadic x 28 ternary;
2. L_minus local terminal depth improves from 26 trits to 24 trits;
3. L_plus local tail depth improves from 40 bits to 39 bits.

These are exposure-depth reductions, not long-bridge existence theorems.
"""

from collections import defaultdict

G = 1 << 33
X_MIN = (1 << 71) + 1
Z_MAX = (1 << 73) - 1

L_MINUS_MIN = 669_562_762_561
L_MINUS_MAX = 934_928_480_993

L_PLUS_MIN = 74 * G + 1
L_PLUS_MAX = 108 * G - 1

# ---------------------------------------------------------------------------
# 1. Refined checkpoint interval and 27x28 mixed-radix singleton.
# ---------------------------------------------------------------------------

Z_MIN = 3 * X_MIN - L_MINUS_MAX
assert Z_MIN > (1 << 72)

Z_SPAN = Z_MAX - Z_MIN
assert Z_SPAN == (1 << 71) + L_MINUS_MAX - 4

M_27_28 = (1 << 27) * (3 ** 28)
M_26_28 = (1 << 26) * (3 ** 28)
M_28_27 = (1 << 28) * (3 ** 27)

assert M_27_28 > Z_SPAN
assert M_26_28 <= Z_SPAN
assert M_28_27 <= Z_SPAN

# Exact tail threshold increments inherited from the 28-step certificate.
req28 = [
    0, 1, 1, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8,
    9, 10, 10, 11, 11, 12, 13, 13, 14, 15, 15, 16, 17, 17,
]


def count_ballot(req):
    states = {0: 1}
    for r in req:
        nxt = defaultdict(int)
        for q, count in states.items():
            for bit in (0, 1):
                q2 = q + bit
                if q2 >= r:
                    nxt[q2] += count
        states = dict(nxt)
    return sum(states.values())


tail27 = count_ballot(req28[:27])
assert tail27 == 8_478_475
assert 15 * tail27 < (1 << 27)

# ---------------------------------------------------------------------------
# 2. L_minus residue exposure: 24 trits now suffice.
# ---------------------------------------------------------------------------

L_MINUS_SPAN = L_MINUS_MAX - L_MINUS_MIN
assert 3 ** 23 <= L_MINUS_SPAN < 3 ** 24

# A known residue modulo 3^24 therefore selects at most one ordinary L_minus
# in the certified corridor. The prefix formula modulo 3^24 uses only the
# final 24 odd-ordinal correction terms, together with X mod 3^24.

# ---------------------------------------------------------------------------
# 3. L_plus residue exposure: 39 bits suffice from the coarse corridor.
# ---------------------------------------------------------------------------

L_PLUS_SPAN = L_PLUS_MAX - L_PLUS_MIN
assert L_PLUS_SPAN == 34 * G - 2
assert (1 << 38) <= L_PLUS_SPAN < (1 << 39)

# Exact first-40 tail requirements; use only the first 39.
req40 = [
    0,1,1,2,3,3,4,5,5,6,
    6,7,8,8,9,10,10,11,11,12,
    13,13,14,15,15,16,17,17,18,18,
    19,20,20,21,22,22,23,23,24,25,
]

tail39 = count_ballot(req40[:39])
assert tail39 == 17_797_009_662
assert 30 * tail39 < (1 << 39)

print("PASS A0 s=1 refined boundary window depths certificate")
print("Z_min", Z_MIN)
print("Z_max", Z_MAX)
print("Z_span", Z_SPAN)
print("checkpoint_singleton", "2^27 x 3^28")
print("tail27_necessary_words", tail27)
print("tail27_fraction_lt_1_over_15", True)
print("Lminus_span", L_MINUS_SPAN)
print("Lminus_terminal_trits", 24)
print("Lplus_span", L_PLUS_SPAN)
print("Lplus_tail_bits", 39)
print("tail39_necessary_words", tail39)
print("tail39_fraction_lt_1_over_30", True)
print("status", "SAFE exposure-depth reduction only")
