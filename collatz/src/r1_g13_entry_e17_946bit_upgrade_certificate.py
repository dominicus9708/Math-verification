#!/usr/bin/env python3
"""Exact current-R1 G13 entrance upgrade after excluding E=13..16.

Input theorem: e_1539 >= 17.
The exact relaxed U=x+1 endpoint optimizer has floor(log2 U_max)=945 at
E=17, and smaller values for every larger relevant even count. Hence
x_1539 < 2^946.

Since 946=49*19+15, natural G13 lift chunks obey
    t_49 < 2^15,
    t_b = 0 for b>=50.
Thus 20026-946=19080 high G13 address bits are forced to zero.
"""
from fractions import Fraction

NMAX=6*3**44+1
U0=Fraction(NMAX+1,1)
T=1539
G13_L=20026

def floor_log2(q):
    k=q.numerator.bit_length()-q.denominator.bit_length()
    while Fraction(1<<k,1)>q:k-=1
    while Fraction(1<<(k+1),1)<=q:k+=1
    return k

def odd_run_then_even(U,r):
    return (Fraction(3,2)**r*U+1)/2

def greedy(evens):
    U=U0; rs=T; re=evens
    for _ in range(evens):
        r=min(floor_log2(U),rs-re)
        U=odd_run_then_even(U,r); rs-=r+1; re-=1
    assert rs<=floor_log2(U)
    return Fraction(3,2)**rs*U

def main():
    expected={17:945,18:944,19:942,20:940}
    for E,k in expected.items():
        U=greedy(E)
        assert floor_log2(U)==k
        assert U < (1<<946)
    coarse=U0*Fraction(3,2)**(T-21)*Fraction(3,4)**21
    assert coarse < (1<<946)
    assert 946==49*19+15
    assert G13_L-946==19080
    print("R1 G13 E>=17 / 946-bit entrance certificate: PASS")
    print("e_1539 >= 17; q_1539 <= 1522; s0 <= 550")
    print("x_1539 < 2^946")
    print("natural_cut t_49 < 2^15; t_b=0 for b>=50")
    print("forced_zero_high_G13_bits 19080")

if __name__=='__main__':
    main()
