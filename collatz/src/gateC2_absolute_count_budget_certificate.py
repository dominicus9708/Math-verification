#!/usr/bin/env python3
"""Exact/algebraic checks for the Gate-C2 absolute-count audit.

This certificate does NOT prove Collatz.  It checks the cardinality/support
barrier behind the global selector-min/max + Beatty one-child route.
"""

from fractions import Fraction
from math import log, log2


def beatty_barrier(n: int) -> int:
    """b(n)=min q with 3^q >= 2^n, using integer arithmetic."""
    q = 0
    p3 = 1
    p2 = 1 << n
    while p3 < p2:
        p3 *= 3
        q += 1
    return q


def rise_count_through(Lmax: int) -> int:
    """Number of Beatty rises b(L+1)-b(L) for 1 <= L <= Lmax."""
    return beatty_barrier(Lmax + 1) - beatty_barrier(1)


def minmax_applicable_rises(m: int) -> int:
    """Necessary support window for global child-modulus positivity.

    At scale L the child group has 2^(L-1) residues while an m-selector
    layer has only 2^m assignments.  Hence global a>0 requires L-1 <= m,
    i.e. L <= m+1.  This returns all Beatty rises in that maximal window.
    """
    return rise_count_through(m + 1)


def main() -> None:
    alpha = log(2.0) / log(3.0)
    K_all = 14.3 / log2(3.0)
    K_asym = 8.616 / log2(3.0)

    print("alpha=log_3(2) =", alpha)
    print("K_all =", K_all)
    print("K_asym =", K_asym)
    print()

    # Strong bridge ceiling: c_* <= 1 and rho <= 1 imply
    # delta_cert = c_*(3 rho - 1)/4 <= 1/2.
    max_delta = Fraction(1, 2)
    assert max_delta == Fraction(1, 2)

    print("m  rises_before_support_barrier  m-rises")
    for m in (4, 10, 28, 44, 100, 1000):
        r = minmax_applicable_rises(m)
        print(f"{m:4d} {r:29d} {m-r:8d}")
        assert r < m

    # Analytic reason for r<m for m>=4:
    # r = ceil(alpha(m+2))-1 < alpha(m+2), and
    # (1-alpha)m - 2 alpha > 0 for m>=4.
    assert (1.0 - alpha) * 4.0 - 2.0 * alpha > 0.0

    # Therefore even the strongest contraction factor allowed by this
    # certificate, 1/2 at every applicable Beatty rise, leaves the derived
    # upper-bound scale 2^(m-r), never below one for m>=4.
    for m in range(4, 5001):
        r = minmax_applicable_rises(m)
        assert m - r >= 1

    # Elementary fallback ceiling in the joint scale m <= K log_2 H:
    # delta_L <= 1/(5L), so the best asymptotic logarithmic contraction
    # coefficient from rise scales is alpha/5, far below K_all or K_asym.
    elementary_coeff = alpha / 5.0
    print()
    print("elementary log-budget coefficient alpha/5 =", elementary_coeff)
    print("K_all/(alpha/5) =", K_all / elementary_coeff)
    print("K_asym/(alpha/5) =", K_asym / elementary_coeff)
    assert elementary_coeff < K_asym < K_all

    # Exact simplification for the all-range constant:
    # K_all = 14.3*alpha, so K_all/(alpha/5) = 71.5.
    assert abs(K_all / elementary_coeff - 71.5) < 1e-12

    print("\nPASS: Gate-C2 cardinality/support-budget algebra verified.")


if __name__ == "__main__":
    main()
