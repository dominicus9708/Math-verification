#!/usr/bin/env python3
"""MATH-248 headroom diagnostic for the MATH-247 original-source bridge."""

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
Q0=72_057_431_991

def full_factor(cell, leaf):
    (L,start_R,E0,q0,lo,hi,tmin,tmax,eps,gs,hcl,H,margin)=cell
    first,count,tres,mod,yres,coeff=leaf
    base_s=(first-tres)//mod
    B=yres+coeff*base_s
    A=start_R+(1<<L)*first
    Q=q0+R
    return H,Q,A,B,count,lo

def extremum_affine(v0, slope, M, want_max=True):
    v1=v0+slope*(M-1)
    return max(v0,v1) if want_max else min(v0,v1)

def main():
    total,safe,singleton,critical=m65.classify_cells(R)
    records=0
    positive_records=0
    positive_mass_possible=0
    maxG=None
    max_item=None
    min_positive=None
    qbound=Fraction(Q0,3)

    for group in (singleton,critical):
        for cell in group:
            leaves,_=m65.negative_candidate_cylinders(cell,R)
            for leaf in leaves:
                H,Q,A,B,M,lo=full_factor(cell,leaf)
                records+=1
                G0=lo*A-B
                slope=lo*(1<<H)-3**Q
                Gmax=extremum_affine(G0,slope,M,True)
                if maxG is None or Gmax>maxG:
                    maxG=Gmax
                    max_item=(H,Q,A,B,M,lo,G0,slope)
                if Gmax>0:
                    positive_records+=1
                    # Count s with G(s)>0 exactly.
                    if slope==0:
                        cnt=M if G0>0 else 0
                    elif slope>0:
                        if G0>0:
                            cnt=M
                        else:
                            x=(-G0)/slope
                            first=x.numerator//x.denominator+1
                            cnt=max(0,M-max(0,first))
                    else:
                        if G0<=0:
                            cnt=0
                        else:
                            x=G0/(-slope)
                            ceilx=-((-x.numerator)//x.denominator)
                            cnt=max(0,min(M,ceilx))
                    positive_mass_possible+=cnt
                    if cnt:
                        # Find smallest strictly positive headroom among the
                        # positive integer points of this affine record.
                        if slope>=0:
                            s0=0 if G0>0 else ((-G0)/slope).numerator//((-G0)/slope).denominator+1
                        else:
                            s0=0
                        gv=G0+slope*s0
                        if gv>0 and (min_positive is None or gv<min_positive):
                            min_positive=gv

    assert records==278_725
    print("MATH-248_RESULT")
    print("records",records)
    print("positive_headroom_records",positive_records)
    print("positive_headroom_mass_possible",positive_mass_possible)
    print("max_headroom_exact",maxG)
    print("max_headroom_float",float(maxG))
    print("q0_over_3_exact",qbound)
    print("q0_over_3_float",float(qbound))
    print("max_headroom_minus_q0over3",maxG-qbound)
    if min_positive is not None:
        print("min_positive_headroom_exact",min_positive)
    print("max_item_H_Q_M_lo",max_item[0],max_item[1],max_item[4],max_item[5])
    print("PASS MATH-248 headroom diagnostic")
    print("DIAGNOSTIC ONLY / NO r10 CLOSURE CLAIM")

if __name__=="__main__":
    main()
