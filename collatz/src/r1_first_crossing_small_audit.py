#!/usr/bin/env python3
"""Exact finite audit for R1-type first coefficient crossings.

Checks every integer 2 <= n <= 4614.  At the first k for which
3^q_k < 2^k, records whether T^k(n) >= n.  All comparisons are exact
integer comparisons; no floating point arithmetic is used.

This is a finite audit only.  It is used together with the external
Rozier--Terracol theorem that any paradoxical start not among their
small-start list must exceed 2.8e19.
"""

LIMIT = 4614


def first_coefficient_crossing(n: int):
    x = n
    q = 0
    pow3 = 1
    pow2 = 1
    k = 0

    while True:
        k += 1
        pow2 *= 2

        if x & 1:
            x = (3 * x + 1) // 2
            q += 1
            pow3 *= 3
        else:
            x //= 2

        if pow3 < pow2:
            return k, q, x


def main() -> None:
    bad = []
    max_crossing = (0, None, None, None)

    for n in range(2, LIMIT + 1):
        k, q, x = first_coefficient_crossing(n)
        if k > max_crossing[0]:
            max_crossing = (k, n, q, x)
        if x >= n:
            bad.append((n, k, q, x))

    print(f"range: 2..{LIMIT}")
    print(f"R1-type first-crossing paradoxical starts: {len(bad)}")
    if bad:
        for row in bad:
            print(row)

    k, n, q, x = max_crossing
    print(
        "largest first coefficient-crossing depth in audit: "
        f"k={k}, n={n}, q={q}, endpoint={x}"
    )

    assert not bad


if __name__ == "__main__":
    main()
