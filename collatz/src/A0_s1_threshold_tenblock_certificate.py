#!/usr/bin/env python3
"""Exact certificate for the A0 s=1 ten-J0 threshold block compression.

Let alpha = log_3(2), and define the lower ballot threshold word by

    b_n = ceil(alpha*(n+1)) - ceil(alpha*n).

For
    J0 = 10_439_860_591,
    R0 =  6_586_818_670,
    eps = J0*alpha - R0,

this certificate proves, with directed rational logarithm bounds,

    0 < eps,
    10*eps < 1/J0.

The arithmetic consequence is that for every interior residue
1 <= r <= J0-1 and every block phase 0 <= k <= 9,

    ceil(alpha*r + k*eps) = ceil(R0*r/J0).

Because gcd(R0,J0)=1, the rational fractional parts are separated from
integers by at least 1/J0, while the total phase drift is smaller.

Hence the length-10*J0 threshold word is exactly

    W_th = U L^9,

where L is the lower rational mechanical word of slope R0/J0,

    L[r] = floor((r+1)R0/J0) - floor(r R0/J0),

and U differs from L only in the first bit:

    U = 1 s 1,
    L = 0 s 1.

Therefore |L|=J0, q(L)=R0, q(U)=R0+1, and
q(W_th)=10R0+1.

This is a block-compression theorem only.  It does not prove membership
of an arbitrary required Collatz correction in the full admissible language.
"""

from fractions import Fraction
from math import gcd

J0 = 10_439_860_591
R0 = 6_586_818_670
T0 = 10 * J0
J_ODD = 10 * R0 + 1
NLOG = 90


def log_bounds(z: Fraction, n: int = NLOG):
    """Directed atanh-series bounds for log((1+z)/(1-z))."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


# log(2) = 2*atanh(1/3), log(3) = 2*atanh(1/2).
l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

alpha_lo = l2 / u3
alpha_hi = u2 / l3

eps_lo = J0 * alpha_lo - R0
eps_hi = J0 * alpha_hi - R0

assert gcd(R0, J0) == 1
assert eps_lo > 0
assert eps_hi > eps_lo
assert 10 * eps_hi < Fraction(1, J0)

# Useful endpoint guards.  They are much weaker than the separation bound,
# but make the block-boundary ceiling argument explicit.
assert 10 * eps_hi < 1
assert alpha_hi + 9 * eps_hi < 1

# At t0 the threshold odd count is exactly 10R0+1.
assert 10 * R0 < alpha_lo * T0
assert alpha_hi * T0 < 10 * R0 + 1
assert J_ODD == 10 * R0 + 1

# The following is the exact integer core of the phase-stability proof.
# For 1 <= r <= J0-1, coprimality gives
#
#     R0*r = m*J0 + s,   1 <= s <= J0-1.
#
# Also
#
#     alpha*r + k*eps
#       = R0*r/J0 + (r/J0 + k)*eps.
#
# For 0 <= k <= 9,
#
#     0 < (r/J0 + k)*eps < 10*eps < 1/J0.
#
# Therefore this perturbation cannot cross the next integer from any
# rational grid point s/J0.  No loop over J0 residues is required.

# Exact symbolic correction transfer for W_th = U L^9.
#
# Put K=C(L).  Since U is L with an added odd event at position 0,
#
#     C(U) = K + 3^R0.
#
# Repeated concatenation C(uv)=3^q(v)C(u)+2^|u|C(v) gives
#
#     C(W_th) = 3^(10R0) + A*K,
#
# where
#
#     A = sum_{i=0}^9 3^((9-i)R0) 2^(iJ0).
#
# This is an exact arithmetic-circuit representation; the enormous integer
# is deliberately not materialized.

print("PASS A0 s=1 ten-J0 threshold block certificate")
print("J0", J0)
print("R0", R0)
print("t0", T0)
print("j0", J_ODD)
print("gcd_R0_J0", gcd(R0, J0))
print("eps_positive", True)
print("ten_eps_lt_inverse_J0", True)
print("threshold_factorization", "W_th = U L^9")
print("L", "lower mechanical word slope R0/J0 = 0 s 1")
print("U", "same interior as L, first bit raised: 1 s 1")
print("correction_transfer", "C(W_th)=3^(10R0)+A*C(L)")
print("A", "sum_{i=0}^9 3^((9-i)R0)2^(iJ0)")
