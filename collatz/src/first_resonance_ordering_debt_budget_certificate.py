#!/usr/bin/env python3
"""Exact ordering-debt budget certificate for the repaired first resonance.

If a terminal reconstruction ever reaches displacement D, ordering lets the
previous displacement fall by at most one at a mechanical gap-2 and not at all
at a gap-1.  Since the first odd ordinal has displacement zero, every such debt
must be fully repaid before the start boundary.

The anchored Christoffel gap word has slope P/Q, hence any h consecutive gaps
contain at most ceil(h P/Q) gap-2 symbols.  This yields an exact lower bound on
the number of positive-displacement positions needed to repay D, and therefore
on normalized correction defect.  Combining with the certified global defect
budget gives a new universal displacement cap.

No floating point is used.
"""

A = 114_208_327_604
Q = 72_057_431_991
P = A - Q
BUDGET = 4_314_000_000


def hmin(D: int) -> int:
    """Least h with ceil(h P/Q) >= D."""
    assert D >= 1
    return ((D - 1) * Q) // P + 1


def integer_cost_numerator(D: int) -> int:
    """Integer part of 12 times the debt lower bound.

    Exact bound:
      defect > (h(D)+D-2+2^(1-D))/12.
    The returned integer is h(D)+D-2.
    """
    return hmin(D) + D - 2


def main() -> None:
    # Mechanical position cap: d_j <= floor((j-1)P/Q), hence globally <= P-1.
    geometric_cap = P - 1
    assert geometric_cap == 42_150_895_612

    # Find the first D whose rigorous debt-cost lower bound is already above
    # the entire first-resonance defect budget.
    lo, hi = 1, geometric_cap
    target = 12 * BUDGET
    while lo < hi:
        mid = (lo + hi) // 2
        if integer_cost_numerator(mid) >= target:
            hi = mid
        else:
            lo = mid + 1
    first_impossible = lo

    assert first_impossible == 19_106_028_519
    assert hmin(first_impossible) == 32_661_971_485
    assert integer_cost_numerator(first_impossible) == 51_768_000_002
    assert integer_cost_numerator(first_impossible) > target

    max_displacement = first_impossible - 1
    assert max_displacement == 19_106_028_518
    assert integer_cost_numerator(max_displacement) == 51_767_999_999

    # A length-L alignment repair is one class modulo 2*3^L.
    # At L=21 this modulus already exceeds every budget-feasible displacement,
    # so a >=21-trit repair has at most one ordinary representative.
    mod20 = 2 * 3**20
    mod21 = 2 * 3**21
    assert mod20 == 6_973_568_802
    assert mod21 == 20_920_706_406
    assert mod20 < max_displacement < mod21

    print("PASS first-resonance ordering-debt budget certificate")
    print("P", P)
    print("Q", Q)
    print("geometric_displacement_cap", geometric_cap)
    print("first_budget_impossible_D", first_impossible)
    print("hmin_at_first_impossible", hmin(first_impossible))
    print("budget_feasible_displacement_max", max_displacement)
    print("2*3^20", mod20)
    print("2*3^21", mod21)
    print("alignment repairs of length >=21 have at most one ordinary d")


if __name__ == "__main__":
    main()
