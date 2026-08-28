#!/usr/bin/env python3
"""SAFE ballot-correction envelope and physical-X pruning for A0 s=1.

This certificate uses only necessary conditions.

For the pure lower-ballot language of length t0 and odd count j0, the
threshold word q(n)=ceil(alpha*n) delays every odd event as far as the
ballot constraint allows.  At fixed odd count, the Collatz correction

    C = sum_r 3^(j0-r) 2^(a_r)

is coordinatewise increasing in the odd positions a_r.  Therefore the
threshold word gives an upper envelope for every admissible pure-ballot
correction.  Extra C4F formation requirements can only shrink the language.

If a_r^th is the r-th threshold odd position, then

    a_r^th = floor((r-1)/alpha).

Since j0-1 < alpha*t0, each normalized threshold atom obeys

    3^(j0-r) 2^(a_r^th-t0) < 1.

Hence the exact, easy-to-use envelope is

    0 <= C/2^t0 < j0.

For an actual bridge,
    C/2^t0 = Z - lambda X
           = (3-lambda)X - (3X-Z),
where
    lambda = 3^j0 / 2^t0
           = 3*(3^R0/2^J0)^10.

Directed rational log bounds plus e^y >= 1+y give a rigorous positive
lower bound for delta=3-lambda.  Combining this with the already certified
physical debit corridor L_-=3X-Z <= L_MAX yields a new hard upper bound on X.

This is pruning only, not a same-orbit existence theorem.
"""

from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670
T0 = 10 * J0
J_ODD = 10 * R0 + 1

L_MIN = 651_202_941_420
L_MAX = 934_928_480_993
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# d = J0*ln2 - R0*ln3 > 0 because R0/J0 < log_3(2).
d_lo = J0 * l2 - R0 * u3
d_hi = J0 * u2 - R0 * l3
assert d_lo > 0
assert d_hi > d_lo

# lambda = 3 exp(-10d), delta = 3-lambda = 3(1-exp(-10d)).
# For y>=0, exp(y)>=1+y, hence exp(-y)<=1/(1+y), so
# 1-exp(-y) >= y/(1+y).
y_lo = 10 * d_lo
delta_lo = Fraction(3) * y_lo / (1 + y_lo)
assert delta_lo > 0

# Pure-ballot correction envelope:
#     C/2^T0 < J_ODD.
#
# Thus for any full admissible bridge (a subset of the pure ballot language),
#
#     delta*X - L_- < J_ODD.
#
# Since delta >= delta_lo and L_- <= L_MAX,
#
#     delta_lo*X < L_MAX + J_ODD.
strict_upper = Fraction(L_MAX + J_ODD, 1) / delta_lo
max_integer_X = (strict_upper.numerator - 1) // strict_upper.denominator

assert 2**71 < max_integer_X < 2**72

shell_size = 2**72 - 2**71
retained_count = max_integer_X - 2**71 + 1

print("PASS A0 s=1 ballot correction envelope pruning certificate")
print("normalized_correction_envelope", f"0 <= C/2^t0 < {J_ODD}")
print("delta_lower_bound_positive", True)
print("physical_X_integer_upper", max_integer_X)
print("previous_shell", f"{2**71} < X < {2**72}")
print("new_safe_pruning", f"X <= {max_integer_X}")
print("retained_fraction_of_72bit_shell_upper", float(Fraction(retained_count, shell_size)))
print("status", "SAFE necessary pruning only")
