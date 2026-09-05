#!/usr/bin/env python3
"""Exact finite-horizon future cone for the Route-B ballot minimum coordinate.

For any slope 0 < alpha < 1 and binary word W of length h, define

    d_W(u) = q_W(u) - floor(alpha*u),
    b(W)   = min_{0<=u<=h} d_W(u),
    e(W)   = q(W) - floor(alpha*h).

For every binary suffix V of length at most ell, define

    Delta_alpha(h,ell)
      = floor(alpha*(h+ell)) - floor(alpha*h).

Then

    b(WV) >= min(b(W), e(W)-Delta_alpha(h,ell)).

This lower bound is EXACT as the worst case over all |V|<=ell: the all-zero
suffix 0^ell attains it.  Hence

    min_{|V|<=ell} b(WV)
      = min(b(W), e(W)-Delta_alpha(h,ell)).

Consequently for a threshold gate b >= beta:

  * if b(W) < beta, rejection is irreversible under every suffix;
  * every suffix of length <= ell is accepted iff

        b(W) >= beta
        and
        e(W)-Delta_alpha(h,ell) >= beta.

This theorem concerns only the ballot-minimum coordinate.  It does not replace
critical-prefix/phase state and does not by itself prove Route-B membership.
"""

from fractions import Fraction
from itertools import product


def floor_mul(alpha: Fraction, n: int) -> int:
    z = alpha * n
    return z.numerator // z.denominator


def ballot(word, alpha: Fraction):
    q = 0
    b = 0
    for u, bit in enumerate(word, 1):
        q += bit
        b = min(b, q - floor_mul(alpha, u))
    e = q - floor_mul(alpha, len(word))
    return b, e


def words(n):
    return product((0, 1), repeat=n)


# Finite regression only.  The proof is direct:
# for an extension prefix of length u with j(u)>=0 ones,
#
#   d_WV(h+u)
#     = e(W) + j(u)
#       - [floor(alpha(h+u))-floor(alpha*h)]
#     >= e(W)-Delta_alpha(h,ell),
#
# while the all-zero suffix of full length ell attains the endpoint value
# e(W)-Delta_alpha(h,ell).  Thus the worst-case lower envelope is exact.
SLOPES = (Fraction(2, 3), Fraction(3, 5), Fraction(5, 8), Fraction(7, 11))
checks = 0
worst_case_checks = 0
irreversible_checks = 0
guaranteed_checks = 0

for alpha in SLOPES:
    for h in range(0, 8):
        for W in words(h):
            bW, eW = ballot(W, alpha)
            for ell in range(0, 6):
                delta = floor_mul(alpha, h + ell) - floor_mul(alpha, h)
                worst = min(bW, eW - delta)
                beta = -2
                guaranteed = bW >= beta and eW - delta >= beta

                observed_min = None
                for vlen in range(ell + 1):
                    for V in words(vlen):
                        bWV, _ = ballot(W + V, alpha)
                        assert bWV >= worst
                        checks += 1
                        observed_min = bWV if observed_min is None else min(observed_min, bWV)

                        if bW < beta:
                            assert bWV < beta
                            irreversible_checks += 1
                        if guaranteed:
                            assert bWV >= beta
                            guaranteed_checks += 1

                zero_suffix = (0,) * ell
                b_zero, _ = ballot(W + zero_suffix, alpha)
                assert b_zero == worst
                assert observed_min == worst
                worst_case_checks += 1

print("PASS A0 s=1 Route-B ballot future-cone certificate")
print("cone_checks", checks)
print("exact_worst_case_checks", worst_case_checks)
print("irreversible_rejection_checks", irreversible_checks)
print("guaranteed_acceptance_checks", guaranteed_checks)
print(
    "exact_worst_case",
    "min_{|V|<=ell} b(WV)=min(b(W),e(W)-[floor(alpha(h+ell))-floor(alpha*h)])",
)
print("worst_suffix", "the all-zero suffix of length ell attains the bound")
print(
    "scope",
    "ballot-minimum threshold coordinate only; critical state and universal Route-B membership remain separate",
)
