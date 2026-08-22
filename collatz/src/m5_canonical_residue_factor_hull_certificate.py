#!/usr/bin/env python3
"""Finite exact regression for the M=5 canonical-residue factor-hull obstruction.

For 18 consecutive mechanical zero-gaps, enumerate all distinct Sturmian gap
factors beginning at a mechanical zero, all exact M=5 record tilings, and all
canonical Collatz start residues. Collect every contiguous binary factor of
length <=18 in those residues.

The test shows that despite the low M=5 parity-prefix entropy, the ordinary
binary digit-factor hull of canonical start residues is already full through
length 15. This is a finite negative diagnostic against a naive low-dimensional
x2-invariant hull; it is not an asymptotic theorem and not a proof of Collatz.
"""
from __future__ import annotations


def barriers(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        target = 1 << k
        while p3 < target:
            p3 *= 3
            q += 1
        out[k] = q
    return out


B = barriers(5000)
D = [0] * len(B)
for k in range(1, len(B)):
    D[k] = B[k] - B[k - 1]


def gap_sequence_from_s(s: int, n_gaps: int):
    assert D[s] == 0
    zeros = []
    k = s + 1
    while len(zeros) < n_gaps:
        if D[k] == 0:
            zeros.append(k)
        k += 1
    z = [s] + zeros
    return tuple(z[i + 1] - z[i] for i in range(n_gaps)), z[-1] - s


def options(gaps, i):
    g = gaps[i]
    out = [(1, (1,) * g)]
    if i + 1 < len(gaps):
        pair = (g, gaps[i + 1])
        if pair == (2, 3):
            out += [(2, (0, 1, 1, 1, 1)), (2, (1, 0, 1, 1, 1))]
        elif pair == (3, 2):
            out += [
                (2, (0, 1, 1, 1, 1)),
                (2, (1, 0, 1, 1, 1)),
                (2, (1, 1, 0, 1, 1)),
            ]
    return out


def parity_masks(gaps):
    dp = {0: [(0, 0)]}
    n = len(gaps)
    for i in range(n):
        if i not in dp:
            continue
        arr = dp[i]
        for adv, bits in options(gaps, i):
            if i + adv > n:
                continue
            bm = sum(bit << j for j, bit in enumerate(bits))
            dest = dp.setdefault(i + adv, [])
            for mask, L in arr:
                dest.append((mask | (bm << L), L + len(bits)))
    return dp[n]


def canonical(mask: int, H: int) -> int:
    R = 0
    q = 0
    for i in range(H):
        if (mask >> i) & 1:
            R = 3 * R + (1 << i)
            q += 1
    mod = 1 << H
    return (-R * pow(pow(3, q, mod), -1, mod)) % mod


def main() -> None:
    n_gaps = 18
    seqs = {}
    for s in range(1, 3000):
        if D[s] == 0:
            gaps, H = gap_sequence_from_s(s, n_gaps)
            seqs.setdefault(gaps, (s, H))
    assert len(seqs) == 19
    assert {H for _, H in seqs.values()} == {48, 49}

    nmax = 18
    factors = [set() for _ in range(nmax + 1)]
    total_words = 0
    max_words = 0
    for gaps, (s, H) in seqs.items():
        arr = parity_masks(gaps)
        assert all(L == H for _, L in arr)
        total_words += len(arr)
        max_words = max(max_words, len(arr))
        seen = set()
        for mask, L in arr:
            r = canonical(mask, H)
            seen.add(r)
            for n in range(1, nmax + 1):
                low = (1 << n) - 1
                for j in range(H - n + 1):
                    factors[n].add((r >> j) & low)
        # The finite parity-cylinder map is a bijection at fixed H.
        assert len(seen) == len(arr)

    assert total_words == 180_144
    assert max_words == 15_552
    expected = {
        1: 2,
        2: 4,
        3: 8,
        4: 16,
        5: 32,
        6: 64,
        7: 128,
        8: 256,
        9: 512,
        10: 1024,
        11: 2048,
        12: 4096,
        13: 8192,
        14: 16384,
        15: 32768,
        16: 65525,
        17: 129694,
        18: 235309,
    }
    for n, want in expected.items():
        got = len(factors[n])
        assert got == want, (n, got, want)

    print("M5 canonical-residue factor-hull regression: PASS")
    print("distinct_gap_factors", len(seqs))
    print("total_parity_words", total_words)
    print("max_words_per_phase_factor", max_words)
    for n in range(1, nmax + 1):
        got = len(factors[n])
        print(n, got, 1 << n)


if __name__ == "__main__":
    main()
