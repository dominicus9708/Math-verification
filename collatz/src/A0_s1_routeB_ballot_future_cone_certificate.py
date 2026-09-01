#!/usr/bin/env python3
"""Exact finite-horizon future cone for the Route-B ballot minimum coordinate.

For any slope 0 < alpha < 1 and binary word W, define

    d_W(u) = q_W(u) - floor(alpha*u),
    b(W)   = min_{0<=u<=|W|} d_W(u),
    e(W)   = q(W) - floor(alpha*|W|).

Let V be any binary suffix of length at most ell.  Then

    min(b(W), e(W)-floor(alpha*ell)-1)
        <= b(WV)
        <= min(b(W), e(W)).

Consequently for a threshold gate b >= beta:

  * if b(W) < beta, rejection is irreversible under every suffix;
  * if b(W) >= beta and
        e(W)-floor(alpha*ell)-1 >= beta,
    then every suffix of length <= ell is guaranteed to remain accepted by
    the ballot-minimum gate.

The -1 is the generic floor carry allowance.  This theorem concerns only the
ballot-minimum coordinate.  It does not replace critical-prefix/phase state and
does not by itself prove Route-B membership.
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


# Finite regression only.  The theorem is the elementary floor inequality
# floor(a+b) <= floor(a)+floor(b)+1 and q_V(u)>=0.
SLOPES = (Fraction(2, 3), Fraction(3, 5), Fraction(5, 8), Fraction(7, 11))
checks = 0
irreversible_checks = 0
guaranteed_checks = 0

for alpha in SLOPES:
    for h in range(0, 8):
        for W in words(h):
            bW, eW = ballot(W, alpha)
            for ell in range(0, 6):
                lower = min(bW, eW - floor_mul(alpha, ell) - 1)
                upper = min(bW, eW)
                beta = -2
                guaranteed = bW >= beta and eW - floor_mul(alpha, ell) - 1 >= beta
                for vlen in range(ell + 1):
                    for V in words(vlen):
                        bWV, _ = ballot(W + V, alpha)
                        assert lower <= bWV <= upper
                        checks += 1
                        if bW < beta:
                            assert bWV < beta
                            irreversible_checks += 1
                        if guaranteed:
                            assert bWV >= beta
                            guaranteed_checks += 1

print("PASS A0 s=1 Route-B ballot future-cone certificate")
print("cone_checks", checks)
print("irreversible_rejection_checks", irreversible_checks)
print("guaranteed_acceptance_checks", guaranteed_checks)
print("exact_lower", "min(b,e-floor(alpha*ell)-1)")
print("exact_upper", "min(b,e)")
print("scope", "ballot-minimum threshold coordinate only; critical state and universal Route-B membership remain separate")
