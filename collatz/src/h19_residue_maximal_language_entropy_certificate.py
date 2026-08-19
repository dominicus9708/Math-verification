#!/usr/bin/env python3
"""Exact weighted-language bound for locally residue-maximal 19-bit blocks.

The unrestricted length-19 full-Hensel class counts c_q are certified by
h19_unrestricted_residue_maximality_certificate.cpp.  A hypothetical minimal
counterexample above the universal local-credit constant 87381 must choose, in
every 19-step block, at most one maximum-correction representative per occupied
full-Hensel class.  Hence c_q is a factor- and height-independent upper bound on
the number of locally credit-free orientations with q odd symbols.

Let Q in {11,12} be the mechanical odd count of the current factor and let the
relative-height increment be q-Q.  For z>1 the weighted transition polynomial is

    P_Q(z)=sum_q c_q z^(q-Q).

For every path starting at nonnegative height, z^(final height)>=1.  Dropping
all intermediate nonnegativity constraints can only increase the weighted sum,
so a product of P_Q(z) is an upper bound for the NUMBER of locally-maximal
coefficient-surviving block words.

At the exact rational choice z=5/4 this verifier proves

    P_12(5/4) < 2^17,
    P_11(5/4) = (5/4) P_12(5/4) < 2^18.

Therefore even the factor-by-factor worst case loses more than one bit of
language entropy per 19 time-expanded steps relative to the complete 2^19
binary cube.

At the exact first-return gate scale there is exactly one Q=11 factor:
G81 has 81 blocks and mechanical q=971=80*12+11; G82 has 82 blocks and
q=983=81*12+11.  The sharper products are therefore

    G81: P_12^81 * (5/4),
    G82: P_12^82 * (5/4).

The displayed integer powers below give simple rigorous bit ceilings.

This is a deterministic language-count theorem, not an intersection theorem
with the ternary selector core and not a Collatz proof.
"""

from fractions import Fraction

C = (
    1,2,6,18,54,162,486,1458,4352,11692,
    23557,31072,27469,17527,8411,3048,817,154,19,1,
)
assert sum(C) == 130_306

z = Fraction(5,4)


def P(Q: int) -> Fraction:
    return sum(Fraction(c) * z**(q-Q) for q,c in enumerate(C))

P12 = P(12)
P11 = P(11)

assert P12 == Fraction(477_477_466_377_643_529, 4_000_000_000_000)
assert P11 == z * P12
assert P12 < 2**17
assert P11 < 2**18

# Exact gate structure: one 11-one factor per first-return gate.
assert 971 == 80*12 + 11
assert 983 == 81*12 + 11

G81 = P12**80 * P11
G82 = P12**81 * P11

# Simple integer-bit ceilings, deliberately not optimized.
assert G81 < 2**1378  # complete G81 binary cube has 2^1539 words
assert G82 < 2**1395  # complete G82 binary cube has 2^1558 words

G81_EXCLUSION_BITS_FLOOR = 1539 - 1378
G82_EXCLUSION_BITS_FLOOR = 1558 - 1395
assert G81_EXCLUSION_BITS_FLOOR == 161
assert G82_EXCLUSION_BITS_FLOOR == 163

print("H19 residue-maximal language entropy certificate: PASS")
print("P12", P12, float(P12))
print("P11", P11, float(P11))
print("worst_block_language_bits", "<18 of 19")
print("G81_language_bits", "<1378 of 1539", "exclusion >161 bits")
print("G82_language_bits", "<1395 of 1558", "exclusion >163 bits")
