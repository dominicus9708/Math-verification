#!/usr/bin/env python3
"""MATH-115 prepare all exact mass-balanced shard files once.

Consumes an AP source TSV produced by the generic MATH-115 exporter, imports
MATH-114 partition semantics unchanged, and writes all shard files plus a
certificate table.  This removes repeated full-source generation/sorting from
matrix jobs without changing mathematics.
"""
import argparse
import importlib.util
from pathlib import Path

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('sharder',HERE/'2026_09_13_math114_mass_balanced_ap_sharder.py')
mod=importlib.util.module_from_spec(spec); assert spec.loader is not None; spec.loader.exec_module(mod)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--input',required=True); ap.add_argument('--shards',type=int,default=128); ap.add_argument('--out-dir',required=True); args=ap.parse_args()
    records=[]
    with open(args.input,encoding='utf-8') as f:
        for i,line in enumerate(f):
            if not line.strip(): continue
            a,b,m=map(int,line.split()); assert b>0 and b%2==1 and m>0
            records.append((a,b,m,i))
    total,cap,shards,masses=mod.build_partition(records,args.shards)
    out=Path(args.out_dir); out.mkdir(parents=True,exist_ok=True)
    with open(out/'certificate.tsv','w',encoding='utf-8') as cert:
        cert.write('shard\tpieces\tmass\tu64_safe\n')
        for s,rows in enumerate(shards):
            safe=masses[s] <= mod.U64_MAX and all(r[2] <= mod.U64_MAX for r in rows)
            assert safe
            cert.write(f'{s}\t{len(rows)}\t{masses[s]}\t1\n')
            with open(out/f'shard-{s:03d}.tsv','w',encoding='utf-8') as g:
                for a,b,m,*_ in rows: g.write(f'{a}\t{b}\t{m}\n')
        cert.write(f'TOTAL_SOURCE_RECORDS\t{len(records)}\n')
        cert.write(f'TOTAL_PIECES\t{sum(len(x) for x in shards)}\n')
        cert.write(f'TOTAL_MASS\t{total}\n')
        cert.write(f'CAP\t{cap}\n')
        cert.write(f'MIN_SHARD_MASS\t{min(masses)}\n')
        cert.write(f'MAX_SHARD_MASS\t{max(masses)}\n')
        cert.write('PASS\texact_mass_balanced_partition\n')
    print('PASS MATH-115 one-shot exact shard preparation',len(records),sum(len(x) for x in shards),total,cap,min(masses),max(masses))

if __name__=='__main__': main()
