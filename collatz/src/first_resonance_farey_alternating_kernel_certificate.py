#!/usr/bin/env python3
"""Exact certificate for the first-resonance Farey alternating-kernel reduction.

The result rewrites the mechanical sign/weight system in the rational Farey
coordinate r=nA mod Q and proves that replacing the true irrational weights by
the ideal geometric grid changes every signed correlation by < 1.

This does not prove the Collatz conjecture.  It isolates the remaining
first-resonance problem as a correlation estimate for the Hensel sign sequence.
"""

from fractions import Fraction

A = 114_208_327_604
Q = 72_057_431_991
AL = 103_768_467_013
QL = 65_470_613_321
OMIT = 46
NLOG = 120


def log_bounds(z: Fraction, n: int):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2*k + 1) / (2*k + 1)
    tail = Fraction(2) * z ** (2*n + 3) / ((2*n + 3) * (1-z*z))
    return s, s + tail


def main() -> None:
    l2,u2 = log_bounds(Fraction(1,3),NLOG)
    l3,u3 = log_bounds(Fraction(1,2),NLOG)

    # Farey trapping of gamma=log_2(3).
    assert AL*u2 < QL*l3
    assert A*l2 > Q*u3
    assert A*QL - AL*Q == 1

    # A is even, Q odd, and QL is the inverse of A modulo Q.
    assert A % 2 == 0 and Q % 2 == 1
    assert (A*QL) % Q == 1

    # For n<Q the Farey neighbours force
    # floor(n log_2 3)=floor(nA/Q).  If r=nA mod Q and b=floor(nA/Q),
    # parity follows algebraically from nA=Qb+r:
    #     b == r (mod 2).
    # Thus the mechanical sign becomes (-1)^r.

    # Let Delta=A/Q-log_2(3).  Adjacency and the lower neighbour give
    # 0<Delta<1/(Q*QL).  Hence for n<Q:
    #   true_weight / ideal_weight = 2^(n Delta) < 2^(1/QL).
    # Bound exp(x)-1 by x/(1-x), x=ln2/QL, with exact rational ln2 upper bound.
    x = u2 / QL
    assert 0 < x < 1
    distortion_factor_minus_1 = x / (1-x)

    # Every ideal weight is <=1/6, so even over the full Q-grid the total
    # absolute signed-correlation perturbation is < this value.
    distortion_total = Fraction(Q,6) * distortion_factor_minus_1
    assert distortion_total < 1

    # Omitting the final 46 zero-target-unavailable terms changes any ideal
    # signed sum by at most 46/6.  This is recorded separately from the
    # irrational-to-rational distortion.
    omitted_mass = Fraction(OMIT,6)

    # Full ideal mechanical signed kernel:
    # x0=2^(-1/Q), Q odd, x0^Q=1/2,
    # (1/6) sum_{r=0}^{Q-1} (-x0)^r = 1/[4(1+x0)].
    # Hence it lies strictly between 1/8 and 1/4.
    # The identity is symbolic; the certificate records its algebraic inputs.
    assert Q % 2 == 1

    # Correlation target handoff.  Previous exact threshold needs actual
    # weighted Hensel/mechanical correlation <= 35,000,000 (a slightly stronger
    # round target than the exact >35M survival requirement).  Since the
    # rational-grid replacement costs <1, it suffices to prove the ideal-grid
    # correlation <= 34,999,999.
    TARGET_ACTUAL = 35_000_000
    TARGET_IDEAL = 34_999_999
    assert TARGET_IDEAL + distortion_total < TARGET_ACTUAL

    print("PASS first-resonance Farey alternating-kernel certificate")
    print("A_inverse_mod_Q",QL)
    print("irrational_to_ideal_total_error_lt",float(distortion_total))
    print("omitted_46_mass_le",float(omitted_mass))
    print("ideal_signed_kernel_symbolic = 1/[4(1+2^(-1/Q))]")
    print("sufficient_ideal_correlation_target",TARGET_IDEAL)


if __name__ == "__main__":
    main()
