#!/usr/bin/env python3
"""Exact rigidity for the E=13 G13 entrance band and a 4096-separated pair.

Let X lie in the exact current-R1 E=13 entrance band.  This certificate proves:

1. any current numerical-window preimage of X, or of X-4096, over the 1539
   pre-G13 accelerated steps must have exactly E=13 even events;
2. if both X and X-4096 have current m=44-core preimages N,N', then
   |N-N'|<115;
3. consequently N and N' have identical ternary selectors a_i for every i>=5,
   so the pair can differ only inside the 32-state low-five-trit fibre.

The first statement follows from the factor-of-three separation between the
fixed-E normalized root coordinates.  E<=12 is already below the current
numerical floor; E>=14 is already above the current numerical ceiling even
after the maximal formation correction.

The second uses the strengthened E=13 run-feasibility theorem epsilon_13<114
and the fact that changing X by 4096 changes the normalized root coordinate by
less than one.

The third is a balanced-ternary separation argument.  If the highest differing
selector index were m>=5, then

    |N-N'| >= 4 * (3^m - sum_{i<m}3^i)
             = 2 * (3^m + 1)
             >= 488,

contradicting |N-N'|<115.

This is a conditional pair-attachment rigidity theorem.  It does not assert
that the alternate G13 entrance must have a current-core preimage, and it does
not prove Collatz.
"""

from fractions import Fraction

T = 1539
SHIFT = 4096

N0 = 3_939_105_844_976_711_153_619
NMAX = 5_908_625_413_101_667_397_287


def eps_prefix_bound(E: int) -> Fraction:
    """Sharp bound from the mandatory first two odd accelerated bits."""
    return Fraction(4 * (2**E - 1), 9)


def Y(X: int, E: int) -> Fraction:
    return Fraction((1 << T) * (X + 1), 3 ** (T - E))


def current_e13_band() -> tuple[int, int]:
    scale = Fraction(3**1526, 1 << 1539)
    lower_z = scale * (N0 + 1)
    upper_z = scale * (Fraction(NMAX + 1) + eps_prefix_bound(13))

    # X+1 is strictly above lower_z and at most below the upper formation edge.
    xmin = lower_z.numerator // lower_z.denominator
    xmax = upper_z.numerator // upper_z.denominator - 1
    return xmin, xmax


def main() -> None:
    xmin, xmax = current_e13_band()
    assert xmin.bit_length() == xmax.bit_length() == 952

    # Allow the alternate G13 entrance X-4096 as well.
    pair_lo = xmin - SHIFT
    pair_hi = xmax

    # Every E<=12 root lies below the current numerical window.  E=12 is the
    # largest such normalized coordinate, and epsilon only decreases the root.
    assert Y(pair_hi, 12) - 1 < N0

    # Every E>=14 root lies above the current numerical window.  Check the
    # smallest boundary case E=14 at the smallest pair entrance.
    lower14 = Y(pair_lo, 14) - 1 - eps_prefix_bound(14)
    assert lower14 > NMAX

    # The lower root bound increases thereafter.  Since Y_{E+1}=3Y_E and
    # epsmax(E+1)-epsmax(E)=(4/9)2^E, it is enough that the increment is
    # positive at E=14; its Y/2^E ratio then grows by 3/2 each step.
    assert 2 * Y(pair_lo, 14) > Fraction(4 * 2**14, 9)

    # Hence a current-window preimage for either member of the 4096-separated
    # entrance pair is rigidly forced into E=13.

    # Strengthened run-feasibility theorem from the companion certificate:
    # every current-core E=13 attachment has epsilon<114.
    EPS_STRONG = Fraction(114, 1)

    # Normalized root-coordinate displacement caused by X -> X-4096.
    dx = Fraction(SHIFT * (1 << 1539), 3**1526)
    assert 0 < dx < 1

    # If both pair entrances have current-core E=13 roots,
    #   N-N' = dx - epsilon + epsilon',
    # with 0<epsilon,epsilon'<114.  Therefore |N-N'|<115.
    pair_root_gap_cap = 115
    assert dx + EPS_STRONG < pair_root_gap_cap

    # m=44 starts have form
    #   N=4(3^44 + sum a_i 3^i)+3.
    # If the highest differing selector is m, the smallest possible absolute
    # difference is obtained by opposing every lower digit:
    #   4(3^m - sum_{i<m}3^i) = 2(3^m+1).
    min_gap_if_highest_diff_5 = 2 * (3**5 + 1)
    assert min_gap_if_highest_diff_5 == 488
    assert min_gap_if_highest_diff_5 > pair_root_gap_cap

    print("R1 E=13 gate-pair rigidity: PASS")
    print("E<=12 attachments: below current numerical floor")
    print("E>=14 attachments: above current numerical ceiling")
    print("therefore X and X-4096 current-window preimages, if any, both have E=13")
    print("4096 entrance displacement changes normalized root coordinate by <1")
    print("two current-core E=13 roots for the pair satisfy |N-N'|<115")
    print("selectors a_5..a_43 must therefore be identical")
    print("only the 32-state low-five-trit fibre can differ")


if __name__ == "__main__":
    main()
