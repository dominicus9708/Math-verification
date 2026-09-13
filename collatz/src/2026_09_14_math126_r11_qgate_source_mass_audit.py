#!/usr/bin/env python3
"""MATH-126 exact r=11 source-mass audit for the MATH-125 q-gate.

Input: directory containing MATH-116 shard-*.tsv files.
Each row is target0<TAB>odd_step<TAB>count.

The credited safe mass is exact and conservative: for each AP, only complete
parameter blocks of length 2^d are credited.  In every complete block, each
parameter residue mod 2^d occurs exactly once, hence the MATH-124 parity-word
bijection makes the number of q-safe residues exact.  The incomplete remainder
of each AP is credited as zero here and must be handled by exact address logic.
"""
import argparse
from math import comb
from pathlib import Path

LO=1<<71
Q0=72_057_431_991
HI=1364*(1<<61)
# Matches the frozen MATH-058 construction.
YBOUND_NUM=2*(3*HI+Q0)
YBOUND_DEN=3
YMAX=(YBOUND_NUM-1)//YBOUND_DEN

EXPECTED_ROWS=605_977
EXPECTED_MASS=3_419_719_061_560
EXPECTED_MAX_N=6_290_339_729_165_775_182_359
EXPECTED_BEST_D=22
EXPECTED_GUARANTEED=2_811_463_801_368
EXPECTED_REMAINDER=608_255_260_192
EXPECTED_QHIST={12:27_420,13:578_557}


def limits(d):
    out=[]
    for q in range(d+1):
        cmax=0 if q==0 else (1<<(d-q))*(3**q-2**q)
        out.append(((1<<d)*LO-cmax)//(3**q))
    return out


def qsafe_for_N(d,N):
    best=-1
    for q,lim in enumerate(limits(d)):
        if N<=lim:
            best=q
        else:
            break
    return best


def read_rows(root):
    for p in sorted(Path(root).glob('shard-*.tsv')):
        with p.open(encoding='utf-8') as f:
            for line in f:
                if not line.strip():
                    continue
                a,b,m=map(int,line.split())
                assert b>0 and b&1 and m>0
                yield a,b,m


def audit_depth(rows,d):
    block=1<<d
    safe_words=[sum(comb(d,j) for j in range(q+1)) for q in range(d+1)]
    guaranteed=0
    qhist={}
    for a,b,m in rows:
        N=a+b*(m-1)
        qs=qsafe_for_N(d,N)
        qhist[qs]=qhist.get(qs,0)+1
        if qs>=0:
            guaranteed += safe_words[qs]*(m//block)
    return guaranteed,qhist


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('root')
    args=ap.parse_args()
    rows=list(read_rows(args.root))
    total_mass=sum(m for _,_,m in rows)
    max_N=max(a+b*(m-1) for a,b,m in rows)
    assert len(rows)==EXPECTED_ROWS
    assert total_mass==EXPECTED_MASS
    assert max_N==EXPECTED_MAX_N
    assert max_N<=YMAX

    best=None
    for d in range(1,35):
        guaranteed,qhist=audit_depth(rows,d)
        rec=(guaranteed,d,qhist)
        if best is None or guaranteed>best[0]:
            best=rec
        print('depth',d,'guaranteed',guaranteed,'remaining',total_mass-guaranteed)

    guaranteed,d,qhist=best
    assert d==EXPECTED_BEST_D
    assert guaranteed==EXPECTED_GUARANTEED
    assert total_mass-guaranteed==EXPECTED_REMAINDER
    assert qhist==EXPECTED_QHIST
    print('BEST depth',d)
    print('rows',len(rows))
    print('total_mass',total_mass)
    print('max_N',max_N)
    print('YMAX',YMAX)
    print('qhist',qhist)
    print('guaranteed_safe_mass',guaranteed)
    print('uncertified_tail_mass',total_mass-guaranteed)
    print('PASS MATH-126 exact conservative r11 q-gate source-mass audit')
    print('NO r=11 CLOSURE CLAIM')


if __name__=='__main__':
    main()
