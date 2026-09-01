#!/usr/bin/env python3
"""Displaced-ranked-one count bounds for the normalized Route-B defect.

For the strict-high/threshold characteristic target let

    a_1 < ... < a_q

be its ranked one positions, and let a dominance candidate have

    b_r <= a_r.

The normalized defect is

    eta = sum_r (2^a_r - 2^b_r)/3^r
        = sum_r w_r (1 - 2^(-delta_r)),

where

    w_r = 2^a_r/3^r,
    delta_r = a_r-b_r >= 0.

The characteristic target inequalities give

    1/6 <= w_r < 1/2.

For every displaced rank delta_r>=1, hence

    1/2 <= 1-2^(-delta_r) < 1.

Therefore, if M is the number of displaced ranked ones,

    M/12 <= eta < M/2.

A sharper phase-weighted form is

    (1/2) * sum_{moved r} w_r <= eta < sum_{moved r} w_r.

This certificate audits the inequalities on finite exact characteristic words.
The theorem is algebraic and does not depend on the regression horizon.
"""

from fractions import Fraction
from itertools import combinations

MAX_H = 13


def requirements(nmax: int):
    q = [0]
    p2 = p3 = 1
    k = 0
    for _ in range(1, nmax + 1):
        p2 *= 2
        while p3 <= p2:
            p3 *= 3
            k += 1
        q.append(k)
    return q


REQ = requirements(MAX_H + 2)


def target_word(h: int):
    return tuple(REQ[i + 1] - REQ[i] for i in range(h))


def correction_positions(pos):
    q = len(pos)
    return sum(3 ** (q - r - 1) * 2 ** a for r, a in enumerate(pos))


weight_checks = 0
candidate_checks = 0
count_bound_checks = 0
phase_bound_checks = 0

for h in range(1, MAX_H + 1):
    T = target_word(h)
    a = tuple(i for i, bit in enumerate(T) if bit)
    q = len(a)
    Ct = correction_positions(a)

    weights = []
    for r, ar in enumerate(a, 1):
        w = Fraction(2 ** ar, 3 ** r)
        assert Fraction(1, 6) <= w < Fraction(1, 2)
        weights.append(w)
        weight_checks += 1

    for b in combinations(range(h), q):
        if not all(b[r] <= a[r] for r in range(q)):
            continue

        Cb = correction_positions(b)
        eta = Fraction(Ct - Cb, 3 ** q)
        moved = [r for r in range(q) if b[r] < a[r]]
        M = len(moved)

        assert eta >= 0
        assert (M == 0) == (eta == 0)
        candidate_checks += 1

        if M == 0:
            continue

        phase_sum = sum((weights[r] for r in moved), Fraction(0))
        phase_lo = phase_sum / 2
        phase_hi = phase_sum

        assert phase_lo <= eta < phase_hi
        assert Fraction(M, 12) <= eta < Fraction(M, 2)
        phase_bound_checks += 1
        count_bound_checks += 1


assert weight_checks > 0
assert candidate_checks > 0
assert count_bound_checks > 0
assert phase_bound_checks > 0

print("PASS A0 s=1 Route-B displaced-rank defect-count certificate")
print("max_h", MAX_H)
print("weight_checks", weight_checks)
print("candidate_checks", candidate_checks)
print("count_bound_checks", count_bound_checks)
print("phase_bound_checks", phase_bound_checks)
print(
    "phase_weighted",
    "0.5*sum_moved(2^a_r/3^r) <= eta < sum_moved(2^a_r/3^r)",
)
print("count_bound", "M/12 <= eta < M/2")
print(
    "dsd_audit",
    "moved-rank count is a coarse membership-defect summary; no adic mismatch or local observation is counted as moved unless formation constraints force b_r<a_r",
)
print(
    "status",
    "displaced-rank defect budget CLOSED; proving extensive forced displacement on long grammar families remains OPEN",
)
