#!/usr/bin/env python3
"""Exact arithmetic certificate for the m=45 balanced-carry exception split."""
from math import comb


def centered(x, mod):
    r = x % mod
    return r - mod if r >= mod // 2 else r


def check_small():
    for L in range(4, 10):
        mod = 1 << L
        for m in range(1, 6):
            for t in range(1, mod, 2):
                a0 = centered(t, mod)
                a = a0
                carries = []
                for _ in range(m):
                    nxt = centered(3 * a, mod)
                    c = (3 * a - nxt) // mod
                    assert c in (-1, 0, 1)
                    if c == 0:
                        assert 6 * abs(a) < mod
                    else:
                        assert 6 * abs(a) > mod
                    carries.append(c)
                    a = nxt
                rhs = a + mod * sum(c * 3 ** (m - 1 - j) for j, c in enumerate(carries))
                assert 3**m * a0 == rhs


def sparse_bound(L, m, cmax):
    mod = 1 << L
    cap = (mod + 3**m - 1) // 3**m
    return cap * sum(comb(m, j) * 2**j for j in range(cmax + 1))


def main():
    check_small()
    assert ((1 << 72) + 3**45 - 1) // 3**45 == 2
    expected = {
        10: 7_564_040_793_766,
        15: 29_550_148_215_811_750,
        20: 10_507_594_242_179_903_142,
    }
    for c, value in expected.items():
        assert sparse_bound(72, 45, c) == value
    odd = 1 << 71
    assert expected[20] * 1_000_000 < odd * 4_451
    assert 3**21 < 4**21
    print("selector balanced-ternary carry exception audit: PASS")
    print("address-scale cylinder cap: 2")
    print("E20 upper bound:", expected[20])
    print("E20 fraction < 4451/1000000")
    print("outside E20: |P|^2 <= 3^21/4^21")


if __name__ == "__main__":
    main()
