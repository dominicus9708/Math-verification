#!/usr/bin/env python3
"""Exact position-dependent branching wedge for first-resonance repairs.

At odd ordinal j, displacement satisfies
    d_j <= floor((j-1) P/Q).
An L-trit alignment repair is one class modulo 2*3^L.  Therefore two ordinary
representatives cannot coexist until the local displacement cap reaches that
modulus.  The global ordering-debt budget further caps d by 19106028518.
"""

P=42_150_895_613
Q=72_057_431_991
GLOBAL_DMAX=19_106_028_518

EXPECTED={
    15:49_059_239,
    16:147_177_713,
    17:441_533_135,
    18:1_324_599_402,
    19:3_973_798_204,
    20:11_921_394_610,
}


def first_possible_multiple_j(L:int):
    M=2*3**L
    if M>GLOBAL_DMAX:
        return None
    # Need floor((j-1)P/Q) >= M, equivalently j-1 >= ceil(MQ/P).
    x=(M*Q + P-1)//P
    return x+1


def main():
    for L,j in EXPECTED.items():
        assert first_possible_multiple_j(L)==j
        M=2*3**L
        assert ((j-2)*P)//Q < M
        assert ((j-1)*P)//Q >= M

    # L>=21 is globally unique because the repair modulus exceeds the full
    # budget-feasible displacement cap.
    assert 2*3**21 > GLOBAL_DMAX
    assert first_possible_multiple_j(21) is None

    print('PASS first-resonance position-dependent repair branching')
    for L in range(15,21):
        j=first_possible_multiple_j(L)
        print(L, 'first_possible_multiple_j', j,
              'unique_prefix_ordinals', j-1)
    print('L>=21: globally at most one ordinary repair representative')


if __name__=='__main__':
    main()
