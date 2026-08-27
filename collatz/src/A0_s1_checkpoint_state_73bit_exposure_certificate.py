#!/usr/bin/env python3
"""Exact rational certificate for the s=1 checkpoint ordinary-state exposure.

In the reset A0 branch, let X=N+d with N<4/3*2^71 and 0<=d<0.478G.
At t0=10J0, the s=1 sector has j0=10R0+1 odd events.  The certificate
proves the checkpoint state Z=T^t0(X) satisfies

    2^72 < Z < 2^73.

No floating point is used in assertions.  This is not a proof of Collatz.
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
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


# ln 2 = 2 atanh(1/3), ln 3 = 2 atanh(1/2)
l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

delta_J_lo = J0 * l2 - R0 * u3
delta_J_hi = J0 * u2 - R0 * l3
assert delta_J_lo > 0

# In the s=1 sector the prefix linear coefficient is
# Cpre = 3^(10R0+1)/2^(10J0) = 3 exp(-10 delta_J).
# Lower bound it by exp(-x)>1-x, and upper-bound its deficit from 3 by
# exp(x)>1+x -> 1-exp(-x)>x/(1+x).
x_hi = 10 * delta_J_hi
x_lo = 10 * delta_J_lo
Cpre_lower = 3 * (1 - x_hi)
deficit_from_3_lower = 3 * x_lo / (1 + x_lo)
assert Cpre_lower > Fraction(299, 100)

# Actual prefix correction is no larger than the mechanical prefix correction.
# With n_j-1=floor((j-1)log_2 3), each normalized term obeys
# 2^(n_j-1)/3^j <= 1/3. Hence the affine prefix correction after division by
# 2^t0 is < Cpre*j0/3 < j0 because Cpre<3.
correction_upper = j0

# Reset input strip: X < (4/3)B + 0.478G.
X_upper_linear_times_3 = 4 * B + Fraction(1434, 1000) * G

# Since X>B, the coefficient deficit removes at least deficit*B from 3X.
Z_upper = X_upper_linear_times_3 - deficit_from_3_lower * B + correction_upper
assert Z_upper < 4 * B  # 2^73

# Lower side: positive correction and X>B give Z>Cpre*B>2.99B>2B=2^72.
Z_lower = Cpre_lower * B
assert Z_lower > 2 * B

print("PASS A0 s=1 checkpoint 73-bit exposure certificate")
print("checkpoint_time_t0", t0)
print("checkpoint_odd_count_j0", j0)
print("Cpre_lower", float(Cpre_lower))
print("deficit_from_3_lower_over_G_after_B", float(deficit_from_3_lower * B / G))
print("coarse_prefix_correction_upper_over_G", float(Fraction(correction_upper, G)))
print("certified_shell", "2^72 < Z < 2^73")
