#!/usr/bin/env python3
"""MATH-095: exact phase-resolution Bellman value on the dyadic envelope.

MATH-094 showed that the Boolean phase danger kernel saturates if accumulated
multi-edge penalty is discarded.  Here the full positive penalty is restored
through the exact Bellman value recursion

 V_R(Omega) = min_e {
   c*rho*Omega - lambda*(h-R),                 h>R,
   c*rho*Omega + V_{R-h}(rho*Omega),           h<=R.
 }

Address compatibility remains deliberately forgotten and the source family is
the MATH-093 power-of-two envelope.  Exact Fraction arithmetic shows that this
stronger phase+resolution+penalty abstraction still admits a negative envelope
path from every one of the 857 actual multi-source first-macro phase states.

For the infimum at each initial open interval lower endpoint, including the
first-macro penalty, all 857 values lie strictly between -5/2 and -2.
Therefore exact carry/address information is indispensable to any successful
remaining quotient.
"""
from fractions import Fraction
from functools import lru_cache
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
S86=spec_from_file_location('m86',HERE/'2026_09_12_math086_onepaid_phase_horizon_certificate.py')
m86=module_from_spec(S86); assert S86.loader is not None; S86.loader.exec_module(m86)
S85=spec_from_file_location('m85',HERE/'2026_09_12_math085_onepaid_depth4_6_current_phase_replay.py')
m85=module_from_spec(S85); assert S85.loader is not None; S85.loader.exec_module(m85)

LAM=Fraction(19,503)
EDGES=m86.merged_phase_edges()


@lru_cache(maxsize=None)
def V(R:int,omega:Fraction):
    best=None
    for h,lo,hi,rho,c in EDGES:
        # Boundary inclusion computes the infimum for the open phase cells.
        if not (lo<=omega<=hi):
            continue
        out=rho*omega
        if h>R:
            val=c*out-LAM*(h-R)
        else:
            child=V(R-h,out)
            if child is None:
                continue
            val=c*out+child
        if best is None or val<best:
            best=val
    return best


def ceil_log2(m:int)->int:
    assert m>=1
    return 0 if m==1 else (m-1).bit_length()


def main():
    assert len(EDGES)==126
    vals=[]
    states=m85.initial_states()
    assert len(states)==857
    for p in states:
        R=ceil_log2(p.count)
        assert R<=69
        future=V(R,p.lo)
        assert future is not None
        total=p.alpha*p.lo+future
        vals.append(total)

    assert len(vals)==857
    assert all(Fraction(-5,2)<x<Fraction(-2,1) for x in vals)
    print('PASS MATH-095 phase-resolution Bellman value negative result')
    print('initial states',len(vals))
    print('all envelope infima satisfy -5/2 < J < -2')
    print('carry/address channel is indispensable')


if __name__=='__main__':
    main()
