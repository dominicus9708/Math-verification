#!/usr/bin/env python3
"""Exact L7+L14 strengthening of the H=0,1 Stage-4 recurrent core.

Every 14-step word must simultaneously
  (i) be full-Hensel residue-maximal at L=14, and
  (ii) have both aligned 7-step halves residue-maximal at L=7.

The exact intersection contains 3620 words.  Using these words in two aligned
14-step blocks per 28-step window, and then multiplying the twelve genuine
mechanical windows over every length-336 Sturmian factor, gives

    150^12 * Pmax12 * (1,2)^T < 2^336 * (1,2)^T.

Thus the unresolved two-state language admits a paired cross-base amplification
scale K=150 per 28-step window on this strengthened deterministic language.
The remaining sufficient conditioned-selector losses are about 82.27% at H=0
and 33.36% at H=1.

This is a reduction theorem, not a proof of the Collatz conjecture.
"""

from collections import defaultdict

EXPECTED_L7_COUNTS=(1,2,6,15,21,16,7,1)
EXPECTED_L14_COUNTS=(1,2,6,18,54,162,462,1011,1405,1215,708,287,79,14,1)
EXPECTED_L14_CLASSES=5425
EXPECTED_L14_DMAX=2730
EXPECTED_INTERSECTION=3620
EXPECTED_MIN_ROW=(317_231,1_192_543)
POTENTIAL=(1,2)
EXPECTED_PMAX=(
    (
        287008777022385183192634182379941849263351653060859905904240025169236332192,
        368006827285029034445186887210876015243265144336829744854860466578814160576,
    ),
    (
        496670536160427357635485652795691405255479010102836599255398510409158495432,
        816643694946679695234411925782811681908820690255877508147111312499160612096,
    ),
)


def correction(bits):
    R=q=0
    for k,b in enumerate(bits):
        if b:
            R=3*R+(1<<k)
            q+=1
    return q,R


def residue_maximal_words(L):
    groups=defaultdict(list)
    for mask in range(1<<L):
        bits=tuple((mask>>k)&1 for k in range(L))
        q,R=correction(bits)
        groups[(q,R%(3**q))].append((R,bits))

    out=[]
    counts=[0]*(L+1)
    dmax=0
    for (q,_),arr in groups.items():
        Rmax,bitsmax=max(arr)
        out.append(bitsmax)
        counts[q]+=1
        for R,_bits in arr:
            dmax=max(dmax,(Rmax-R)//(3**q))
    return tuple(out),tuple(counts),dmax


def strengthened_words14():
    w7,c7,d7=residue_maximal_words(7)
    assert c7==EXPECTED_L7_COUNTS
    assert len(w7)==69 and d7==21
    s7=set(w7)

    w14,c14,d14=residue_maximal_words(14)
    assert len(w14)==EXPECTED_L14_CLASSES
    assert c14==EXPECTED_L14_COUNTS
    assert d14==EXPECTED_L14_DMAX

    out=tuple(w for w in w14 if w[:7] in s7 and w[7:] in s7)
    assert len(out)==EXPECTED_INTERSECTION
    return out


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
        assert start<20000
    assert len(seen)==length+1
    return seen


def transition14(seg,words,incoming):
    out=defaultdict(int)
    for word in words:
        h=incoming
        ok=True
        for b,mb in zip(word,seg):
            h+=b-mb
            if h<0:
                ok=False
                break
        if ok:
            out[h]+=1
    return out


def matrix28(mech28,words):
    rows=[]
    for incoming in range(2):
        dp={incoming:1}
        for seg in (mech28[:14],mech28[14:]):
            nxt=defaultdict(int)
            for h,mass in dp.items():
                for hh,c in transition14(seg,words,h).items():
                    nxt[hh]+=mass*c
            dp=nxt
        rows.append((dp.get(0,0),dp.get(1,0)))
    return tuple(rows)


def matmul(A,B):
    return (
        (A[0][0]*B[0][0]+A[0][1]*B[1][0], A[0][0]*B[0][1]+A[0][1]*B[1][1]),
        (A[1][0]*B[0][0]+A[1][1]*B[1][0], A[1][0]*B[0][1]+A[1][1]*B[1][1]),
    )


def main():
    words=strengthened_words14()

    f28=all_factors(28)
    assert len(f28)==29
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

    K=150
    for i,row in enumerate(pmax):
        pv=row[0]*POTENTIAL[0]+row[1]*POTENTIAL[1]
        lhs=K**12*pv
        rhs=(1<<336)*POTENTIAL[i]
        assert lhs<rhs
        print("row",i,"margin",rhs-lhs)

    # Neither H=0 nor H=1 is automatic yet at K=150.
    assert K*min_rows[0]<(1<<28)
    assert K*min_rows[1]<(1<<28)

    print("L14 classes:",EXPECTED_L14_CLASSES)
    print("L14 predecessor-credit max:",EXPECTED_L14_DMAX)
    print("L7+L14 aligned 14-step words:",EXPECTED_INTERSECTION)
    print("min H=0,1 row masses:",min_rows)
    print("K=150 twelve-window potential inequality: PASS")
    print("remaining incoming heights: H=0,1")


if __name__=="__main__":
    main()
