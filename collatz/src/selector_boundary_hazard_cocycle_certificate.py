#!/usr/bin/env python3
"""Exact algebra/regression certificate for the Stage-4 boundary-hazard cocycle.

At a Beatty rise, let
  C  = selector mass in coefficient-surviving parents,
  D  = selector mass in one-child boundary parents,
  K  = oriented sibling-correlation repair,
  Uc = unweighted number of coefficient-surviving parents,
  B  = unweighted number of one-child boundary parents.

Then
    2 Cnext = 2 C - D + K,
    Uc_next = 2 Uc - B.

For normalized overlap
    Xi_L = (C/2^m)/(Uc/2^(L-2)),
this gives the exact rise cocycle

    Xi_(L+1)/Xi_L
      = [1-(D-K)/(2C)] / [1-B/(2Uc)].

Plateau steps have D=K=B=0 in this representation and leave Xi unchanged.

This file checks the algebra and selected exact m=44 checkpoints already
certified by m44_full_mass_transport_certificate.cpp.
"""

from fractions import Fraction
from math import log2

# L, selector C, selector D, exact K, unweighted Uc, unweighted B,
# expected child selector mass when separately available in the existing table.
ROWS = [
    (14, 3152505354815, 743029190277, -14271, 734, 173, 2780990752541),
    (17, 2269889787451, 515932831671, 271723, 4228, 961, 2011923507477),
    (19, 2011923507477, 355945413895, 209309, 14990, 2652, 1833950905184),
    (20, 1833950905184, 539891337183, -207085, 27328, 8045, 1564005133050),
    (22, 1564005133050, 295899305006, 45056, 93222, 17637, 1416055503075),
]


def main() -> None:
    for L, C, D, K, Uc, B, expected_next in ROWS:
        assert (2 * C - D + K) % 2 == 0
        Cnext = (2 * C - D + K) // 2
        assert Cnext == expected_next

        Uc_next = 2 * Uc - B
        assert Uc_next > 0

        # Direct overlap ratio after cancelling the fixed 2^m selector mass.
        direct = Fraction(Cnext, Uc_next) / Fraction(C, Uc) * 2
        # Hazard form.
        hazard = (
            Fraction(1, 1) - Fraction(D - K, 2 * C)
        ) / (
            Fraction(1, 1) - Fraction(B, 2 * Uc)
        )
        assert direct == hazard

        effective_ratio = Fraction(D - K, C) / Fraction(B, Uc)
        log_increment = log2(float(hazard))

        print(
            "L", L,
            "effective_hazard_ratio", float(effective_ratio),
            "log2_Xi_increment", log_increment,
        )

    print("selector-boundary hazard cocycle: PASS")


if __name__ == "__main__":
    main()
