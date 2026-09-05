#!/usr/bin/env python3
"""Exact algebra certificate for the Gate-S harmonic good-scale reduction.

This script verifies only algebraic implications.  It does not prove that the
actual Collatz selector ratios satisfy the asymptotic good-scale hypotheses.
"""

from fractions import Fraction


def kappa_from_rho(rho: Fraction) -> Fraction:
    return Fraction(3 * rho - 1, 10)


def fixed_margin_floor(eta: Fraction) -> Fraction:
    """If rho >= 1/3 + eta, then kappa >= 3 eta / 10."""
    assert eta > 0
    return Fraction(3 * eta, 10)


def symmetric_kappa_floor(eps: Fraction) -> Fraction:
    assert 0 <= eps < Fraction(1, 2)
    return Fraction(1 - 2 * eps, 5 * (1 + eps))


def asymmetric_margin(d: Fraction, u: Fraction) -> Fraction:
    assert 0 <= d <= 1
    assert u >= 0
    return Fraction(2 - 3 * d - u, 1 + u)


def main() -> None:
    # Verify fixed-margin identity on a rational grid.
    for E in range(1, 100):
        eta = Fraction(E, 300)  # rho remains <= 2/3 on this grid
        rho = Fraction(1, 3) + eta
        assert kappa_from_rho(rho) == fixed_margin_floor(eta)

    # Verify symmetric discrepancy conversion.
    for E in range(0, 50):
        eps = Fraction(E, 100)
        rho_floor = Fraction(1 - eps, 1 + eps)
        assert kappa_from_rho(rho_floor) == symmetric_kappa_floor(eps)

    # Verify asymmetric identity:
    # 3*(1-d)/(1+u)-1 = (2-3d-u)/(1+u).
    for D in range(0, 21):
        d = Fraction(D, 20)
        for U in range(0, 21):
            u = Fraction(U, 10)
            rho_floor = Fraction(1 - d, 1 + u)
            lhs = 3 * rho_floor - 1
            rhs = asymmetric_margin(d, u)
            assert lhs == rhs

    # A finite toy block calculation demonstrates the exact bookkeeping only.
    # Each block receives harmonic good-scale mass delta=1/8, eta=1/12.
    eta = Fraction(1, 12)
    delta = Fraction(1, 8)
    per_block_log_loss_floor = fixed_margin_floor(eta) * delta
    assert per_block_log_loss_floor == Fraction(1, 320)

    print("Gate S harmonic good-scale algebra certificate: PASS")
    print("fixed-margin rise coefficient: 3*eta/10")
    print("toy block eta=1/12, delta=1/8 -> exponent contribution >= 1/320 per block")
    print()
    print("ASYMPTOTIC STATUS: OPEN")
    print("Need exact-selector proof that positive-margin good rises have divergent")
    print("harmonic weight, or an equivalent discrepancy/Fourier-tail block theorem.")


if __name__ == "__main__":
    main()
