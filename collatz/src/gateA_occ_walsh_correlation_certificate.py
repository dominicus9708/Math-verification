#!/usr/bin/env python3
"""Exact algebraic certificate for the occupied-selector Walsh correlation bridge.

This is not a Collatz proof.  It certifies a support-aware sufficient condition
for transferring the Beatty macro-pair Lyapunov contraction to an arbitrary
selector-conditioned distribution on the 5- or 6-bit extension block.
"""

from fractions import Fraction
from itertools import product, combinations
from math import comb

A = Fraction(3, 2)
PATTERNS = {
    "AB": (5, 3, Fraction(3125, 3456)),
    "BA": (5, 3, Fraction(3125, 3456)),
    "BB": (6, 4, Fraction(15625, 20736)),
}


def payoff(u, rises):
    return A ** (sum(u) - rises)


def walsh(u, mask):
    parity = sum(u[i] for i in range(len(u)) if (mask >> i) & 1) & 1
    return -1 if parity else 1


def check_walsh_expansion(L, rises, sigma):
    words = list(product((0, 1), repeat=L))
    # Pointwise identity:
    # g(u)=sigma*sum_S (-1/5)^|S| chi_S(u).
    for u in words:
        rhs = Fraction(0, 1)
        for mask in range(1 << L):
            rhs += Fraction((-1) ** mask.bit_count(), 5 ** mask.bit_count()) * walsh(u, mask)
        rhs *= sigma
        assert rhs == payoff(u, rises)


def top_k_uniform_support_threshold(L, rises):
    vals = []
    for j in range(L + 1):
        vals += [A ** (j - rises)] * comb(L, j)
    vals.sort(reverse=True)
    running = Fraction(0, 1)
    for k, v in enumerate(vals, 1):
        running += v
        if running / k < 1:
            return k, running / k
    raise AssertionError("full support should contract")


def main():
    for name, (L, rises, sigma) in PATTERNS.items():
        expected = ((1 + A) / 2) ** L / (A ** rises)
        assert expected == sigma
        check_walsh_expansion(L, rises, sigma)

        signed_margin = 1 / sigma - 1
        total_abs_walsh_weight = Fraction(6, 5) ** L - 1
        beta_threshold = signed_margin / total_abs_walsh_weight

        gmin = A ** (-rises)
        gmax = A ** (L - rises)
        tv_threshold = (1 - sigma) / (gmax - gmin)

        k_threshold, worst_at_k = top_k_uniform_support_threshold(L, rises)

        print(name)
        print("  L", L, "rises", rises)
        print("  sigma", f"{sigma.numerator}/{sigma.denominator}", float(sigma))
        print("  signed_walsh_margin", f"{signed_margin.numerator}/{signed_margin.denominator}", float(signed_margin))
        print("  abs_walsh_total_weight", f"{total_abs_walsh_weight.numerator}/{total_abs_walsh_weight.denominator}", float(total_abs_walsh_weight))
        print("  uniform_nonempty_walsh_beta_threshold", f"{beta_threshold.numerator}/{beta_threshold.denominator}", float(beta_threshold))
        print("  total_variation_threshold", f"{tv_threshold.numerator}/{tv_threshold.denominator}", float(tv_threshold))
        print("  arbitrary_uniform_support_first_contracting_k", k_threshold, "of", 1 << L,
              "worst_avg", f"{worst_at_k.numerator}/{worst_at_k.denominator}", float(worst_at_k))

    # Exact constants used in the note.
    assert Fraction(1, PATTERNS["AB"][2]) - 1 == Fraction(331, 3125)
    assert Fraction(1, PATTERNS["BB"][2]) - 1 == Fraction(5111, 15625)
    assert (Fraction(1, PATTERNS["AB"][2]) - 1) / (Fraction(6, 5) ** 5 - 1) == Fraction(331, 4651)
    assert (Fraction(1, PATTERNS["BB"][2]) - 1) / (Fraction(6, 5) ** 6 - 1) == Fraction(5111, 31031)
    assert (1 - PATTERNS["AB"][2]) / (A**2 - A**-3) == Fraction(331, 6752)
    assert (1 - PATTERNS["BB"][2]) / (A**2 - A**-4) == Fraction(269, 2240)

    print("PASS")


if __name__ == "__main__":
    main()
