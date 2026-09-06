#!/usr/bin/env python3
"""Regression certificate for the COV-1 companion-word merge calculus.

For a forward parity word w of length h with s odd bits, let C(w) be the
standard affine constant

    T^h(n) = (3^s n + C(w))/2^h.

A binary companion z has length h+3 and s+2 odd bits.  If

    D = (C(z)-8*C(w))/3^(s+2)

is integral, then the reversed companion is an admissible padded reverse word
from the h-step turning point on the corresponding 36*k+27 dyadic cylinder.
For k=2^(h-2)u+c the endpoint is exactly

    m = 2^(h+3)u + 32c + 24 - D,

so

    x-m = 2^h u + 4c + 3 + D.

Thus D=1 or 2 gives a positive uniform smaller merge for every c,u>=0.
Appending the same suffix bit to w and z preserves D exactly.

The infinite seed family proved symbolically is, for every r>=4,

    w_r  = 1^r 00,
    z1_r = 11100 1^(r-2) 01,   D=1,
    z2_r = 0110  1^(r-1) 01,   D=2.

The w_r form a prefix-free dyadic family of total k-density 1/8.

Finite loops below are regressions for the displayed algebra, not the proof.
"""

from fractions import Fraction
from itertools import product


def C(bits):
    c = 0
    s = 0
    for j, e in enumerate(bits):
        if e:
            c = 3*c + (1 << j)
            s += 1
    return c, s


def extend(bits, suffix):
    return tuple(bits) + tuple(suffix)


def defect(w, z):
    cw, s = C(w)
    cz, q = C(z)
    assert len(z) == len(w) + 3
    assert q == s + 2
    num = cz - 8*cw
    mod = 3 ** (s + 2)
    assert num % mod == 0
    return num // mod


def seed(r, D):
    assert r >= 4 and D in (1, 2)
    w = (1,)*r + (0,0)
    if D == 1:
        z = (1,1,1,0,0) + (1,)*(r-2) + (0,1)
    else:
        z = (0,1,1,0) + (1,)*(r-1) + (0,1)
    return w, z


def main():
    # Closed-form constants for the infinite family.
    for r in range(4, 31):
        w, z1 = seed(r, 1)
        _, z2 = seed(r, 2)
        cw, s = C(w)
        c1, q1 = C(z1)
        c2, q2 = C(z2)

        assert s == r
        assert q1 == q2 == r + 2
        assert cw == 3**r - 2**r
        assert c1 == 17*3**r - 8*2**r
        assert c2 == 26*3**r - 8*2**r
        assert defect(w, z1) == 1
        assert defect(w, z2) == 2

    # D is exactly invariant under a common suffix extension.
    for r in range(4, 9):
        for D in (1, 2):
            w, z = seed(r, D)
            for ell in range(0, 7):
                for suffix in product((0,1), repeat=ell):
                    assert defect(extend(w, suffix), extend(z, suffix)) == D

    # Prefix-free family density in the free parameter k.
    density = sum(Fraction(1, 2**r) for r in range(4, 200))
    # finite truncation plus exact geometric tail
    density += Fraction(1, 2**199)
    assert density == Fraction(1, 8)

    # Exact endpoint inequalities for D=1,2 are automatic for all c,u>=0:
    # m0 = 32c+24-D > 0 and x-m = 2^h*u+4c+3+D > 0.
    for D in (1, 2):
        for c in range(64):
            assert 32*c + 24 - D > 0
            for u in range(8):
                assert (1 << 6)*u + 4*c + 3 + D > 0

    print('SAFE companion-word seed-family regression')
    print('w_r = 1^r00, r>=4')
    print('D=1 companion: 11100 1^(r-2) 01')
    print('D=2 companion: 0110 1^(r-1) 01')
    print('prefix-free k-density = 1/8')
    print('GLOBAL COV-1: OPEN')


if __name__ == '__main__':
    main()
