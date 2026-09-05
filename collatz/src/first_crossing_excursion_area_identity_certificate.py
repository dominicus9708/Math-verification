#!/usr/bin/env python3
"""Finite regression certificate for the exact first-crossing excursion-area identity.

The mathematical identity is elementary and general; this script checks the
bookkeeping formulas on all short admissible examples and the local rise bound.
It is a regression certificate, not the proof itself.
"""

from itertools import combinations


def mechanical_positions(A: int, Q: int):
    # For a rational first-crossing model, use b_j=floor((j-1)A/Q).
    return [(j * A) // Q for j in range(Q)]


def prefix_counts(pos, A):
    s = set(pos)
    out = []
    q = 0
    for i in range(1, A + 1):
        if i - 1 in s:
            q += 1
        out.append(q)
    return out


def audit(A: int, Q: int):
    b = mechanical_positions(A, Q)
    kb = prefix_counts(b, A)
    count = 0
    for a in combinations(range(A), Q):
        if any(x > y for x, y in zip(a, b)):
            continue
        qa = prefix_counts(a, A)
        h = [x - y for x, y in zip(qa, kb)]
        if min(h) < 0 or h[-1] != 0:
            continue
        s = [y - x for x, y in zip(a, b)]
        assert sum(h[:-1]) == sum(s)
        for j in range(Q - 1):
            assert s[j + 1] - s[j] <= 1
        S = max(s)
        assert sum(s) >= S * (S + 1) // 2
        count += 1
    return count


def main():
    total = 0
    for A, Q in [(5, 3), (8, 5), (11, 7), (13, 8)]:
        c = audit(A, Q)
        assert c > 0
        total += c
        print(f"A={A} Q={Q} admissible={c}")
    print(f"PASS excursion-area identity regression; total={total}")


if __name__ == "__main__":
    main()
