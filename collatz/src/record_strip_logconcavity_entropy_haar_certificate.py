#!/usr/bin/env python3
"""Finite exact/numerical regression for the record-strip log-concavity,
critical-Haar, entropy-budget and boundary-commutator identities.

The companion note contains the all-length proofs.  This program checks the
identities on finite record first-passage languages and exact integer transfer
matrices.  It is not a proof of the Collatz conjecture.
"""

from __future__ import annotations

import cmath
import math
from collections import defaultdict

ALPHA = math.log(2.0) / math.log(3.0)


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


B = barriers(400)


def record_words(s: int, r: int, L: int) -> list[tuple[int, ...]]:
    out: list[tuple[int, ...]] = []

    def rec(j: int, q: int, bits: list[int]) -> None:
        if j == L:
            g = q - (B[s + L] - B[s])
            if g == 1:
                out.append(tuple(bits))
            return
        for bit in (0, 1):
            qq = q + bit
            jj = j + 1
            g = qq - (B[s + jj] - B[s])
            if jj < L and not (-r <= g <= 0):
                continue
            if jj == L and g != 1:
                continue
            bits.append(bit)
            rec(jj, qq, bits)
            bits.pop()

    rec(0, 0, [])
    return out


def completion_vectors(s: int, r: int, L: int) -> list[list[int]]:
    # F[j][y] = completions after j bits from state y to the record exit.
    F = [[0] * (r + 1) for _ in range(L)]
    dlast = B[s + L] - B[s + L - 1]
    if dlast == 0:
        F[L - 1][0] = 1

    for j in range(L - 2, -1, -1):
        d = B[s + j + 1] - B[s + j]
        nxt = F[j + 1]
        cur = F[j]
        for y in range(r + 1):
            y0 = y + d
            y1 = y + d - 1
            if 0 <= y0 <= r:
                cur[y] += nxt[y0]
            if 0 <= y1 <= r:
                cur[y] += nxt[y1]
    return F


def is_log_concave(v: list[int]) -> bool:
    supp = [i for i, x in enumerate(v) if x]
    if supp and supp != list(range(supp[0], supp[-1] + 1)):
        return False
    return all(v[i] * v[i] >= v[i - 1] * v[i + 1]
               for i in range(1, len(v) - 1))


def canonical_residue(bits: tuple[int, ...]) -> int:
    L = len(bits)
    Q = sum(bits)
    R = 0
    odd_pos = [i for i, bit in enumerate(bits) if bit]
    for i, p in enumerate(odd_pos, start=1):
        R += 3 ** (Q - i) * (1 << p)
    mod = 1 << L
    x = (-R * pow(3, -Q, mod)) % mod
    return x


def conditional_rows(words: list[tuple[int, ...]], j: int):
    rows: dict[tuple[int, ...], list[int]] = defaultdict(lambda: [0, 0])
    for w in words:
        rows[w[:j]][w[j]] += 1
    return rows


def h2(p: float) -> float:
    if p <= 0.0 or p >= 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def kl_bern(p: float, q: float) -> float:
    ans = 0.0
    if p > 0.0:
        ans += p * math.log(p / q)
    if p < 1.0:
        ans += (1.0 - p) * math.log((1.0 - p) / (1.0 - q))
    return ans


def critical_fourier(words: list[tuple[int, ...]], j: int, odd_part: int = 1) -> complex:
    L = len(words[0])
    t = (1 << (L - j - 1)) * odd_part
    mod = 1 << L
    z = 0.0j
    for w in words:
        rr = canonical_residue(w)
        z += cmath.exp(2j * math.pi * t * rr / mod)
    return z / len(words)


def entropy_haar_check(s: int, r: int, L: int) -> None:
    words = record_words(s, r, L)
    if not words:
        return
    N = len(words)
    sum_H = 0.0
    sum_kappa = 0.0
    shell_sq = 0.0

    Qs = {sum(w) for w in words}
    assert len(Qs) == 1
    Q = next(iter(Qs))

    for j in range(L):
        rows = conditional_rows(words, j)
        Delta = 0.0
        H = 0.0
        kappa = 0.0
        for c0, c1 in rows.values():
            m = c0 + c1
            wt = m / N
            p = c1 / m
            delta = abs(1.0 - 2.0 * p)
            Delta += wt * delta
            H += wt * h2(p)
            kappa += wt * kl_bern(p, ALPHA)

        # Pinsker / Shannon level bounds.
        assert Delta * Delta <= 2.0 * math.log(2.0) * (1.0 - H) + 1e-12
        assert Delta <= abs(2.0 * ALPHA - 1.0) + math.sqrt(2.0 * kappa) + 1e-12

        # Every odd Fourier part at the same valuation has the same critical
        # child sign mechanism.  Check several representatives directly.
        worst = 0.0
        maxodd = min(15, (1 << (j + 1)) - 1)
        for u in range(1, maxodd + 1, 2):
            mag = abs(critical_fourier(words, j, u))
            assert mag <= Delta + 2e-10, (s, r, L, j, u, mag, Delta)
            worst = max(worst, mag)
        shell_sq += worst * worst
        sum_H += H
        sum_kappa += kappa

    assert abs(sum_H - math.log2(N)) < 2e-10
    shannon_budget = 2.0 * math.log(2.0) * (L - math.log2(N))
    assert shell_sq <= shannon_budget + 2e-9

    weight = (ALPHA ** Q) * ((1.0 - ALPHA) ** (L - Q))
    total_K = -math.log(N * weight)
    assert abs(sum_kappa - total_K) < 2e-10


def matmul(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]


def matsub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def boundary_commutator_check(r: int) -> None:
    n = r + 1
    I = [[int(i == j) for j in range(n)] for i in range(n)]
    Sm = [[0] * n for _ in range(n)]
    Sp = [[0] * n for _ in range(n)]
    for y in range(n):
        if y - 1 >= 0:
            Sm[y][y - 1] = 1
        if y + 1 < n:
            Sp[y][y + 1] = 1
    M0 = [[I[i][j] + Sm[i][j] for j in range(n)] for i in range(n)]
    M1 = [[I[i][j] + Sp[i][j] for j in range(n)] for i in range(n)]
    C = matsub(matmul(M0, M1), matmul(M1, M0))
    want = [[0] * n for _ in range(n)]
    want[r][r] = 1
    want[0][0] -= 1
    assert C == want, (r, C, want)


def main() -> None:
    # Completion log-concavity over a broad exact finite grid.
    checked = 0
    for r in range(1, 9):
        for s in range(12):
            for L in range(3, 70):
                if B[s + L] == B[s + L - 1]:
                    F = completion_vectors(s, r, L)
                    assert all(is_log_concave(v) for v in F)
                    checked += 1

    # Exact small-language entropy/Fourier checks.
    for r in (0, 1, 2, 3):
        for s in range(4):
            for L in range(3, 13):
                if B[s + L] == B[s + L - 1]:
                    entropy_haar_check(s, r, L)

    for r in range(1, 12):
        boundary_commutator_check(r)

    print("record-strip log-concavity/entropy-Haar certificate: PASS")
    print("completion_instances", checked)
    print("delta_alpha", abs(2.0 * ALPHA - 1.0))


if __name__ == "__main__":
    main()
