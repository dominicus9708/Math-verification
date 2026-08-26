#!/usr/bin/env python3
"""Exact arithmetic certificate for the first-resonance dyadic-shell theorem.

The proof note uses Farey adjacency to show that for every proper odd prefix
1<=j<Q, the cumulative mechanical time A_j obeys

    A_j = floor(j log_2 3)
    j log_2(3+1/B) < A_j+1,

with B=2^71.  Combined with the scaled-state block product this yields

    N < z_j < 2N,

so the left displacement d_j is exactly the dyadic height shell of the actual
odd state x_j relative to N.

This script certifies the exact Farey neighbours and logarithmic ordering and
runs finite regressions of the floor/ceiling statements.  The all-j step is the
Farey-neighbour lemma proved in the companion note.
"""

from fractions import Fraction

B = 1 << 71
A = 114_208_327_604
Q = 72_057_431_991

# Lower time/odd Farey neighbour U and upper time/odd Farey neighbour S.
A_U = 103_768_467_013
Q_U = 65_470_613_321
A_S = 10_439_860_591
Q_S = 6_586_818_670

NLOG = 120


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / (
        (2 * n + 3) * (1 - z * z)
    )
    return s, s + tail


def main() -> None:
    # Farey adjacency on both sides of the root time/odd ratio A/Q.
    assert A * Q_U - A_U * Q == 1
    assert A_S * Q - A * Q_S == 1

    l2, u2 = log_bounds(Fraction(1, 3))
    l3, u3 = log_bounds(Fraction(1, 2))

    # gamma=log_2 3 lies strictly between U and the root.
    # A_U/Q_U < gamma < A/Q.
    assert A_U * u2 < Q_U * l3
    assert Q * u3 < A * l2

    # gamma_B=log_2(3+1/B) lies strictly between root and S.
    X = Fraction(3 * B + 1, B)
    zz = (X - 1) / (X + 1)
    lA, uA = log_bounds(zz)
    # A/Q < gamma_B < A_S/Q_S.
    assert A * u2 < Q * lA
    assert Q_S * uA < A_S * l2

    # Root children sum back to root.
    assert A_U + A_S == A
    assert Q_U + Q_S == Q

    # Finite exact regressions of the two universal statements.
    # The proof for all 1<=j<Q is Farey adjacency, not this loop.
    for j in range(1, 100_001):
        Aj = (j * A) // Q

        # floor(j gamma)=floor(j A/Q), certified by log intervals here.
        flo_lo = (j * l3 / u2).numerator // (j * l3 / u2).denominator
        flo_hi = (j * u3 / l2).numerator // (j * u3 / l2).denominator
        assert flo_lo == flo_hi == Aj

        # j gamma_B < Aj+1.
        assert j * uA < (Aj + 1) * l2

    print("PASS first-resonance scaled dyadic shell certificate")
    print("lower_Farey_neighbor", A_U, Q_U)
    print("root", A, Q)
    print("upper_Farey_neighbor", A_S, Q_S)
    print("universal theorem: N < z_j < 2N for 1<=j<Q")
    print("therefore d_j=floor(log2(x_j/N)) exactly")


if __name__ == "__main__":
    main()
