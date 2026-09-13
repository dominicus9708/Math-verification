#!/usr/bin/env python3
"""MATH-115 generic exact source exporter for remaining layers r=2..12.

Reuses unchanged MATH-065 exact classifier/generator and freezes the audited
workload totals from MATH-110, MATH-112 and MATH-113.  Emits complete AP source
rows target0<TAB>odd_step<TAB>count for one requested layer.

This is executor infrastructure only; it makes no closure claim.
"""
import argparse
import sys
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location("m65", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py")
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

EXPECTED = {
12: ((1013,126,457,430), 8278602, 1053555, 580472268528, 12976298271),
11: ((1013,119,414,480), 3994436, 605972, 3419719061560, 51905193085),
10: ((994,91,396,507), 1994258, 278725, 27557263803397, 830483089363),
9: ((977,72,349,556), 915218, 141002, 172107496438700, 3381256733001),
8: ((977,60,330,587), 436659, 65811, 1281026785265013, 67269130238384),
7: ((963,42,291,630), 201298, 29342, 8499072326407060, 807229562860607),
6: ((963,34,250,679), 95577, 15133, 53251059016858758, 3228918251442427),
5: ((952,20,226,706), 46721, 6525, 407471475426308081, 51662692023078828),
4: ((944,14,172,758), 23058, 3675, 1845330088960999169, 227070381217324903),
3: ((944,9,152,783), 12133, 1873, 13093636650601823230, 1816563049738599228),
2: ((939,3,104,832), 6218, 1116, 74283701945452943666, 21350398233904928148),
}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--r',type=int,required=True); args=ap.parse_args(); r=args.r
    if r not in EXPECTED: raise ValueError('r must be 2..12')
    total,safe,singleton,critical=m65.classify_cells(r)
    got_class=(total,len(safe),len(singleton),len(critical))
    assert got_class==EXPECTED[r][0]
    nodes=cyl=occ=mx=0
    for group in (singleton,critical):
        for cell in group:
            leaves,n=m65.negative_candidate_cylinders(cell,r); nodes+=n
            for first,count,tres,mod,yres,coeff in leaves:
                base_s=(first-tres)//mod
                target0=yres+coeff*base_s
                print(target0,coeff,count,sep='\t')
                cyl+=1; occ+=count; mx=max(mx,count)
    assert (nodes,cyl,occ,mx)==EXPECTED[r][1:]
    print(f'MATH-115 export PASS r={r} cylinders={cyl} occurrences={occ} max_multiplicity={mx}',file=sys.stderr)
    print('NO LAYER CLOSURE CLAIM',file=sys.stderr)

if __name__=='__main__': main()
