#!/usr/bin/env python3
"""Exact algebra for the Gate A tail-budget -> atom-floor closure theorem.

This is a conditional theorem certificate, not a Collatz proof.  It verifies the
universal block majorant

    lambda = rho + (9/4-rho)*tau

and the exact m=22, block 32->37 finite diagnostic quoted in the companion note.
"""

from fractions import Fraction

G = Fraction(9, 4)


def threshold(rho: Fraction) -> Fraction:
    assert 0 <= rho < 1
    return (1 - rho) / (G - rho)


def main():
    # Exact worst low-surplus stratum ratio in the m=22, 32->37 diagnostic
    # when D=8 (low region d=0,...,7).
    rho = Fraction(800339, 879282)

    # Exact weighted input tail fraction from d>=8 in the same finite block.
    tau = Fraction(203391, 160192007)

    tau_star = threshold(rho)
    lam = rho + (G - rho) * tau

    print("G", f"{G.numerator}/{G.denominator}", float(G))
    print("rho", f"{rho.numerator}/{rho.denominator}", float(rho))
    print("tail_fraction_tau", f"{tau.numerator}/{tau.denominator}", float(tau))
    print("allowable_tail_threshold", f"{tau_star.numerator}/{tau_star.denominator}", float(tau_star))
    print("tail_slack_factor", float(tau_star / tau))
    print("crude_tail_budget_lambda", f"{lam.numerator}/{lam.denominator}", float(lam))

    assert tau < tau_star
    assert lam < 1

    # Actual exact aggregate ratio from the full histogram is even better.
    actual = Fraction(7819656391, 8650368378)
    print("actual_aggregate_ratio", f"{actual.numerator}/{actual.denominator}", float(actual))
    assert actual < lam < 1

    print("PASS")


if __name__ == "__main__":
    main()
