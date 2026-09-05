#!/usr/bin/env python3
"""Exact terminal-46 3-adic defect certificate for the first global resonance.

This certificate proves D_tail>=2 and classifies the D_tail=2 equality layer.
It uses only exact integer modular arithmetic and ordering.  No ternary
selector, repeated L7/L14 pullback, or independence assumption is used.
"""

from itertools import combinations

A = 114_208_327_604
Q = 72_057_431_991
MOD = 3**46
LOW = 2**71
UPPER_TIMES_3 = 4 * 2**71 + 3 * 2**33
B = [
    114208327531,114208327532,114208327534,114208327535,
    114208327537,114208327539,114208327540,114208327542,
    114208327543,114208327545,114208327546,114208327548,
    114208327550,114208327551,114208327553,114208327554,
    114208327556,114208327558,114208327559,114208327561,
    114208327562,114208327564,114208327565,114208327567,
    114208327569,114208327570,114208327572,114208327573,
    114208327575,114208327577,114208327578,114208327580,
    114208327581,114208327583,114208327584,114208327586,
    114208327588,114208327589,114208327591,114208327592,
    114208327594,114208327596,114208327597,114208327599,
    114208327600,114208327602,
]
assert len(B) == 46
GAP = [None] + [B[t]-B[t-1] for t in range(1,46)]
assert all(g in (1,2) for g in GAP[1:])
INV = pow(2,-A,MOD)


def endpoint(delta):
    apos = [b-d for b,d in zip(B,delta)]
    assert all(d >= 0 for d in delta)
    assert all(apos[t] < apos[t+1] for t in range(45))
    s = 0
    for t,a in enumerate(apos):
        s = (s + pow(3,45-t,MOD)*pow(2,a,MOD)) % MOD
    return INV*s % MOD


def admissible(y):
    return LOW < y and 3*y < UPPER_TIMES_3 and y % 4 == 3


# Exact order ord_{3^(t+1)}(2)=2*3^t.
for t in range(46):
    m = 3**(t+1)
    p = 2*3**t
    assert pow(2,p,m) == 1
    if t == 0:
        assert pow(2,1,m) != 1
    else:
        assert pow(2,p//3,m) != 1

Y_MECH = endpoint([0]*46)
assert Y_MECH == 4_699_104_266_570_964_686_821
assert not admissible(Y_MECH)

# D_tail=1.
singletons = []
for d0 in (1,2):
    d=[0]*46; d[0]=d0
    singletons.append(((0,d0%2),endpoint(d)))
for t in range(1,46):
    if GAP[t] == 2:
        d=[0]*46; d[t]=1
        singletons.append(((t,1),endpoint(d)))
assert len(singletons) == 28
broad = [(k,y) for k,y in singletons if LOW < y and 3*y < UPPER_TIMES_3]
assert broad == [((9,1),2_994_179_304_232_351_671_382)]
assert broad[0][1] % 4 == 2
assert not any(admissible(y) for _,y in singletons)

# D_tail=2.
pairs=[]
assert GAP[1] == 1
for r0 in (0,1):
    for r1 in range(6):
        d1 = r1 if r1 else 6
        d0 = d1 if d1 % 2 == r0 else d1+1
        d=[0]*46; d[0]=d0; d[1]=d1
        pairs.append(((0,1,r0,r1),endpoint(d)))
for k in range(2,46):
    if GAP[k] == 2:
        for r0 in (0,1):
            d=[0]*46; d[0]=(1 if r0 else 2); d[k]=1
            pairs.append(((0,k,r0,1),endpoint(d)))
for i,k in combinations(range(1,46),2):
    if GAP[i] != 2:
        continue
    if k == i+1:
        for dk in range(1,GAP[k]+1):
            d=[0]*46; d[i]=1; d[k]=dk
            pairs.append(((i,k,1,dk),endpoint(d)))
    elif GAP[k] == 2:
        d=[0]*46; d[i]=1; d[k]=1
        pairs.append(((i,k,1,1),endpoint(d)))

assert len(pairs) == 414
survivors=[(k,y) for k,y in pairs if admissible(y)]
EXPECTED=[
    ((0,1,0,3),2_729_562_462_203_742_221_059),
    ((0,1,1,5),2_729_562_462_203_742_221_059),
    ((2,24,1,1),3_059_622_251_880_574_799_467),
    ((5,26,1,1),2_390_750_338_045_521_993_103),
    ((7,26,1,1),2_768_988_818_993_959_778_023),
    ((9,11,1,1),2_463_461_351_003_862_446_095),
    ((12,19,1,1),3_104_589_732_879_008_787_067),
    ((14,41,1,1),2_697_452_540_596_458_587_755),
    ((33,38,1,1),2_556_248_067_081_360_242_587),
]
assert survivors == EXPECTED
assert len(survivors) == 9
assert len({y for _,y in survivors}) == 8

assert Q-46 > 72
assert 11+2 == 13

print("PASS first-resonance terminal-46 triangular defect")
print("mechanical_endpoint",Y_MECH)
print("singleton_classes",len(singletons))
print("pair_classes",len(pairs))
print("pair_survivors",len(survivors))
print("distinct_pair_endpoints",len({y for _,y in survivors}))
print("D_tail>=2; with D_72>=11, r_*>=13")
for k,y in survivors:
    print("pair_survivor",k,y)
