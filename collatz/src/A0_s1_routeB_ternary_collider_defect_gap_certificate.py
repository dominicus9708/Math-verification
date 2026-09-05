#!/usr/bin/env python3
"""Positive normalized-defect gap for a nontrivial ternary suffix collider.

Consider the strict-high / H-characteristic target.  Let its r-th one be at
position a_r.  With alpha=log_3(2), prefix count satisfies

    r = floor(alpha*(a_r+1)) + 1.

Hence the normalized defect weight of that one is

    w_r = 2^{a_r}/3^r
        = 3^{ frac(alpha*(a_r+1)) } / 6,

so universally

    1/6 <= w_r < 1/2.

Now compare a prefix-dominance candidate that collides with the target modulo
3^L.  Process the last L one-position pairs from the right using the normalized
suffix recurrence.

If all earlier processed displacements are zero, the normalized carry remains
u=0.  Therefore the *first* nonzero displacement delta encountered in this
suffix must satisfy

    1 - 2^{-delta} == 0 mod 3,

so delta is even.  Nonzero therefore means delta>=2.  Its single positive
normalized correction-defect atom is

    w_r (1-2^{-delta})
      >= (1/6)(1-1/4)
      = 1/8.

All other dominance-defect atoms are nonnegative.  Consequently:

    any mod-3^L collider that differs from the target within the last L one
    positions has eta >= 1/8 from that suffix deviation alone.

If the last L one positions match exactly, the theorem makes no claim about
where an earlier defect lies; this distinction is essential.

This connects the projective ternary decoder to the actual monotone eta used by
the physical real-envelope pruning certificates.
"""

from fractions import Fraction
from itertools import combinations

MAX_H = 13

# Exact requirement construction avoids floating point.
def requirements(nmax):
    q=[0]
    p2=p3=1
    k=0
    for _ in range(1,nmax+1):
        p2*=2
        while p3<=p2:
            p3*=3
            k+=1
        q.append(k)
    return q

REQ=requirements(MAX_H+2)


def hchar(h):
    return tuple(REQ[i+1]-REQ[i] for i in range(h))


def correction_positions(pos):
    q=len(pos)
    return sum(3**(q-r-1)*2**a for r,a in enumerate(pos))


def v3(n):
    n=abs(n)
    assert n
    out=0
    while n%3==0:
        n//=3
        out+=1
    return out


weight_checks=0
collider_gap_checks=0
for h in range(2,MAX_H+1):
    T=hchar(h)
    apos=tuple(i for i,b in enumerate(T) if b)
    q=len(apos)
    Ct=correction_positions(apos)

    # Exact rational weight bound, derived also directly from the threshold
    # inequalities 3^(r-1) <= 2^(a+1) < 3^r.
    for r,a in enumerate(apos,1):
        w=Fraction(2**a,3**r)
        assert Fraction(1,6) <= w < Fraction(1,2)
        weight_checks+=1

    for bpos in combinations(range(h),q):
        if bpos==apos or not all(bpos[i]<=apos[i] for i in range(q)):
            continue
        Cw=correction_positions(bpos)
        eta=Fraction(Ct-Cw,3**q)
        assert eta>0

        for L in range(1,q+1):
            if (Ct-Cw)%(3**L):
                continue
            start=q-L
            if bpos[start:]==apos[start:]:
                continue

            # First differing one when scanning this suffix from the right.
            first=None
            for idx in range(q-1,start-1,-1):
                if bpos[idx]!=apos[idx]:
                    first=idx
                    break
            assert first is not None
            delta=apos[first]-bpos[first]
            # All positions to its right are equal, so the incoming carry is 0;
            # mod-3 collision forces even displacement.
            assert delta>=2 and delta%2==0
            atom=Fraction(
                2**apos[first]-2**bpos[first],
                3**(first+1),
            )
            assert atom>=Fraction(1,8)
            assert eta>=atom
            collider_gap_checks+=1

assert weight_checks>0
assert collider_gap_checks>0

print("PASS A0 s=1 Route-B ternary-collider defect-gap certificate")
print("max_h",MAX_H)
print("weight_checks",weight_checks)
print("collider_gap_checks",collider_gap_checks)
print("weight_bound","1/6 <= 2^a_r/3^r < 1/2")
print("nontrivial_suffix_collider_gap","eta_suffix >= 1/8")
print(
    "dsd_audit",
    "the gap applies only when the observed last-L one positions contain a real deviation; exact suffix agreement is kept separate",
)
print(
    "status",
    "ternary arithmetic -> positive physical defect bridge CLOSED; shell-wide rejection threshold still OPEN",
)
