#!/usr/bin/env python3
"""Exact algebra certificate for the selector-discrepancy version of Gate S.

This file does NOT certify an asymptotic Fourier bound.  It verifies the exact
algebra that converts selector min/max (or a uniform relative discrepancy bound)
into the Beatty one-child contraction coefficient used by the cumulative bridge.

Notation:
  hbar > 0                    selector mean
  h_min >= (1-d) hbar         lower one-sided discrepancy
  h_max <= (1+u) hbar         upper one-sided discrepancy
  rho = h_min / h_max

Then
  rho >= (1-d)/(1+u)
and the previous Beatty+repair bridge gives a rise-step loss coefficient
  kappa = (3 rho - 1)/10.
Therefore
  kappa >= (2 - 3d - u) / (10(1+u)).
The condition 3d+u<2 is sufficient for positive contraction.

Under the symmetric bound d,u <= eps,
  kappa >= (1-2 eps)/(5(1+eps)),
so eps<1/2 is sufficient.
"""

from fractions import Fraction

STATS = {
    "H24_full": (4_188_525, 4_199_983),
    "H25_full": (2_092_917, 2_102_038),
    "H24_Q7_high": (32_039, 33_523),
    "H24_Q8_high": (15_871, 16_878),
    "H24_Q9_high": (7_826, 8_584),
    "H25_Q7_high": (15_828, 16_923),
}


def asymmetric_floor(d: Fraction, u: Fraction) -> Fraction:
    assert 0 <= d <= 1
    assert u >= 0
    return Fraction(2 - 3 * d - u, 10 * (1 + u))


def symmetric_floor(eps: Fraction) -> Fraction:
    assert 0 <= eps < 1
    return Fraction(1 - 2 * eps, 5 * (1 + eps))


def main() -> None:
    # Exact symbolic spot checks over a rational grid.
    for D in range(0, 20):
        d = Fraction(D, 20)
        for U in range(0, 21):
            u = Fraction(U, 10)
            rho_floor = Fraction(1 - d, 1 + u)
            kappa_from_rho = Fraction(3 * rho_floor - 1, 10)
            assert kappa_from_rho == asymmetric_floor(d, u)
            assert (kappa_from_rho > 0) == (3 * d + u < 2)

    for E in range(0, 20):
        eps = Fraction(E, 40)  # eps < 1/2 on this grid
        rho_floor = Fraction(1 - eps, 1 + eps)
        kappa_from_rho = Fraction(3 * rho_floor - 1, 10)
        assert kappa_from_rho == symmetric_floor(eps)
        assert kappa_from_rho > 0

    print("Gate S discrepancy algebra: PASS")
    print("asymmetric positivity condition: 3*d + u < 2")
    print("symmetric sufficient condition: eps < 1/2")
    print()

    # Existing finite min/max ratios.  eps_proxy is the symmetric spread proxy
    # that reproduces the same rho exactly:
    #   eps_proxy=(B-a)/(B+a), rho=(1-eps_proxy)/(1+eps_proxy).
    # It is NOT asserted to be the actual discrepancy from the true mean.
    for name, (a, B) in STATS.items():
        assert 0 < a <= B
        rho = Fraction(a, B)
        eps_proxy = Fraction(B - a, B + a)
        reconstructed_rho = Fraction(1 - eps_proxy, 1 + eps_proxy)
        assert reconstructed_rho == rho

        kappa = Fraction(3 * rho - 1, 10)
        kappa_from_proxy = symmetric_floor(eps_proxy)
        assert kappa == kappa_from_proxy

        print(name)
        print("  rho", float(rho))
        print("  symmetric_spread_proxy", float(eps_proxy))
        print("  kappa", float(kappa))

    print()
    print("ASYMPTOTIC STATUS: OPEN")
    print("Need a growing-scale exact-fibre theorem implying harmonic accumulation")
    print("of positive Gate-S discrepancy margins; finite ratios do not prove it.")


if __name__ == "__main__":
    main()
