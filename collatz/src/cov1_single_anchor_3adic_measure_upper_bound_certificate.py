#!/usr/bin/env python3
"""Exact certificate for a global 3-adic measure ceiling on the single-anchor
inverse-merge language for x=36*k+27.

Let R be the set of k for which some canonical contracting reverse word from
T(x)=54*k+41 yields a smaller positive predecessor m<x.

Every q-O reverse word determines at most one cylinder modulo 3^(q-3), hence

    mu_3(R) <= sum_{q>=3} N_q / 3^(q-3),

where N_q may be overcounted by the number of contracting position sets whose
first three O positions pass the necessary mod-27 integrality condition.

This program computes that exact overcount for q<500 and bounds the remaining
tail by all contracting q-position subsets, without the mod-27 filter.

For P_q=floor((q-1)log_2 3), n=P_q+1 < (8/5)q.  For x=5/3,

    C(n,q) x^q <= (1+x)^n

implies

    C(n,q)/3^(q-3) <= 27*r^q,
    r=(8/3)^(8/5)/5.

The exact fifth-power comparison proves r < 193/200.  Therefore the tail from
q=500 is at most

    27*(193/200)^500 / (1-193/200).

The resulting exact rational bound is < 2/25 = 0.08.

This is an upper bound on this particular single-anchor reverse language, not
on all possible recursive merges and not on Collatz convergence.
"""

from fractions import Fraction
from math import comb

Q = 500
RAT = Fraction(193, 200)


def pmax(q: int) -> int:
    """Largest integer p with 2^p < 3^(q-1), exactly."""
    target = 3 ** (q - 1)
    p = target.bit_length() - 1
    if (1 << p) >= target:
        p -= 1
    return p


def build_pair_counts(max_p: int):
    """pair_count[p2] = number of p0<p1<p2 passing the mod-27 condition."""
    powval = [pow(2, -p - 1, 27) for p in range(max_p + 1)]

    # 2 is primitive modulo 27, so p mod 18 is uniquely determined by its unit value.
    residue_for_unit = {
        pow(2, -r - 1, 27): r
        for r in range(18)
    }

    pair_count = [0] * (max_p + 1)
    for p2 in range(max_p + 1):
        total = 0
        for p1 in range(p2):
            required = (41 - 3 * powval[p1] - 9 * powval[p2]) % 27
            r = residue_for_unit.get(required)
            if r is None:
                continue
            # Count p0 in [0,p1) with p0 == r mod 18.
            if r < p1:
                total += 1 + (p1 - 1 - r) // 18
        pair_count[p2] = total
    return pair_count


def admissible_word_count(q: int, pair_count) -> int:
    """Exact count of contracting q-position sets passing first-three mod 27."""
    P = pmax(q)
    rem = q - 3
    total = 0
    for p2 in range(P + 1):
        available = P - p2
        if available >= rem:
            total += pair_count[p2] * comb(available, rem)
    return total


def main():
    max_p = pmax(Q - 1)
    pair_count = build_pair_counts(max_p)

    partial = Fraction(0, 1)
    rows = []
    for q in range(3, Q):
        Nq = admissible_word_count(q, pair_count)
        term = Fraction(Nq, 3 ** (q - 3))
        partial += term
        if q <= 15 or q in (20, 30, 50, 100, 200, 499):
            rows.append((q, Nq, term))

    # Rigorous rational proof of r < 193/200:
    # r^5=(8/3)^8/5^5.
    r5 = Fraction(8, 3) ** 8 / (5 ** 5)
    assert r5 < RAT ** 5

    # P_q+1 < (8/5)q because log_2(3)<8/5.
    # Verify the simple rational comparison 3^5 < 2^8.
    assert 3 ** 5 < 2 ** 8

    tail = Fraction(27, 1) * RAT ** Q / (1 - RAT)
    total_bound = partial + tail

    assert total_bound < Fraction(2, 25)

    print("SAFE single-anchor 3-adic measure ceiling")
    print("exact filtered partial q<500 =", partial)
    print("decimal partial =", float(partial))
    print("rigorous tail upper bound =", tail)
    print("decimal tail =", float(tail))
    print("total rigorous upper bound =", total_bound)
    print("decimal total bound =", float(total_bound))
    print("asserted ceiling: mu_3(R) < 2/25 = 0.08")
    print("therefore complement Haar measure > 23/25 = 0.92")
    print("sample exact counts:")
    for q, Nq, term in rows:
        print(q, Nq, term)


if __name__ == "__main__":
    main()
