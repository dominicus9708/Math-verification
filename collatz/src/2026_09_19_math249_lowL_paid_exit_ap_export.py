#!/usr/bin/env python3
"""MATH-249 exact odd-step AP exporter for paid-exit singleton shells."""

import argparse
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
import sys

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location(
    "m58", HERE/"2026_09_11_paid_macro_transition_certificate.py"
)
m58=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m58)

def rows_for_L(L):
    out=[]
    for lo,hi,R,E0,q in m58.paid_exit_sources(L):
        tmin,tmax=m58.lift_bounds(L,R,lo,hi)
        wanted=(1-E0)&1
        first=m58.first_with_parity(tmin,tmax,wanted)
        if first is None:
            continue
        count=(tmax-first)//2+1
        E=E0+first*(3**q)
        assert E&1
        Z=(3*E+1)//2
        step=3**(q+1)
        assert step&1
        out.append((Z,step,count))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--L",type=int,required=True)
    args=ap.parse_args()
    L=args.L
    assert 13<=L<=54
    rows=rows_for_L(L)
    assert rows
    mass=sum(x[2] for x in rows)
    assert mass < 2**64
    for row in rows:
        print(*row,sep="\t")
    print(f"META {len(rows)} {mass} L={L}",file=sys.stderr)

if __name__=="__main__":
    main()
