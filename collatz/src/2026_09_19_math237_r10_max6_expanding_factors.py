#!/usr/bin/env python3
"""MATH-237 exact expansion-run bound under total odd count <=24."""

from fractions import Fraction

QMAX=24

def emin(q):
    h=(3**q).bit_length()-1
    r=Fraction(3**q,2**h)
    assert 1<r<2
    return r

def main():
    # best[(total_q,n)] = (minimum product, witness sequence)
    best={(0,0):(Fraction(1),())}

    for total in range(QMAX+1):
        for n in range(QMAX+1):
            item=best.get((total,n))
            if item is None:
                continue
            prod,seq=item
            for q in range(1,QMAX-total+1):
                p=prod*emin(q)
                key=(total+q,n+1)
                if key not in best or p<best[key][0]:
                    best[key]=(p,seq+(q,))

    mins={}
    for n in (5,6,7):
        candidates=[
            (prod,total,seq)
            for (total,nn),(prod,seq) in best.items()
            if nn==n and total<=QMAX
        ]
        prod,total,seq=min(candidates,key=lambda x:x[0])
        mins[n]=(prod,total,seq)
        print("n",n,"total_q",total,"product",prod,"sequence",seq)

    assert mins[5][0]==Fraction(3**20,2**31)
    assert mins[6][0]==Fraction(3**22,2**34)
    assert mins[7][0]==Fraction(3**24,2**37)
    assert mins[6][0] < 2
    assert mins[7][0] > 2
    assert mins[7][2] == (2,2,2,2,2,2,12)

    print("PASS MATH-237 maximum consecutive expanding factors = 6")
    print("NO r10 LAYER CLOSURE CLAIM")

if __name__=="__main__":
    main()
