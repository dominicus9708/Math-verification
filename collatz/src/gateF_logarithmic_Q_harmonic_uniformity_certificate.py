#!/usr/bin/env python3
"""Algebra certificate for logarithmically growing-Q Gate F uniformity.

This checks the exponent arithmetic behind the theorem recorded in
2026-09-06-gate-F-uniformity-closed-by-harmonic-moving-strip.md.
It is NOT a Collatz proof.

Input already proved elsewhere in the repository:

  h_i = floor(i log_2 3) - A_i,
  lambda_i = 2^(-h_i-theta_i), 0<=theta_i<1,
  sum_{i<q} lambda_i <= C_N q^(1/9).

Hence

  N_q(H) := #{i<q : h_i<=H} < C_N 2^(H+1) q^(1/9).

For H_Q=floor(Q log_2(3/2)),

  Bad(q,Q) <= (Q+2) N_q(H_Q+1)
           < 4 C_N (Q+2) (3/2)^Q q^(1/9).

If Q(q)=floor(c log_2 q), the bad fraction is

  O_N((log q) q^(-8/9 + c log_2(3/2))).

It tends to zero whenever

  c < 8/(9 log_2(3/2)).
"""

import math
from fractions import Fraction

LOG2_3_OVER_2 = math.log2(3.0 / 2.0)
CSTAR = 8.0 / (9.0 * LOG2_3_OVER_2)


def exponent(c: float) -> float:
    # exponent of q in the unnormalised bad count
    return 1.0 / 9.0 + c * LOG2_3_OVER_2


def bad_fraction_power(c: float) -> float:
    # Bad/q = O(log q * q^power)
    return exponent(c) - 1.0


def main() -> None:
    assert 0.0 < LOG2_3_OVER_2 < 1.0
    assert abs(CSTAR - 1.5195655923124043) < 1e-14

    # Particularly simple admissible law.
    c1 = 1.0
    assert bad_fraction_power(c1) < 0.0
    assert abs(exponent(c1) - 0.6960736118322672) < 1e-14

    # A near-critical but still admissible law.
    c15 = 1.5
    assert c15 < CSTAR
    assert bad_fraction_power(c15) < 0.0
    assert abs(exponent(c15) - 0.9885548621928455) < 1e-14

    # Exact elementary floor inequality used in the proof:
    # 2^floor(Q log2(3/2)) <= (3/2)^Q.
    # Verify over a wide finite regression range; the theorem itself is
    # immediate from floor(x)<=x.
    for Q in range(1, 10000):
        H = math.floor(Q * LOG2_3_OVER_2)
        # Compare logarithms to avoid floating overflow.
        assert H <= Q * LOG2_3_OVER_2 + 1e-12

    print("log2_3_over_2", repr(LOG2_3_OVER_2))
    print("critical_c", repr(CSTAR))
    print("c_1_bad_fraction_power", repr(bad_fraction_power(c1)))
    print("c_1p5_bad_fraction_power", repr(bad_fraction_power(c15)))
    print("PASS")


if __name__ == "__main__":
    main()
