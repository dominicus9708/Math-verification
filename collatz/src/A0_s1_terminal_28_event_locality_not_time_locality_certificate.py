#!/usr/bin/env python3
"""Exact rational certificate for terminal 28-event locality vs bit-time locality."""

from fractions import Fraction

T0 = 104_398_605_910
J0 = 65_868_186_701
Q_ACT = J0 - 28
EXPECTED_TPOS = 104_398_605_865
EXPECTED_MIN_REMAINING = 44
EXPECTED_MAX_REMAINING = 38_530_419_237


def log_bounds(z: Fraction, n: int = 110):
    """Exact lower/upper bounds for log((1+z)/(1-z))."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


# ln 2 = log((1+1/3)/(1-1/3)); ln 3 similarly with z=1/2.
L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))

# Exact rational enclosure of log_2 3 = ln 3 / ln 2.
R_LO = L3 / U2
R_HI = U3 / L2
assert R_LO < R_HI

x_lo = (Q_ACT - 1) * R_LO
x_hi = (Q_ACT - 1) * R_HI
floor_lo = x_lo.numerator // x_lo.denominator
floor_hi = x_hi.numerator // x_hi.denominator
assert floor_lo == floor_hi == EXPECTED_TPOS

# r-th threshold one position formula audit on a finite exact prefix.
def Q(n: int) -> int:
    if n == 0:
        return 0
    p2 = 1 << n
    p3 = 1
    q = 0
    while p3 <= p2:
        p3 *= 3
        q += 1
    return q

req = tuple(Q(n) for n in range(0, 200))
th = tuple(req[n + 1] - req[n] for n in range(199))
tpos = tuple(i for i, b in enumerate(th) if b)

small_checks = 0
for r in range(1, len(tpos) + 1):
    lo = (r - 1) * R_LO
    hi = (r - 1) * R_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi == tpos[r - 1]
    small_checks += 1

# Canonical seam immediately after q-th candidate one.
h_min = Q_ACT                    # earliest possible ordered q-th one: q-1
h_max = EXPECTED_TPOS + 1        # dominance latest possible q-th one
assert h_min <= h_max

remaining_min = T0 - h_max
remaining_max = T0 - h_min
assert remaining_min == EXPECTED_MIN_REMAINING
assert remaining_max == EXPECTED_MAX_REMAINING

# The interval is dramatically wider than a short terminal bit shell.
assert remaining_max > 10**10
assert remaining_min == 44

print("PASS A0 s=1 terminal 28-event locality not time-locality certificate")
print("target_length", T0)
print("target_one_count", J0)
print("activation_used_ones", Q_ACT)
print("activation_remaining_ones", 28)
print("threshold_qth_one_position", EXPECTED_TPOS)
print("activation_h_min", h_min)
print("activation_h_max", h_max)
print("remaining_bit_length_min", remaining_min)
print("remaining_bit_length_max", remaining_max)
print("small_threshold_position_checks", small_checks)
print("exact_log2_3_floor_interval_width_numerator", (x_hi - x_lo).numerator)
print("exact_log2_3_floor_interval_width_denominator", (x_hi - x_lo).denominator)
print("rejected", "q_rem=28 does not imply a universal ~43-bit late shell")
print("next", "compress the final 28 one-events by valuation-gap/event state rather than raw parity-bit enumeration")
