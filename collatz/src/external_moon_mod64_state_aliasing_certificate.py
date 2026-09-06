#!/usr/bin/env python3
"""Exact certificate for the mod-64 state-aliasing obstruction.

A claimed finite-state odd-to-odd Collatz quotient may define, for each odd
residue r mod 64,

    k(r) = v2(3r+1),
    r'   = (3r+1)/2^k mod 64.

This is not a well-defined quotient of the actual accelerated Collatz map,
because for the residue r=21 mod 64 the exact valuation v2(3n+1) and the
odd successor depend on higher binary digits of n.

The script also records the representative-substitution issue in a drift term
log(3+1/r): the actual multiplicative factor is log(3+1/n).
"""


def v2(n: int) -> int:
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def odd_successor(n: int) -> int:
    m = 3 * n + 1
    return m >> v2(m)


def main():
    samples = [21, 85, 149]
    rows = []
    for n in samples:
        assert n % 64 == 21
        k = v2(3 * n + 1)
        nxt = odd_successor(n)
        rows.append((n, k, nxt, nxt % 64))

    assert rows == [
        (21, 6, 1, 1),
        (85, 8, 1, 1),
        (149, 6, 7, 7),
    ]

    print("SAFE exact state-aliasing certificate")
    print("All samples are 21 mod 64, but transitions differ:")
    for row in rows:
        print(row)
    print("Therefore exact v2(3n+1) and odd successor are not functions of n mod 64.")
    print("A deterministic 31-state mod-64 quotient using those functions is not faithful.")


if __name__ == "__main__":
    main()
