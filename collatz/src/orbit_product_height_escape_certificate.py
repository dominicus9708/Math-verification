#!/usr/bin/env python3
"""Exact arithmetic regression for the orbit-product / height-escape bridge.

External theorem input (NOT proved here): Garcia--Tal (1999), equation (6)
plus Corollary 1, gives a uniform power-saving interval count for every
infinite nonperiodic accelerated Collatz orbit. That external input implies
sum_j 1/x_j < infinity by a dyadic-shell argument.

This script certifies only the internal algebra used after that input:

    x_k = x_0 * 3^m_k / 2^k * product_{odd j<k}(1+1/(3 x_j)),

and

    v_k := 2^k x_k / 3^m_k = x_0 * product(...).

It also checks the exact barrier-height decomposition

    x_k = x_0 * 3^h_k * (3^b_k/2^k) * product(...),
    h_k=m_k-b_k.

This is a regression certificate, not a proof of the external sparsity result
and not a proof of the Collatz conjecture.
"""

from fractions import Fraction


def T(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def barriers(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        p2 = 1 << k
        while p3 < p2:
            p3 *= 3
            q += 1
        out[k] = q
    return out


def check_start(x0: int, K: int, b: list[int]) -> None:
    x = x0
    m = 0
    corr = Fraction(1, 1)

    for k in range(K + 1):
        product_form = Fraction(x0 * (3 ** m), 1 << k) * corr
        assert product_form == x, (x0, k, x, product_form)

        v = Fraction((1 << k) * x, 3 ** m)
        assert v == x0 * corr

        if k > 0:
            h = m - b[k]
            height_form = (
                Fraction(x0 * (3 ** h) * (3 ** b[k]), 1 << k) * corr
            )
            assert height_form == x
            assert 1 < Fraction(3 ** b[k], 1 << k) < 3

        if k == K:
            break

        if x & 1:
            corr *= Fraction(3 * x + 1, 3 * x)
            m += 1
        x = T(x)


def main() -> None:
    K = 160
    b = barriers(K)

    for x0 in range(1, 301):
        check_start(x0, K, b)

    # A standalone exact check of the dyadic-shell analytic implication:
    # for every rational beta<1, sum (r+1) 2^{-(1-beta)r} converges
    # geometrically. We do not approximate the Garcia--Tal beta here.
    # The identity below is the closed form for sum_{r>=0}(r+1) z^r.
    for z in (Fraction(1, 2), Fraction(3, 4), Fraction(7, 8), Fraction(15, 16)):
        closed = Fraction(1, (1 - z) ** 2)
        # finite partial sums must increase toward the finite closed form
        partial = Fraction(0, 1)
        for r in range(200):
            partial += (r + 1) * (z ** r)
            assert partial < closed

    print("orbit product / height escape algebra regression: PASS")
    print("starts_checked", 300)
    print("steps_per_start", K)


if __name__ == "__main__":
    main()
