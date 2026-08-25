#!/usr/bin/env python3
"""Exact terminal-46 3-adic defect certificate for the first global resonance.

This certificate works only at the repaired first global binary resonance

    (A,Q) = (114208327604, 72057431991).

It proves a necessary endpoint-side condition for any hypothetical minimal
counterexample in this cell:

* the last 46 odd ordinals cannot all be mechanical;
* they cannot differ from the mechanical tail at exactly one ordinal;
* hence D_tail >= 2;
* if D_tail == 2, the endpoint condition reduces to 9 finite residue classes
  and only 8 distinct ordinary endpoint values.

Combined with the separately certified D_72 >= 11 prefix theorem, the two
supports are disjoint and therefore the total number of displaced odd ordinals
is at least 13.

No floating point, ternary selector, repeated L7/L14 pullback, or independence
assumption is used.  This is not a proof of the Collatz conjecture.
"""

from itertools import combinations

A = 114_208_327_604
Q = 72_057_431_991
MOD = 3**46
LOW = 2**71
UPPER_TIMES_3 = 4 * 2**71 + 3 * 2**33

# Exact mechanical positions b_{Q-45},...,b_Q, certified independently by
# global_first_resonance_two_ended_mechanical_exclusion.py.
B = [
    114208327531, 114208327532, 114208327534, 114208327535,
    114208327537, 114208327539, 114208327540, 114208327542,
    114208327543, 114208327545, 114208327546, 114208327548,
    114208327550, 114208327551, 114208327553, 114208327554,
    114208327556, 114208327558, 114208327559, 114208327561,
    114208327562, 114208327564, 114208327565, 114208327567,
    114208327569, 114208327570, 114208327572, 114208327573,
    114208327575, 114208327577, 114208327578, 114208327580,
    114208327581, 114208327583, 114208327584, 114208327586,
    114208327588, 114208327589, 114208327591, 114208327592,
    114208327594, 114208327596, 114208327597, 114208327599,
    114208327600, 114208327602,
]
assert len(B) == 46
assert all(B[t] < B[t + 1] for t in range(45))

INV_2A = pow(2, -A, MOD)
GAP = [None] + [B[t] - B[t - 1] for t in range(1, 46)]
assert all(g in (1, 2) for g in GAP[1:])


def endpoint(delta):
    """Least nonnegative endpoint residue modulo 3^46.

    delta[t] = B[t]-a_{Q-45+t}.  Since every candidate endpoint is below
    3^46, an admissible residue is the ordinary endpoint itself.
    """
    assert len(delta) == 46
    assert all(d >= 0 for d in delta)
    apos = [b - d for b, d in zip(B, delta)]
    assert all(a >= 0 for a in apos)
    assert all(apos[t] < apos[t + 1] for t in range(45))

    total = 0
    for t, a in enumerate(apos):
        ell = 45 - t
        total = (total + pow(3, ell, MOD) * pow(2, a, MOD)) % MOD
    return (INV_2A * total) % MOD


def endpoint_band_and_mod4(y):
    # N>2^71, 0<g<2^33, y=N+g, N == y == 3 (mod 4).
    return LOW < y and 3 * y < UPPER_TIMES_3 and y % 4 == 3


# Triangular periodicity.  The t-th earliest terminal term carries 3^(45-t),
# so modulo 3^46 it sees 2^(-delta[t]) only modulo 3^(t+1).  The exact order
# of 2 modulo 3^(t+1) is 2*3^t.
for t in range(46):
    m = 3 ** (t + 1)
    period = 2 * 3**t
    assert pow(2, period, m) == 1
    if t == 0:
        assert pow(2, 1, m) != 1
    else:
        assert pow(2, period // 3, m) != 1

# Mechanical endpoint regression.
Y_MECH = endpoint([0] * 46)
assert Y_MECH == 4_699_104_266_570_964_686_821
assert not endpoint_band_and_mod4(Y_MECH)

# -------------------------------------------------------------------------
# D_tail = 1: exhaustive finite residue classification.
# -------------------------------------------------------------------------
# If only t=0 is displaced, its contribution depends only on delta_0 mod 2.
# Positive representatives 1 and 2 cover the two classes.
singletons = []
for d0 in (1, 2):
    d = [0] * 46
    d[0] = d0
    singletons.append(((0, d0 % 2), endpoint(d)))

# If t>0 is the unique displaced coordinate, delta[t-1]=0.  Strict ordering
# a[t-1] < a[t] gives
#   delta[t] <= delta[t-1] + (B[t]-B[t-1]) - 1.
# Hence positivity is possible only across a mechanical gap 2, and then
# delta[t]=1 exactly.
for t in range(1, 46):
    if GAP[t] == 2:
        d = [0] * 46
        d[t] = 1
        singletons.append(((t, 1), endpoint(d)))

assert len(singletons) == 28
broad_only = [
    (key, y) for key, y in singletons
    if LOW < y and 3 * y < UPPER_TIMES_3
]
assert broad_only == [((9, 1), 2_994_179_304_232_351_671_382)]
assert broad_only[0][1] % 4 == 2
assert not any(endpoint_band_and_mod4(y) for _, y in singletons)

# Therefore D_tail=0 and D_tail=1 are both impossible.
D_TAIL_LOWER = 2
assert D_TAIL_LOWER == 2

# -------------------------------------------------------------------------
# D_tail = 2: exact finite residue classification.
# -------------------------------------------------------------------------
pairs = []

# Support {0,1}.  Ordering only requires delta_1 <= delta_0 because GAP[1]=1.
# Endpoint dependence is delta_0 mod 2 and delta_1 mod 6.  Every residue pair
# has positive ordered representatives, so all 2*6 classes are enumerated.
assert GAP[1] == 1
for r0 in (0, 1):
    for r1 in range(6):
        d1 = r1 if r1 else 6
        d0 = d1 if d1 % 2 == r0 else d1 + 1
        assert d1 <= d0 and d0 > 0 and d1 > 0
        d = [0] * 46
        d[0], d[1] = d0, d1
        pairs.append(((0, 1, r0, r1), endpoint(d)))

# Support {0,k}, k>=2.  The zero immediately before k forces delta_k=1 and
# requires GAP[k]=2.  delta_0 contributes only its parity class.
for k in range(2, 46):
    if GAP[k] == 2:
        for r0 in (0, 1):
            d0 = 1 if r0 else 2
            d = [0] * 46
            d[0], d[k] = d0, 1
            pairs.append(((0, k, r0, 1), endpoint(d)))

# Supports entirely inside t>=1.  The first positive coordinate starts after
# a zero, hence is exactly 1 across a gap 2.  If the second positive coordinate
# is adjacent it may be 1..GAP[k]; if separated by a zero, it again must be 1
# across a gap 2.
for i, k in combinations(range(1, 46), 2):
    if GAP[i] != 2:
        continue
    if k == i + 1:
        for dk in range(1, GAP[k] + 1):
            d = [0] * 46
            d[i], d[k] = 1, dk
            pairs.append(((i, k, 1, dk), endpoint(d)))
    elif GAP[k] == 2:
        d = [0] * 46
        d[i], d[k] = 1, 1
        pairs.append(((i, k, 1, 1), endpoint(d)))

assert len(pairs) == 414
pair_survivors = [(key, y) for key, y in pairs if endpoint_band_and_mod4(y)]
assert len(pair_survivors) == 9
assert len({y for _, y in pair_survivors}) == 8

EXPECTED_PAIR_SURVIVORS = [
    ((0, 1, 0, 3), 2_729_562_462_203_742_221_059),
    ((0, 1, 1, 5), 2_729_562_462_203_742_221_059),
    ((2, 24, 1, 1), 3_059_622_251_880_574_799_467),
    ((5, 26, 1, 1), 2_390_750_338_045_521_993_103),
    ((7, 26, 1, 1), 2_768_988_818_993_959_778_023),
    ((9, 11, 1, 1), 2_463_461_351_003_862_446_095),
    ((12, 19, 1, 1), 3_104_589_732_879_008_787_067),
    ((14, 41, 1, 1), 2_697_452_540_596_458_807_755),
    ((33, 38, 1, 1), 2_556_248_067_081_360_242_587),
]
assert pair_survivors == EXPECTED_PAIR_SURVIVORS

# The prefix theorem independently gives D_72>=11.  Every terminal ordinal has
# index at least Q-45, hence its actual position is at least (Q-45)-1 = Q-46,
# far beyond position 71.  Thus the prefix and terminal displaced-ordinal
# supports are disjoint.
assert Q - 46 > 72
TOTAL_DISPLACED_LOWER = 11 + D_TAIL_LOWER
assert TOTAL_DISPLACED_LOWER == 13

print("first-resonance terminal-46 triangular defect certificate: PASS")
print("mechanical_endpoint", Y_MECH)
print("terminal_singleton_classes", len(singletons))
print("singleton_broad_band_hits", len(broad_only))
print("singleton_full_endpoint_hits", 0)
print("terminal_defect_lower_bound", D_TAIL_LOWER)
print("terminal_pair_classes", len(pairs))
print("terminal_pair_endpoint_classes", len(pair_survivors))
print("terminal_pair_distinct_endpoints", len({y for _, y in pair_survivors}))
print("total_displaced_lower_with_D72", TOTAL_DISPLACED_LOWER)
for key, y in pair_survivors:
    print("pair_survivor", key, y)
