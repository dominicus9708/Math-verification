#!/usr/bin/env python3
"""MATH-257 static geometry of frozen r=10 negative full factors by zero-prefix L."""

from collections import defaultdict
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location(
    "m206", HERE/"2026_09_19_math206_initial_overshoot_reset_catalogue.py"
)
m206=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m206)

m65=m206.m65
R=10

def main():
    total,safe,singleton,critical=m65.classify_cells(R)
    by=defaultdict(lambda:[0,0,0]) # rows,mass,max_m
    records=mass=0
    for group in (singleton,critical):
        for cell in group:
            L=cell[0]
            leaves,_=m65.negative_candidate_cylinders(cell,R)
            for leaf in leaves:
                H,Q,A,B,M=m206.full_factor(cell,leaf)
                records+=1
                mass+=M
                x=by[L]
                x[0]+=1
                x[1]+=M
                x[2]=max(x[2],M)

    assert records==278_725
    assert mass==27_557_263_803_397

    for L in sorted(by):
        rows,mm,mx=by[L]
        print("L",L,"rows",rows,"mass",mm,"max_m",mx)
    print("L_range",min(by),max(by))
    print("nonempty_L",len(by))
    print("records",records)
    print("mass",mass)
    print("PASS MATH-257 r10 negative-factor geometry")

if __name__=="__main__":
    main()
