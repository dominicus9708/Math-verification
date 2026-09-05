#!/usr/bin/env python3
"""Exact rational certificate for the s=1 renewal debit/credit corridor.

In the post-A0,A0,J0 reset hard branch write

    X --(10 J0, s=1)--> Z --(U,P-1)--> Y.

Define the ordinary renewal observables

    L_minus = 3 X - Z,
    L_plus  = 3 Y - Z.

The certificate proves, without using the defect lower-bound machinery,

    75 G < L_minus < 112 G < 2^40,
    52 G < L_plus  < 108 G < 2^40,

and after inserting only the independently certified reset near-return window,

    75.810... G < L_minus < 108.842... G,
    74.376... G < L_plus  < 107.408... G,
    |L_plus-L_minus| < 2^34.

Thus equality of the 73-bit checkpoint can be represented equivalently as a
near match of two ordinary <40-bit renewal addresses.  This is a direct
physical-intersection coordinate, not an independent Hensel lower bound and
not a proof of Collatz.
"""

from fractions import Fraction

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


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# ---------------------------------------------------------------------------
# Prefix debit L_minus = 3X-Z.
# Cpre = 3 exp(-x), x = 10(J0 ln2 - R0 ln3)>0, and
# Z = Cpre X + prefix_correction.
# The companion 73-bit checkpoint certificate proves the normalized prefix
# correction is positive and < j0.
# ---------------------------------------------------------------------------
delta_J_lo = J0 * l2 - R0 * u3
delta_J_hi = J0 * u2 - R0 * l3
assert delta_J_lo > 0
x_lo = 10 * delta_J_lo
x_hi = 10 * delta_J_hi

# 1-exp(-x) > x/(1+x), and 1-exp(-x) < x.
pre_deficit_lo = 3 * x_lo / (1 + x_lo)
pre_deficit_hi = 3 * x_hi

X_upper = Fraction(4, 3) * B + Fraction(478, 1000) * G
Lminus_lo = pre_deficit_lo * B - j0
Lminus_hi = pre_deficit_hi * X_upper

assert Lminus_lo > 75 * G
assert Lminus_hi < 112 * G
assert 112 * G < (1 << 40)

# ---------------------------------------------------------------------------
# Tail credit L_plus = 3Y-Z.
# For s=1, qtail=P-1 and Ctail=exp(delta_U)/3, so
#
#   L_plus = (exp(delta_U)-1) Z + exp(delta_U) S_tail.
#
# Every proper tail odd event lies under the first-passage coefficient wall.
# In the local affine correction S_tail=sum 2^a_r/3^r this gives the safe
# coarse termwise bound 2^a_r/3^r < 3, hence S_tail < 3 qtail.
# ---------------------------------------------------------------------------
delta_U_lo = P * l3 - U * u2
delta_U_hi = P * u3 - U * l2
assert delta_U_lo > 0
assert delta_U_hi < 1

# e^y-1 > y and e^y < 1/(1-y) for 0<y<1.
tail_gain_lo = delta_U_lo
tail_gain_hi = delta_U_hi / (1 - delta_U_hi)
exp_tail_hi = Fraction(1, 1) / (1 - delta_U_hi)

# Companion checkpoint theorem: 2^72 < Z < 2^73 = 4B.
Lplus_lo = tail_gain_lo * (2 * B)
Lplus_hi = tail_gain_hi * (4 * B) + exp_tail_hi * (3 * qtail)

assert Lplus_lo > 52 * G
assert Lplus_hi < 108 * G
assert 108 * G < (1 << 40)

# ---------------------------------------------------------------------------
# Exact ordinary coupling.
# L_plus-L_minus = 3(Y-X).
# In the reset strip, -0.478G < Y-X < 0.5023G.
# ---------------------------------------------------------------------------
diff_lo = -Fraction(1434, 1000) * G
diff_hi = Fraction(15069, 10000) * G
assert diff_hi < (1 << 34)
assert -diff_lo < (1 << 34)
assert diff_hi < 3 ** 22
assert -diff_lo < 3 ** 22

# Propagate the coupling through the independent one-sided intervals.
Lminus_consistent_lo = max(Lminus_lo, Lplus_lo - diff_hi)
Lminus_consistent_hi = min(Lminus_hi, Lplus_hi - diff_lo)
Lplus_consistent_lo = max(Lplus_lo, Lminus_lo + diff_lo)
Lplus_consistent_hi = min(Lplus_hi, Lminus_hi + diff_hi)

assert Lminus_consistent_lo > 75 * G
assert Lminus_consistent_hi < Fraction(108842, 1000) * G
assert Lplus_consistent_lo > Fraction(74376, 1000) * G
assert Lplus_consistent_hi < Fraction(107408, 1000) * G

# Both observables need at most 40 ordinary binary bits and at most 26 trits.
assert Lminus_consistent_hi < (1 << 40)
assert Lplus_consistent_hi < (1 << 40)
assert Lminus_consistent_hi < 3 ** 26
assert Lplus_consistent_hi < 3 ** 26

print("PASS A0 s=1 40-bit debit-credit corridor certificate")
print("Lminus_over_G", float(Lminus_consistent_lo / G), float(Lminus_consistent_hi / G))
print("Lplus_over_G", float(Lplus_consistent_lo / G), float(Lplus_consistent_hi / G))
print("difference_over_G", float(diff_lo / G), float(diff_hi / G))
print("binary_address_bits", 40)
print("ternary_address_digits", 26)
print("difference_abs_lt_2pow34", True)
