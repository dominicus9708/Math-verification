#!/usr/bin/env python3
"""Exact certificate for the fixed-layer post-address Stage-4 handoff.

The certificate verifies:
- the m=44 and m=45 full binary-address exposure depths;
- the first aligned 28-step window starting after both exposures is 84->112;
- the exact L7+L14 two-state transition matrix at mechanical start 84;
- a surviving post-address singleton would have conditional amplification >150;
- the asymptotic address-exposure slope is strictly below the root-safe slope.

This is a structural handoff certificate, not a proof of the Collatz conjecture.
"""

from collections import defaultdict
import math

EXPECTED_L7_COUNTS=(1,2,6,15,21,16,7,1)
EXPECTED_L14_COUNTS=(1,2,6,18,54,162,462,1011,1405,1215,708,287,79,14,1)
EXPECTED_L14_CLASSES=5425
EXPECTED_L14_DMAX=2730
EXPECTED_INTERSECTION=3620
EXPECTED_M84=((89_202,228_029),(331_500,861_043))
WINDOW=28
K_ALLOW=150


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


def transition14(seg,words,incoming):
    out=defaultdict(int)
    for word in words:
        z=incoming
        ok=True
        for b,mb in zip(word,seg):
            z+=b-mb
            if z<0:
                ok=False
                break
        if ok:
            out[z]+=1
    return out


def matrix28(mech28,words):
    rows=[]
    for incoming in range(2):
        dp={incoming:1}
        for seg in (mech28[:14],mech28[14:]):
            nxt=defaultdict(int)
            for z,mass in dp.items():
                for zz,c in transition14(seg,words,z).items():
                    nxt[zz]+=mass*c
            dp=nxt
        rows.append((dp.get(0,0),dp.get(1,0)))
    return tuple(rows)


def main():
    nmax44=6*3**44+1
    nmax45=6*3**45+1
    kaddr44=nmax44.bit_length()
    kaddr45=nmax45.bit_length()
    assert kaddr44==73
    assert kaddr45==74
    assert nmax44 < 1<<kaddr44
    assert nmax45 < 1<<kaddr45

    first_aligned=((max(kaddr44,kaddr45)+WINDOW-1)//WINDOW)*WINDOW
    assert first_aligned==84

    words=strengthened_words14()
    M84=matrix28(mechanical_factor(first_aligned,WINDOW),words)
    assert M84==EXPECTED_M84
    row0=sum(M84[0])
    row1=sum(M84[1])
    assert row0==317_231
    assert row1==1_192_543

    dyadic=1<<WINDOW
    assert K_ALLOW*row0 < dyadic
    assert K_ALLOW*row1 < dyadic

    amp0=dyadic/row0
    amp1=dyadic/row1
    assert amp0>K_ALLOW
    assert amp1>K_ALLOW

    alpha=math.log(2.0,3.0)
    rho=math.log2(3.0)/(1.0-alpha)
    addr_slope=math.log2(3.0)
    handoff_gap=rho-addr_slope
    assert handoff_gap>0

    print("Post-address Stage-4 handoff certificate: PASS")
    print("K_addr(44) =",kaddr44)
    print("K_addr(45) =",kaddr45)
    print("first aligned post-address window =",first_aligned,"->",first_aligned+WINDOW)
    print("M84 =",M84)
    print("row masses =",(row0,row1))
    print("singleton amplification z=0 =",amp0)
    print("singleton amplification z=1 =",amp1)
    print("address slope log2(3) =",addr_slope)
    print("root-safe slope rho =",rho)
    print("post-address root-safe slope gap =",handoff_gap)


if __name__=="__main__":
    main()
