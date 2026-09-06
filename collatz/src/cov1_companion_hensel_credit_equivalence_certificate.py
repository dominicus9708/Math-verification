#!/usr/bin/env python3
"""Regression certificate for the D=1/2 companion--Hensel equivalence.

For a binary word w beginning with 1, length h, weight s and affine constant C:

D=1 companion z (length h+3, weight s+2) exists iff
    z = 111 y,
    |y|=h, |y|_1=s-1,
    C(y)=C(w)+3^(s-1).

D=2 companion exists iff
    z = 011 y,
    |y|=h, |y|_1=s,
    C(y)=C(w)+3^s.

The D=2 condition is therefore exactly a same-length, same-weight full-Hensel
competitor with unit credit Delta=(C(y)-C(w))/3^s=1.

The proof is algebraic.  Finite enumeration below is a regression only.
"""

from itertools import product


def C(bits):
    c = 0
    s = 0
    for j, e in enumerate(bits):
        if e:
            c = 3*c + (1 << j)
            s += 1
    return c, s


def all_by_len_weight(h):
    tab = {}
    for bits in product((0,1), repeat=h):
        c,s = C(bits)
        key=(s,c)
        assert key not in tab, 'exact correction constant should encode word uniquely at fixed weight'
        tab[key]=bits
    return tab


def companion_direct(w,D,tabz):
    cw,s=C(w); h=len(w); q=s+2
    target=8*cw+D*(3**q)
    return tabz.get((q,target))


def main():
    for h in range(1,10):
        tabw=all_by_len_weight(h)
        tabz=all_by_len_weight(h+3)
        for (s,cw),w in tabw.items():
            if not w or w[0]!=1 or s==0:
                continue

            # D=1 exact equivalence.
            z1=companion_direct(w,1,tabz)
            y1=tabw.get((s-1,cw+3**(s-1))) if s>=1 else None
            assert (z1 is not None)==(y1 is not None)
            if z1 is not None:
                assert z1[:3]==(1,1,1)
                assert z1[3:]==y1
                assert C(z1)[0]-8*cw==3**(s+2)

            # D=2 exact equivalence.
            z2=companion_direct(w,2,tabz)
            y2=tabw.get((s,cw+3**s))
            assert (z2 is not None)==(y2 is not None)
            if z2 is not None:
                assert z2[:3]==(0,1,1)
                assert z2[3:]==y2
                assert C(z2)[0]-8*cw==2*3**(s+2)
                assert (C(y2)[0]-cw)//(3**s)==1

    print('SAFE companion/Hensel-credit regression')
    print('D=1 <=> lower-weight +3^(s-1) correction successor')
    print('D=2 <=> same-weight unit full-Hensel credit successor')
    print('GLOBAL COV-1: OPEN')


if __name__=='__main__':
    main()
