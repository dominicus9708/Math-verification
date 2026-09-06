#!/usr/bin/env python3
"""Exact certificate for the dangerous interaction dimension at the current R1 resonance.

This certificate is arithmetic-only.  It proves that for

    (A,q)=(217976794617,137528045312)

one has

    3^(-26) < 2^A/3^q - 1 < 3^(-25),

and therefore the dangerous-axis count in the mixed-interaction theorem is
exactly 25.

No gigantic powers 2^A or 3^q are constructed.  Instead we compare

    E = A*ln(2)-q*ln(3)

against ln(1+3^-25) and ln(1+3^-26), using rigorous rational atanh-series
bounds only.

The certificate also counts the number of admissible prefixes of the first
25 odd positions.  The value 820236724 is a warning that dimension 25 is not
the same as 2^25 independent binary states.

Scope note: using this resonance as the sole R1 cell for a hypothetical minimal
counterexample is CONDITIONAL on the V_33 / ternary-coverage hypothesis audited
on 2026-09-06.  The arithmetic statement for this fixed (A,q) is unconditional.
"""

from fractions import Fraction

A = 217_976_794_617
Q = 137_528_045_312


def ln_bounds(num: int, den: int = 1, terms: int = 80):
    """Rigorous rational lower/upper bounds for ln(num/den), num>den>0.

    With z=(x-1)/(x+1),
      ln x = 2 sum_{k>=0} z^(2k+1)/(2k+1).
    The positive tail after `terms` terms is bounded by replacing every
    denominator by the first omitted denominator.
    """
    x = Fraction(num, den)
    assert x > 1
    z = (x - 1) / (x + 1)
    s = Fraction(0)
    for k in range(terms):
        s += 2 * z ** (2 * k + 1) / (2 * k + 1)
    first_den = 2 * terms + 1
    tail = 2 * z ** first_den / (first_den * (1 - z * z))
    return s, s + tail


def log_one_plus_3minus_bounds(i: int):
    p = 3**i
    # z is tiny here, so five terms are far more than enough; the returned
    # interval is still rigorous by the same positive-tail formula.
    return ln_bounds(p + 1, p, terms=5)


def kappa(i: int) -> int:
    """floor(i*log_2 3) using exact integer powers, for small local i."""
    # floor(i log_2 3) is the unique k with 2^k <= 3^i < 2^(k+1).
    p = 3**i
    return p.bit_length() - 1


def admissible_odd_prefix_count(h: int) -> int:
    """Count strict odd positions alpha_j <= floor((j-1)log_2 3), j=1..h."""
    # dp[a] = number of prefixes whose last odd position is a.
    dp = {-1: 1}
    for j in range(1, h + 1):
        hi = kappa(j - 1)
        nd = {}
        running = 0
        # accumulate counts from previous positions p<a
        prev_items = sorted(dp.items())
        idx = 0
        for a in range(0, hi + 1):
            while idx < len(prev_items) and prev_items[idx][0] < a:
                running += prev_items[idx][1]
                idx += 1
            if running:
                nd[a] = running
        dp = nd
    return sum(dp.values())


def main():
    ln2_lo, ln2_hi = ln_bounds(2, 1, terms=80)
    ln3_lo, ln3_hi = ln_bounds(3, 1, terms=80)

    # Rigorous interval for E=A ln2-Q ln3.
    E_lo = A * ln2_lo - Q * ln3_hi
    E_hi = A * ln2_hi - Q * ln3_lo
    assert E_lo > 0

    t25_lo, t25_hi = log_one_plus_3minus_bounds(25)
    t26_lo, t26_hi = log_one_plus_3minus_bounds(26)

    # ln(1+3^-26) < E < ln(1+3^-25)
    assert E_lo > t26_hi
    assert E_hi < t25_lo

    # Exponentiating yields 3^-26 < exp(E)-1 < 3^-25.
    # exp(E)=2^A/3^Q, hence the dangerous condition
    # 3^(Q-i) >= 2^A-3^Q is true exactly for i=1,...,25.
    dangerous_dimension = 25
    assert dangerous_dimension == 25

    prefixes = admissible_odd_prefix_count(dangerous_dimension)
    assert prefixes == 820_236_724

    print("SAFE fixed-resonance arithmetic certificate")
    print("A =", A)
    print("q =", Q)
    print("proved: 3^(-26) < 2^A/3^q - 1 < 3^(-25)")
    print("dangerous interaction dimension =", dangerous_dimension)
    print("admissible first-25 odd-position prefixes =", prefixes)
    print("GLOBAL minimal-counterexample use of this resonance: CONDITIONAL on V33 coverage")


if __name__ == "__main__":
    main()
