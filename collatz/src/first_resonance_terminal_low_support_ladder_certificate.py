#!/usr/bin/env python3
"""Exact low-support ladder for the first-global-resonance terminal address.

Proves, in the repaired first-global-resonance branch,

    D_tail(50) >= 3,
    D_tail(52) >= 4,
    D_tail(56) >= 5,
    D_tail(58) >= 6.

Here D_tail(m) counts displaced odd ordinals among the final m odd ordinals.
Together with the independent D_72>=11 prefix theorem this gives r_*>=17.

The enumeration is exact integer modular arithmetic.  It does not use the
ternary recursively-sufficient selector, repeated L7/L14 pullback, random
sampling, floating point, or an independence assumption.
"""

from fractions import Fraction
from itertools import combinations, product

A = 114_208_327_604
Q = 72_057_431_991
AL = 103_768_467_013
QL = 65_470_613_321
LOW = 2**71
UPPER_TIMES_3 = 4 * 2**71 + 3 * 2**33
NLOG = 120


def log_bounds(z: Fraction, n: int):
    s = Fraction(0)
    for k in range(n + 1):
        s += 2 * z ** (2*k + 1) / (2*k + 1)
    tail = 2 * z ** (2*n + 3) / ((2*n + 3) * (1-z*z))
    return s, s + tail


# Self-audit the Farey floor model used for the mechanical positions.
l2, u2 = log_bounds(Fraction(1,3), NLOG)
l3, u3 = log_bounds(Fraction(1,2), NLOG)
assert AL * u2 < QL * l3
assert A * l2 > Q * u3
assert A * QL - AL * Q == 1


def b(j: int) -> int:
    # For 1<=j<=Q, Farey adjacency gives
    # floor((j-1) log_2 3) = floor((j-1) A/Q).
    assert 1 <= j <= Q
    return ((j-1) * A) // Q


def admissible(y: int) -> bool:
    # y=N+g, N>2^71, 0<g<2^33, N==y==3 mod 4.
    return LOW < y and 3*y < UPPER_TIMES_3 and y % 4 == 3


def precompute(m: int):
    M = 3**m
    inv = pow(2,-A,M)
    B = [b(Q-m+1+t) for t in range(m)]
    gaps = [None] + [B[t]-B[t-1] for t in range(1,m)]
    assert all(g in (1,2) for g in gaps[1:])

    base=[]
    y_mech=0
    for t,Bt in enumerate(B):
        w = inv * pow(3,m-1-t,M) * pow(2,Bt,M) % M
        base.append(w)
        y_mech = (y_mech+w) % M
    return M,B,gaps,base,y_mech


def contribution(base_t: int, d: int, M: int) -> int:
    assert d > 0
    return base_t * (pow(2,-d,M)-1) % M


def enumerate_exact_support(m: int, k: int):
    """Enumerate all endpoint residue classes with exactly k terminal defects.

    If a support begins at t=0 with a positive run 0,...,L-1, there is no
    left boundary inside the window.  The t-th displacement is visible only
    modulo 2*3^t, so all residue tuples are enumerated.  Every tuple has
    positive representatives satisfying the one-sided ordering constraints:
    choose representatives backward from t=L-1, adding periods to earlier
    coordinates as needed.

    Every later positive run starts after a zero.  Ordering then forces its
    first displacement to be exactly 1 across a mechanical gap 2; adjacent
    positive values satisfy d_t <= d_{t-1}+gap_t-1.  Hence those runs have a
    finite exact enumeration.
    """
    M,B,gaps,base,y_mech = precompute(m)
    total_classes=0
    survivors=[]

    for support_tuple in combinations(range(m),k):
        support=set(support_tuple)
        L=0
        while L<m and L in support:
            L+=1

        if L:
            initial_residues = product(*[range(2*3**t) for t in range(L)])
        else:
            initial_residues = [()]

        later=[]
        def rec(t,cur):
            if t==m:
                later.append(dict(cur));
                return
            if t not in support:
                rec(t+1,cur)
                return
            assert t>=L and t>0
            if (t-1) not in support:
                if gaps[t] != 2:
                    return
                vals=(1,)
            else:
                prev=cur[t-1]
                vals=range(1,prev+gaps[t])
            for val in vals:
                cur[t]=val
                rec(t+1,cur)
            cur.pop(t,None)
        rec(L,{})
        if not later:
            continue

        later_sums=[]
        for dmap in later:
            s=0
            for t,d in dmap.items():
                s=(s+contribution(base[t],d,M))%M
            later_sums.append((s,dmap))

        for residues in initial_residues:
            s0=0
            for t,r in enumerate(residues):
                period=2*3**t
                d = r if r else period
                s0=(s0+contribution(base[t],d,M))%M
            for slater,dmap in later_sums:
                total_classes += 1
                y=(y_mech+s0+slater)%M
                if admissible(y):
                    survivors.append((support_tuple,residues,dict(dmap),y))

    return total_classes,survivors


def endpoint_from_global_displacements(m: int, global_disp) -> int:
    M=3**m
    inv=pow(2,-A,M)
    total=0
    for t in range(m):
        j=Q-m+1+t
        d=global_disp.get(j,0)
        a=b(j)-d
        total=(total + pow(3,m-1-t,M)*pow(2,a,M))%M
    return inv*total%M


# -------------------------------------------------------------------------
# Last 50: supports 0,1,2 are empty; support 3 has one class.
# -------------------------------------------------------------------------
EXPECTED_COUNTS_50 = {0:1,1:31,2:502,3:5828}
for k in range(3):
    count,surv=enumerate_exact_support(50,k)
    assert count == EXPECTED_COUNTS_50[k]
    assert surv == []

count3,surv3=enumerate_exact_support(50,3)
assert count3 == EXPECTED_COUNTS_50[3]
assert surv3 == [
    ((0,18,45),(1,),{18:1,45:1},2_697_452_540_596_458_587_755)
]
# Therefore D_tail(50)>=3.

# If D_tail(52)=3, all three defects must be the unique last-50 class and the
# two newly prepended ordinals must be mechanical.  That extension fails at
# modulus 3^52.
g3={Q-49:1,Q-31:1,Q-4:1}
y3=2_697_452_540_596_458_587_755
assert endpoint_from_global_displacements(50,g3)==y3
assert endpoint_from_global_displacements(51,g3)==y3
assert endpoint_from_global_displacements(52,g3)!=y3
# Hence D_tail(52)>=4.

# -------------------------------------------------------------------------
# Last 52: exact four-defect equality layer.
# -------------------------------------------------------------------------
count4,surv4=enumerate_exact_support(52,4)
assert count4 == 72_305
assert surv4 == [
    ((11,12,41,51),(),{11:1,12:1,41:1,51:1},
     2_704_820_911_452_840_622_043)
]
g4={Q-40:1,Q-39:1,Q-10:1,Q:1}
y4=2_704_820_911_452_840_622_043
assert endpoint_from_global_displacements(52,g4)==y4
for m in (53,54,55):
    assert endpoint_from_global_displacements(m,g4)==y4
assert endpoint_from_global_displacements(56,g4)!=y4
# Hence D_tail(56)>=5.

# -------------------------------------------------------------------------
# Last 56: exact five-defect equality layer.
# -------------------------------------------------------------------------
count5,surv5=enumerate_exact_support(56,5)
assert count5 == 2_886_114
assert surv5 == [
    ((0,15,16,45,55),(1,),{15:1,16:1,45:1,55:1},
     2_704_820_911_452_840_622_043)
]
g5={Q-55:1,Q-40:1,Q-39:1,Q-10:1,Q:1}
assert endpoint_from_global_displacements(56,g5)==y4
assert endpoint_from_global_displacements(57,g5)==y4
assert endpoint_from_global_displacements(58,g5)!=y4
# Hence D_tail(58)>=6.

# The earliest of the final 58 odd ordinals has ordinal Q-57 and therefore
# actual position at least Q-58, far beyond the first 72 positions.  The
# terminal and D_72 supports are disjoint.
assert Q-58 > 72
PREFIX_LOWER=11
TAIL58_LOWER=6
TOTAL_LOWER=PREFIX_LOWER+TAIL58_LOWER
assert TOTAL_LOWER==17

print("PASS first-resonance terminal low-support ladder")
print("D_tail(50)>=3")
print("D_tail(52)>=4")
print("D_tail(56)>=5")
print("D_tail(58)>=6")
print("last50_k3_classes",count3,"survivors",len(surv3))
print("last52_k4_classes",count4,"survivors",len(surv4))
print("last56_k5_classes",count5,"survivors",len(surv5))
print("with D_72>=11: r_*>=17")
print("coarse normalized correction: E/3^Q > 17/12")
