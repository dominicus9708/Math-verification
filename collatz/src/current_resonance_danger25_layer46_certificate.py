#!/usr/bin/env python3
"""Exact rational reduction certificate for the current isolated first-crossing resonance.

This certificate does NOT prove Collatz.  It records two finite reductions used
by the closure program:

1. the dangerous interaction dimension of the current resonance is exactly 25;
2. the mechanical-envelope start ceiling lies below the m=47 Cantor-core base,
   so only m=44,45,46 can occur above the currently verified V33 floor; moreover
   the m=46 part lies in a union of two simple selector subcubes of total size
   2^43+2^40.

No floating point is used in any assertion.
"""
from fractions import Fraction

Q = 137_528_045_312
SIGMA = 217_976_794_617
NLOG = 80


def log_bounds(x: Fraction, n: int = NLOG):
    # log((1+x)/(1-x)) = 2 sum x^(2j+1)/(2j+1)
    s = Fraction(0)
    for j in range(n + 1):
        s += Fraction(2) * x ** (2*j + 1) / (2*j + 1)
    tail = Fraction(2) * x ** (2*n + 3) / ((2*n + 3) * (1 - x*x))
    return s, s + tail


def log1p_three_power_bounds(k: int):
    t = Fraction(1, 3**k)
    x = t / (2 + t)
    return log_bounds(x)


# ln 2 and ln 3 exact rational enclosures.
L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))

EPS_LO = SIGMA * L2 - Q * U3
EPS_HI = SIGMA * U2 - Q * L3
assert EPS_LO > 0

# D = 2^sigma - 3^q = 3^q (exp(eps)-1).
# Show 3^(q-26) < D < 3^(q-25) by comparing eps with
# log(1+3^-26) and log(1+3^-25).
L26, U26 = log1p_three_power_bounds(26)
L25, U25 = log1p_three_power_bounds(25)
assert EPS_LO > U26
assert EPS_HI < L25

# Therefore ceil(log_3 D)=q-25 and h=q-ceil(log_3 D)=25.
DANGEROUS_DIMENSION = 25
assert DANGEROUS_DIMENSION == 25

# Mechanical first-crossing correction bound
#   S <= q/(6 ln2)+1/3,
# and delta=exp(eps)-1 > eps >= EPS_LO give the safe rational ceiling
#   x < S_upper/EPS_LO.
S_UPPER = Fraction(Q, 1) / (6 * L2) + Fraction(1, 3)
X_UPPER = S_UPPER / EPS_LO

V33 = 4 * (3**44 + 3**33) + 2
M47_BASE = 4 * 3**47 + 3
assert X_UPPER < M47_BASE
assert V33 < 4 * 3**44 + 3 + 4 * ((3**44 - 1)//2)

# For m=46 write N=4(3^46+S)+3.  Any candidate below X_UPPER has
# S < SELECTOR_CAP.  The safe over-family bound
#   SELECTOR_CAP < 3^43 + 3^40
# implies:
#   a_44=a_45=0;
#   if a_43=0, a_0..a_42 are unrestricted (2^43 possibilities);
#   if a_43=1, then a_40=a_41=a_42=0 and a_0..a_39 are unrestricted
#   (2^40 possibilities).
SELECTOR_CAP = (X_UPPER - 3) / 4 - 3**46
assert SELECTOR_CAP < 3**44
assert SELECTOR_CAP < 3**43 + 3**40
M46_OVERFAMILY = (1 << 43) + (1 << 40)

print("current resonance reduction certificate: PASS")
print("dangerous_dimension", DANGEROUS_DIMENSION)
print("eps_interval", float(EPS_LO), float(EPS_HI))
print("safe_start_ceiling", float(X_UPPER))
print("candidate_Cantor_layers", (44, 45, 46))
print("m46_overfamily_size", M46_OVERFAMILY)
