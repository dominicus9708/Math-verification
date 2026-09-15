#!/usr/bin/env python3
"""MATH-173 static geometry audit for all fragmented r=10 original shards.

This is SIDE/SUPPORT only.  It regenerates the frozen MATH-115 r=10 source,
reconstructs the exact MATH-114 original 128-way partition, rechecks the known
MATH-161 64-way aggregate, and then computes a 256-way exact scheduling geometry
for every fragmented original shard 14..127.

No MATH-108 closure is executed and no shard/layer closure claim is made.
"""
import argparse
import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


sharder = load('math114', HERE / '2026_09_13_math114_mass_balanced_ap_sharder.py')


def export_r10():
    p = subprocess.run(
        [sys.executable, str(HERE / '2026_09_13_math115_generic_r2_r12_exporter.py'), '--r', '10'],
        text=True, capture_output=True, check=True,
    )
    assert 'MATH-115 export PASS r=10 cylinders=278725 occurrences=27557263803397 max_multiplicity=830483089363' in p.stderr
    rows=[]
    for i,line in enumerate(p.stdout.splitlines()):
        if not line.strip():
            continue
        a,b,m=map(int,line.split())
        rows.append((a,b,m,i))
    assert len(rows)==278725
    assert sum(r[2] for r in rows)==27557263803397
    assert max(r[2] for r in rows)==830483089363
    return rows


def repartition(rows, n):
    total,cap,shards,masses=sharder.build_partition(rows,n)
    return total,cap,shards,masses


def stripped(rows):
    return [(a,b,m,i) for i,(a,b,m,*_) in enumerate(rows)]


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--output', default='-')
    args=ap.parse_args()

    source=export_r10()
    total128,cap128,original,masses128=repartition(source,128)
    assert total128==27557263803397
    assert cap128==215291123465
    assert all(len(original[s])==1 and masses128[s]==215291123465 for s in range(14))
    assert min(masses128)==215291123463 and max(masses128)==215291123465

    # Reproduce the already-recorded MATH-161 all-fragmented 64-way aggregate
    # before computing the new 256-way support geometry.
    a64=[]
    for s in range(14,128):
        src=stripped(original[s])
        total,cap,subs,masses=repartition(src,64)
        a64.append((len(src),total,sum(len(x) for x in subs),cap,
                    max(masses)-min(masses),max(len(x) for x in subs)))
    assert (min(x[0] for x in a64),max(x[0] for x in a64))==(2427,2448)
    assert (min(x[1] for x in a64),max(x[1] for x in a64))==(215291123463,215291123464)
    assert (min(x[2] for x in a64),max(x[2] for x in a64))==(2481,2494)
    assert {x[3] for x in a64}=={3363923805}
    assert (min(x[4] for x in a64),max(x[4] for x in a64))==(3,6)
    assert max(x[5] for x in a64)==244

    header=('original_shard\tsource_records\tsource_mass\tcap256\tsplit_pieces\t'
            'full_cap_prefixes\tterminal_remainders\tsplit_source_records\t'
            'max_source_pieces\tmin_subshard_mass\tmax_subshard_mass\tmass_spread\t'
            'min_pieces_per_subshard\tmax_pieces_per_subshard\tmax_source_multiplicity')
    out=[header]
    aggregate=[]
    for s in range(14,128):
        src=stripped(original[s])
        total,cap,subs,masses=repartition(src,256)
        mult=[r[2] for r in src]
        full=sum(m//cap for m in mult)
        terminal=sum(1 for m in mult if m%cap)
        split_sources=sum(1 for m in mult if m>cap)
        max_source_pieces=max((m+cap-1)//cap for m in mult)
        row=(s,len(src),total,cap,sum(len(x) for x in subs),full,terminal,
             split_sources,max_source_pieces,min(masses),max(masses),
             max(masses)-min(masses),min(len(x) for x in subs),
             max(len(x) for x in subs),max(mult))
        aggregate.append(row)
        out.append('\t'.join(map(str,row)))

    # Frozen MATH-173 aggregate assertions.
    assert len(aggregate)==114
    assert {r[3] for r in aggregate}=={840980952}
    assert (min(r[4] for r in aggregate),max(r[4] for r in aggregate))==(2657,2669)
    assert (min(r[5] for r in aggregate),max(r[5] for r in aggregate))==(219,230)
    assert (min(r[7] for r in aggregate),max(r[7] for r in aggregate))==(12,29)
    assert max(r[8] for r in aggregate)==220
    assert (min(r[11] for r in aggregate),max(r[11] for r in aggregate))==(7,10)
    assert max(r[13] for r in aggregate)==95
    assert sum(r[4] for r in aggregate)==303954
    assert sum(r[1] for r in aggregate)==278725
    assert sum(r[5] for r in aggregate)==25229
    assert sum(r[2] for r in aggregate)==24543188074887
    assert all(r[6]==r[1] for r in aggregate)  # no source multiplicity is cap-divisible

    text='\n'.join(out)+'\n'
    if args.output=='-':
        sys.stdout.write(text)
    else:
        Path(args.output).write_text(text,encoding='utf-8')
    print('PASS MATH-173 all 114 fragmented r=10 shards recursive256 static geometry',file=sys.stderr)
    print('NO ORIGINAL-SHARD OR LAYER CLOSURE CLAIM',file=sys.stderr)


if __name__=='__main__':
    main()
