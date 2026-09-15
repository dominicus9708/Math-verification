#!/usr/bin/env python3
"""MATH-156 generic exact consecutive-parameter microsharder for one AP."""
import argparse
from pathlib import Path


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--out-dir', required=True)
    ap.add_argument('--parts', type=int, required=True)
    ap.add_argument('--expected-mass', type=int)
    args=ap.parse_args()
    assert args.parts > 0

    rows=[ln.rstrip('\n').split('\t') for ln in Path(args.input).open(encoding='utf-8') if ln.strip()]
    assert len(rows)==1, f'expected one AP row, got {len(rows)}'
    a,b,m=map(int,rows[0])
    assert m>0 and b>0
    if args.expected_mass is not None:
        assert m==args.expected_mass, (m,args.expected_mass)

    out=Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    q,r=divmod(m,args.parts)
    assert q>0, 'parts must not exceed mass'

    off=0
    cert=[]
    for j in range(args.parts):
        mj=q+(1 if j<r else 0)
        aj=a+b*off
        (out/f'micro-{j:04d}.tsv').write_text(f'{aj}\t{b}\t{mj}\n',encoding='utf-8')
        cert.append((j,off,aj,b,mj))
        off+=mj

    assert off==m
    assert sum(row[4] for row in cert)==m
    assert max(row[4] for row in cert)-min(row[4] for row in cert)<=1

    with (out/'certificate.tsv').open('w',encoding='utf-8') as f:
        f.write('micro\toffset\tstart\tstep\tmass\n')
        for row in cert:
            f.write('\t'.join(map(str,row))+'\n')
        f.write(f'TOTAL\t{args.parts}\t{a}\t{b}\t{m}\n')

    print(
        f'PASS exact single-AP microshard parts={args.parts} source_mass={m} '
        f'q={q} r={r} min_mass={q} max_mass={q+(1 if r else 0)}'
    )


if __name__=='__main__':
    main()
