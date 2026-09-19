#!/usr/bin/env python3
"""MATH-238 affine-orientation audit for frozen low-paid full factors r=2..12.

For each exact negative-candidate factor
    N=A+2^H s, Y=B+3^Q s,
audit the signs of
    intercept gap d0=B-A
    slope gap ds=3^Q-2^H.

Orientation coherence means d0 and ds have the same strict sign, so the whole
cylinder is all-descending (both negative) or all-nondescending (both positive)
with no internal crossing in the represented parameter interval.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location("m65",HERE/"2026_09_11_math065_paid_count_18plus_closure_certificate.py")
m65=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

EXPECTED_COUNTS={
12:1_053_555,11:605_972,10:278_725,9:141_002,8:65_811,7:29_342,
6:15_133,5:6_525,4:3_675,3:1_873,2:1_116,
}

def full_factor(cell,leaf,r):
    L,start_R,E0,q0,lo,hi,tmin,tmax,eps,gs,hcl,H,margin=cell
    first,count,tres,mod,yres,coeff=leaf
    assert coeff==3**(q0+r)
    base_s=(first-tres)//mod
    B=yres+coeff*base_s
    A=start_R+(1<<L)*first
    Q=q0+r
    return H,Q,A,B,count

def audit(r):
    total,safe,singleton,critical=m65.classify_cells(r)
    same=opposite=zero=0
    descend_records=survive_records=0
    descend_mass=survive_mass=0
    records=0
    for group in (singleton,critical):
        for cell in group:
            leaves,_=m65.negative_candidate_cylinders(cell,r)
            for leaf in leaves:
                H,Q,A,B,M=full_factor(cell,leaf,r)
                d0=B-A
                ds=3**Q-(1<<H)
                records+=1
                if d0==0 or ds==0:
                    zero+=1
                elif (d0>0)==(ds>0):
                    same+=1
                else:
                    opposite+=1
                if d0<0 and ds<0:
                    descend_records+=1; descend_mass+=M
                elif d0>=0 and ds>=0:
                    survive_records+=1; survive_mass+=M
    assert records==EXPECTED_COUNTS[r]
    return records,same,opposite,zero,descend_records,survive_records,descend_mass,survive_mass

def main():
    print("r records same_sign opposite zero whole_descend whole_survive descend_mass survive_mass")
    for r in range(12,1,-1):
        x=audit(r)
        print(r,*x)
    print("PASS MATH-238 low-paid affine-orientation audit")
    print("NO NEW LAYER CLOSURE CLAIM")

if __name__=="__main__":
    main()
