#!/usr/bin/env python3
"""Exact finite bootstrap certificate for the first 18 ternary selectors of F_44.

We verify only the recursively sufficient representatives

    N = 4*(3^44 + sum_{i=0}^{17} a_i 3^i) + 3,
    a_i in {0,1},

not every integer in the surrounding interval.  For every one of the 2^18
representatives, the time-expanded accelerated Collatz map

    T(n) = (3n+1)/2 if n is odd, else n/2

is iterated until it first drops below its start.  Such a representative is
recursive in Ansari's sense.  Once all of these representatives are recursive,
recursive sufficiency advances the verified floor to the integer immediately
before the next F-element, namely

    4*(3^44 + 3^18) + 2.

All arithmetic is exact integer arithmetic.
"""

D = 18
BASE = 4 * 3**44 + 3
OLD_FLOOR = BASE - 1
NEW_FLOOR = 4 * (3**44 + 3**18) + 2
EXPECTED_MAX_TAU = 211
EXPECTED_RECORD_S = 188_369_256
EXPECTED_RECORD_N = 3_939_083_608_735_198_408_551


def T(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def first_descent(n: int, limit: int = 10_000) -> int:
    x = n
    for k in range(1, limit + 1):
        x = T(x)
        if x < n:
            return k
    raise RuntimeError(f"no descent within {limit} steps for {n}")


def main() -> None:
    powers = [3**i for i in range(D)]

    # Gray-code traversal updates S by one ternary weight at a time.
    S = 0
    prev_gray = 0
    max_tau = -1
    record_S = None
    record_N = None
    record_mask = None

    for index in range(1 << D):
        gray = index ^ (index >> 1)
        if index:
            diff = gray ^ prev_gray
            i = (diff & -diff).bit_length() - 1
            if (gray >> i) & 1:
                S += powers[i]
            else:
                S -= powers[i]
        prev_gray = gray

        n = BASE + 4 * S
        tau = first_descent(n)
        if tau > max_tau:
            max_tau = tau
            record_S = S
            record_N = n
            record_mask = gray

    assert max_tau == EXPECTED_MAX_TAU
    assert record_S == EXPECTED_RECORD_S
    assert record_N == EXPECTED_RECORD_N
    assert NEW_FLOOR - OLD_FLOOR == 4 * 3**18

    print("representatives checked:", 1 << D)
    print("maximum first-descent depth:", max_tau)
    print("record selector sum S:", record_S)
    print("record ternary-selector mask:", record_mask)
    print("record start N:", record_N)
    print("old verified floor:", OLD_FLOOR)
    print("new verified floor:", NEW_FLOOR)
    print("verified-floor increment:", NEW_FLOOR - OLD_FLOOR)


if __name__ == "__main__":
    main()
