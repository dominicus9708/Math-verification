#!/usr/bin/env python3
"""MATH-229 algebraic safe-prefix contraction regression."""

from fractions import Fraction
import random

LAM = Fraction(19,503)
ZMIN = {2:1,3:2,4:3,5:6,6:7,7:8,8:10,9:11,10:13}

def ceil_log2(M):
    return 0 if M==1 else (M-1).bit_length()

def compose(A,B,H,Q,M,Ae,Be,h,q):
    mod=1<<h
    r=((Ae-B)*pow(pow(3,Q,mod),-1,mod))%mod
    if r>=M:
        return None
    M2=1+(M-1-r)//mod
    u0=(B+(3**Q)*r-Ae)//mod
    assert B+(3**Q)*r-Ae == mod*u0
    return (
        A+(1<<H)*r,
        Be+(3**q)*u0,
        H+h,
        Q+q,
        M2,
    )

def main():
    random.seed(229)
    checked=0

    # Exact affine-composition regression on random canonical cylinders.
    for _ in range(5000):
        H=random.randrange(0,20)
        Q=random.randrange(0,14)
        M=random.randrange(1,500)
        A=random.randrange(0,1<<max(H,1)) if H else random.randrange(0,10)
        B=random.randrange(0,10000)

        h=random.randrange(1,12)
        q=random.randrange(0,h+1)
        # Choose one compatible source residue from a random family member.
        s0=random.randrange(0,M)
        Y=B+(3**Q)*s0
        Ae=Y%(1<<h)
        # Arbitrary target intercept for canonical second factor.
        Be=random.randrange(0,10000)

        out=compose(A,B,H,Q,M,Ae,Be,h,q)
        assert out is not None
        A2,B2,H2,Q2,M2=out

        # Every child parameter u reproduces both composed affine formulas.
        mod=1<<h
        r=((Ae-B)*pow(pow(3,Q,mod),-1,mod))%mod
        u0=(B+(3**Q)*r-Ae)//mod
        for u in range(min(M2,5)):
            s=r+mod*u
            src_old=A+(1<<H)*s
            src_new=A2+(1<<H2)*u
            assert src_old==src_new

            mid=B+(3**Q)*s
            t=u0+(3**Q)*u
            assert mid==Ae+mod*t

            end2=Be+(3**q)*t
            end_comp=B2+(3**Q2)*u
            assert end2==end_comp

        checked+=1

    # Reserve algebra and selector fanout ceilings.
    for R in range(0,41):
        for r,z in ZMIN.items():
            Lstar=R+z
            assert Lstar<=53
            assert Lstar+1<=54

    print("PASS MATH-229 safe-prefix composition regression")
    print("affine_cases",checked)
    print("max_first_danger_length",53)
    print("max_raw_first_danger_phase_cells",54)
    print("NO r10 CLOSURE CLAIM")

if __name__=="__main__":
    main()
