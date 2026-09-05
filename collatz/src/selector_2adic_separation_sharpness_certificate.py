#!/usr/bin/env python3
"""Exact checks for the sharp selector 2-adic separation theorem."""


def v2(n: int) -> int:
    n = abs(n)
    assert n
    return (n & -n).bit_length() - 1


def n_value(m: int, mask: int) -> int:
    s = 0
    p = 1
    for i in range(m):
        if (mask >> i) & 1:
            s += p
        p *= 3
    return 4 * (3**m + s) + 3


def k_sep(m: int) -> int:
    return (2 * (3**m - 1)).bit_length()


def k_addr(m: int) -> int:
    return (6 * 3**m + 1).bit_length()


def exhaustive_small() -> None:
    for m in range(1, 10):
        vals = [n_value(m, mask) for mask in range(1 << m)]
        max_v = -1
        for i in range(len(vals)):
            for j in range(i):
                max_v = max(max_v, v2(vals[i] - vals[j]))
        A = (3**m - 1) // 2
        expected = 2 + (A.bit_length() - 1)
        assert max_v == expected
        assert k_sep(m) == expected + 1
        residues = {x % (1 << k_sep(m)) for x in vals}
        assert len(residues) == len(vals)


def balanced_ternary(n: int, m: int):
    """Return m balanced ternary digits for |n| <= (3^m-1)/2."""
    out = []
    x = n
    for _ in range(m):
        r = x % 3
        if r == 0:
            d = 0
        elif r == 1:
            d = 1
        else:
            d = -1
            x += 1
        out.append(d)
        x = (x - d) // 3
    assert x == 0
    return out


def sharp_witness(m: int):
    A = (3**m - 1) // 2
    s = 1 << (A.bit_length() - 1)
    eps = balanced_ternary(s, m)
    a = 0
    b = 0
    for i, e in enumerate(eps):
        if e == 1:
            a |= 1 << i
        elif e == -1:
            b |= 1 << i
    na = n_value(m, a)
    nb = n_value(m, b)
    assert na - nb == 4 * s
    assert v2(na - nb) == k_sep(m) - 1
    return na, nb


def main() -> None:
    exhaustive_small()
    assert k_addr(44) == 73
    assert k_sep(44) == 71
    assert k_addr(45) == 74
    assert k_sep(45) == 73
    for m in (10, 44, 45, 100):
        na, nb = sharp_witness(m)
        assert na != nb
        assert (na - nb) % (1 << (k_sep(m) - 1)) == 0
        assert (na - nb) % (1 << k_sep(m)) != 0
    print("selector 2-adic separation sharpness: PASS")
    print("m44: K_addr=73 K_sep=71")
    print("m45: K_addr=74 K_sep=73")


if __name__ == "__main__":
    main()
