#!/usr/bin/env python3
"""Finite regression for the MATH-123 lexicographic AP rank."""
from math import ceil, log2


def T(n: int) -> int:
    return n//2 if n % 2 == 0 else (3*n+1)//2


def main():
    cases=0
    equal_W_cases=0
    for a in range(1,80):
        for b in range(1,24,2):
            for m in range(2,80):
                N=a+b*(m-1)
                W=(N+1)*m
                for parity in (0,1):
                    vals=[T(a+b*k) for k in range(m) if (a+b*k)%2==parity]
                    if not vals:
                        continue
                    mp=len(vals)
                    Np=max(vals)
                    Wp=(Np+1)*mp
                    assert mp <= (m+1)//2
                    assert mp < m
                    assert Wp <= W, (a,b,m,parity,N,W,mp,Np,Wp)
                    assert (Wp < W) or (mp < m)
                    if Wp == W:
                        equal_W_cases += 1
                    cases += 1
    for m in range(2,10000):
        assert 3*((m+1)//2) <= 2*m
    print('child_cases',cases)
    print('equal_W_cases',equal_W_cases)
    print('PASS MATH-123 linear AP resolution rank regression')
    print('NO PAID-LAYER CLOSURE CLAIM')


if __name__=='__main__':
    main()
