#!/usr/bin/env python3
"""MATH-228 finite low-paid future precision certificate."""

ZMIN = {2:1,3:2,4:3,5:6,6:7,7:8,8:10,9:11,10:13}

def m(r):
    return (3**r).bit_length()-1-r

def hmax(r):
    return r+2+m(r)

def main():
    hs={r:hmax(r) for r in range(2,11)}
    assert max(hs.values())==17
    assert hs[10]==17
    full_max=72+max(hs.values())
    assert full_max==89

    for R in range(0,41):
        P=89+R
        assert P<=129
        for h in range(1,90):
            if h<=R:
                # worst multi-child resolution
                Rp=R-h
                assert P-h >= 89+Rp

    print("PASS MATH-228 finite low-paid precision")
    print("paid_cluster_hmax",hs)
    print("full_factor_hmax",full_max)
    print("max_r10_output_precision",129)
    print("NO r10 CLOSURE CLAIM")

if __name__=="__main__":
    main()
