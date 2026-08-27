#!/usr/bin/env python3
"""Exact boundary-counter certificate for the repaired first A0 resonance.

This is a boundary/arithmetic certificate only.  It does not prove Collatz and
it does not use a Hensel-cost lower bound.
"""

A0 = 114_208_327_604
Q0 = 72_057_431_991
LOW = 1 << 71
G = 1 << 33
N0 = LOW + 3

# First-global physical root band:
#   LOW < N < (4/3) LOW,
#   N == 3 (mod 4).
# Hence N=N0+4s with 0<=s<S.
S = (LOW - 10) // 12 + 1
assert S == 196_765_270_119_568_550_570
assert 3**42 < S < 3**43

# First-global gap g=4r, 0<g<G.
R = G // 4
assert R == 1 << 31
assert 3**19 < R < 3**20

# Exact physical two-counter parametrization:
#   N=N0+4s, 0<=s<S,
#   g=4r, 1<=r<R,
#   Y=N0+4(s+r).
# The endpoint index k=s+r runs over one complete integer interval.
KMIN = 1
KMAX = S + R - 2
assert KMAX == 196_765_270_121_716_034_216

# The coarser endpoint-only interval used previously contains exactly two
# additional congruence points: the impossible g=0 lower endpoint and the
# impossible simultaneous top-endpoint point.
U3 = 4 * LOW + 3 * G
YMAX_COARSE = (U3 - 1) // 3
YFIRST_COARSE = N0
YLAST_COARSE = YMAX_COARSE - ((YMAX_COARSE - 3) % 4)
YCOUNT_COARSE = (YLAST_COARSE - YFIRST_COARSE) // 4 + 1
assert YCOUNT_COARSE == S + R
assert YCOUNT_COARSE - (KMAX - KMIN + 1) == 2

# Root residue saturation barrier.  Because the step 4 is a unit modulo 3^h,
# the first S values N0+4s cover every residue modulo 3^h whenever S>=3^h.
for h in range(1, 43):
    assert S >= 3**h
assert S < 3**43

# At depth 43 the root parameter s itself is exposed as an ordinary bounded
# counter; the accepted fraction is S/3^43.
assert 3**43 - S == 131_491_697_274_968_527_057

# LSB-first bounded-counter comparator.  For x<=B<3^digits, subtract x from B
# from low to high; final borrow 0 is equivalent to x<=B.
def ternary_digits(x: int, digits: int):
    out = []
    for _ in range(digits):
        out.append(x % 3)
        x //= 3
    assert x == 0
    return out


def lsb_leq(x: int, B: int, digits: int) -> bool:
    xd = ternary_digits(x, digits)
    bd = ternary_digits(B, digits)
    borrow = 0
    for a, b in zip(xd, bd):
        t = b - a - borrow
        borrow = 1 if t < 0 else 0
    return borrow == 0

for x in [0, 1, S - 2, S - 1, S, S + 1, 3**43 - 1]:
    assert lsb_leq(x, S - 1, 43) == (x < S)
for x in [0, 1, R - 2, R - 1, R, R + 1, 3**20 - 1]:
    assert lsb_leq(x, R - 1, 20) == (x < R)

# Exact mechanical terminal residue at the first resonance.
def mech(j: int) -> int:
    return ((j - 1) * A0) // Q0


def terminal_mechanical_mod(m: int, depth: int | None = None) -> int:
    if depth is None:
        depth = m
    M = 3**depth
    inv2 = pow(2, -1, M)
    invA = pow(inv2, A0, M)
    total = 0
    for t in range(m):
        j = Q0 - m + 1 + t
        B = mech(j)
        total = (total + pow(3, m - 1 - t, M) * pow(2, B, M)) % M
    return (invA * total) % M

# The zero-displacement terminal ray has one unique physical endpoint lift
# through depth 44, then fails at the 45th ternary digit.
y44 = terminal_mechanical_mod(44, 44)
mod44 = 3**44
inv4_44 = pow(4, -1, mod44)
kstar = ((y44 - N0) * inv4_44) % mod44
assert 1 <= kstar <= KMAX
YSTAR = N0 + 4 * kstar
assert YSTAR == 2_729_562_462_203_742_221_059

for h in (42, 43, 44):
    assert terminal_mechanical_mod(h, h) == YSTAR % (3**h)

YMECH46 = terminal_mechanical_mod(46, 46)
assert YMECH46 == 4_699_104_266_570_964_686_821
assert YMECH46 - YSTAR == 2 * 3**44
assert terminal_mechanical_mod(45, 45) != YSTAR % (3**45)

# Reset-strip ordinary counters.  These are safe integer supersets from
# d<0.478G and d'<0.9803G; both are completely exposed in 21 ternary digits.
def ceil_div(a: int, b: int) -> int:
    return (a + b - 1) // b

D_START_COUNT = ceil_div(478 * G, 1000)
D_END_COUNT = ceil_div(9803 * G, 10000)
assert D_START_COUNT == 4_105_988_735
assert D_END_COUNT == 8_420_712_881
assert D_START_COUNT < 3**21
assert D_END_COUNT < 3**21

print("PASS physical boundary counter automaton certificate")
print("root_counter_count", S)
print("root_counter_trits", 43)
print("gap_counter_count", R - 1)
print("gap_counter_trits", 20)
print("physical_endpoint_k_range", KMIN, KMAX)
print("unique_mechanical_endpoint_through_h44", YSTAR)
print("mechanical_minus_candidate", YMECH46 - YSTAR, "= 2*3^44")
print("reset_start_offset_counter_count", D_START_COUNT)
print("reset_end_offset_counter_count", D_END_COUNT)
