#!/usr/bin/env python3
"""Numerical companion for the universal reverse-potential rarity theorem.

The theorem itself is analytic and recorded in the accompanying note.
For any reverse exponent string a_1,...,a_r with a_i>=1,
    Lambda = prod_i (3/2^{a_i}) = 3^r/2^K.
A fixed exponent string determines at most one endpoint residue mod 3^r,
so its residue fraction at any larger ternary resolution is at most 3^{-r}.

For t=3/2 the Chernoff sum per inverse step is
    A = sqrt(3)/(2*sqrt(2)-1) < 1,
and therefore the admissible-residue fraction with Lambda>3^d is at most
    (3/2) * A/(1-A) * 3^{-3d/2},
uniformly in the ternary resolution Q.

This script evaluates the constant and checks finite exact composition sums
against the analytic bound. It is a scope certificate, not a Collatz proof.
"""

from decimal import Decimal, getcontext
from fractions import Fraction
from math import comb

getcontext().prec = 80

THREE = Decimal(3)
TWO = Decimal(2)
SQRT3 = THREE.sqrt()
SQRT2 = TWO.sqrt()
A = SQRT3 / (TWO * SQRT2 - Decimal(1))
C_ADM = Decimal(3) / Decimal(2) * A / (Decimal(1) - A)


def max_K(r: int, d: int):
    """Largest K>=r with 3^r > 3^d 2^K; None if no such K."""
    if r <= d:
        return None
    lhs = 3 ** (r - d)
    K = r
    if lhs <= 2 ** K:
        return None
    while lhs > 2 ** (K + 1):
        K += 1
    return K


def exact_partial_all_residue_union_bound(d: int, R: int) -> Fraction:
    """Union bound over reverse lengths 1<=r<=R, all endpoint residues."""
    out = Fraction(0, 1)
    for r in range(1, R + 1):
        M = max_K(r, d)
        if M is None:
            continue
        out += Fraction(comb(M, r), 3 ** r)
    return out


def chernoff_admissible_bound(d: int) -> Decimal:
    return C_ADM * (THREE ** (Decimal(-3 * d) / Decimal(2)))


def main():
    assert 3 < 4
    assert A < 1

    print("A_3_over_2", A)
    print("admissible_constant", C_ADM)
    print("d admissible_fraction_upper")
    for d in (1, 2, 3, 5, 10, 20):
        print(d, chernoff_admissible_bound(d))

    for d in (1, 2, 3, 5):
        partial = exact_partial_all_residue_union_bound(d, 200)
        partial_dec = (Decimal(partial.numerator) / Decimal(partial.denominator)) * Decimal(3) / Decimal(2)
        bound = chernoff_admissible_bound(d)
        assert partial_dec < bound
        print("partial_R200", d, partial_dec, "bound", bound)

    print("PASS")


if __name__ == "__main__":
    main()
