#!/usr/bin/env python3
"""MATH-092: normalized 2-adic address transducer identity.

For a current exact family

    B + 3^Q s, 0<=s<M,

set X = 3^{-Q} B in Z_2.  For an edge with source A+2^h t and
target B_e+3^q t, define

    eta = 3^{-Q} A,
    beta = 3^{-(Q+q)} B_e.

The required source residue is

    r = eta-X mod 2^h.

If r<M, the exact child normalized intercept is

    X' = (X+r-eta)/2^h + beta.

Thus address evolution is subtract/low-bit selection/right-shift/add in the
2-adic integers.  Finite precision P bits propagates exactly to P-h bits.
"""
import random


def inv3(Q: int, bits: int) -> int:
    mod=1<<bits
    return pow(pow(3,Q,mod),-1,mod)


def original_step(B,Q,M,A,h,Be,qe):
    mod=1<<h
    r=((A-B)*inv3(Q,h))%mod
    if r>=M:
        return None
    cnt=(M-1-r)//mod+1
    d=(B+3**Q*r-A)//mod
    Bp=Be+3**qe*d
    return r,cnt,Bp,Q+qe


def normalized_step(X,Q,M,A,h,Be,qe,P):
    assert P>=h
    modP=1<<P
    eta=(A*inv3(Q,P))%modP
    r=(eta-X)% (1<<h)
    if r>=M:
        return None
    cnt=(M-1-r)//(1<<h)+1
    # X+r-eta is divisible by 2^h in Z/2^P after choosing the representative
    delta=(X+r-eta)%modP
    assert delta%(1<<h)==0
    high=(delta>>h)%(1<<(P-h))
    beta=(Be*inv3(Q+qe,P-h))%(1<<(P-h))
    Xp=(high+beta)%(1<<(P-h))
    return r,cnt,Xp,Q+qe


def main():
    rng=random.Random(20260912)
    for _ in range(20000):
        Q=rng.randrange(0,20); qe=rng.randrange(1,12); h=rng.randrange(1,13)
        P=rng.randrange(h+4,h+20)
        M=rng.randrange(1,1<<min(h+2,10))
        A=rng.randrange(-(1<<18),1<<18)
        B=rng.randrange(-(1<<18),1<<18)
        Be=rng.randrange(-(1<<18),1<<18)
        o=original_step(B,Q,M,A,h,Be,qe)
        X=(B*inv3(Q,P))%(1<<P)
        n=normalized_step(X,Q,M,A,h,Be,qe,P)
        if o is None:
            assert n is None
            continue
        r,cnt,Bp,Qp=o
        rn,cntn,Xp,Qpn=n
        assert (r,cnt,Qp)==(rn,cntn,Qpn)
        expect=(Bp*inv3(Qp,P-h))%(1<<(P-h))
        assert Xp==expect

    print("PASS MATH-092 normalized 2-adic address transducer")


if __name__=='__main__':
    main()
