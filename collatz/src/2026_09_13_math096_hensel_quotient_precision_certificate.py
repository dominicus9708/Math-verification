#!/usr/bin/env python3
"""MATH-096: normalized Hensel quotient identity and future-precision bound.

For an exact composed Collatz cylinder

    source  = A + 2^H s,
    target  = B + 3^Q s,

write the affine correction as

    2^H B = 3^Q A + C,   S=C/3^Q.

Then the normalized target intercept

    X = 3^{-Q} B

satisfies

    X = (A+S)/2^H.

Thus X is exactly the Hensel quotient left after the low H source-address bits
have been consumed by A == -S (mod 2^H).

For a multi-source family of size M let R=ceil(log2 M).  Every future one-paid
edge has resolution h<=73.  The finite precision

    P(R)=73+R

is sufficient for all future exact one-paid address decisions: a multi edge
h<=R reduces the required resolution to R'<=R-h, and MATH-092 propagates P bits
exactly to P-h bits, while

    P(R') <= P(R)-h.

A terminal edge is decided immediately and needs at most 73 current bits.
"""
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE=Path(__file__).resolve().parent
S85=spec_from_file_location('m85',HERE/'2026_09_12_math085_onepaid_depth4_6_current_phase_replay.py')
m85=module_from_spec(S85); assert S85.loader is not None; S85.loader.exec_module(m85)


def ceil_log2(m:int)->int:
    assert m>=1
    return 0 if m==1 else (m-1).bit_length()


def main():
    # Exact Hensel-quotient identity on all 910 canonical one-paid cylinders.
    assert len(m85.EDGES)==910
    for e in m85.EDGES:
        C=(e.target_B<<e.H) - 3**e.Q*e.source_A
        S=Fraction(C,3**e.Q)
        X=Fraction(e.target_B,3**e.Q)
        assert X == Fraction(e.source_A,1<<e.H) + S/Fraction(1<<e.H,1)

    # Finite-precision budget.  R<=69 is the first-macro envelope maximum in
    # the audited first-cell source window, but the inequality itself is valid
    # for every nonnegative R.
    for R in range(0,70):
        P=73+R
        for h in range(1,74):
            assert P>=h
            if h<=R:
                # Any exact multi child obeys R'<=R-h.
                for Rp in range(0,R-h+1):
                    assert 73+Rp <= P-h

    print('PASS MATH-096 Hensel quotient / P(R)=73+R precision certificate')
    print('canonical_edges',len(m85.EDGES))


if __name__=='__main__':
    main()
