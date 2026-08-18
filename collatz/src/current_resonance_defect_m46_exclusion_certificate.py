#!/usr/bin/env python3
"""Exact defect-corrected exclusion of the m=46 Cantor layer at the current resonance.

This is a finite reduction inside the current isolated first-coefficient-crossing
branch; it is not a proof of the Collatz conjecture.

Inputs already certified elsewhere in this repository:

* current resonance (q,sigma)=(137528045312,217976794617);
* overlapping-window defect theorem: every candidate in the relevant start
  range has at least R_STAR=21960410645 positive odd-position defects;
* mechanical correction envelope S* <= q/(6 ln 2)+1/3.

If d_i=floor(i log_2 3) is the mechanical odd position and an admissible word
has alpha_i=d_i-h_i, then its normalized correction term is

    2^alpha_i / 3^(i+1) = u_i 2^(-h_i),
    u_i = 2^d_i / 3^(i+1).

Because 2^d_i <= 3^i < 2^(d_i+1), one has u_i>1/6.  Hence every h_i>=1
removes strictly more than u_i/2>1/12 from the mechanical correction.  With
R_STAR positive coordinates,

    S < q/(6 ln2)+1/3 - R_STAR/12.

At a paradoxical first crossing,

    S >= x (exp(eps)-1) > x eps,
    eps=sigma ln2-q ln3>0.

Exact rational log intervals below prove that even the smallest m=46 Cantor
start makes x*eps exceed the defect-corrected correction ceiling.  Thus the
entire m=46 layer is impossible at this resonance.
"""

from fractions import Fraction

Q = 137_528_045_312
SIGMA = 217_976_794_617
R_STAR = 21_960_410_645
U_CERT = 36_797_925_187_243_805_015_225
NLOG = 80


def log_bounds(x: Fraction, n: int = NLOG):
    # log((1+x)/(1-x)) = 2 sum_{j>=0} x^(2j+1)/(2j+1).
    s = Fraction(0)
    for j in range(n + 1):
        s += Fraction(2) * x ** (2*j + 1) / (2*j + 1)
    tail = Fraction(2) * x ** (2*n + 3) / ((2*n + 3) * (1 - x*x))
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))   # ln 2
L3, U3 = log_bounds(Fraction(1, 2))   # ln 3

EPS_LO = SIGMA * L2 - Q * U3
EPS_HI = SIGMA * U2 - Q * L3
assert EPS_LO > 0

# Safe mechanical envelope and its defect-corrected version.
S_MECH_UPPER = Fraction(Q, 1) / (6 * L2) + Fraction(1, 3)
S_DEFECT_UPPER = S_MECH_UPPER - Fraction(R_STAR, 12)
assert S_DEFECT_UPPER > 0

# The defect theorem was proved on N<U_CERT.  The uncorrected mechanical
# envelope already places every current-resonance candidate inside that range.
X_UNCORRECTED_UPPER = S_MECH_UPPER / EPS_LO
assert X_UNCORRECTED_UPPER < U_CERT

# Least possible m=46 recursively-sufficient Cantor start.
M46_MIN = 4 * 3**46 + 3

# Since exp(eps)-1 > eps >= EPS_LO, a paradoxical m=46 start would require
# S > M46_MIN*EPS_LO.  This is already larger than the defect-corrected ceiling.
MARGIN = M46_MIN * EPS_LO - S_DEFECT_UPPER
assert MARGIN > 0

# m=45 is intentionally NOT claimed: the same argument does not close it.
M45_MIN = 4 * 3**45 + 3
assert M45_MIN * EPS_LO < S_DEFECT_UPPER

print("current-resonance defect m46 exclusion: PASS")
print("defect_lower_bound", R_STAR)
print("defect_fraction_lower_bound", float(Fraction(R_STAR, Q)))
print("mechanical_correction_upper", float(S_MECH_UPPER))
print("defect_correction_upper", float(S_DEFECT_UPPER))
print("defect_to_mechanical_ratio", float(S_DEFECT_UPPER / S_MECH_UPPER))
print("m46_required_eps_correction", float(M46_MIN * EPS_LO))
print("positive_exact_margin", float(MARGIN))
print("remaining_current_resonance_layers", (44, 45))
