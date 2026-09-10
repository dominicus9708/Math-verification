#!/usr/bin/env python3
"""
Fixed-d Collatz signature / bounded-carry certificate.

This is a certificate for the exact algebraic reduction used after MATH-050.
It does NOT implement the large subset-state DP by itself.

For a length-k parity word, specify the positions of the d even bits
(0-indexed). All remaining bits are odd for the shortcut map

    E: n -> n/2
    O: n -> (3n+1)/2.

The correction C satisfies
    T^k(N) = (3^(k-d) N + C) / 2^k.

For fixed d define
    Sigma_d(E) = sum_j 3^j (2/3)^e_j
for sorted even positions e_0 < ... < e_(d-1).

Then for same k,d,
    C(F)-C(E) = 3^(k-d) [Sigma_d(F)-Sigma_d(E)].

Hence E,F are in the same exact Hensel class iff the Sigma difference is
an integer; a positive integer difference is exactly the translation credit.

In gap coordinates G_j=e_j-j,
    Sigma_d = sum_j 2^j (2/3)^G_j.

Grouping equal G_j gives an integer-coefficient expansion
    sum_r a_r (2/3)^r.
Integrality of a difference can be checked from high r to low r with
    h_{r-1} = 2(h_r + Delta a_r)/3,
requiring divisibility by 3 at each step.

Finite exact algebraic certificate only. Collatz remains OPEN.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import combinations
import random


def correction(k: int, evens: tuple[int, ...]) -> tuple[int, int]:
    es = set(evens)
    C = 0
    q = 0
    for p in range(k):
        if p in es:
            continue
        C = 3 * C + (1 << p)
        q += 1
    return C, q


def sigma_fraction(evens: tuple[int, ...]) -> Fraction:
    out = Fraction(0, 1)
    for j, e in enumerate(sorted(evens)):
        out += Fraction((3 ** j) * (2 ** e), 3 ** e)
    return out


def gap_coeffs(evens: tuple[int, ...]) -> dict[int, int]:
    coeff: dict[int, int] = {}
    for j, e in enumerate(sorted(evens)):
        G = e - j
        if G < 0:
            raise ValueError("even positions must be strictly increasing")
        coeff[G] = coeff.get(G, 0) + (1 << j)
    return coeff


def carry_credit(candidate: tuple[int, ...],
                 competitor: tuple[int, ...]) -> int | None:
    """Return integer Sigma(comp)-Sigma(cand), or None if nonintegral."""
    if len(candidate) != len(competitor):
        raise ValueError("fixed-d comparison requires equal even counts")
    ca = gap_coeffs(candidate)
    cb = gap_coeffs(competitor)
    M = max(max(ca, default=0), max(cb, default=0))
    delta = [cb.get(r, 0) - ca.get(r, 0) for r in range(M + 1)]
    h = 0
    for r in range(M, 0, -1):
        num = h + delta[r]
        if num % 3:
            return None
        h = 2 * num // 3
    return delta[0] + h


def verify_pair(k: int,
                candidate: tuple[int, ...],
                competitor: tuple[int, ...]) -> int | None:
    d = len(candidate)
    if d != len(competitor):
        raise ValueError("different d")
    Cc, qc = correction(k, candidate)
    Cw, qw = correction(k, competitor)
    assert qc == qw == k - d
    mod = 3 ** (k - d)
    direct_same = (Cc - Cw) % mod == 0
    cc = carry_credit(candidate, competitor)
    carry_same = cc is not None
    assert direct_same == carry_same
    if cc is not None:
        assert Cw - Cc == cc * mod
    return cc


def selftest() -> None:
    rng = random.Random(20260910)

    # General signature identity and carry-vs-direct congruence.
    for k in range(7, 14):
        for d in range(1, min(5, k)):
            words = list(combinations(range(k), d))
            for _ in range(min(100, len(words) * 2)):
                a = rng.choice(words)
                b = rng.choice(words)
                Ca, _ = correction(k, a)
                lhs = Fraction(Ca, 3 ** (k - d))
                rhs = (Fraction(1, 1) + sigma_fraction(a)
                       - Fraction((3 ** d) * (2 ** k), 3 ** k))
                assert lhs == rhs
                verify_pair(k, a, b)

    # d=2 persistent credit-1 family.
    for k in range(4, 35):
        for j in range(1, k - 1):
            cand = (j, j + 1)
            comp = (0, j)
            assert verify_pair(k, cand, comp) == 1

    # d=6 extracted credit-3 motif families.
    for k in range(16, 35):
        for n in range(10, k - 5):
            A = tuple(sorted((n-2, n, n+1, n+2, n+3, k-2)))
            Ap = tuple(sorted((0, 1, n-2, n, k-2, k-1)))
            B = tuple(sorted((n-3, n, n+1, n+2, n+3, k-2)))
            Bp = tuple(sorted((0, 1, n-3, n+1, k-2, k-1)))
            assert verify_pair(k, A, Ap) == 3
            assert verify_pair(k, B, Bp) == 3

    print("PASS fixed-d signature and bounded-carry certificate")


if __name__ == "__main__":
    selftest()
