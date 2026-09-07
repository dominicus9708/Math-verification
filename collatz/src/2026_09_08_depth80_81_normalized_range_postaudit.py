#!/usr/bin/env python3
"""Post-audit normalized endpoint ranges for MATH-020.

Usage:
  python 2026_09_08_depth80_81_normalized_range_postaudit.py \
      left80.txt right80.txt left81.txt right81.txt
"""

import sys
from collections import Counter


def load(path):
    out={}
    with open(path,"r",encoding="utf-8") as f:
        for line in f:
            b,Q,mn,mx=line.split()
            out[(int(b),int(Q))]=(int(mn),int(mx))
    return out


def audit(K,left,right):
    M=1<<(K-61)
    gap_min=None
    gap_witness=None
    hist=Counter()
    cells=0

    for b in range(1025,1364):
        qL={Q for bb,Q in left if bb==b}
        qR={Q for bb,Q in right if bb==b}
        common=sorted(qL&qR)
        hist[len(common)]+=1
        for Q in common:
            cells+=1
            lmn,lmx=left[(b,Q)]
            rmn,rmx=right[(b,Q)]
            shifted_min=rmn+3**Q
            shifted_max=rmx+3**Q
            assert lmx < shifted_min, (K,b,Q,"interval overlap/order failure")
            gap=shifted_min-lmx
            assert gap % M == 0
            if gap_min is None or gap<gap_min:
                gap_min=gap
                gap_witness=(b,Q,gap//M)
            assert shifted_max > shifted_min

    if K==80:
        assert cells==4993
        assert hist==Counter({14:114,15:203,16:22})
        assert gap_min==656_932_864
        assert gap_witness==(1275,51,1253)
    elif K==81:
        assert cells==4899
        assert hist==Counter({13:6,14:179,15:149,16:5})
        assert gap_min==1_971_322_880
        assert gap_witness==(1073,52,1880)
    else:
        raise AssertionError("unsupported depth")

    return cells,hist,gap_witness


def main():
    if len(sys.argv)!=5:
        raise SystemExit("usage: postaudit left80 right80 left81 right81")

    l80,r80,l81,r81=map(load,sys.argv[1:])
    a80=audit(80,l80,r80)
    a81=audit(81,l81,r81)

    print("PASS")
    print("depth80:",a80)
    print("depth81:",a81)
    print("strict max(E_left)<min(E_right) in every common-Q cell at depths 80 and 81")
    print("minimum same-Q endpoint separations: 1253, 1880")
    print("NO COMPLETE COLLATZ PROOF CLAIM")


if __name__=="__main__":
    main()
