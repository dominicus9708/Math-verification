#!/usr/bin/env python3
"""MATH-175 static profiler for MATH-161 shard18 composite tail 47..63.

Input: extracted directory r10-shard18-sub64 containing shard-000.tsv ...
Output: exact static workload descriptors only. No closure claim.
"""
import argparse, math
from pathlib import Path

CAP = 1_000_000

def p3exp(n):
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    assert n == 1
    return e

def depth_bound(m):
    if m <= CAP:
        return 0
    d = 0
    x = m
    while x > CAP:
        x = (x + 1) // 2
        d += 1
    return d

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('source_dir', type=Path)
    args = ap.parse_args()
    print('shard\tpieces\tmass\tmax_m\tmax_m_share\tmax_m_step_exp\tle_1m\tsingletons\tdmax\tsum_leaf_bound\tmin_exp\tmax_exp')
    for s in range(47, 64):
        rows=[]
        for ln in (args.source_dir / f'shard-{s:03d}.tsv').read_text().splitlines():
            if ln.strip():
                a,b,m = map(int, ln.split('\t'))
                rows.append((a,b,m))
        ms=[x[2] for x in rows]
        exps=[p3exp(x[1]) for x in rows]
        top=max(rows, key=lambda x:x[2])
        ds=[depth_bound(m) for m in ms]
        mass=sum(ms)
        print(s, len(rows), mass, top[2], f'{top[2]/mass:.12f}', p3exp(top[1]),
              sum(m <= CAP for m in ms), sum(m == 1 for m in ms), max(ds),
              sum(1 << d for d in ds), min(exps), max(exps), sep='\t')

if __name__ == '__main__':
    main()
