#!/usr/bin/env python3
"""Exact finite regression for the height-neutral mechanical coboundary.

For b_n=ceil(n log_3 2), c_{s,h}=2^s/3^(b_s+h), and a height-neutral
macro of length L, Q=b_{s+L}-b_s. Hence

    c_{s+L,h}/c_{s,h} = 2^L/3^Q.

For any concatenation of height-neutral macros at fixed h, the product of
these raw scale ratios telescopes exactly to the endpoint ratio. Since
c_{s,h}=3^(-h-delta_s), delta_s in (0,1) for s>0, the product is always
strictly between 1/3 and 3.

This script checks the integer identity on a large finite grid without using
floating point. It is a regression certificate, not a Collatz proof.
"""

from fractions import Fraction


def barriers(n: int) -> list[int]:
    out = [0] * (n + 1)
    p2 = p3 = 1
    q = 0
    for k in range(1, n + 1):
        p2 *= 2
        while p3 < p2:
            p3 *= 3
            q += 1
        out[k] = q
    return out


def scale(s: int, h: int, b: list[int]) -> Fraction:
    return Fraction(1 << s, 3 ** (b[s] + h))


def main() -> None:
    S_MAX = 250
    L_MAX = 80
    H_MAX = 8
    b = barriers(S_MAX + L_MAX + 5)

    one_slack = full = 0
    for s in range(1, S_MAX + 1):
        for L in range(1, L_MAX + 1):
            Q = b[s + L] - b[s]
            assert Q in (b[L] - 1, b[L])

            if Q == b[L] - 1:
                one_slack += 1
                assert 3 ** Q < 2 ** L < 3 ** (Q + 1)
            else:
                full += 1
                assert 2 ** L < 3 ** Q

            for h in range(H_MAX + 1):
                ratio = Fraction(1 << L, 3 ** Q)
                assert scale(s + L, h, b) / scale(s, h, b) == ratio
                # Endpoint phase scales differ by less than a factor 3.
                assert Fraction(1, 3) < ratio < 3

    # Explicit telescoping over many variable-length neutral segments.
    lengths = (5, 7, 3, 11, 19, 2, 23, 13, 17)
    for s0 in range(1, 80):
        for h in range(5):
            s = s0
            prod = Fraction(1, 1)
            for L in lengths:
                Q = b[s + L] - b[s]
                prod *= Fraction(1 << L, 3 ** Q)
                s += L
            endpoint = scale(s, h, b) / scale(s0, h, b)
            assert prod == endpoint
            assert Fraction(1, 3) < prod < 3

    assert one_slack > 0 and full > 0
    print("height-neutral phase coboundary regression: PASS")
    print("one_slack_cases", one_slack)
    print("full_barrier_cases", full)


if __name__ == "__main__":
    main()
