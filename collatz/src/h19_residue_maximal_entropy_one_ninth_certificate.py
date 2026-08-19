#!/usr/bin/env python3
"""Exact rational one-ninth entropy bound for the H19 residue-maximal language.

This is a structural certificate inside the Collatz proof program, not a proof
of the Collatz conjecture.

The unrestricted length-19 full-Hensel residue-class counts c_q were certified
by h19_unrestricted_residue_maximality_certificate.cpp.  For a mechanical
Q=12 factor define

    P12(z) = sum_{q=0}^{19} c_q z^(q-12).

For Q=11, P11(z)=z*P12(z).  Along a first-return gate there is exactly one
Q=11 factor and all remaining length-19 factors have Q=12.  Since z>1,
positive endpoint height only enlarges the weighted sum, so these products are
rigorous upper bounds even after dropping intermediate nonnegativity.

With the exact rational choice z=19/15 we prove, using integer arithmetic only,

    (z P12(z)^81)^9 < 2^(8*1539)   [G81]
    (z P12(z)^82)^9 < 2^(8*1558)   [G82].

Thus both gate languages have entropy rate < 8/9 bit per binary step, i.e. a
deterministic local-residue-maximality exclusion rate > 1/9.
"""
from fractions import Fraction

C = (
    1,2,6,18,54,162,486,1458,4352,11692,
    23557,31072,27469,17527,8411,3048,817,154,19,1,
)
Z = Fraction(19,15)


def p12(z: Fraction) -> Fraction:
    s = Fraction(0)
    for q,c in enumerate(C):
        s += c * z**(q-12)
    return s


def verify_gate(nblocks: int, horizon: int) -> None:
    # Exactly one Q=11 block, hence one extra factor z.
    P = p12(Z)
    F = Z * P**nblocks
    # log2(F)/H < 8/9 iff F^9 < 2^(8H).
    assert F.numerator**9 < F.denominator**9 * (1 << (8*horizon))
    print(
        "gate", nblocks,
        "horizon", horizon,
        "one_ninth_exclusion", True,
        "weighted_factor_num_bits", F.numerator.bit_length(),
        "weighted_factor_den_bits", F.denominator.bit_length(),
    )


def main() -> None:
    assert Z > 1
    P = p12(Z)

    # G81: 81 factors = 80 Q=12 + one Q=11.
    verify_gate(81,1539)
    # G82: 82 factors = 81 Q=12 + one Q=11.
    verify_gate(82,1558)

    # Clean consequence: if same-integer overlap amplification Xi_H has
    # exponential rate lambda<1/9, the net exclusion rate is positive.
    # In particular Xi_H=2^o(H) needs any asymptotic H>Cm with C>9.
    print("z", Z)
    print("P12", P)
    print("residue_maximal_exclusion_rate_gt", "1/9")
    print("subexponential_overlap_sufficient_slope", "C>9")
    print("H19 one-ninth entropy certificate: PASS")


if __name__ == "__main__":
    main()
