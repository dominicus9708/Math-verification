#!/usr/bin/env python3
"""Regression certificate for mechanical-alignment credit in the Hensel control model.

The accompanying note proves two all-depth statements:

1. A length-L future mechanical zero-displacement block determines one current
   carry class modulo 3^L,

       Z_L = -sum_{i=0}^{L-1} 3^i 2^{e_i}  (mod 3^L).

2. When the zero-control alignment is exhausted, an odd repair displacement
   that seeds L new alignment digits is unique modulo 2*3^L.  Equivalently,
   d -> 2^e(2^{-d}-1) maps odd classes modulo 2*3^L bijectively onto one
   unit coset modulo 3^(L+1).

This file exhaustively checks small depths.  It is a regression certificate,
not the proof and not a proof of the Collatz conjecture.
"""

from itertools import product


def invpow2(d: int, M: int) -> int:
    return pow(pow(2, d, M), -1, M)


def repair_term(e: int, d: int, L: int) -> int:
    M = 3 ** (L + 1)
    return (pow(2, e, M) * (invpow2(d, M) - 1)) % M


def alignment_class(exponents, L: int) -> int:
    M = 3**L
    return (-sum((3**i) * pow(2, exponents[i], M) for i in range(L))) % M


def main() -> None:
    # Odd repair classes: exact cardinality and fixed mod-3 image coset.
    for L in range(1, 8):
        period = 2 * 3**L
        for e in range(-4, 5):
            vals = [repair_term(e, d, L) for d in range(1, period, 2)]
            assert len(vals) == 3**L
            assert len(set(vals)) == 3**L
            mod3 = {v % 3 for v in vals}
            assert len(mod3) == 1
            assert 0 not in mod3

    # Zero-control alignment class on all small {1,2}-gap words.
    for L in range(1, 8):
        for gaps in product((1, 2), repeat=L - 1):
            e = [0]
            for g in gaps:
                e.append(e[-1] - g)

            Z = alignment_class(e, L)
            assert Z % 3 != 0

            # Verify the nested recurrence of the unique alignment classes.
            for i in range(L - 1):
                rem = L - i
                M = 3**rem
                cur = alignment_class(e[i:], rem)
                nxt = alignment_class(e[i + 1 :], rem - 1)
                assert (cur + pow(2, e[i], M) - 3 * nxt) % M == 0
                assert cur % 3 != 0

    print("PASS Hensel mechanical-alignment credit regression")
    print("zero-control future block -> one carry class mod 3^L")
    print("odd repair d mod 2*3^L -> one-to-one unit repair class mod 3^(L+1)")
    print("checked all {1,2}-gap blocks through L=7")


if __name__ == "__main__":
    main()
