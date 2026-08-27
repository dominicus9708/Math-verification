#!/usr/bin/env python3
"""Regression for the abstract greedy Hensel address / mismatch-tax theorem.

This test intentionally uses integer-valued toy transition functions

    u_i(d) = 2^(d + offset_i)

rather than the stored Collatz-specialized expression `2^(e_i-d)`.
Therefore it does not assume or repair the still-open admissible-domain
question for the main operator.

The symbolic theorem is proved in the companion note; finite enumeration here
is regression only.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product


INF = None  # None denotes an empty feasible set / +infinity.


def greedy_controls(p, gaps):
    out = []
    cur = p
    for g in gaps:
        cur = max(0, cur - g + 1)
        out.append(cur)
    return tuple(out)


def local_cost(weight, d):
    return 2 * weight * (1 - Fraction(1, 2**d))


def toy_u(i, d, offsets):
    return 2 ** (d + offsets[i])


def ordering_cost(p, gaps, weights):
    L = greedy_controls(p, gaps)
    return sum(local_cost(weights[i], L[i]) for i in range(len(gaps)))


def theta(p, gaps, offsets, h):
    L = greedy_controls(p, gaps)
    total = sum(
        (3**i) * toy_u(i, L[i], offsets)
        for i in range(h)
    )
    return (-total) % (3**h)


def first_greedy_failure(p, gaps, offsets, K, h):
    """Return the first level r (1-based) where greedy prefix divisibility fails."""
    L = greedy_controls(p, gaps)
    total = K
    for r in range(1, h + 1):
        total += (3 ** (r - 1)) * toy_u(r - 1, L[r - 1], offsets)
        if total % (3**r) != 0:
            return r
    return None


def exact_free_terminal_cost(p, gaps, offsets, weights, K, dmax):
    """Exact finite toy Hensel cost over a finite declared action domain."""
    n = len(gaps)

    @lru_cache(None)
    def rec(i, Kcur, pcur):
        if i == n:
            return Fraction(0)

        lower = max(0, pcur - gaps[i] + 1)
        vals = []
        for d in range(lower, dmax + 1):
            u = toy_u(i, d, offsets)
            if (Kcur + u) % 3 != 0:
                continue
            tail = rec(i + 1, (Kcur + u) // 3, d)
            if tail is not None:
                vals.append(local_cost(weights[i], d) + tail)

        return min(vals) if vals else None

    return rec(0, K, p)


def check_case(p, gaps, offsets, weights, dmax):
    h = len(gaps)
    L = greedy_controls(p, gaps)
    B = ordering_cost(p, gaps, weights)
    th = theta(p, gaps, offsets, h)

    # Nested cylinders: theta_h reduces to theta_r for every r<h.
    for r in range(1, h):
        assert th % (3**r) == theta(p, gaps, offsets, r)

    checks = 0
    for K in range(3**h):
        exact = exact_free_terminal_cost(
            p, gaps, offsets, weights, K, dmax
        )

        # Exact equality with ordering optimum iff K is the unique theta class.
        assert (exact == B) == (K == th), (
            "zero-penalty address failure",
            p,
            gaps,
            offsets,
            K,
            th,
            B,
            exact,
        )

        r = first_greedy_failure(p, gaps, offsets, K, h)
        if r is not None and exact is not None:
            delta = min(
                weights[k] * Fraction(1, 2 ** L[k])
                for k in range(r)
            )
            assert exact - B >= delta, (
                "mismatch-tax failure",
                p,
                gaps,
                offsets,
                K,
                r,
                L,
                exact - B,
                delta,
            )

        checks += 1

    return checks


def main():
    total = 0
    dmax = 8

    for h in range(1, 5):
        for gaps in product((1, 2), repeat=h):
            for offsets in product(range(2), repeat=h):
                weights = tuple(Fraction(i + 2, 17) for i in range(h))
                for p in range(4):
                    assert max(greedy_controls(p, gaps), default=0) <= dmax
                    total += check_case(
                        p, gaps, offsets, weights, dmax
                    )

    assert total == 90480
    print("PASS")
    print(f"checked state/residue cases: {total}")
    print("unique zero-penalty address: PASS")
    print("first-mismatch minimum tax: PASS")
    print("nested 3-adic cylinders: PASS")


if __name__ == "__main__":
    main()
