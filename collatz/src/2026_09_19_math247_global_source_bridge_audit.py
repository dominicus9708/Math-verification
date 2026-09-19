#!/usr/bin/env python3
"""MATH-247 exact original-source bridge audit for frozen r=10 factors."""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location(
    "m65", HERE/"2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

R=10
LO=1<<71
Q0=72_057_431_991

EXPECTED_RECORDS=278_725
EXPECTED_MASS=27_557_263_803_397

def ceil_frac(x: Fraction) -> int:
    return -((-x.numerator)//x.denominator)

def bridge_interval(D0: Fraction, slope: Fraction, M: int):
    """Return [lo,hi) integer interval in [0,M) where D0+s*slope>0."""
    if M<=0:
        return None
    if slope==0:
        return (0,M) if D0>0 else None
    if slope>0:
        if D0>0:
            return (0,M)
        # s > -D0/slope
        first=(-D0//slope) if False else None
        x=(-D0)/slope
        first=x.numerator//x.denominator + 1
        if first>=M:
            return None
        if first<0:
            first=0
        return (first,M)
    # slope < 0
    if D0<=0:
        return None
    x=D0/(-slope)  # require s < x
    count=ceil_frac(x)
    if count<=0:
        return None
    return (0,min(M,count))

def floor_interval(B: int, step: int, M: int):
    if B>LO:
        return None
    count=(LO-B)//step+1
    count=min(M,count)
    return (0,count) if count>0 else None

def union_count(a,b):
    ints=[x for x in (a,b) if x is not None and x[0]<x[1]]
    if not ints:
        return 0
    ints.sort()
    lo,hi=ints[0]
    total=0
    for x,y in ints[1:]:
        if x<=hi:
            hi=max(hi,y)
        else:
            total+=hi-lo
            lo,hi=x,y
    total+=hi-lo
    return total

def full_factor(cell, leaf):
    (L,start_R,E0,q0,lo,hi,tmin,tmax,eps,gs,hcl,H,margin)=cell
    first,count,tres,mod,yres,coeff=leaf
    base_s=(first-tres)//mod
    B=yres+coeff*base_s
    A=start_R+(1<<L)*first
    Q=q0+R
    assert H==L+hcl
    assert coeff==3**Q
    return H,Q,A,B,count,lo

def main():
    total,safe,singleton,critical=m65.classify_cells(R)
    records=0
    mass=0
    bridge_mass=0
    floor_mass=0
    union_mass=0
    all_closed=partial=unchanged=0
    rem_max=0
    rem_records=0
    bridge_records=0

    for group in (singleton,critical):
        for cell in group:
            leaves,_=m65.negative_candidate_cylinders(cell,R)
            for leaf in leaves:
                H,Q,A,B,M,lo=full_factor(cell,leaf)
                records+=1
                mass+=M

                D0=lo*A-B-Fraction(Q0,3)
                slope=lo*(1<<H)-3**Q
                bi=bridge_interval(D0,slope,M)
                fi=floor_interval(B,3**Q,M)

                bc=0 if bi is None else bi[1]-bi[0]
                fc=0 if fi is None else fi[1]-fi[0]
                uc=union_count(bi,fi)

                bridge_mass+=bc
                floor_mass+=fc
                union_mass+=uc
                if bc:
                    bridge_records+=1

                rem=M-uc
                if rem==0:
                    all_closed+=1
                elif rem<M:
                    partial+=1
                    rem_records+=1
                    rem_max=max(rem_max,rem)
                else:
                    unchanged+=1
                    rem_records+=1
                    rem_max=max(rem_max,rem)

    assert records==EXPECTED_RECORDS
    assert mass==EXPECTED_MASS
    assert all_closed+partial+unchanged==records
    assert 0<=union_mass<=mass

    print("MATH-247_RESULT")
    print("records",records)
    print("mass",mass)
    print("bridge_records_nonempty",bridge_records)
    print("bridge_closed_mass_raw",bridge_mass)
    print("floor_closed_mass_raw",floor_mass)
    print("union_closed_mass",union_mass)
    print("remaining_mass",mass-union_mass)
    print("all_closed_records",all_closed)
    print("partial_records",partial)
    print("unchanged_records",unchanged)
    print("remaining_records",rem_records)
    print("max_remaining_cylinder_mass",rem_max)
    print("PASS MATH-247 exact original-source bridge audit")
    print("NO r10 CLOSURE CLAIM")

if __name__=="__main__":
    main()
