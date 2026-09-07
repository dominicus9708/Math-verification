#!/usr/bin/env python3
"""MATH-012: DSD complete descriptor for the root-Hensel arithmetic-credit gate.

Scope
-----
This certificate audits and accelerates only the arithmetic credit condition
used by the existing root-Hensel branch at the frozen theorem-facing floor
B_pub = 2^71.

It does NOT prove that a Collatz candidate with failed credit is impossible.
It only says that this particular arbitrary-competitor Hensel credit cannot be
legally claimed there.

Legacy exact inequality
-----------------------
    2^(k-q) * (1 - (2/3)^q) < 2^71.

For q >= 2 this is exactly equivalent to
    k - q <= 71.

Proof:
- If d=k-q <= 71, then 0 < 1-(2/3)^q < 1, so credit < 2^d <= 2^71.
- If d>=72 and q>=2, then 1-(2/3)^q >= 1-4/9 = 5/9 > 1/2,
  so credit > 2^(d-1) >= 2^71.

Thus d=k-q, the number of even shortcut steps in a length-k parity prefix,
is a complete descriptor for this arithmetic-credit predicate.
"""

from collections import defaultdict
from time import perf_counter

B_EXP = 71
REGRESSION_MAX_K = 512


def min_q_survival(k: int) -> int:
    """Smallest q with 3^q >= 2^k."""
    q = 0
    p3 = 1
    target = 1 << k
    while p3 < target:
        p3 *= 3
        q += 1
    return q


def legacy_credit_safe(k: int, q: int) -> bool:
    """Exact integer form of 2^(k-q)*(1-(2/3)^q) < 2^71."""
    if q < 1:
        raise ValueError("q must be positive")
    a = 3**q - 2**q
    b = 3**q
    if k >= q:
        return (1 << (k - q)) * a < (1 << B_EXP) * b
    return a < (1 << B_EXP) * b * (1 << (q - k))


def even_budget_descriptor(k: int, q: int) -> int:
    """Complete descriptor d=k-q for the credit predicate."""
    return k - q


def descriptor_credit_safe(k: int, q: int) -> bool:
    if q < 2:
        # The exact d<=71 equivalence proved here is intentionally scoped q>=2.
        return legacy_credit_safe(k, q)
    return even_budget_descriptor(k, q) <= B_EXP


def combined_required_q(k: int) -> int:
    """q threshold satisfying both coefficient survival and Hensel credit."""
    return max(min_q_survival(k), k - B_EXP)


def exhaustive_regression(max_k: int = REGRESSION_MAX_K):
    checked = 0
    for k in range(2, max_k + 1):
        for q in range(2, k + 1):
            checked += 1
            lhs = legacy_credit_safe(k, q)
            rhs = descriptor_credit_safe(k, q)
            assert lhs == rhs, (k, q, lhs, rhs)
    return checked


def first_uniform_tightening(search_max: int = 512):
    """First k where coefficient-safe q_min(k) is not Hensel-credit safe."""
    for k in range(2, search_max + 1):
        q0 = min_q_survival(k)
        if not descriptor_credit_safe(k, q0):
            return k, q0, combined_required_q(k)
    return None


def threshold_table(lo: int = 188, hi: int = 205):
    rows = []
    for k in range(lo, hi + 1):
        qc = min_q_survival(k)
        qh = k - B_EXP
        qstar = max(qc, qh)
        rows.append((k, qc, qh, qstar, qh - qc))
    return rows


def count_prefix_words(K: int, require_hensel_credit: bool):
    """Count symbolic parity words obeying every prefix coefficient boundary.

    If require_hensel_credit is True, also require k-q<=71 at every prefix.
    These are exact symbolic prefix counts for the two inequalities only.
    They are NOT counts of minimal counterexamples or proof that rejected words
    cannot occur as Collatz trajectories.
    """
    # State is e = number of even bits.  q=j-e.
    dp = {0: 1}
    for j in range(1, K + 1):
        coeff_even_cap = j - min_q_survival(j)
        cap = min(coeff_even_cap, B_EXP) if require_hensel_credit else coeff_even_cap
        nxt = defaultdict(int)
        for e, count in dp.items():
            # odd next bit: e unchanged
            if e <= cap:
                nxt[e] += count
            # even next bit: e increases by one
            if e + 1 <= cap:
                nxt[e + 1] += count
        dp = dict(nxt)
    return sum(dp.values())


def benchmark(max_k: int = REGRESSION_MAX_K):
    """Session-local diagnostic only; not a theorem-facing speed claim."""
    states = [(k, q) for k in range(2, max_k + 1) for q in range(2, k + 1)]

    t0 = perf_counter()
    legacy_sum = sum(legacy_credit_safe(k, q) for k, q in states)
    legacy_seconds = perf_counter() - t0

    t0 = perf_counter()
    descriptor_sum = sum(descriptor_credit_safe(k, q) for k, q in states)
    descriptor_seconds = perf_counter() - t0

    assert legacy_sum == descriptor_sum
    return len(states), legacy_seconds, descriptor_seconds


def main():
    checked = exhaustive_regression()

    # Historical boundary and its branchwise refinement.
    assert descriptor_credit_safe(195, 124)
    assert not descriptor_credit_safe(196, 124)
    assert descriptor_credit_safe(196, 125)
    assert first_uniform_tightening() == (196, 124, 125)

    # Before the first tightening, the coefficient threshold alone implies credit.
    for k in range(2, 196):
        assert combined_required_q(k) == min_q_survival(k)

    print("PASS")
    print("exact descriptor: root-Hensel arithmetic credit safe iff k-q <= 71 (q>=2)")
    print("exhaustive regression states:", checked)
    print("first uniform tightening:", first_uniform_tightening())
    print("k q_coeff q_hensel q_combined q_hensel_minus_q_coeff")
    for row in threshold_table():
        print(*row)

    print("symbolic prefix coverage diagnostics")
    for K in (195, 196, 200, 256, 512):
        coeff = count_prefix_words(K, False)
        joint = count_prefix_words(K, True)
        print(K, "coefficient=", coeff, "joint_credit=", joint)

    nstates, tlegacy, tdesc = benchmark()
    print("benchmark states:", nstates)
    print("legacy seconds:", tlegacy)
    print("descriptor seconds:", tdesc)
    print("benchmark ratio legacy/descriptor:", tlegacy / tdesc if tdesc else float("inf"))

    print("scope warning:")
    print("d>71 means Hensel arithmetic-credit UNAVAILABLE, not Collatz candidate EXCLUDED.")
    print("States with the same d may be merged only for this credit predicate, not as full Collatz states.")
    print("Collatz remains OPEN.")


if __name__ == "__main__":
    main()
