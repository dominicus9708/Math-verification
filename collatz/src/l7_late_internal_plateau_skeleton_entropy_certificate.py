#!/usr/bin/env python3
"""Exact finite quotient counts for late internal plateau orientations in L7.

For H divisible by 7, count coefficient-surviving, aligned-L7-residue-maximal
boundary words with q_H=b(H). Then quotient only mixed Beatty plateau pairs
whose starts are
  * late: j >= 71, and
  * internal to one aligned 7-block: j % 7 <= 5.
The internal-only choice is conservative: cross-block plateau pairs are left
fully resolved and contribute no quotient gain.

Regression values are certified at the critical m=44 depth H=315 and at the
700-step L7 macro scale. This is a weighted-L2/common-spectrum auxiliary
certificate, not by itself a first-order same-integer overlap theorem.
"""

from collections import defaultdict


def barrier_table(H):
    out=[]
    p3=1
    q=0
    for j in range(H+1):
        p2=1<<j
        while p3<p2:
            p3*=3
            q+=1
        out.append(q)
    return out


def l7_allowed():
    best=[{} for _ in range(8)]
    for mask in range(128):
        q=0
        R=0
        for i in range(7):
            if (mask>>i)&1:
                R=3*R+(1<<i)
                q+=1
        key=R%(3**q)
        old=best[q].get(key)
        if old is None or R>old[0]:
            best[q][key]=(R,mask)
    counts=tuple(len(d) for d in best)
    assert counts==(1,2,6,15,21,16,7,1)
    return tuple(sorted(mask for d in best for _,mask in d.values()))

ALLOWED=l7_allowed()


def canon_block(mask, off, b, threshold=71):
    bits=[(mask>>k)&1 for k in range(7)]
    for k in range(6):
        j=off+k
        if j>=threshold and b[j+1]==b[j] and bits[k]+bits[k+1]==1:
            bits[k],bits[k+1]=0,1
    return sum(bit<<k for k,bit in enumerate(bits))


def counts(H, threshold=71):
    assert H%7==0
    b=barrier_table(H)
    full={0:1}
    quotient={0:1}

    for off in range(0,H,7):
        q0s=set(full)|set(quotient)
        ta={}
        tq={}
        for q0 in q0s:
            accepted=[]
            for mask in ALLOWED:
                q=q0
                ok=True
                for k in range(7):
                    q+=(mask>>k)&1
                    if q<b[off+k+1]:
                        ok=False
                        break
                if ok:
                    accepted.append((mask,q))

            ca=defaultdict(int)
            cq=defaultdict(set)
            for mask,q1 in accepted:
                ca[q1]+=1
                cq[q1].add(canon_block(mask,off,b,threshold))
            ta[q0]=dict(ca)
            tq[q0]={q1:len(keys) for q1,keys in cq.items()}

        nf=defaultdict(int)
        for q0,n in full.items():
            for q1,mult in ta[q0].items():
                nf[q1]+=n*mult
        nq=defaultdict(int)
        for q0,n in quotient.items():
            for q1,mult in tq[q0].items():
                nq[q1]+=n*mult
        full=dict(nf)
        quotient=dict(nq)

    q=b[H]
    return full.get(q,0), quotient.get(q,0), q


EXPECTED={
    315: (
        517885458235304308157182410734564932221743686697609244752296472620411591960348,
        63820688520932622184721715929174699158591849888248537439621754920000435,
        199,
    ),
    700: (
        645689734914183363821586792441235488458868199403315076106181388545396779258640538805225372262002990810695394148445364291510021385381790982033492390207338527017080420714113841399,
        1325116145742994128504793391221753016111408517063735997913466408888656679579695514192819981925155986595337748471956945110285694798063467723859180975004214036843,
        442,
    ),
}

for H,expected in EXPECTED.items():
    got=counts(H)
    assert got==expected, (H,got,expected)
    A,Q,bH=got
    print(f"H={H} bH={bH}")
    print(f"full={A}")
    print(f"quotient={Q}")
    if H==315:
        assert A>Q*(1<<22)
        assert not A>Q*(1<<23)
        print("exact gap: 2^22 < full/quotient <= 2^23")
    if H==700:
        assert A>Q*(1<<58)
        assert not A>Q*(1<<59)
        print("exact gap: 2^58 < full/quotient <= 2^59")

print("late internal plateau skeleton entropy certificate: PASS")
