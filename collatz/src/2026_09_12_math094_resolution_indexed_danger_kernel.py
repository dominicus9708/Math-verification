#!/usr/bin/env python3
"""MATH-094: resolution-indexed phase danger kernel for one-paid chains.

This generator imports the exact merged phase-edge catalogue from MATH-086.
It uses the MATH-093 dyadic envelope, so a multi-edge of resolution h<=R
updates R exactly to R-h and contributes only a positive penalty.  Therefore a
path can be globally dangerous only if its final terminal edge is locally
phase-dangerous.

Define D_R as the phase values from which the address-forgotten envelope can
reach such a locally dangerous terminal.  The exact over-approximation obeys

 D_R = union_{h<=R} [ I_e intersect rho_e^{-1} D_{R-h} ]
       union
       union_{h>R}  [ I_e intersect {Omega: c_e*rho_e*Omega < lambda(h-R)} ].

Because every one-paid edge has h>=3, the recursion is acyclic in R.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location('m86',HERE/'2026_09_12_math086_onepaid_phase_horizon_certificate.py')
m86=module_from_spec(SPEC); assert SPEC.loader is not None; SPEC.loader.exec_module(m86)

LAM=Fraction(19,503)
RMAX=69


def union_intervals(ints):
    if not ints: return []
    ints=sorted(ints)
    out=[]; lo,hi=ints[0]
    for a,b in ints[1:]:
        if a<=hi:
            hi=max(hi,b)
        else:
            out.append((lo,hi)); lo,hi=a,b
    out.append((lo,hi))
    return out


def kernel(edges,Rmax=RMAX):
    D={}
    for R in range(Rmax+1):
        pieces=[]
        for h,lo,hi,rho,c in edges:
            if h>R:
                cut=LAM*(h-R)/(c*rho)
                a=lo; b=min(hi,cut)
                if a<b: pieces.append((a,b))
            else:
                for clo,chi in D[R-h]:
                    a=max(lo,clo/rho)
                    b=min(hi,chi/rho)
                    if a<b: pieces.append((a,b))
        D[R]=union_intervals(pieces)
    return D


def main():
    edges=m86.merged_phase_edges()
    assert len(edges)==126
    assert min(e[0] for e in edges)>=3
    D=kernel(edges)
    assert set(D)==set(range(RMAX+1))
    for R in range(RMAX+1):
        for lo,hi in D[R]:
            assert Fraction(1,2)<=lo<hi<=1
    print('PASS MATH-094 danger-kernel construction')
    for R in range(RMAX+1):
        if D[R]:
            print(R,len(D[R]),D[R][0],D[R][-1])
        else:
            print(R,0)


if __name__=='__main__':
    main()
