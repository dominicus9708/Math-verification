#!/usr/bin/env python3
"""Normalized correction defect as a positive compositional functional.

For equal-one-count target/candidate words define

    eta(T,W) = (C(T)-C(W))/3^q.

If corresponding blocks split as

    T=U V,  W=U' V',

with equal component lengths and one-counts, correction composition gives

    eta(T,W)
      = eta(U,U') + mu(U) eta(V,V'),

where

    mu(U)=2^|U| / 3^q(U) > 0.

Thus eta is a positive affine/semiring functional on exact family products.
For a Cartesian product of dominance factors, minimum defect bounds compose
without enumerating product leaves.

There is also an exact positive-gap theorem for a prefix-dominance family.
Let T have q ones and let W range over words whose r-th one position is no
later than the target r-th one.  Every W can be obtained from T by a sequence
of adjacent moves

    01 -> 10.

Moving the r-th one from p+1 to p decreases C by

    3^(q-r) 2^p,

so it increases normalized eta by

    2^p / 3^r > 0.

Consequently the minimum positive normalized defect in the whole dominance
family is exactly the cheapest legal *single* adjacent swap available in T:

    eta_min^+(T)
      = min_{T[p:p+2]=01} 2^p/3^r(p+1).

If T admits no 01, its dominance family is a singleton.

For the threshold/mechanical target, a legal swap ending at prefix length n=p+2
has r=floor(alpha*n)+1, alpha=log_3(2), hence

    2^p/3^r = 3^{ {alpha*n} } / 12,

so every positive dominance defect is at least 1/12.  The exact finite minimum
is determined by the smallest fractional phase among legal 01 swap positions.

This connects the H/L/slack family language directly to the existing monotone
prefix-defect/real-envelope pruning metric.  It does not by itself show that
the current physical shells exceed the rejection threshold.
"""

from fractions import Fraction
from itertools import combinations, product

MAX_H = 8


def correction(bits):
    C = 0
    q = 0
    for h,bit in enumerate(bits):
        if bit:
            C = 3*C + (1 << h)
            q += 1
    return C,q


def eta(T,W):
    CT,qT = correction(T)
    CW,qW = correction(W)
    assert len(T)==len(W) and qT==qW
    return Fraction(CT-CW,3**qT)


def mu(U):
    _,q = correction(U)
    return Fraction(2**len(U),3**q)


def positions(bits):
    return tuple(i for i,b in enumerate(bits) if b)


def dominates(W,T):
    a=positions(T)
    b=positions(W)
    return len(a)==len(b) and all(b[i]<=a[i] for i in range(len(a)))


def min_adjacent_swap_cost(T):
    costs=[]
    prefix_ones=0
    for p in range(len(T)-1):
        prefix_ones += T[p]
        if T[p]==0 and T[p+1]==1:
            r=prefix_ones+1
            costs.append(Fraction(2**p,3**r))
    return min(costs) if costs else None


composition_checks=0
for n in range(1,7):
    for T in product((0,1),repeat=n):
        for cut in range(n+1):
            U,V=T[:cut],T[cut:]
            qU=sum(U);qV=sum(V)
            Ucands=[x for x in product((0,1),repeat=len(U)) if sum(x)==qU]
            Vcands=[x for x in product((0,1),repeat=len(V)) if sum(x)==qV]
            for U2 in Ucands[:3]:
                for V2 in Vcands[:3]:
                    lhs=eta(T,U2+V2)
                    rhs=eta(U,U2)+mu(U)*eta(V,V2)
                    assert lhs==rhs
                    composition_checks+=1


gap_checks=0
for h in range(1,MAX_H+1):
    for T in product((0,1),repeat=h):
        q=sum(T)
        if q==0:
            continue
        target_pos=positions(T)
        defects=[]
        for posW in combinations(range(h),q):
            if not all(posW[r]<=target_pos[r] for r in range(q)):
                continue
            W=tuple(1 if i in set(posW) else 0 for i in range(h))
            if W!=T:
                val=eta(T,W)
                assert val>0
                defects.append(val)

        direct_min=min(defects) if defects else None
        swap_min=min_adjacent_swap_cost(T)
        assert direct_min==swap_min
        gap_checks+=1

assert gap_checks==502
assert composition_checks>0

print("PASS A0 s=1 Route-B normalized-defect semiring certificate")
print("composition_checks",composition_checks)
print("dominance_gap_checks",gap_checks)
print(
    "composition",
    "eta(UV)=eta(U)+[2^|U|/3^q(U)]*eta(V)",
)
print(
    "positive_gap",
    "minimum nonzero dominance defect equals the cheapest target 01->10 adjacent swap",
)
print(
    "threshold_bound",
    "each legal threshold adjacent-swap cost is 3^{frac(alpha*n)}/12 >= 1/12",
)
print(
    "dsd_audit",
    "target-collision coordinates and actual monotone membership defect are kept distinct; this file addresses the latter",
)
print(
    "status",
    "positive defect composition/gap CLOSED; sufficient physical-shell rejection from long grammar remains OPEN",
)
