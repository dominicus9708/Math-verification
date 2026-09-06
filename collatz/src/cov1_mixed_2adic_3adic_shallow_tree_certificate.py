#!/usr/bin/env python3
"""Exact finite-symbolic mixed-certificate tree for x=36*k+27.

Components:
  * forward affine descent cylinders through h<=8;
  * shifted reverse anchors h=1,2,3;
  * exact inverse words through q<=16;
  * CRT combination of dyadic forward cylinders and triadic inverse cylinders.

The resulting natural-density coverage is asserted exactly as

    6011273 / 8503056 ~= 0.7069544173294872.

This is FINITE ONLY.  It does not imply a limiting density and does not prove
all of 36*N0+27 recursive.
"""

from fractions import Fraction
from itertools import combinations


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def pmax(q: int) -> int:
    target = 3 ** (q - 1)
    p = target.bit_length() - 1
    if (1 << p) >= target:
        p -= 1
    return p


def branch_anchor(h: int, c: int):
    """For h>=2 and k=2^(h-2)u+c, return T^h(36k+27)=A*u+B and odd count s."""
    assert h >= 2

    def eval_u(u):
        k = (1 << (h - 2)) * u + c
        z = 36 * k + 27
        s = 0
        for _ in range(h):
            if z & 1:
                s += 1
            z = T(z)
        return z, s

    B, s0 = eval_u(0)
    z1, s1 = eval_u(1)
    assert s0 == s1
    A = z1 - B
    assert A == 3 ** (s0 + 2)
    return A, B, s0


def anchor_data(h: int, c: int = 0):
    if h == 1:
        return dict(h=1, a=0, c=0, A=54, B=41, s=1)
    A, B, s = branch_anchor(h, c)
    return dict(h=h, a=h - 2, c=c, A=A, B=B, s=s)


def valuation3(n: int):
    v = 0
    while n % 3 == 0:
        n //= 3
        v += 1
    return v, n


def branch_direct(h: int, c: int) -> bool:
    A, B, _ = branch_anchor(h, c)
    a = h - 2
    XA = 36 * (1 << a)
    XB = 36 * c + 27
    return A <= XA and B < XB


def prefix_free_direct(H: int):
    out = []
    for h in range(2, H + 1):
        a = h - 2
        for c in range(1 << a):
            if not branch_direct(h, c):
                continue
            if any(a0 <= a and c % (1 << a0) == c0 for a0, c0 in out):
                continue
            out.append((a, c))
    return out


def anchor_q_residues(h: int, c: int, q: int):
    d = anchor_data(h, c)
    A, B, s, a = d["A"], d["B"], d["s"], d["a"]
    v, unitA = valuation3(A)
    if q < v or q <= s:
        return set()

    P = h - 1 + pmax(q - s + 1)
    if P + 1 < q:
        return set()

    mod = 3 ** q
    base_mod = 3 ** v
    rmod = 3 ** (q - v)
    inv_unit = pow(unitA, -1, rmod) if rmod > 1 else 0

    term = [
        [(3 ** j) * pow(2, -p - 1, mod) % mod for p in range(P + 1)]
        for j in range(q)
    ]

    residues = set()
    for pre in combinations(range(P + 1), v):
        check = sum((3 ** j) * pow(2, -p - 1, base_mod) for j, p in enumerate(pre)) % base_mod
        if check != B % base_mod:
            continue
        rem = q - v
        if P - pre[-1] < rem:
            continue
        fixed = sum(term[j][p] for j, p in enumerate(pre)) % mod

        for rest in combinations(range(pre[-1] + 1, P + 1), rem):
            pos = pre + rest
            S = fixed
            for j, p in enumerate(rest, start=v):
                S += term[j][p]
            S %= mod

            u = ((((S - B) // base_mod) * inv_unit) % rmod) if rmod > 1 else 0

            K = pos[-1] + 1
            C = sum((3 ** j) * (2 ** (K - 1 - p)) for j, p in enumerate(pos))
            numerator = (2 ** K) * (A * u + B) - C
            assert numerator % mod == 0
            m = numerator // mod

            k = (1 << a) * u + c
            x = 36 * k + 27
            if 0 < m < x:
                residues.add(u)

    return residues


def prefix_free_anchor(h: int, c: int, Q: int):
    d = anchor_data(h, c)
    v, _ = valuation3(d["A"])
    raw = []
    for q in range(v, Q + 1):
        b = q - v
        for r in anchor_q_residues(h, c, q):
            raw.append((b, r))

    out = []
    for b, r in sorted(raw):
        if any(b0 <= b and r % (3 ** b0) == r0 for b0, r0 in out):
            continue
        out.append((b, r))
    return out


def expand_triadic(cylinders, B: int, transform):
    M = 3 ** B
    mask = bytearray(M)
    for b, r in cylinders:
        period = 3 ** b
        rr = transform(b, r) % period
        for x in range(rr, M, period):
            mask[x] = 1
    return mask


def main():
    # Forward exact descent through h<=8.
    direct = prefix_free_direct(8)
    assert direct == [
        (2, 2),
        (3, 4), (3, 7),
        (5, 3), (5, 8), (5, 21),
        (6, 9), (6, 19), (6, 24), (6, 37), (6, 43), (6, 48), (6, 61),
    ]

    forward_density = sum(Fraction(1, 1 << a) for a, _ in direct)
    assert forward_density == Fraction(45, 64)

    surviving_mod64 = [
        c for c in range(64)
        if not any(c % (1 << a) == c0 for a, c0 in direct)
    ]
    assert len(surviving_mod64) == 19
    even_survivors = sum((c & 1) == 0 for c in surviving_mod64)
    odd_survivors = len(surviving_mod64) - even_survivors
    assert (even_survivors, odd_survivors) == (4, 15)

    # Reverse anchors through q<=16.
    h1 = prefix_free_anchor(1, 0, 16)
    h2 = prefix_free_anchor(2, 0, 16)
    h30 = prefix_free_anchor(3, 0, 16)
    h31 = prefix_free_anchor(3, 1, 16)

    assert len(h1) == 742
    assert len(h2) == 994
    assert len(h30) == 994
    assert len(h31) == 213

    B = max(b for b, _ in h1 + h2 + h30 + h31)
    assert B == 12
    M3 = 3 ** B

    common = expand_triadic(h1 + h2, B, lambda b, r: r)
    even = bytearray(common)
    odd = bytearray(common)

    # At h=3, k=2u+c, so the u-cylinder maps to k == 2r+c mod 3^b.
    add_even = expand_triadic(h30, B, lambda b, r: 2 * r)
    add_odd = expand_triadic(h31, B, lambda b, r: 2 * r + 1)

    for i in range(M3):
        if add_even[i]:
            even[i] = 1
        if add_odd[i]:
            odd[i] = 1

    common_count = sum(common)
    even_count = sum(even)
    odd_count = sum(odd)

    assert common_count == 6848
    assert even_count == 6848
    assert odd_count == 6857

    mixed_density = (
        forward_density
        + Fraction(even_survivors, 64) * Fraction(even_count, M3)
        + Fraction(odd_survivors, 64) * Fraction(odd_count, M3)
    )

    assert mixed_density == Fraction(6011273, 8503056)

    print("SAFE finite mixed 2-adic/3-adic certificate")
    print("forward prefix-free density h<=8:", forward_density)
    print("survivors mod 64: even=4, odd=15")
    print("triadic common/even/odd counts at depth 12:", common_count, even_count, odd_count)
    print("mixed exact density:", mixed_density)
    print("mixed decimal density:", float(mixed_density))
    print("GLOBAL COV-1: OPEN")


if __name__ == "__main__":
    main()
