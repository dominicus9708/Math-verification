#!/usr/bin/env python3
from __future__ import annotations
import argparse, bisect, glob, os
from collections import defaultdict

LO = 1 << 71
BASE_SAFE_D22 = 3_209_065_424_947
EXPECT_TOTAL = 3_419_719_061_560
EXPECT_ROWS = 605_977
EXPECT_MAX_SPLIT_M = 26_716_555_169
EXPECT_D23 = 3_151_665_357
EXPECT_ADD_23_34 = 77_081_911_098
EXPECT_SAFE_34 = 3_286_147_336_045
EXPECT_TAIL_34 = 133_571_725_515

EXPECTED = {
    23: 3_151_665_357,
    24: 17_456_818_136,
    25: 15_350_900_431,
    26: 5_512_456_558,
    27: 13_125_146_222,
    28: 5_153_825_838,
    29: 5_433_928_840,
    30: 6_978_119_195,
    31: 561_706_378,
    32: 2_728_613_739,
    33: 1_501_750_221,
    34: 126_980_183,
}

def lim(d: int, q: int) -> int:
    cmax = 0 if q == 0 else (1 << (d-q)) * (3**q - 2**q)
    return (((1 << d) * LO) - cmax) // (3**q)

def cdf(hist: dict[int,int]):
    items = sorted(hist.items())
    vals=[]; pref=[]; s=0
    for x,c in items:
        vals.append(x); s += c; pref.append(s)
    return vals,pref

def weighted_lt(cp, n: int) -> int:
    vals,pref=cp
    i=bisect.bisect_left(vals,n)-1
    return pref[i] if i>=0 else 0

def iter_rows(path: str):
    if os.path.isdir(path):
        files=sorted(glob.glob(os.path.join(path,'shard-*.tsv')))
        if not files:
            raise SystemExit('no shard-*.tsv files found')
    else:
        files=[path]
    for fn in files:
        with open(fn,encoding='utf-8') as f:
            for line in f:
                if not line.strip(): continue
                a,b,m=map(int,line.split())
                yield a,b,m

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('prepared_source', help='MATH-115 prepared shard directory or concatenated TSV')
    args=ap.parse_args()

    rows=[]; total=0; maxm=0
    for a,b,m in iter_rows(args.prepared_source):
        nmax=a+b*(m-1)
        rows.append((nmax,m)); total += m; maxm=max(maxm,m)
    assert len(rows)==EXPECT_ROWS
    assert total==EXPECT_TOTAL
    assert maxm==EXPECT_MAX_SPLIT_M

    states={(0,-1):1}
    increments={}
    for d in range(1,35):
        nxt=defaultdict(int)
        hp=defaultdict(int); hn=defaultdict(int)
        for (q,best),cnt in states.items():
            for bit in (0,1):
                q2=q+bit
                ldq=lim(d,q2)
                if ldq>best:
                    hp[best]+=cnt
                    hn[ldq]+=cnt
                nxt[(q2,max(best,ldq))]+=cnt
        states=nxt
        if d<23: continue
        cp,cn=cdf(hp),cdf(hn)
        inc=0
        for nmax,m in rows:
            blocks=m >> d
            if blocks==0: continue
            new_per_cycle=weighted_lt(cp,nmax)-weighted_lt(cn,nmax)
            inc += blocks*new_per_cycle
        increments[d]=inc

    assert increments[23]==EXPECT_D23
    assert increments==EXPECTED
    add=sum(increments.values())
    safe=BASE_SAFE_D22+add
    tail=total-safe
    assert add==EXPECT_ADD_23_34
    assert safe==EXPECT_SAFE_34
    assert tail==EXPECT_TAIL_34
    assert maxm < (1<<35)

    print('metric\tvalue')
    print(f'prepared_split_pieces\t{len(rows)}')
    print(f'total_occurrence_mass\t{total}')
    print(f'base_exact_safe_through_d22\t{BASE_SAFE_D22}')
    for d in range(23,35):
        print(f'new_complete_cycle_safe_d{d}\t{increments[d]}')
    print(f'new_complete_cycle_safe_d23_d34\t{add}')
    print(f'certified_safe_mass_through_complete_cycle_d34\t{safe}')
    print(f'uncertified_tail_upper_bound\t{tail}')
    print(f'certified_safe_fraction_percent\t{safe*100/total:.15f}')
    print(f'max_prepared_piece_multiplicity\t{maxm}')
    print('complete_cycle_extension_exhausted_at_d34\t1')
    print('status\tEXACT_FINITE_COMPLETE_CYCLE_DP_LOWER_BOUND_NO_R11_CLOSURE_CLAIM')
    print('PASS MATH-131 complete-cycle DP audit', file=__import__('sys').stderr)
    print('NO r=11 CLOSURE CLAIM', file=__import__('sys').stderr)

if __name__=='__main__': main()
