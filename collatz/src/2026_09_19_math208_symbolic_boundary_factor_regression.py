#!/usr/bin/env python3
"""MATH-208 symbolic boundary-factor generator regression.

Checks:
- closed Beatty-position zero-prefix formula against every frozen MATH-058R
  paid-exit prefix;
- ballot gap-vector representation and correction formula through r=10.

Regression evidence only.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from fractions import Fraction

HERE=Path(__file__).resolve().parent
SPEC=spec_from_file_location(
    "m58", HERE/"2026_09_11_paid_macro_transition_certificate.py"
)
m58=module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m58)


def prefix_formula(q,omega):
    pos=[]
    for j in range(q):
        p=0 if j==0 else j+m58.M[j]+(1 if omega<=m58.TAU[j] else 0)
        pos.append(p)
    C=sum(3**(q-1-j)*(1<<p) for j,p in enumerate(pos))
    L=q+m58.M[q]+(1 if omega<=m58.TAU[q] else 0)-1
    return L,C,pos


def local_eps(varpi,r):
    out=[]
    v=varpi
    for _ in range(r):
        e=0 if v>Fraction(3,4) else 1
        out.append(e)
        v*=Fraction(2,3) if e==0 else Fraction(4,3)
    return out


def gap_vectors(eps):
    r=len(eps)
    total=1+sum(eps)
    out=[]

    def rec(j,prefix,used):
        if j==r-1:
            a=total-used
            if a>=0:
                out.append(tuple(prefix+[a]))
            return

        # Strictly positive slack before the final return.
        cap=sum(eps[:j+1])-used
        for a in range(cap+1):
            rec(j+1,prefix+[a],used+a)

    rec(0,[],0)
    return out


def correction_from_gaps(gaps):
    r=len(gaps)
    used=0
    C=0
    for j,a in enumerate(gaps):
        p=j+used
        C+=3**(r-1-j)*(1<<p)
        used+=a
    return C


def direct_word(gaps):
    bits=[]
    for a in gaps:
        bits.append(1)
        bits.extend([0]*a)
    return tuple(bits)


def main():
    prefix_checks=0
    for L in range(1,73):
        for lo,hi,R,E0,q in m58.paid_exit_sources(L):
            omega=(lo+hi)/2
            bits=m58.mechanical_factor(L,omega)
            C0,q0=m58.correction_and_q(bits)
            L2,C2,pos=prefix_formula(q,omega)
            assert q0==q
            assert L2==L
            assert C2==C0
            prefix_checks+=1

    assert prefix_checks==937

    phase_cuts={Fraction(1,2),Fraction(1,1)}
    for j in range(1,11):
        phase_cuts.add(m58.TAU[j])
    s=sorted(phase_cuts)

    pattern_counts=[]
    word_checks=0

    for a,b in zip(s[:-1],s[1:]):
        v=(a+b)/2
        eps=local_eps(v,10)
        gs=gap_vectors(eps)
        pattern_counts.append(len(gs))

        for g in gs:
            w=direct_word(g)
            C,q=m58.correction_and_q(w)
            assert q==10
            assert C==correction_from_gaps(g)

            # First-return slack semantics.
            u=1
            j=0
            for k,bit in enumerate(w):
                if bit:
                    u+=eps[j]
                    j+=1
                else:
                    u-=1
                if k<len(w)-1:
                    assert u>0
            assert u==0
            assert j==10
            word_checks+=1

    assert len(pattern_counts)==11
    assert min(pattern_counts)==476
    assert max(pattern_counts)==1966
    assert sum(pattern_counts)==10962

    print("PASS MATH-208 symbolic boundary-factor generator regression")
    print("frozen_prefix_checks",prefix_checks)
    print("r10_phase_patterns",len(pattern_counts))
    print("r10_gap_occurrences",sum(pattern_counts))
    print("r10_gap_count_minmax",min(pattern_counts),max(pattern_counts))
    print("gap_word_checks",word_checks)
    print("NO r10 CLOSURE CLAIM")


if __name__=="__main__":
    main()
