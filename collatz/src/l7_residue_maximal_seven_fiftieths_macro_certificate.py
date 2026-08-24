#!/usr/bin/env python3
"""Exact L=7 residue-maximal 700-step macro entropy certificate.

This is a structural certificate in the Collatz proof program, not a proof of
the Collatz conjecture.

The complete 2^7 full-Hensel class counts are

    c_q = (1,2,6,15,21,16,7,1),

and the largest ordinary predecessor credit inside any class is 21.

SCOPE CORRECTION (2026-08-25): for a block beginning at a current orbit state
x, a non-maximal representative with credit Delta gives a smaller current
predecessor x-Delta.  This proves x-Delta<x, but for an arbitrary later block it
does NOT by itself prove x-Delta<N for the original least-counterexample root N.
Therefore the locally residue-maximal language and the entropy calculation
below are exact, but membership of every later block of a hypothetical least
counterexample requires a separate root-pullback/headroom or repair-budget
theorem.  See `2026-08-25-l7-global-maximality-scope-correction.md` and
`l7_later_block_globality_counterexample_certificate.py`.

For an aligned seven-step mechanical reference block, the critical odd count Q
is either 4 or 5 because

    3^4 < 2^7 < 3^5.

Take z=4/3.  For Q=5 put

    P5(z)=sum_q c_q z^(q-5).

A Q=4 block contributes the larger factor z*P5(z).

In any 700 consecutive mechanical steps there are 100 seven-step blocks.  Exact
integer comparison gives

    3^441 < 2^700 < 3^442,

so the total critical odd-count increment is at least 441.  If n4 is the number
of Q=4 blocks, then

    4 n4 + 5(100-n4) >= 441,

hence n4<=59, uniformly over the starting phase (the usual floor/ceiling
mechanical discrepancy is at most one, and this is the worse choice).

Therefore the complete weighted locally residue-maximal language of a 700-step
macro is bounded by

    F = P5(z)^100 z^59.

The exact integer inequality

    F^50 < 2^30100

is equivalent to F<2^602.  Thus the locally residue-maximal language loses more
than 98 of every 700 binary information bits:

    eta > 98/700 = 7/50.

This rate is a conditional/local-language exclusion rate until a valid
later-block globalization theorem is supplied.
"""
from fractions import Fraction
from itertools import product

L=7
Z=Fraction(4,3)
EXPECTED=(1,2,6,15,21,16,7,1)


def correction(bits):
    R=0; q=0
    for i,b in enumerate(bits):
        if b:
            R=3*R+(1<<i)
            q+=1
    return q,R


def enumerate_classes():
    p3=[1]
    for _ in range(L): p3.append(3*p3[-1])
    classes=[{} for _ in range(L+1)]
    for bits in product((0,1),repeat=L):
        q,R=correction(bits)
        r=R%p3[q]
        e=classes[q].get(r)
        if e is None: classes[q][r]=[R,R]
        else:
            e[0]=min(e[0],R)
            e[1]=max(e[1],R)
    return classes,p3


def main():
    classes,p3=enumerate_classes()
    assert tuple(len(x) for x in classes)==EXPECTED

    max_credit=0
    for q,cls in enumerate(classes):
        for lo,hi in cls.values():
            assert (hi-lo)%p3[q]==0
            max_credit=max(max_credit,(hi-lo)//p3[q])
    assert max_credit==21

    assert 3**4 < 2**7 < 3**5
    assert 3**441 < 2**700 < 3**442

    # Worst block polynomial: Q=4 is z times the Q=5 polynomial.
    P5=sum(Fraction(c)*Z**(q-5) for q,c in enumerate(EXPECTED))
    N4_MAX=59
    F=P5**100 * Z**N4_MAX

    # F < 2^602, checked without logarithms.
    assert F.numerator**50 < F.denominator**50 * (1<<30100)

    print("L7 class counts", EXPECTED)
    print("max_local_predecessor_credit", max_credit)
    print("macro_steps",700)
    print("Q4_blocks_max",N4_MAX)
    print("weighted_macro_allowed_bits_lt",602)
    print("local_language_exclusion_rate_gt","7/50")
    print("later_block_globalization","REQUIRES_SEPARATE_BRIDGE")
    print("L7 seven-fiftieths macro certificate: PASS")


if __name__=="__main__":
    main()
