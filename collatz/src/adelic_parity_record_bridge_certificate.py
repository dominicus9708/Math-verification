#!/usr/bin/env python3
"""Exact finite regression for the common real/2-adic parity-series coordinate.

For the accelerated Collatz map
    T(x)=x/2 (even), (3x+1)/2 (odd),
let p_1<p_2<... be the odd-step positions and m_k the number of odd
steps among positions 0,...,k-1.  Put

    S_n = sum_{i=1}^n 2^(p_i)/3^i.

The exact finite identity is

    2^k T^k(N) / 3^(m_k) = N + S_(m_k).

Hence the same partial sums are positive real correction sums and, because
3^(m_k) is odd, N+S_(m_k) has 2-adic valuation at least k.  Along an
infinite parity sequence this is the finite form of the Bernstein/Lagarias
inverse-conjugacy series converging 2-adically to -N.

This script checks only the exact algebra.  The real convergence and orbit
occupation consequences in the companion note use the Garcia--Tal/Heppner
orbit-count theorem as an external input.
"""

from fractions import Fraction


def T(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def v2(n: int) -> int:
    if n == 0:
        return 10**9
    out = 0
    while n % 2 == 0:
        out += 1
        n //= 2
    return out


def check_start(N: int, K: int) -> None:
    x = N
    m = 0
    S = Fraction(0, 1)
    odd_positions: list[int] = []

    for k in range(K + 1):
        V = Fraction((1 << k) * x, 3**m)
        assert V == N + S, (N, k, x, m, V, N + S)
        # Denominator is odd, so the reduced numerator still contains 2^k.
        assert v2(V.numerator) >= k, (N, k, V)

        if k == K:
            break

        if x & 1:
            odd_positions.append(k)
            m += 1
            S += Fraction(1 << k, 3**m)
        x = T(x)

    # Direct affine correction reconstruction from the odd positions.
    R = 0
    q = len(odd_positions)
    for i, p in enumerate(odd_positions, start=1):
        R += 3 ** (q - i) * (1 << p)
    x_direct = (3**q * N + R) // (1 << K)
    assert x_direct == x


def check_record_endpoint_mod3(N: int, K: int) -> None:
    """Every strict +1 height record is entered by an odd plateau step,
    hence its endpoint is 2 mod 3.  This regression checks that finite fact.
    """
    # Exact barrier b_k = least q with 3^q >= 2^k.
    b = [0] * (K + 1)
    qbar = 0
    p3 = 1
    for k in range(1, K + 1):
        while p3 < (1 << k):
            p3 *= 3
            qbar += 1
        b[k] = qbar

    x = N
    m = 0
    hmax = 0
    for k in range(K):
        bit = x & 1
        old_h = m - b[k]
        if bit:
            m += 1
        x = T(x)
        new_h = m - b[k + 1]
        if new_h > hmax:
            assert new_h == hmax + 1
            assert bit == 1
            assert b[k + 1] == b[k]  # plateau-odd crossing
            assert x % 3 == 2
            hmax = new_h
        assert new_h - old_h in (-1, 0, 1)


def main() -> None:
    for N in range(1, 200):
        check_start(N, 128)
        check_record_endpoint_mod3(N, 128)
    print("adelic parity-series finite bridge: PASS")
    print("starts_checked", 199)
    print("steps_per_start", 128)


if __name__ == "__main__":
    main()
