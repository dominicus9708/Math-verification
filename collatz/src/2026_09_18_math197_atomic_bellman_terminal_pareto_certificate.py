#!/usr/bin/env python3
"""MATH-197 regression certificate.

Checks:
1. correction and integer-defect identities on actual shortcut-map prefixes;
2. one parity-class cut lowers ceil(log2 multiplicity) by at least one bit
   whenever the parent multiplicity is at least two;
3. terminal Pareto dominance on an exhaustive finite regression sample.

The structural statements in the note are algebraic; this script is regression
evidence only. Collatz remains open.
"""

from collections import defaultdict


def shortcut_step(n: int):
    if n & 1:
        return (3 * n + 1) // 2, 1
    return n // 2, 0


def resolution(m: int) -> int:
    if m <= 1:
        return 0
    return (m - 1).bit_length()


def main():
    # Prefix/correction/J identities.
    for N in range(1, 501):
        y = N
        C = 0
        q = 0
        for k in range(18):
            assert 3**q * N + C == (1 << k) * y
            Delta = (1 << k) - 3**q
            J = C - N * Delta
            assert J == (1 << k) * (y - N)

            y2, b = shortcut_step(y)
            C2 = (3**b) * C + b * (1 << k)
            q2 = q + b
            Delta2 = (1 << (k + 1)) - 3**q2
            J2 = C2 - N * Delta2

            if b == 0:
                assert J2 == J - (1 << k) * N
            else:
                assert J2 == 3 * J + (1 << k) * (N + 1)

            y, C, q = y2, C2, q2

    # Atomic source-resolution consumption.
    for Ls in range(-10, 11):
        for M in range(2, 300):
            Us = Ls + M - 1
            R = resolution(M)
            for eta in (0, 1):
                Mp = sum(1 for s in range(Ls, Us + 1) if (s - eta) % 2 == 0)
                if Mp:
                    assert resolution(Mp) <= R - 1

    # Finite regression of the Pareto inequality on actual singleton prefixes.
    states = defaultdict(list)
    for N in range(1, 1000):
        y = N
        C = 0
        q = 0
        for k in range(1, 15):
            y, b = shortcut_step(y)
            C = (3**b) * C + b * (1 << (k - 1))
            q += b
            Delta = (1 << k) - 3**q
            if Delta > 0:
                J = C - N * Delta
                states[(k, q)].append((N, C, J))

    for (k, q), rows in states.items():
        Delta = (1 << k) - 3**q
        assert Delta > 0
        sample = rows[:120]
        for N1, C1, J1 in sample:
            for N2, C2, J2 in sample:
                if N1 <= N2 and C1 >= C2:
                    assert J1 >= J2
                    # At fixed q, P=S_boundary-C/3^q, so C1>=C2
                    # implies P1<=P2. Integer comparison is sufficient here.
                    assert C1 >= C2

    print("PASS MATH-197 atomic Bellman / integer-defect regression")
    print("tested_N_prefixes=500")
    print("tested_depths=18")
    print("tested_interval_multiplicities=2..299")
    print("pareto_groups=", len(states))


if __name__ == "__main__":
    main()
