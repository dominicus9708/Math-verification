#!/usr/bin/env python3
"""Regression checks for the finite-depth Hensel-prefix relaxation hierarchy.

IMPORTANT
---------
This file tests the abstract finite-horizon theorem on finite toy operators.
It is NOT a proof of a Collatz global statement and it does NOT settle the
operator-domain question for u_i(d)=2^(e_i-d) in the main construction.

The toy operator below explicitly restricts d <= e so that u_i(d) is an
ordinary integer.  That restriction belongs to the regression model only;
it must not be imported into the main proof without an independent domain
argument.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product


INF = None  # None represents +infinity / empty feasible set.


def geq_extended(a, b):
    """Return a >= b in Q union {+infinity}, with None = +infinity."""
    if b is None:
        return a is None
    if a is None:
        return True
    return a >= b


def local_cost(weight: Fraction, d: int) -> Fraction:
    """Toy instance of kappa_i(d)=2 w_i (1-2^{-d})."""
    return 2 * weight * (1 - Fraction(1, 2**d))


def exact_actions(K: int, p: int, g: int, e: int):
    """Toy exact actions.

    The explicit d<=e bound is intentionally local to this regression.
    """
    lower = max(0, p - g + 1)
    out = []
    for d in range(lower, e + 1):
        u = 2 ** (e - d)
        if (K + u) % 3 == 0:
            out.append((d, (K + u) // 3))
    return out


def relaxed_actions(p: int, g: int, e: int):
    """Ordering-only toy actions over the same finite regression domain."""
    lower = max(0, p - g + 1)
    return range(lower, e + 1)


def min_or_inf(values):
    finite = [v for v in values if v is not None]
    return min(finite) if finite else None


def hierarchy_cost(K, p, gaps, exponents, weights, h, terminal=None):
    """Compute B^[h] for the finite toy model.

    Steps i<h enforce the exact toy Hensel transition.  Steps i>=h retain
    only ordering.  When terminal is None, the terminal carry is free.
    """
    n = len(gaps)
    assert 0 <= h <= n

    @lru_cache(None)
    def rec(i, Kcur, pcur):
        if i == n:
            if terminal is None or Kcur == terminal:
                return Fraction(0)
            return None

        values = []
        if i < h:
            for d, Knew in exact_actions(Kcur, pcur, gaps[i], exponents[i]):
                tail = rec(i + 1, Knew, d)
                if tail is not None:
                    values.append(local_cost(weights[i], d) + tail)
        else:
            # Carry has been forgotten after exact depth h.
            for d in relaxed_actions(pcur, gaps[i], exponents[i]):
                tail = rec(i + 1, Kcur, d)
                if tail is not None:
                    values.append(local_cost(weights[i], d) + tail)

        return min_or_inf(values)

    return rec(0, K, p)


def run_monotonicity_and_residue_regression():
    cases = 0

    for n in range(1, 5):
        for gaps in product((1, 2), repeat=n):
            for exponents in product(range(1, 4), repeat=n):
                weights = tuple(Fraction(i + 1, 11) for i in range(n))

                for p in range(4):
                    for K in range(1, 15):
                        vals = [
                            hierarchy_cost(
                                K, p, gaps, exponents, weights, h
                            )
                            for h in range(n + 1)
                        ]

                        # Feasible-set nesting: B^[h+1] >= B^[h].
                        for h in range(n):
                            assert geq_extended(vals[h + 1], vals[h]), (
                                "monotonicity",
                                gaps,
                                exponents,
                                p,
                                K,
                                h,
                                vals,
                            )

                        # Full depth is the exact/free-terminal toy minimum.
                        assert vals[n] == hierarchy_cost(
                            K, p, gaps, exponents, weights, n
                        )

                        # Exact finite-horizon residue invariance.
                        for h in range(n + 1):
                            shifted = K + 3**h
                            assert hierarchy_cost(
                                shifted,
                                p,
                                gaps,
                                exponents,
                                weights,
                                h,
                            ) == vals[h], (
                                "finite residue invariance",
                                gaps,
                                exponents,
                                p,
                                K,
                                h,
                            )

                        cases += 1

    return cases


def run_terminal_regression():
    samples = [
        ((1, 1), (1, 1), 0, 1),
        ((2, 1, 2), (2, 2, 2), 1, 2),
        ((1, 2), (3, 2), 2, 5),
    ]
    checks = 0

    for gaps, exponents, p, K in samples:
        n = len(gaps)
        weights = tuple(Fraction(i + 1, 13) for i in range(n))
        free = hierarchy_cost(K, p, gaps, exponents, weights, n)

        for terminal in range(10):
            fixed = hierarchy_cost(
                K,
                p,
                gaps,
                exponents,
                weights,
                n,
                terminal=terminal,
            )
            assert geq_extended(fixed, free), (
                "terminal lower bound",
                gaps,
                exponents,
                p,
                K,
                terminal,
                free,
                fixed,
            )
            checks += 1

    return checks


def run_global_quotient_counterexample():
    """Show that mod 3^h exactness does not persist automatically to h+1."""
    gaps = (1, 1)
    exponents = (1, 1)
    weights = (Fraction(1, 7), Fraction(2, 7))
    p = 0
    h = 1

    K1 = 1
    K2 = 4
    assert K1 % 3 == K2 % 3

    # Same depth-1 relaxed value: K mod 3 is sufficient for depth 1.
    assert hierarchy_cost(K1, p, gaps, exponents, weights, h) == 0
    assert hierarchy_cost(K2, p, gaps, exponents, weights, h) == 0

    # One extra exact step sees the carry difference.
    assert hierarchy_cost(K1, p, gaps, exponents, weights, h + 1) == 0
    assert hierarchy_cost(K2, p, gaps, exponents, weights, h + 1) == Fraction(2, 7)


if __name__ == "__main__":
    cases = run_monotonicity_and_residue_regression()
    terminal_checks = run_terminal_regression()
    run_global_quotient_counterexample()

    print("PASS")
    print(f"monotonicity/residue cases: {cases}")
    print(f"prescribed-terminal checks: {terminal_checks}")
    print("finite-h residue split counterexample: PASS")
