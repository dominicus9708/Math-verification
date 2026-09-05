#!/usr/bin/env python3
"""Exact fixed-count ballot future cone for A0 s=1 Route-B.

Let W have length h, ballot minimum b(W), and endpoint discrepancy

    e(W) = q(W) - floor(alpha*h),   0 < alpha < 1.

Consider suffixes V with EXACT length ell and EXACT one-count s.
Write z = ell-s for the required number of zeros.

Among all such suffixes:

  * the pointwise smallest suffix prefix-one-count profile is 0^z 1^s;
  * the pointwise largest profile is 1^s 0^z.

Consequently

    min_V b(WV)
      = min(b(W), e(W)-Delta(h,z)),

    max_V b(WV)
      = min(b(W), e(W)+s-Delta(h,ell)),

where Delta(h,t)=floor(alpha*(h+t))-floor(alpha*h).

For a threshold gate b >= beta this gives an exact three-way status:

  F: no fixed-count completion passes iff max_V b(WV) < beta;
  P: every fixed-count completion passes iff min_V b(WV) >= beta;
  U: otherwise some completions pass and some fail.

This concerns the ballot-minimum coordinate only; literal critical-prefix data
remains separate when queried.
"""

from fractions import Fraction
from itertools import combinations, product


def fl(alpha: Fraction, n: int) -> int:
    z = alpha * n
    return z.numerator // z.denominator


def ballot(word, alpha: Fraction):
    q = 0
    b = 0
    for u, bit in enumerate(word, 1):
        q += bit
        b = min(b, q - fl(alpha, u))
    return b, q - fl(alpha, len(word))


def fixed_count_words(ell: int, s: int):
    for ones in combinations(range(ell), s):
        one_set = set(ones)
        yield tuple(int(i in one_set) for i in range(ell))


SLOPES = (Fraction(2, 3), Fraction(3, 5), Fraction(5, 8), Fraction(7, 11))
cone_checks = 0
extremal_checks = 0
status_checks = 0

for alpha in SLOPES:
    for h in range(0, 7):
        for W in product((0, 1), repeat=h):
            bW, eW = ballot(W, alpha)
            for ell in range(0, 7):
                for s in range(ell + 1):
                    z = ell - s
                    delta_zero = fl(alpha, h + z) - fl(alpha, h)
                    delta_full = fl(alpha, h + ell) - fl(alpha, h)
                    predicted_worst = min(bW, eW - delta_zero)
                    predicted_best = min(bW, eW + s - delta_full)

                    vals = []
                    for V in fixed_count_words(ell, s):
                        bWV, _ = ballot(W + V, alpha)
                        vals.append(bWV)
                        assert predicted_worst <= bWV <= predicted_best
                        cone_checks += 1

                    assert min(vals) == predicted_worst
                    assert max(vals) == predicted_best
                    assert ballot(W + (0,) * z + (1,) * s, alpha)[0] == predicted_worst
                    assert ballot(W + (1,) * s + (0,) * z, alpha)[0] == predicted_best
                    extremal_checks += 1

                    for beta in range(-3, 2):
                        no_pass = max(vals) < beta
                        all_pass = min(vals) >= beta
                        some_pass = any(v >= beta for v in vals)
                        assert no_pass == (predicted_best < beta)
                        assert all_pass == (predicted_worst >= beta)
                        assert some_pass == (predicted_best >= beta)
                        status_checks += 1

print("PASS A0 s=1 Route-B fixed-count ballot future-cone certificate")
print("cone_checks", cone_checks)
print("extremal_checks", extremal_checks)
print("status_checks", status_checks)
print("worst_suffix", "0^(ell-s) 1^s")
print("best_suffix", "1^s 0^(ell-s)")
print("exact_status", "F/P/U for a ballot-minimum threshold is determined by the two extremal envelopes")
print("scope", "ballot-minimum coordinate only; critical-prefix data remains separate")
