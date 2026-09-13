#!/usr/bin/env python3
"""Finite regression for MATH-125 correction envelope and q monotonicity."""
from itertools import combinations


def correction(d, positions):
    pos=set(positions)
    c=0
    q=0
    for j in range(d):
        if j in pos:
            c=3*c+(1<<j)
            q+=1
    return q,c


def main():
    word_classes=0
    words=0
    for d in range(1,13):
        for q in range(d+1):
            vals=[]
            for positions in combinations(range(d),q):
                q2,c=correction(d,positions)
                assert q2==q
                vals.append(c)
                words+=1
            cmin=0 if q==0 else 3**q-2**q
            cmax=0 if q==0 else (1<<(d-q))*(3**q-2**q)
            assert min(vals)==cmin
            assert max(vals)==cmax
            word_classes+=1

    LO=1<<71
    for d in range(1,80):
        for mult in (1,2,3,10,100):
            N=mult*LO
            prev=None
            for q in range(d+1):
                # Compare the integer numerator of U(d,q;N)+1 over 2^d.
                # U = 3^q N/2^d + (3/2)^q - 1.
                # Common positive denominator 2^d is enough after rewriting
                # cmax exactly.
                num=3**q*N + ((1<<(d-q))*(3**q-2**q) if q else 0)
                if prev is not None:
                    assert num>prev
                prev=num
    print('word_classes',word_classes)
    print('words',words)
    print('PASS MATH-125 sharp correction envelope regression')
    print('NO PAID-LAYER CLOSURE CLAIM')


if __name__=='__main__':
    main()
