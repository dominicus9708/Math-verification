#!/usr/bin/env python3
"""Exact 12-window phase-coupled certificate for the H=0,1,2 core.

Earlier certificates show that incoming H>=3 is automatically controlled by
available Stage-4 repair budgets.  Hence only H=0,1,2 need remain in the
recurrent cross-base core.

For each of the exactly 337 length-336 Sturmian/mechanical factors, this
certificate multiplies the twelve exact 28-step H=0,1,2 transition matrices.
The entrywise maximum of those genuine phase products is Pmax12.

The positive integer potential

    v=(1000,1903,2829)^T

satisfies exactly

    56^12 * Pmax12 * v < 2^336 * v

entrywise.  Thus the H=0,1,2 recurrent dyadic core has a 12-window average
exclusion allowance strictly larger than log2(56)/28 per step-window.

The exact minimum H=2 one-window low-to-{0,1,2} mass is 4,867,480, and
56*4,867,480 > 2^28. Therefore incoming H=2 itself requires no selector-side
regularity at the K<56 scale. The remaining genuinely cross-base incoming
states are H=0,1.

This is a reduction theorem, not a proof of the Collatz conjecture.
"""

from collections import defaultdict

L=7
W=28
MAXH=2
EXPECTED_CLASS_COUNTS=(1,2,6,15,21,16,7,1)
EXPECTED_MIN_ROW=(683_512,2_588_174,4_867_480)
POTENTIAL=(1000,1903,2829)
EXPECTED_PMAX=(
    (
        18_024_055_040_374_257_656_472_327_059_932_914_888_073_619_248_707_563_304_598_665_996_187_922_683_937_280,
        22_427_198_531_540_734_995_314_853_792_312_525_159_154_133_671_232_142_065_433_992_175_523_719_066_083_712,
        22_427_198_531_540_734_995_314_853_792_312_525_159_154_133_671_232_142_065_433_992_175_523_719_066_083_712,
    ),
    (
        34_297_897_328_688_792_643_777_636_733_718_557_623_965_365_739_023_106_930_847_659_030_868_103_951_170_560,
        42_676_620_265_632_085_870_041_415_391_040_412_431_766_772_812_836_970_661_794_315_540_364_526_835_559_424,
        42_676_620_265_632_085_870_041_415_391_040_412_431_766_772_812_836_970_661_794_315_540_364_526_835_559_424,
    ),
    (
        45_824_111_234_033_606_033_134_157_849_860_859_063_736_876_735_933_232_328_421_440_568_355_913_109_436_800,
        62_032_022_064_840_691_917_999_207_307_705_814_913_667_144_595_449_116_790_115_557_571_130_500_790_850_032,
        66_236_967_407_237_243_935_402_028_929_914_934_491_420_125_423_307_337_895_095_514_229_107_480_405_324_376,
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
    return tuple(dp.get(h,0) for h in range(MAXH+1))


def matrix28(mech28,words):
    return tuple(transition_row(mech28,words,h) for h in range(MAXH+1))


def matmul(A,B):
    n=len(A)
    return tuple(
        tuple(sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n))
        for i in range(n)
    )


def main():
    words=residue_maximal_words()
    f28=all_factors(28)
    mats={f:matrix28(f,words) for f in f28}

    min_rows=tuple(min(sum(M[i]) for M in mats.values()) for i in range(3))
    assert min_rows==EXPECTED_MIN_ROW

    factors=all_factors(336)
    assert len(factors)==337

    I=((1,0,0),(0,1,0),(0,0,1))
    pmax=[[0]*3 for _ in range(3)]
    for f in factors:
        P=I
        for t in range(0,336,28):
            P=matmul(P,mats[f[t:t+28]])
        for i in range(3):
            for j in range(3):
                pmax[i][j]=max(pmax[i][j],P[i][j])
    pmax=tuple(tuple(row) for row in pmax)
    assert pmax==EXPECTED_PMAX

    for i,row in enumerate(pmax):
        pv=sum(row[j]*POTENTIAL[j] for j in range(3))
        lhs=56**12*pv
        rhs=(1<<336)*POTENTIAL[i]
        assert lhs<rhs
        print("row",i,"margin",rhs-lhs)

    assert 56*min_rows[2]>(1<<28)
    assert 56*min_rows[1]<(1<<28)

    print("length-336 mechanical factors=337")
    print("three-state growth < 2^336/56^12: PASS")
    print("incoming H=2 automatic at K<56: PASS")
    print("remaining incoming heights: H=0,1")


if __name__=="__main__":
    main()
