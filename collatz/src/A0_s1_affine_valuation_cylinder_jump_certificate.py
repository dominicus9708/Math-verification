#!/usr/bin/env python3
"""Exact affine valuation-cylinder jump transducer.

Let a positive current-state family be

    Y(m) = y + A m,

where A is odd and m ranges over an integer interval.  For every finite
valuation a=v2(Y(m)), the condition is exactly one residue class

    m == rho_a (mod 2^(a+1)),

where

    rho_a = (2^a-y) A^(-1)  (mod 2^(a+1)).

Writing

    m = rho_a + 2^(a+1) k,

the accelerated Collatz evolution through the forced prefix 0^a 1 is

    Y' = (3Y+2^a)/2^(a+1)
       = y'_a + 3 A k.

Thus an affine cylinder is partitioned exactly by next-one position and each
nonempty valuation child is again an affine cylinder with odd coefficient.
The jump consumes a+1 parity bits and exactly one odd event.

This is a source-family theorem.  It does not by itself enforce ballot, H/L,
C4F, endpoint, tail, or Route-B predicates.
"""


def T(x: int) -> int:
    assert x > 0
    return (3 * x + 1) // 2 if x & 1 else x // 2


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def child_for_valuation(y: int, A: int, m_lo: int, m_hi: int, a: int):
    assert A & 1
    assert m_lo <= m_hi
    assert a >= 0
    M = 1 << (a + 1)
    rho = (((1 << a) - y) * pow(A, -1, M)) % M
    k_lo = ceil_div(m_lo - rho, M)
    k_hi = (m_hi - rho) // M
    if k_lo > k_hi:
        return None

    numer = 3 * (y + A * rho) + (1 << a)
    assert numer % M == 0
    y2 = numer // M
    A2 = 3 * A
    return rho, M, k_lo, k_hi, y2, A2


def direct_jump(Y: int, a: int):
    bits = []
    x = Y
    for _ in range(a + 1):
        bits.append(x & 1)
        x = T(x)
    assert tuple(bits) == (0,) * a + (1,)
    return x


# Exhaustive finite regression on many affine families.
for y in range(32):
    for A in range(1, 16, 2):
        m_lo, m_hi = 0, 31
        actual = {}
        for m in range(m_lo, m_hi + 1):
            Y = y + A * m
            if Y <= 0:
                continue
            a = v2(Y)
            actual.setdefault(a, []).append(m)

        recovered = set()
        for a, members in actual.items():
            child = child_for_valuation(y, A, m_lo, m_hi, a)
            assert child is not None
            rho, M, k_lo, k_hi, y2, A2 = child

            child_members = []
            for k in range(k_lo, k_hi + 1):
                m = rho + M * k
                assert m_lo <= m <= m_hi
                Y = y + A * m
                assert Y > 0
                assert v2(Y) == a
                got = direct_jump(Y, a)
                assert got == y2 + A2 * k
                child_members.append(m)
                recovered.add(m)

            assert child_members == members

        expected = {m for m in range(m_lo, m_hi + 1) if y + A * m > 0}
        assert recovered == expected


# The child coefficient remains odd, so the theorem is recursively closed.
for A in range(1, 100, 2):
    assert (3 * A) & 1

print("PASS A0 s=1 affine valuation-cylinder jump certificate")
print("family", "Y=y+A*m, A odd")
print("valuation_class", "m=rho_a mod 2^(a+1)")
print("forced_prefix", "0^a1")
print("child_family", "Y'=y'_a+3A*k")
print("endpoint_needed", False)
print("recursive_odd_coefficient", True)
print("status", "EXACT source-family jump; remaining formation predicates separate")
