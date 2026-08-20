#!/usr/bin/env python3
"""Exact finite regression for the critical-scale Haar identity of a Beatty
record strip.

For a length-L parity word, the canonical start residue modulo 2^L is a
bijection of the parity vector.  If t != 0 and

    j* = L - v2(t) - 1,

then the character exp(2*pi*i*t*r/2^L) depends only on the first j*+1
parity bits.  The two children of any common j*-prefix have residues that
differ by 2^j*, so their characters differ by exactly -1.

For the record-strip language this turns the Fourier coefficient at level
v2(t) into a signed child-completion imbalance.  Triangle inequality gives
an exact frequency-level bound in terms of a finite-state suffix gradient.

This file verifies the character pairing algebra and checks the resulting
bound against direct Fourier sums for small exact record-strip languages.
"""

from __future__ import annotations

import cmath
import math


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


B = barriers(1400)


def v2(n: int) -> int:
    out = 0
    while n and n % 2 == 0:
        out += 1
        n //= 2
    return out


def canonical_residue(bits: tuple[int, ...]) -> int:
    L = len(bits)
    Q = sum(bits)
    odd = [j for j, bit in enumerate(bits) if bit]
    R = 0
    for i, p in enumerate(odd, start=1):
        R += 3 ** (Q - i) * (1 << p)
    mod = 1 << L
    r = (-R * pow(3, -Q, mod)) % mod
    return mod if r == 0 else r


def record_words(L: int, r: int, s: int = 0) -> list[tuple[int, ...]]:
    if L > 16:
        raise ValueError("direct word enumeration intentionally limited to L<=16")
    out = []
    for mask in range(1 << L):
        q = 0
        bits = []
        ok = True
        for j in range(1, L + 1):
            bit = (mask >> (j - 1)) & 1
            bits.append(bit)
            q += bit
            g = q - (B[s + j] - B[s])
            if j < L:
                if not (-r <= g <= 0):
                    ok = False
                    break
            elif g != 1:
                ok = False
        if ok:
            out.append(tuple(bits))
    return out


def prefix_counts(L: int, r: int, s: int = 0) -> list[list[int]]:
    A = [[0] * (r + 1) for _ in range(L)]
    A[0][0] = 1
    for j in range(L - 1):
        d = B[s + j + 1] - B[s + j]
        for y, c in enumerate(A[j]):
            if not c:
                continue
            y0 = y + d
            if 0 <= y0 <= r:
                A[j + 1][y0] += c
            y1 = y + d - 1
            if 0 <= y1 <= r:
                A[j + 1][y1] += c
    return A


def suffix_completions(L: int, r: int, s: int = 0) -> list[list[int] | None]:
    F: list[list[int] | None] = [None] * (L + 1)
    if B[s + L] - B[s + L - 1] != 0:
        return F

    # At time L-1, a record completion exists only from y=0: the final bit
    # is the forced plateau-odd exit.
    f = [0] * (r + 1)
    f[0] = 1
    F[L - 1] = f[:]

    for j in range(L - 2, -1, -1):
        d = B[s + j + 1] - B[s + j]
        nf = [0] * (r + 1)
        for y in range(r + 1):
            y0 = y + d
            if 0 <= y0 <= r:
                nf[y] += f[y0]
            y1 = y + d - 1
            if 0 <= y1 <= r:
                nf[y] += f[y1]
        f = nf
        F[j] = f[:]
    return F


def record_count(L: int, r: int, s: int = 0) -> int:
    F = suffix_completions(L, r, s)
    f0 = F[0]
    return 0 if f0 is None else f0[0]


def gradient_bound(L: int, r: int, critical_bit: int, s: int = 0) -> float:
    """Triangle bound for all frequencies with critical bit j*.

    critical_bit is zero-indexed.  The parent is after critical_bit prefix
    steps, before processing bit critical_bit.
    """
    j = critical_bit
    A = prefix_counts(L, r, s)
    F = suffix_completions(L, r, s)
    f = F[j + 1]
    if f is None:
        return 0.0
    d = B[s + j + 1] - B[s + j]
    num = 0
    den = 0
    for y, pre in enumerate(A[j]):
        if not pre:
            continue
        y0 = y + d
        y1 = y + d - 1
        c0 = f[y0] if 0 <= y0 <= r else 0
        c1 = f[y1] if 0 <= y1 <= r else 0
        num += pre * abs(c0 - c1)
        den += pre * (c0 + c1)
    assert den == record_count(L, r, s)
    return num / den if den else 0.0


def direct_fourier(L: int, r: int, t: int, s: int = 0) -> complex:
    words = record_words(L, r, s)
    if not words:
        return 0.0j
    mod = 1 << L
    z = 0.0j
    for w in words:
        rr = canonical_residue(w) % mod
        z += cmath.exp(2j * math.pi * t * rr / mod)
    return z / len(words)


def pairing_algebra() -> None:
    # Pure modular check: at critical scale the two child residues differ by
    # 2^j and hence their characters differ by -1 for every odd unit u.
    for L in range(2, 20):
        mod = 1 << L
        for j in range(L):
            v = L - j - 1
            for u in (1, 3, 5, 17):
                t = (1 << v) * u
                phase_num = (t * (1 << j)) % mod
                assert phase_num == (1 << (L - 1)), (L, j, u, phase_num)


def direct_bound_regression() -> None:
    # L=11 is small enough to check every nonzero dyadic frequency directly.
    L = 11
    for r in (0, 1, 2, 3):
        count = record_count(L, r)
        assert count == len(record_words(L, r))
        for t in range(1, 1 << L):
            j = L - v2(t) - 1
            got = abs(direct_fourier(L, r, t))
            bound = gradient_bound(L, r, j)
            assert got <= bound + 2e-12, (r, t, j, got, bound)


def long_diagnostic() -> None:
    # Exact integer transfers, only the final ratios are floating diagnostics.
    L = 1201
    assert B[L] == B[L - 1]
    for r in (1, 2, 3, 5, 10, 20):
        vals = []
        for v in (5, 10, 20, 40):
            j = L - v - 1
            vals.append((v, gradient_bound(L, r, j)))
        print("r", r, "critical_suffix_gradient", vals)


def main() -> None:
    pairing_algebra()
    direct_bound_regression()
    print("record-strip critical Haar identity regression: PASS")
    long_diagnostic()


if __name__ == "__main__":
    main()
