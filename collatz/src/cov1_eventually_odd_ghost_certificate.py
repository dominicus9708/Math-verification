#!/usr/bin/env python3
"""Regression certificate for the eventually-all-odd ghost terminal lemma.

If a finite shortcut parity prefix p of length H, odd count s and affine
constant C(p) is followed by 1 forever, the state after H steps must be the
unique all-odd 2-adic fixed point -1.  Hence the initial value is

    N = -(2^H + C(p))/3^s < 0.

Therefore no positive ordinary integer can have an eventually-all-odd infinite
parity sequence.  In particular the all-ones path for 36*k+27 has
N=-1 and k=-7/9 in Z_2, not k in N_0.

The companion calculation for w=1^h is also regressed: any length-(h+3)
companion with h+2 ones has one zero at position j and would have defect

    D = 1/9 + (2/3)^j,

which is never an integer.  Hence the all-ones ghost survives the companion
congruence at every finite depth, as it must.
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


def main():
    # All-ones companion obstruction regression.
    for h in range(2, 25):
        w = (1,)*h
        cw, s = C(w)
        assert cw == 3**h - 2**h
        assert s == h

        for j in range(h+3):
            z = tuple(0 if i == j else 1 for i in range(h+3))
            cz, q = C(z)
            assert q == h+2
            expected = 3**(h+2) + (2**j)*3**(h+2-j) - 2**(h+3)
            assert cz == expected
            num = cz - 8*cw
            # D = 1/9 + (2/3)^j is not integral.
            assert num % (3**(h+2)) != 0

    # Eventually-all-odd negative-rational formula for representative prefixes.
    for H in range(1, 9):
        for bits in product((0,1), repeat=H):
            c, s = C(bits)
            if s == 0:
                continue
            N = -Fraction((1 << H) + c, 3**s)
            assert N < 0
            # Exact affine formula sends N to -1 after the prefix.
            assert Fraction((3**s)*N + c, 1 << H) == -1

    # Pure all-ones ray in the progression coordinate.
    N = Fraction(-1,1)
    k = (N - 27) / 36
    assert k == Fraction(-7,9)
    assert k < 0

    print('SAFE eventually-all-odd ghost regression')
    print('all-ones path: N=-1, k=-7/9')
    print('every eventually-all-odd path has negative rational initial N')
    print('GLOBAL COV-1: OPEN; terminal target = prove all infinite survivors eventually odd')


if __name__ == '__main__':
    main()
