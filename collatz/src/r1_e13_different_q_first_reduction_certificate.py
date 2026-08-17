#!/usr/bin/env python3
"""Exact first reduction of different-q E=13 pre-G13 pullback channels.

The actual path has E=13 and Q=1526.  Let an alternate path have

    E' = 13-s,   Q' = Q+s,   s>=1.

Reindex the alternate even events by r=s+j.  Then

    e'_r = Q-p'_j+r

and every normalized correction term is again

    2^(r-e'_r) 3^e'_r,

but the alternate coefficient ranks 0,...,s-1 are absent.  Thus different-q
pullback is the same formation automaton with low alternate channels deleted.

The actual E=13 formation bound epsilon_actual<114 gives the exact alternate
root envelope

    U_0' < (NMAX+115)/3^s.

Using the exact odd-run cap r<=floor(log2 U), the maximal number of steps
coverable with E'=13-s evens is obtained by repeatedly taking the longest
currently admissible odd run before each even.  At s=8 (E'=5) the maximum is
1473<1539, and the bound decreases thereafter.  Hence s>=8 is impossible.

For the remaining s=1,...,7, the terminal inverse-limit relation is unchanged
for s<=5 because the retained terminal ranks are 5,...,12 on both sides.  It
therefore has the same 403 transition-parent labels as the same-q terminal
certificate.  Deleting rank 5 at s=6 leaves exactly 158 labels; deleting ranks
5 and 6 at s=7 leaves exactly 61.

Thus the entire different-q frontier reduces to seven channels and 2234
(s,credit) terminal fibres before the early-rank/time-gap/core-residue filters.
This is a reduction theorem, not a proof that those fibres exist physically.
"""
from fractions import Fraction
from functools import lru_cache
import hashlib

T=1539
NMAX=5_908_625_413_101_667_397_287
BASE_403=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 45, 46, 47, 48, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 72, 74, 75, 76, 77, 78, 79, 81, 83, 84, 85, 86, 87, 88, 90, 91, 92, 93, 94, 95, 96, 97, 99, 101, 102, 103, 104, 105, 106, 108, 111, 112, 113, 114, 115, 116, 117, 118, 119, 121, 122, 123, 124, 126, 128, 129, 130, 131, 132, 135, 137, 138, 139, 141, 142, 144, 145, 146, 147, 148, 151, 152, 153, 155, 156, 157, 159, 160, 162, 166, 168, 170, 171, 172, 173, 174, 175, 176, 177, 178, 182, 183, 186, 189, 191, 192, 193, 194, 195, 197, 198, 202, 203, 204, 205, 207, 209, 212, 213, 216, 219, 220, 221, 222, 227, 228, 229, 230, 231, 232, 234, 237, 238, 239, 240, 243, 249, 250, 252, 254, 255, 256, 257, 258, 259, 261, 263, 264, 267, 268, 273, 274, 276, 279, 283, 284, 288, 290, 291, 292, 295, 297, 303, 306, 307, 310, 318, 319, 320, 324, 328, 330, 333, 335, 338, 342, 344, 345, 348, 349, 351, 355, 357, 360, 364, 365, 367, 372, 374, 375, 378, 381, 384, 385, 387, 388, 391, 394, 396, 401, 402, 409, 411, 414, 426, 432, 435, 436, 438, 445, 446, 459, 465, 472, 477, 480, 486, 492, 495, 499, 507, 513, 516, 517, 522, 526, 540, 544, 546, 558, 561, 567, 576, 578, 581, 582, 583, 587, 591, 594, 603, 607, 621, 633, 639, 648, 654, 657, 662, 668, 669, 689, 708, 720, 729, 738, 774, 783, 789, 810, 816, 819, 837, 864, 867, 871, 873, 891, 895, 924, 972, 981, 993, 1002, 1003, 1039, 1062, 1080, 1094, 1107, 1154, 1161, 1175, 1215, 1224, 1296, 1312, 1336, 1366, 1384, 1386, 1458, 1503, 1593, 1620, 1640, 1641, 1690, 1731, 1732, 1750, 1822, 1836, 1849, 1944, 1958, 1968, 1984, 2004, 2049, 2065, 2076, 2077, 2079, 2083, 2187, 2257, 2309, 2430, 2460, 2461, 2535, 2551, 2597, 2598, 2625, 2733, 2754, 2916, 2937, 2952, 2976, 3006, 3113, 3114, 3281, 3382, 3645, 3690, 3897, 4131, 4374, 4428, 4464, 4509, 4669, 4671, 4677, 5072, 5073, 5535, 6226, 6561, 6642, 6696]
assert len(BASE_403)==403

EXPECTED_S6_SHA="86ad015d5f33df41885c7bf109cae203a24441bbe9f443291112b9099af56326"
EXPECTED_S7_SHA="9ebabc5fb6d5efd5864a27b061b3c94ce7bfe308ebe681ba8f939f786c82e1de"

def pow2(k):
    return Fraction(1<<k,1) if k>=0 else Fraction(1,1<<(-k))

def floor_log2(q):
    k=q.numerator.bit_length()-q.denominator.bit_length()
    while pow2(k)>q: k-=1
    while pow2(k+1)<=q: k+=1
    return k

def odd_run_then_even(U,r):
    return (Fraction(3,2)**r*U+1)/2

def max_cover(U,evens):
    total=0
    for _ in range(evens):
        r=floor_log2(U)
        total+=r+1
        U=odd_run_then_even(U,r)
    return total+floor_log2(U)

def block_sum(offset,after,before):
    return (1<<(offset+before))-(1<<(offset+after))

def terminal_survivors(s):
    # For s<=5 the terminal coefficient ranks 5..12 are literally unchanged.
    if s<=5:
        return BASE_403[:]
    off=max(5,s)
    b0=13-off
    @lru_cache(None)
    def accepts(a,b,c):
        if c==0:
            return True
        if c%3==0:
            c2=2*(c//3)
            if abs(c2)<abs(c) and accepts(a,b,c2):
                return True
        for a2 in range(a+1):
            A=block_sum(5,a2,a)
            for b2 in range(b+1):
                if a2==a and b2==b:
                    continue
                B=block_sum(off,b2,b)
                z=c+B-A
                if z%3==0 and accepts(a2,b2,2*(z//3)):
                    return True
        return False
    return [d for d in BASE_403 if accepts(8,b0,(1<<13)*d)]

def digest(v):
    return hashlib.sha256(",".join(map(str,v)).encode()).hexdigest()

def main():
    # Root/run-cover exclusion for s>=8.
    covers={}
    for s in range(1,14):
        Ealt=13-s
        Ucap=Fraction(NMAX+115,3**s)
        covers[s]=max_cover(Ucap,Ealt)
    assert covers[8]==1473
    assert all(covers[s]<T for s in range(8,14))
    assert covers[7]>=T

    s6=terminal_survivors(6)
    s7=terminal_survivors(7)
    assert len(s6)==158 and digest(s6)==EXPECTED_S6_SHA
    assert len(s7)==61 and digest(s7)==EXPECTED_S7_SHA

    counts={s:(403 if s<=5 else len(s6) if s==6 else len(s7)) for s in range(1,8)}
    assert counts=={1:403,2:403,3:403,4:403,5:403,6:158,7:61}
    assert sum(counts.values())==2234

    print("different-q E13 first reduction: PASS")
    print("max-cover steps by s:", covers)
    print("s>=8 impossible by root/run-cover envelope")
    print("terminal fibre counts s=1..7:", counts)
    print("total remaining (s,credit) terminal fibres =",sum(counts.values()))
    print("s6 sha256 =",digest(s6))
    print("s7 sha256 =",digest(s7))

if __name__=="__main__":
    main()
