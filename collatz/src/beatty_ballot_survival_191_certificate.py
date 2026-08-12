#!/usr/bin/env python3
"""Exact certificate for the Beatty-ballot survival theorem through depth 191.

For N >= V0 = 4*3^44+2 with N == 3 (mod 4), the first two time-expanded
parity symbols are forced odd.  At fixed prefix length j and odd count q,
this script computes the exact maximum affine correction numerator R_j by
placing every optional odd symbol as far right as possible.  It then checks
that every subcritical coefficient prefix satisfies T^j(N) < N uniformly for
all N >= V0 through j=191, and that the simple uniform inequality first fails
at j=192.

It also counts the exact Beatty-ballot survivor language by dynamic
programming on the odd count only.
"""

from collections import defaultdict

V0 = 4 * 3**44 + 2


def ceil_log3_2_times(j: int) -> int:
    """Return ceil(j*log_3 2) using exact integer comparison only."""
    # Small monotone search is enough for the certificate range.
    q = 0
    p3 = 1
    p2 = 1 << j
    while p3 < p2:
        q += 1
        p3 *= 3
    return q


def rmax_forced_oo(j: int, q: int) -> int:
    """Maximum correction R_j at fixed length j, odd count q, initial OO."""
    assert 2 <= q <= j
    m = q - 2
    return 5 * 3**m + 2 ** (j - m) * (3**m - 2**m)


def uniform_subcritical_safe(j: int, q: int) -> bool:
    """Whether every such prefix forces descent for every N >= V0."""
    assert 3**q < 2**j
    rmax = rmax_forced_oo(j, q)
    return rmax < V0 * (2**j - 3**q)


def ballot_count(B: int) -> int:
    """Count forced-OO parity words satisfying q_i >= ceil(i log_3 2)."""
    dp = {0: 1}
    for j in range(1, B + 1):
        threshold = ceil_log3_2_times(j)
        nd = defaultdict(int)
        bits = (1,) if j <= 2 else (0, 1)
        for q, c in dp.items():
            for bit in bits:
                q2 = q + bit
                if q2 >= threshold:
                    nd[q2] += c
        dp = nd
    return sum(dp.values())


def main() -> None:
    # Exact uniform theorem through 191.
    for j in range(2, 192):
        k = ceil_log3_2_times(j)
        for q in range(2, k):
            assert uniform_subcritical_safe(j, q), (j, q)

    # At 192 the worst-case uniform comparison first fails.
    j = 192
    k = ceil_log3_2_times(j)
    bad = [q for q in range(2, k) if not uniform_subcritical_safe(j, q)]
    assert bad, "expected first loss of the simple uniform bound at j=192"
    assert max(bad) == 121

    expected = {
        28: 3_524_586,
        50: 3_734_259_929_440,
        100: 302_560_669_500_543_257_546_172_187,
        150: 36_669_896_893_826_317_415_292_528_305_119_465_918_904,
        191: 14_603_890_878_430_725_479_972_220_655_907_544_270_840_991_721_772_560,
    }

    for B, target in expected.items():
        got = ballot_count(B)
        assert got == target, (B, got, target)
        print(B, got, got / (1 << (B - 2)))

    print("uniform exact Beatty-ballot equivalence certified through depth 191")
    print("simple worst-case additive bound first loses uniformity at depth 192")


if __name__ == "__main__":
    main()
