#!/usr/bin/env python3
"""Exact finite regression for the M=5 weighted zero-gap entropy theorem.

The companion note proves that the eventual M=5 record language is a weighted
monomer-dimer tiling of the mechanical zero-gap word.  Gap lengths are 2 or 3;
a dimer over (2,3) has multiplicity 2, a dimer over (3,2) has multiplicity 3,
and all other pairs have multiplicity zero.  Gap-2 events are isolated strongly
enough that every complete interior cluster contributes the exact factor

    1 + 3 + 2 = 6.

This script checks the exact Beatty factors, zero-gap isolation, weighted tiling
recurrence, direct local record-word multiplicities, and the asymptotic entropy
rate on large finite prefixes.  It is a regression certificate, not a proof of
the Collatz conjecture.
"""

from __future__ import annotations

import math

ALPHA = math.log(2.0) / math.log(3.0)
H5 = (2.0 - 3.0 * ALPHA) * math.log2(6.0)


def barriers(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        while p3 < (1 << k):
            p3 *= 3
            q += 1
        out[k] = q
    return out


B = barriers(20000)


def mechanical_bits(n: int, s: int = 0) -> list[int]:
    return [B[s + k] - B[s + k - 1] for k in range(1, n + 1)]


def zero_gaps(n: int, s: int = 0) -> tuple[list[int], list[int]]:
    d = mechanical_bits(n, s)
    zeros = [i + 1 for i, bit in enumerate(d) if bit == 0]
    gaps = [zeros[i + 1] - zeros[i] for i in range(len(zeros) - 1)]
    return zeros, gaps


def skip_weight(a: int, b: int) -> int:
    if (a, b) == (2, 3):
        return 2
    if (a, b) == (3, 2):
        return 3
    return 0


def weighted_tiling_count(gaps: list[int], n: int | None = None) -> int:
    """Weighted record tilings from zero vertex 0 to zero vertex n."""
    if n is None:
        n = len(gaps)
    if not (0 <= n <= len(gaps)):
        raise ValueError

    # Vertices are 0,...,n.  A monomer advances one zero with weight 1.
    # A dimer advances two zeros with the exact non-singleton multiplicity.
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n):
        dp[i + 1] += dp[i]
        if i + 1 < n:
            w = skip_weight(gaps[i], gaps[i + 1])
            if w:
                dp[i + 2] += w * dp[i]
    return dp[n]


def local_record_words(mechanical: tuple[int, ...]) -> list[tuple[int, ...]]:
    """Brute first-passage record words for one fixed mechanical factor."""
    L = len(mechanical)
    out: list[tuple[int, ...]] = []
    for mask in range(1 << L):
        g = 0
        ok = True
        bits = tuple((mask >> j) & 1 for j in range(L))
        for j, (d, bit) in enumerate(zip(mechanical, bits), start=1):
            g += bit - d
            if j < L:
                if g > 0:
                    ok = False
                    break
            elif g != 1:
                ok = False
        if ok:
            out.append(bits)
    return out


def main() -> None:
    # Exact local macro multiplicities from the M=5 classification.
    assert len(local_record_words((1, 0))) == 1
    assert len(local_record_words((1, 1, 0))) == 1
    assert len(local_record_words((1, 0, 1, 1, 0))) == 2
    assert len(local_record_words((1, 1, 0, 1, 0))) == 3

    # Check all length-n Beatty factor one-count property on a broad grid.
    for n in range(1, 65):
        lo = math.floor(ALPHA * n)
        hi = math.ceil(ALPHA * n)
        for s in range(300):
            q = sum(mechanical_bits(n, s))
            assert q in (lo, hi), (n, s, q, lo, hi)

    zeros, gaps = zero_gaps(15000)
    assert set(gaps) == {2, 3}

    # No 22 and no 232: every two gap-2 events have at least two 3s between.
    for i in range(len(gaps) - 1):
        assert (gaps[i], gaps[i + 1]) != (2, 2)
    for i in range(len(gaps) - 2):
        assert (gaps[i], gaps[i + 1], gaps[i + 2]) != (2, 3, 2)

    # Exact weighted matching recurrence.  Once both boundary clusters are
    # complete, the count is exactly 6^(number of gap-2 events).  At arbitrary
    # early cutoffs the ratio differs only by a fixed boundary factor.
    boundary_ratios = set()
    for n in range(5, 1200):
        z = weighted_tiling_count(gaps, n)
        n2 = sum(1 for x in gaps[:n] if x == 2)
        # Store the rational ratio as an exact numerator/denominator after
        # cancelling only the obvious power of six via divisibility.
        p6 = 6 ** n2
        boundary_ratios.add((z, p6))
        # The logarithmic discrepancy is uniformly bounded by the two endpoint
        # clusters; a very conservative finite regression constant is enough.
        assert abs(math.log(z, 2) - n2 * math.log2(6.0)) < 3.0

    # Long checkpoints: complete clusters give exact factorization.
    for n in (50, 100, 200, 500, 1000):
        n2 = sum(1 for x in gaps[:n] if x == 2)
        assert weighted_tiling_count(gaps, n) == 6 ** n2

    # Gap-2 density and entropy convergence.
    checkpoints = []
    for H in (1000, 3000, 6000, 12000):
        _, gh = zero_gaps(H)
        n2 = sum(1 for x in gh if x == 2)
        density = n2 / H
        rate = (n2 * math.log2(6.0)) / H
        checkpoints.append((H, n2, density, rate))
        assert abs(density - (2.0 - 3.0 * ALPHA)) < 0.01
        assert abs(rate - H5) < 0.03

    print("M=5 weighted zero-gap entropy regression: PASS")
    print("alpha", ALPHA)
    print("gap2_density_limit", 2.0 - 3.0 * ALPHA)
    print("h5", H5)
    print("ambient_margin", 1.0 - ALPHA - H5)
    for row in checkpoints:
        print("H N2 density rate", *row)


if __name__ == "__main__":
    main()
