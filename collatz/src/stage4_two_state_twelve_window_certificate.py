#!/usr/bin/env python3
"""Exact 12-window phase-coupled certificate for the H=0,1 core.

After the companion certificates show that every incoming H>=2 can be handled
without a new cross-base regularity theorem, this file treats transitions into
H>=2 as exits from the still-unresolved recurrent core.

For all 337 length-336 mechanical factors, multiply the twelve exact 28-step
H=0,1 transition matrices.  The entrywise maximum Pmax12 obeys

    117^12 * Pmax12 * (1,2)^T < 2^336 * (1,2)^T

componentwise.

Thus the unresolved two-state dyadic core has twelve-window average exclusion
allowance strictly above log2(117)/28.  The resulting sufficient selector-loss
targets are about 34.03% at incoming H=1 and 82.32% at H=0.

This is a reduction theorem, not a proof of the Collatz conjecture.
"""

from collections import defaultdict

L=7
W=28
EXPECTED_CLASS_COUNTS=(1,2,6,15,21,16,7,1)
EXPECTED_MIN_ROW=(405_550,1_513_565)
POTENTIAL=(1,2)
EXPECTED_PMAX=(
    (
        5_420_989_033_005_741_994_466_829_925_744_616_150_372_978_448_553_471_085_632_422_011_649_601_422_480,
        6_535_758_559_679_090_596_615_964_974_758_100_454_723_656_321_310_415_866_171_578_871_628_607_490_208,
    ),
    (
        9_986_846_317_718_188_796_227_476_512_967_599_231_780_531_055_101_592_900_704_821_147_103_202_624_960,
        15_428_773_549_657_007_353_811_384_502_892_045_440_367_157_385_919_481_503_148_660_803_568_995_111_440,
    ),
)


def correction(bits):
    R=q=0
    for k,b in enumerate(bits):
        if b:
            R=3*R+(1<<k)
            q+=1
    return q,R


def residue_maximal_words():
    groups=defaultdict(list)
    for mask in range(1<<L):
        bits=tuple((mask>>k)&1 for k in range(L))
        q,R=correction(bits)
        groups[(q,R%(3**q))].append((R,bits))
    out=[]
    counts=[0]*(L+1)
    for (q,_),arr in groups.items():
        _,bits=max(arr)
        out.append(bits)
        counts[q]+=1
    assert tuple(counts)==EXPECTED_CLASS_COUNTS
    assert len(out)==69
    return tuple(out)


def ceil_alpha_count(n):
    if n==0:
        return 0
    p2=1<<n
    p3=1
    k=0
    while p3<p2:
        p3*=3
        k+=1
    return k


def mechanical_factor(start,length):
    return tuple(
        ceil_alpha_count(start+i+1)-ceil_alpha_count(start+i)
        for i in range(length)
    )


def all_factors(length):
    seen={}
    start=0
    while len(seen)<length+1:
        f=mechanical_factor(start,length)
        seen.setdefault(f,start)
        start+=1
        assert start<10000
    assert len(seen)==length+1
    return seen


def transition_row(mech28,words,incoming):
    dp={incoming:1}
    for block in range(4):
        seg=mech28[7*block:7*(block+1)]
        nxt=defaultdict(int)
        for h,mass in dp.items():
            for word in words:
                hh=h
                ok=True
                for b,mb in zip(word,seg):
                    hh+=b-mb
                    if hh<0:
                        ok=False
                        break
                if ok:
                    nxt[hh]+=mass
        dp=nxt
    return tuple(dp.get(h,0) for h in range(2))


def matrix28(mech28,words):
    return tuple(transition_row(mech28,words,h) for h in range(2))


def matmul(A,B):
    return tuple(
        tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2))
        for i in range(2)
    )


def main():
    words=residue_maximal_words()
    f28=all_factors(28)
    mats={f:matrix28(f,words) for f in f28}

    min_rows=tuple(min(sum(M[i]) for M in mats.values()) for i in range(2))
    assert min_rows==EXPECTED_MIN_ROW

    factors=all_factors(336)
    assert len(factors)==337

    I=((1,0),(0,1))
    pmax=[[0,0],[0,0]]
    for f in factors:
        P=I
        for t in range(0,336,28):
            P=matmul(P,mats[f[t:t+28]])
        for i in range(2):
            for j in range(2):
                pmax[i][j]=max(pmax[i][j],P[i][j])
    pmax=tuple(tuple(row) for row in pmax)
    assert pmax==EXPECTED_PMAX

    for i,row in enumerate(pmax):
        pv=row[0]*POTENTIAL[0]+row[1]*POTENTIAL[1]
        lhs=117**12*pv
        rhs=(1<<336)*POTENTIAL[i]
        assert lhs<rhs
        print("row",i,"margin",rhs-lhs)

    # Neither remaining state is automatic at the K=117 scale.
    assert 117*min_rows[0]<(1<<28)
    assert 117*min_rows[1]<(1<<28)

    print("two-state growth < 2^336/117^12: PASS")
    print("remaining incoming heights: H=0,1")


if __name__=="__main__":
    main()
