#!/usr/bin/env python3
"""Exact certificate for the 10*J0 + upper-tail decomposition of A0.

This certificate records the continued-fraction macrostructure

    (A0,Q0) = 10*(J0,R0) + (U,P)

and its consequence for every first coefficient crossing at A0/Q0.
At each checkpoint m*J0, 1<=m<=10, proper-prefix coefficient survival forces
at least one odd-event surplus above m*R0.  At the tenth checkpoint let that
surplus be s>=1.  Then the terminal U-block contains exactly P-s odd events.
The coefficient logarithms split as

    log C_pre  = s ln 3 - 10 delta_J > 0,
    log C_tail = delta_U - s ln 3 < 0,
    log C_A    = log C_pre + log C_tail = -delta_A < 0.

Thus the A0 resonance necessarily transports an integer surplus token s into
a terminal coefficient-deficit block; the token cancels algebraically in the
full coefficient.  All numerical sign checks use exact rational log intervals.
This is not a proof of the Collatz conjecture.
"""

from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670
A0 = 114_208_327_604
Q0 = 72_057_431_991
U = A0 - 10 * J0
P = Q0 - 10 * R0
NLOG = 90

assert U == 9_809_721_694
assert P == 6_189_245_291
assert 10 * J0 < A0 < 11 * J0
assert 10 * R0 < Q0


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))
l3, u3 = log_bounds(Fraction(1, 2))

# Lower J0 resonance: delta_J = J0 ln2 - R0 ln3 > 0.
delta_J_lo = J0 * l2 - R0 * u3
delta_J_hi = J0 * u2 - R0 * l3
assert delta_J_lo > 0

# The fractional phase at every mJ0 checkpoint, m<=10, is positive but <1.
# In log units this is 0 < m*delta_J < ln3.
assert 10 * delta_J_hi < l3

# Upper tail: delta_U = P ln3 - U ln2 is positive but below ln3.
delta_U_lo = P * l3 - U * u2
delta_U_hi = P * u3 - U * l2
assert delta_U_lo > 0
assert delta_U_hi < l3

# Equivalently P-1 < alpha*U < P for alpha=ln2/ln3.
assert U * l2 - (P - 1) * u3 > 0
assert P * l3 - U * u2 > 0

# Full A0 lower resonance and exact phase decomposition.
delta_A_lo = A0 * l2 - Q0 * u3
delta_A_hi = A0 * u2 - Q0 * l3
assert delta_A_lo > 0

# Interval verification of delta_A = 10 delta_J - delta_U.
assert 10 * delta_J_lo - delta_U_hi <= delta_A_hi
assert 10 * delta_J_hi - delta_U_lo >= delta_A_lo
assert 10 * delta_J_lo - delta_U_hi > 0

# For any transported surplus integer s>=1:
#   pre-log  = s ln3 - 10 delta_J >0,
#   tail-log = delta_U - s ln3 <0.
# It suffices to check the weakest case s=1.
pre_log_lower_s1 = l3 - 10 * delta_J_hi
tail_log_upper_s1 = delta_U_hi - l3
assert pre_log_lower_s1 > 0
assert tail_log_upper_s1 < 0

# A simple explicit amplification lower bound at the tenth checkpoint:
# exp(pre_log)>1+pre_log, and pre_log is extremely close to ln3.
# We certify the weaker but convenient coefficient factor > 2.99 by
# showing 10*delta_J < 1/300 and using e^{-x}>1-x:
# 3 e^{-10 delta_J} > 3(1-1/300)=2.99.
assert 10 * delta_J_hi < Fraction(1, 300)

print("PASS A0 ten-J0 upper-tail surplus certificate")
print("U_P", U, P)
print("delta_J", float((delta_J_lo + delta_J_hi) / 2))
print("delta_U", float((delta_U_lo + delta_U_hi) / 2))
print("delta_A", float((delta_A_lo + delta_A_hi) / 2))
print("checkpoint_min_surplus", 1)
print("prefix_coefficient_factor_lower", 2.99)
print("terminal_tail_is_coefficient_subcritical", True)
