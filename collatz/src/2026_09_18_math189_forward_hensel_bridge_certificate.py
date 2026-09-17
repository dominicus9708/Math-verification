#!/usr/bin/env python3
"""MATH-189 exact regression for the forward Hensel bridge.

Finite regression only.  It verifies, for all parity words through depth 10,
that

1. grouping even positions by G_j=e_j-j reproduces the direct MATH-051 Sigma;
2. the forward integer recurrence

       W_r = 3 W_{r-1} + 2^r (B_r - A_r)

   satisfies W_q = 3^q (Sigma_B-Sigma_A) for every same-(k,d) word pair;
3. positive exact Hensel class membership is equivalent to

       W_q > 0 and W_q % 3^q == 0.

This certificate does not extend the audited depth-41 theorem and makes no
Collatz closure claim.
"""

from fractions import Fraction
from itertools import product

MAX_K = 10


def direct_sigma(bits: tuple[int, ...]) -> Fraction:
    even_positions = [i for i, b in enumerate(bits) if b == 0]
    out = Fraction(0)
    for j, e in enumerate(even_positions):
        out += Fraction(3**j * 2**e, 3**e)
    return out


def gap_blocks(bits: tuple[int, ...]) -> list[int]:
    q = 0
    out = [0]
    for b in bits:
        if b == 0:
            out[q] += 1
        else:
            q += 1
            out.append(0)
    return out


def grouped_sigma(a: list[int]) -> Fraction:
    p = 0
    out = Fraction(0)
    for r, block in enumerate(a):
        powers = (2**block - 1) * 2**p
        out += powers * Fraction(2**r, 3**r)
        p += block
    return out


def forward_W(a: list[int], b: list[int]) -> tuple[int, int]:
    q = max(len(a), len(b)) - 1
    aa = a + [0] * (q + 1 - len(a))
    bb = b + [0] * (q + 1 - len(b))

    pa = 0
    pb = 0
    W = 0
    for r in range(q + 1):
        A = (2**aa[r] - 1) * 2**pa
        B = (2**bb[r] - 1) * 2**pb
        W = 3 * W + 2**r * (B - A)
        pa += aa[r]
        pb += bb[r]
    return W, q


def main() -> None:
    words_checked = 0
    pairs_checked = 0
    positive_class_checks = 0

    by_k_q: dict[tuple[int, int], list[tuple[int, ...]]] = {}

    for k in range(MAX_K + 1):
        for bits in product((0, 1), repeat=k):
            bits = tuple(bits)
            words_checked += 1
            a = gap_blocks(bits)
            assert direct_sigma(bits) == grouped_sigma(a), (bits, a)
            q = sum(bits)
            by_k_q.setdefault((k, q), []).append(bits)

    for (k, q), words in by_k_q.items():
        for A_bits in words:
            A_blocks = gap_blocks(A_bits)
            A_sigma = direct_sigma(A_bits)
            for B_bits in words:
                pairs_checked += 1
                B_blocks = gap_blocks(B_bits)
                B_sigma = direct_sigma(B_bits)

                W, q2 = forward_W(A_blocks, B_blocks)
                assert q2 == q
                diff = B_sigma - A_sigma
                assert W == diff * 3**q, (k, q, A_bits, B_bits, W, diff)

                direct_positive_class = diff.denominator == 1 and diff > 0
                forward_positive_class = W > 0 and W % (3**q) == 0
                assert direct_positive_class == forward_positive_class
                positive_class_checks += 1

    print("PASS MATH-189 forward Hensel bridge regression")
    print(f"max_depth={MAX_K}")
    print(f"words_checked={words_checked}")
    print(f"same_(k,q)_pairs_checked={pairs_checked}")
    print(f"positive_class_equivalence_checks={positive_class_checks}")
    print("NO NEW HENSEL DEPTH OR COLLATZ CLOSURE CLAIM")


if __name__ == "__main__":
    main()
