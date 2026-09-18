#!/usr/bin/env python3
"""MATH-207 exact phase-clock / boundary-telescope regression.

Regression evidence for the algebraic theorem in the companion note.
No closure claim.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location(
    "m58", HERE/"2026_09_11_paid_macro_transition_certificate.py"
)
m58=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m58)


def phase_step(varpi: Fraction, r: int) -> Fraction:
    E=m58.M[r]+(1 if varpi<=m58.TAU[r] else 0)
    return varpi*Fraction(2**(r+E),3**r)


def paid_length(varpi: Fraction, r: int) -> int:
    return r+1+m58.M[r]+(1 if varpi<=m58.TAU[r] else 0)


def main():
    checks=0

    # Exact phase cells and all r<=21.
    cuts={Fraction(1,2),Fraction(1,1)}
    for r in range(1,22):
        cuts.add(m58.TAU[r])
    cells=list(zip(sorted(cuts)[:-1],sorted(cuts)[1:]))

    for a,b in cells:
        x=(a+b)/2
        for r in range(1,22):
            y=phase_step(x,r)
            assert Fraction(1,2)<y<=1

            h=paid_length(x,r)
            # Exact paid-cluster coefficient cocycle.
            assert Fraction(3**r,2**h)==x/(2*y)
            checks+=1

    # Variable-r cumulative paid-length identity in multiplicative form.
    # We avoid floating logs: the telescoping cocycle itself is exact.
    sequences=[
        [1,2,3,4,5],
        [10,10,10,10],
        [2,21,7,3,18,1],
        list(range(1,22)),
    ]

    for seq in sequences:
        for a,b in cells[:8]:
            v=(a+b)/2
            v0=v
            H=0
            R=0
            for r in seq:
                H+=paid_length(v,r)
                R+=r
                v=phase_step(v,r)
            assert Fraction(3**R,2**H)==v0/(2**len(seq)*v)
            checks+=1

    # Full boundary coefficient identity on every frozen MATH-058R prefix,
    # paired with every r<=21 phase formula.  This is an algebra regression,
    # not a claim that all such pairs are same-integer legal.
    boundary_checks=0
    for L in range(1,73):
        for lo,hi,R0,E0,q0 in m58.paid_exit_sources(L):
            omega=(lo+hi)/2
            phi=omega*m58.phase_multiplier(q0,omega)
            assert Fraction(3**q0,2**L)==2*omega/phi

            for r in range(1,22):
                out=phase_step(phi,r)
                h=paid_length(phi,r)
                left=Fraction(3**(q0+r),2**(L+h))
                right=omega/out
                assert left==right
                boundary_checks+=1

    print("PASS MATH-207 phase rotation / coefficient telescope regression")
    print("phase_checks",checks)
    print("boundary_checks",boundary_checks)
    print("NO LAYER CLOSURE CLAIM")


if __name__=="__main__":
    main()
