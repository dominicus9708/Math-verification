#!/usr/bin/env python3
"""Finite regression for MATH-122 exact non-singleton AP rank.

Checks the exact child multiplicity bound and strict integer rank decrease
for deterministic AP samples. The algebraic theorem is proved in the note.
"""
from math import ceil, log2


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3*n + 1)//2


def children(a: int, b: int, m: int):
    assert b > 0 and b % 2 == 1 and m >= 2
    out = []
    for parity in (0, 1):
        vals = [T(a+b*k) for k in range(m) if (a+b*k) % 2 == parity]
        if vals:
            out.append(vals)
    return out


def main():
    cases = 0
    for a in range(1, 80):
        for b in range(1, 24, 2):
            for m in range(2, 80):
                N = a+b*(m-1)
                V = (N+1)*m*m
                R = ceil(log2(m))
                for vals in children(a,b,m):
                    mp = len(vals)
                    Np = max(vals)
                    Vp = (Np+1)*mp*mp
                    Rp = 0 if mp == 1 else ceil(log2(mp))
                    assert mp <= (m+1)//2
                    assert mp < m
                    assert Rp <= R-1
                    assert Vp < V, (a,b,m,N,V,mp,Np,Vp)
                    cases += 1
    print('child_cases', cases)
    print('PASS MATH-122 exact AP resolution/value rank regression')
    print('NO PAID-LAYER CLOSURE CLAIM')


if __name__ == '__main__':
    main()
