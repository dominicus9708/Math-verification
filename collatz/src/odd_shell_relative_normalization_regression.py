#!/usr/bin/env python3
"""Regression for the relative normalization of the odd-shell child correlation.

The exact child-level count transform is raw, while the triangular Beatty
boundary theorem is naturally normalized by the boundary-set cardinality.
This verifier checks on actual ternary subset-sum count functions that

  K/U = sum_{s odd} (Chat(s)/2^d) (G(s)/|D|),

where

  K = sum_{r in D} v(r) [C(r)-C(r+M)],
  U = 2^d |D|/M

is the uniform one-child baseline.  In particular the factor 1/M from the
raw Fourier identity disappears after division by U.  Therefore an averaged
boundary L1 estimate (1/M) sum |G|/|D| <= eps gives only
sum |G|/|D| <= M eps unless selector Fourier decay is also used.

This is an implementation regression; the identity itself is algebraic.
"""

import cmath
import itertools
import math


def one_case(L: int, d: int) -> None:
    M = 1 << (L - 2)
    mod = 2 * M
    base = pow(3, 44, mod)

    C = [0] * mod
    for bits in itertools.product((0, 1), repeat=d):
        y = base
        for i, bit in enumerate(bits):
            if bit:
                y += pow(3, i, mod)
        C[y % mod] += 1

    # A deterministic nonempty signed one-child test set.  The Fourier
    # identity is valid for every signed g supported on parent residues; the
    # particular rule is irrelevant and deliberately nonperiodic-looking.
    g = [0] * M
    for r in range(M):
        if (3 * r + L) % 5 in (0, 1):
            g[r] = 1 if ((r + L) & 1) == 0 else -1

    D = sum(x != 0 for x in g)
    assert D > 0

    u = [C[r] - C[r + M] for r in range(M)]
    K = sum(g[r] * u[r] for r in range(M))

    zeta = cmath.exp(2j * math.pi / mod)
    hatC = []
    G = []
    for s in range(mod):
        hatC.append(sum(C[x] * zeta ** (-s * x) for x in range(mod)))
        G.append(sum(g[r] * zeta ** (s * r) for r in range(M)))

    raw_fourier = sum(hatC[s] * G[s] for s in range(1, mod, 2)) / M
    assert abs(raw_fourier - K) < 1e-8

    uniform_baseline = (2**d) * D / M
    relative_direct = K / uniform_baseline
    relative_fourier = sum(
        (hatC[s] / (2**d)) * (G[s] / D)
        for s in range(1, mod, 2)
    )
    assert abs(relative_fourier - relative_direct) < 1e-8

    normalized_boundary_l1 = (
        sum(abs(G[s] / D) for s in range(1, mod, 2)) / M
    )
    full_boundary_l1 = sum(abs(G[s] / D) for s in range(1, mod, 2))
    assert abs(full_boundary_l1 - M * normalized_boundary_l1) < 1e-10


def main() -> None:
    cases = 0
    for L in range(4, 10):
        one_case(L, min(6, L))
        cases += 1
    print(f"checked_cases {cases}")
    print("odd-shell relative normalization regression: PASS")


if __name__ == "__main__":
    main()
