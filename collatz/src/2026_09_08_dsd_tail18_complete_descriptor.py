#!/usr/bin/env python3
"""MATH-018: exact 18-step tail complete descriptor for depth 61 -> 79.

This certificate verifies the finite descriptor

    G18(r) = (H18(r), s18(r), T^18(r)),   0 <= r < 2^18,

where H18 is the least base q61 threshold needed for coefficient survival
through depths 62..79.  For every n = h*2^18 + r, the first 18 shortcut
parity bits depend only on r, hence

    T^18(n) = T^18(r) + h*3^s18(r).

No Collatz proof is claimed.
"""

from collections import Counter

L = 18
MOD = 1 << L


def T(n: int) -> int:
    return (3 * n + 1) // 2 if n & 1 else n // 2


def min_q_survival(k: int) -> int:
    q = 0
    p3 = 1
    target = 1 << k
    while p3 < target:
        p3 *= 3
        q += 1
    return q


QMIN = tuple([0] + [min_q_survival(k) for k in range(1, 80)])


def descriptor(r: int):
    n = r
    s = 0
    H = -10**9
    for j in range(1, L + 1):
        b = n & 1
        s += b
        H = max(H, QMIN[61 + j] - s)
        n = T(n)
    return H, s, n


def direct_tail(n: int):
    x = n
    bits = []
    s = 0
    for _ in range(L):
        b = x & 1
        bits.append(b)
        s += b
        x = T(x)
    return tuple(bits), s, x


def direct_survives(r: int, q61: int) -> bool:
    n = r
    q = q61
    for j in range(1, L + 1):
        b = n & 1
        q += b
        if q < QMIN[61 + j]:
            return False
        n = T(n)
    return True


def main():
    table = [descriptor(r) for r in range(MOD)]

    # Exact H18 distribution over all 2^18 tail residues.
    dist = Counter(H for H, _, _ in table)
    expected = {
        39: 16936,
        40: 42414,
        41: 55274,
        42: 55882,
        43: 44050,
        44: 27498,
        45: 13384,
        46: 5002,
        47: 1394,
        48: 274,
        49: 34,
        50: 2,
    }
    assert dict(sorted(dist.items())) == expected
    assert sum(dist.values()) == MOD
    assert QMIN[79] == 50

    # Descriptor survival gate is exact for every r and every relevant q61.
    for r, (H, _, _) in enumerate(table):
        for q61 in range(39, 62):
            assert direct_survives(r, q61) == (q61 >= H)

    # The first 18 parity bits are invariant under adding h*2^18, and the
    # endpoint is affine in h.  Exhaustively regress every residue for several
    # deterministic h values spanning the current address scale.
    HTEST = (0, 1, 2, 17, 339, 1024, 1363)
    for r, (_, s, tr) in enumerate(table):
        base_bits, base_s, base_t = direct_tail(r)
        assert base_s == s and base_t == tr
        p3 = 3 ** s
        for h in HTEST:
            bits, s2, out = direct_tail(h * MOD + r)
            assert bits == base_bits
            assert s2 == s
            assert out == tr + h * p3

    # Cumulative number of tail residues surviving for each low-surplus q61.
    cumulative = {
        q: sum(c for H, c in expected.items() if H <= q)
        for q in range(39, 51)
    }
    assert cumulative == {
        39: 16936,
        40: 59350,
        41: 114624,
        42: 170506,
        43: 214556,
        44: 242054,
        45: 255438,
        46: 260440,
        47: 261834,
        48: 262108,
        49: 262142,
        50: 262144,
    }

    print("PASS")
    print("G18(r)=(H18,s18,T18) exact for all 2^18 residues")
    print("H18 distribution:")
    for H in sorted(expected):
        print(H, expected[H])
    print("cumulative survivors:")
    for q in cumulative:
        print(q, cumulative[q])
    print("depth79 q_min =", QMIN[79])
    print("NO COMPLETE COLLATZ PROOF CLAIM")


if __name__ == "__main__":
    main()
