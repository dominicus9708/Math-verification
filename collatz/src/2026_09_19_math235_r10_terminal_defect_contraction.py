#!/usr/bin/env python3
"""MATH-235 exact terminal-defect contraction of frozen r=10 factors.

For each synchronized full factor
    N=A+2^H s
    Y=B+3^Q s, 0<=s<M,
compute
    C=2^H B-3^Q A
    J(s)=C-N(s)(2^H-3^Q)=2^H(Y-N).
The J>=0 survivor set is obtained by one exact integer threshold, never by
ordinary-source enumeration.

This is an initial-factor contraction audit, not full r=10 closure.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from collections import Counter

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location("m206",HERE/"2026_09_19_math206_initial_overshoot_reset_catalogue.py")
m206=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m206)

def cres(m):
    return 0 if m<=1 else (m-1).bit_length()

def survivors(row):
    H,Q,A,B,M=row
    two=1<<H
    three=3**Q
    C=two*B-three*A
    D=two-three
    J0=C-A*D
    step=two*D

    if D>0:
        if J0<0:
            return 0
        maxs=J0//step
        return min(M,maxs+1)
    elif D==0:
        return M if C>=0 else 0
    else:
        # J(s)=J0 + two*(-D)s increases.
        if J0>=0:
            return M
        rise=two*(-D)
        first=(-J0+rise-1)//rise
        if first>=M:
            return 0
        return M-first

def main():
    rec=m206.build_frozen_factors()
    assert len(rec)==278_725
    total=sum(x[4] for x in rec)
    assert total==27_557_263_803_397

    closed_records=0
    contracted_records=0
    unchanged_records=0
    survivor_mass=0
    removed_mass=0
    max_survivor=0
    max_Rbad=0
    min_kappa=10**9
    kappa_hist=Counter()
    sign_hist=Counter()

    for row in rec:
        H,Q,A,B,M=row
        D=(1<<H)-3**Q
        sign_hist[0 if D==0 else (1 if D>0 else -1)] += 1
        S=survivors(row)
        assert 0<=S<=M
        survivor_mass += S
        removed_mass += M-S
        max_survivor=max(max_survivor,S)

        R=cres(M)
        Rb=cres(S)
        max_Rbad=max(max_Rbad,Rb)
        k=R-Rb
        min_kappa=min(min_kappa,k)
        kappa_hist[k]+=1

        if S==0: closed_records+=1
        elif S<M: contracted_records+=1
        else: unchanged_records+=1

    assert survivor_mass+removed_mass==total

    print("records",len(rec))
    print("coefficient_sign_Dpositive_Dzero_Dnegative",
          sign_hist[1],sign_hist[0],sign_hist[-1])
    print("closed_records_J",closed_records)
    print("contracted_records_J",contracted_records)
    print("unchanged_records_J",unchanged_records)
    print("survivor_mass",survivor_mass)
    print("removed_mass",removed_mass)
    print("removed_fraction_num_den",removed_mass,total)
    print("max_survivor_multiplicity",max_survivor)
    print("max_survivor_resolution",max_Rbad)
    print("min_resolution_contraction_credit",min_kappa)
    print("kappa_hist",sorted(kappa_hist.items()))
    print("PASS MATH-235 frozen r10 terminal-defect contraction audit")
    print("NO r10 LAYER CLOSURE CLAIM")

if __name__=="__main__":
    main()
