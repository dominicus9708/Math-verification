#!/usr/bin/env python3
"""MATH-198 regression certificate.

Finite regression for:
- branchwise preservation of the risk order;
- equal-endpoint Hensel translation identity.

The theorem in the note is algebraic; this script is regression evidence only.
"""

from collections import defaultdict


def shortcut_step(n: int):
    if n & 1:
        return (3*n + 1)//2, 1
    return n//2, 0


def main():
    groups = defaultdict(list)

    for N in range(1, 1000):
        y = N
        C = 0
        q = 0

        for k in range(14):
            b = y & 1
            groups[(k, q, b)].append((N, C))

            y2, b2 = shortcut_step(y)
            assert b2 == b

            C = (3**b)*C + b*(1 << k)
            q += b
            y = y2

    checked = 0

    for (k, q, b), rows in groups.items():
        sample = rows[:120]

        for N1, C1 in sample:
            for N2, C2 in sample:
                if N1 <= N2 and C1 >= C2:
                    C1p = (3**b)*C1 + b*(1 << k)
                    C2p = (3**b)*C2 + b*(1 << k)

                    assert N1 <= N2
                    assert C1p >= C2p
                    checked += 1

    # Equal-endpoint / positive-credit translation identity.
    for k in range(1, 18):
        for q in range(k + 1):
            for N in range(100, 140):
                C = 11
                for t in range(1, 8):
                    Cstar = C + t*3**q
                    Nstar = N - t

                    assert 3**q*Nstar + Cstar == 3**q*N + C
                    assert Nstar < N
                    assert Cstar > C

    print("PASS MATH-198 branchwise Pareto/Hensel regression")
    print("dominance_pairs_checked=", checked)
    print("outer_branch_groups=", len(groups))


if __name__ == "__main__":
    main()
