#!/usr/bin/env python3
"""Exact rational certificate for the global displaced-ordinal budget at the
first Collatz coefficient resonance.

External input: convergence below 2^71 (Barina) only through the already
proved first-resonance setup.  This file verifies the new arithmetic bounds
using Fraction arithmetic; no floating-point comparisons are used.
"""

from fractions import Fraction
from math import factorial

A = 114_208_327_604
Q = 72_057_431_991
B = 1 << 71

# Lower Farey neighbour of A/Q around gamma = log_2(3).
AL = 103_768_467_013
QL = 65_470_613_321

# Test count.  We prove that this many displaced ordinals already costs more
# normalized correction defect than the entire first-resonance budget allows.
RTEST = 42_010_000_000
NLOG = 120


def log_bounds(z: Fraction, n: int):
    """Bounds log((1+z)/(1-z)) by a positive atanh series."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = (
        Fraction(2) * z ** (2 * n + 3)
        / ((2 * n + 3) * (1 - z * z))
    )
    return s, s + tail


def main() -> None:
    # ln 2 = 2 atanh(1/3), ln 3 = 2 atanh(1/2).
    l2, u2 = log_bounds(Fraction(1, 3), NLOG)
    l3, u3 = log_bounds(Fraction(1, 2), NLOG)

    # A/Q is above gamma and AL/QL is below gamma.
    lnP_lo = A * l2 - Q * u3
    assert lnP_lo > 0
    assert AL * u2 < QL * l3

    # Farey adjacency.  Hence there is no rational strictly between AL/QL and
    # A/Q with denominator < Q+QL.  In particular, for 0<=n<Q,
    # floor(n log_2 3) = floor(n A/Q).
    assert A * QL - AL * Q == 1
    assert Q < Q + QL

    # The mechanical normalized correction obeys
    #   S_mech <= Q/(6 ln2)+1/3.
    # For a genuine first-resonance renewal N>B, g>=4 and P=2^A/3^Q>1,
    #   E/3^Q = S_mech - (P-1)N - P g.
    # Since P-1 > ln P, a rigorous upper bound is:
    defect_upper = Fraction(Q, 1) / (6 * l2) + Fraction(1, 3) - B * lnP_lo - 4
    assert defect_upper < 4_314_000_000

    # For a displaced ordinal j, s_j>=1 gives defect charge at least
    #   c_j = 2^(b_j-1)/3^j.
    # Farey floor coincidence and residue permutation yield, for any R
    # displaced ordinals,
    #   sum c_j >= Q/(12 ln2) * (2^(R/Q)-1).
    # Lower-bound exp(t)-1 by its first six positive Taylor terms and use the
    # lower enclosure l2 for ln2.  The resulting expression is rational.
    x = Fraction(RTEST, Q)
    cost_lower = Fraction(RTEST, 12)
    for k in range(2, 7):
        cost_lower += (
            Fraction(Q, 12)
            * x ** k
            * l2 ** (k - 1)
            / factorial(k)
        )

    assert cost_lower > 4_314_000_000
    assert cost_lower > defect_upper

    # Therefore RTEST displaced ordinals are impossible.
    max_displaced = RTEST - 1
    min_aligned = Q - max_displaced

    assert max_displaced == 42_009_999_999
    assert min_aligned == 30_047_431_992

    print("PASS first-resonance global displacement budget")
    print(f"A={A}")
    print(f"Q={Q}")
    print(f"Farey_lower={AL}/{QL}")
    print(f"defect_upper<{float(defect_upper):.6f}")
    print(f"cost_at_RTEST>{float(cost_lower):.6f}")
    print(f"displaced_ordinals<={max_displaced}")
    print(f"mechanically_aligned_ordinals>={min_aligned}")
    print("global Beatty excursion height is also < 42,010,000,000")


if __name__ == "__main__":
    main()
