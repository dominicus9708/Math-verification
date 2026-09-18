#!/usr/bin/env python3
"""MATH-227 r=10 factor length + resolution ceiling regression."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location(
    "m206", HERE/"2026_09_19_math206_initial_overshoot_reset_catalogue.py"
)
m206=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m206)

def cres(M):
    return 0 if M==1 else (M-1).bit_length()

def main():
    records=m206.build_frozen_factors()
    checked_multi=0
    checked_single=0
    for H,Q,A,B,M in records:
        R=cres(M)
        if M>=2:
            assert H+R<=73, (H,R,M,A)
            checked_multi+=1
        else:
            checked_single+=1

    print("PASS MATH-227 r10 H+R ceiling")
    print("multi_records",checked_multi)
    print("singleton_records",checked_single)
    print("geometry_only_H_plus_R_le_73", True)
    print("NO LOCAL 89-STEP RESERVE CLAIM")\n    print("NO r10 LAYER CLOSURE CLAIM")

if __name__=="__main__":
    main()
