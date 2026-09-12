#!/usr/bin/env python3
"""MATH-093: exact dyadic power-of-two source-envelope lemma.

For an exact family 0<=s<M set R=ceil(log2 M) and enlarge it to
0<=s<2^R.  This is a superset of the actual source family.

An edge of dyadic resolution h selects one residue r mod 2^h.
If h<=R, the enlarged family always contains that residue and after
s=r+2^h u the envelope child is exactly 0<=u<2^(R-h).
Thus R'=R-h exactly.

If h>R, the envelope contains at most one selected source and compatibility is
r<2^R; the terminal overshoot is z=h-R.

With potential H_R=-lambda R, every multi-edge has exact reduced contribution
p, while the terminal edge has p-lambda z.
"""
from fractions import Fraction

LAM=Fraction(19,503)


def ceil_log2(m:int)->int:
    assert m>=1
    return 0 if m==1 else (m-1).bit_length()


def envelope_child_count(R:int,h:int,r:int)->int:
    assert 0<=r<(1<<h)
    M=1<<R
    if r>=M:
        return 0
    return (M-1-r)//(1<<h)+1


def main()->None:
    for R in range(0,13):
        for h in range(1,13):
            for r in range(1<<h):
                c=envelope_child_count(R,h,r)
                if h<=R:
                    assert c==(1<<(R-h))
                    Rp=R-h
                    # -lambda*h + H(R')-H(R) = 0 for H=-lambda R
                    assert -LAM*h - LAM*Rp + LAM*R == 0
                else:
                    assert c in (0,1)
                    assert (c==1)==(r<(1<<R))
                    if c==1:
                        z=h-R
                        assert -LAM*h + LAM*R == -LAM*z

    # Every exact family is contained in its dyadic envelope.
    for M in range(1,1000):
        R=ceil_log2(M)
        assert M<=1<<R
        if R>0:
            assert (1<<(R-1))<M

    print("PASS MATH-093 dyadic resolution envelope")


if __name__=='__main__':
    main()
