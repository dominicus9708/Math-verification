#!/usr/bin/env python3
"""Exact L=8 local-residue-maximal entropy certificate.

This is a structural certificate in the Collatz proof program, not a proof of
the Collatz conjecture.

For each 8-bit parity word w with q odd symbols, let R(w) be its affine
correction.  Within each full-Hensel class R mod 3^q, replacing a non-maximal
word by a larger-correction sibling gives a smaller predecessor of the current
block state.

SCOPE CORRECTION (2026-08-25): for a later block beginning at x this local
predecessor is x-Delta<x, but it need not be smaller than the original
least-counterexample root N.  Therefore the local class arithmetic and the
entropy bound below are exact, while the claim that every later actual block is
forced into this locally maximal language requires a separate root-pullback,
headroom, or repair-budget theorem.  See
`2026-08-25-l7-global-maximality-scope-correction.md`; the same logical issue
applies to L8.

The complete 2^8 cube has occupied class counts

    c_q = (1,2,6,17,34,36,22,8,1).

The exact maximum predecessor credit in any class is 42.

For coefficient-surviving paths, an aligned length-8 mechanical block has
reference odd count Q in {5,6}.  With z=23/18>1, the worse weighted class sum is
therefore the Q=5 polynomial

    F = sum_q c_q z^(q-5).

We prove using integer arithmetic only that

    F^15 < 2^104.

Fifteen blocks have length 120.  Hence, after dropping all intermediate
nonnegativity constraints (which only enlarges the language), the number of
locally residue-maximal coefficient-surviving 120-step words is <2^104.
Thus the locally maximal sublanguage has exclusion rate >16/120=2/15 bits per
step.  This is a conditional/local-language rate until a valid later-block
globalization theorem is supplied.
"""
from fractions import Fraction
from itertools import product

L = 8
Z = Fraction(23,18)
EXPECTED = (1,2,6,17,34,36,22,8,1)


def correction(bits):
    R=0
    q=0
    for i,b in enumerate(bits):
        if b:
            R=3*R+(1<<i)
            q+=1
    return q,R


def enumerate_classes():
    p3=[1]
    for _ in range(L): p3.append(3*p3[-1])
    classes=[{} for _ in range(L+1)]
    for bits in product((0,1), repeat=L):
        q,R=correction(bits)
        r=R%p3[q]
        ent=classes[q].get(r)
        if ent is None:
            classes[q][r]=[R,R]
        else:
            ent[0]=min(ent[0],R)
            ent[1]=max(ent[1],R)
    return classes,p3


def main():
    classes,p3=enumerate_classes()
    counts=tuple(len(c) for c in classes)
    assert counts==EXPECTED

    max_credit=0
    for q,cls in enumerate(classes):
        for lo,hi in cls.items():
            pass
    for q,cls in enumerate(classes):
        for lo_hi in cls.values():
            lo,hi=lo_hi
            assert (hi-lo)%p3[q]==0
            max_credit=max(max_credit,(hi-lo)//p3[q])
    assert max_credit==42

    # Worst reference Q is 5 since z>1; Q=6 is smaller by a factor z.
    F=sum(Fraction(c)*Z**(q-5) for q,c in enumerate(EXPECTED))

    # Exact macro entropy inequality: 15*8=120 steps, allowed exponent <104.
    assert F.numerator**15 < F.denominator**15 * (1<<104)

    print("L8 class counts", counts)
    print("max_local_predecessor_credit", max_credit)
    print("z", Z)
    print("worst_block_factor", F)
    print("macro_steps", 120)
    print("macro_allowed_bits_lt", 104)
    print("local_language_exclusion_rate_gt", "2/15")
    print("later_block_globalization", "REQUIRES_SEPARATE_BRIDGE")
    print("L8 residue-maximal entropy certificate: PASS")


if __name__=="__main__":
    main()
