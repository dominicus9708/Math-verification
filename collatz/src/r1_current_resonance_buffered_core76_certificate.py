#!/usr/bin/env python3
"""Exact buffered-core certificate for the current fixed R1 resonance.

For (A,q)=(217976794617,137528045312), the buffered-core co-order theorem uses

    D*2^B > q*3^(q-1),
    D=2^A-3^q.

Dividing by 3^q and writing E=A ln2-q ln3, this is

    exp(E)-1 > q/(3*2^B).

We prove exactly, with rational atanh-series log bounds, that B=75 fails and
B=76 succeeds.  We also compute the latest possible position of the 76th odd
event and the exact count of admissible first-76 odd-position prefixes.

The fixed-cell arithmetic is SAFE.  Using this fixed resonance as the sole R1
cell for every hypothetical minimal counterexample is CONDITIONAL on the V33 /
ternary-coverage hypothesis audited on 2026-09-06.
"""

from fractions import Fraction

A = 217_976_794_617
Q = 137_528_045_312


def ln_bounds(num: int, den: int = 1, terms: int = 80):
    x = Fraction(num, den)
    assert x > 1
    z = (x - 1) / (x + 1)
    s = Fraction(0)
    for k in range(terms):
        s += 2 * z ** (2 * k + 1) / (2 * k + 1)
    first_den = 2 * terms + 1
    tail = 2 * z ** first_den / (first_den * (1 - z * z))
    return s, s + tail


def kappa(i: int) -> int:
    """floor(i log_2 3), exactly for integer i>=0."""
    return (3**i).bit_length() - 1


def admissible_odd_prefix_count(h: int) -> int:
    # alpha_j strictly increase and alpha_j <= floor((j-1) log_2 3).
    dp = {-1: 1}
    for j in range(1, h + 1):
        hi = kappa(j - 1)
        prev = sorted(dp.items())
        nd = {}
        running = 0
        idx = 0
        for a in range(hi + 1):
            while idx < len(prev) and prev[idx][0] < a:
                running += prev[idx][1]
                idx += 1
            if running:
                nd[a] = running
        dp = nd
    return sum(dp.values())


def threshold_log_bounds(B: int):
    # ln(1 + Q/(3*2^B)) = ln((3*2^B+Q)/(3*2^B)).
    den = 3 * (1 << B)
    return ln_bounds(den + Q, den, terms=8)


def main():
    ln2_lo, ln2_hi = ln_bounds(2, terms=80)
    ln3_lo, ln3_hi = ln_bounds(3, terms=80)
    E_lo = A * ln2_lo - Q * ln3_hi
    E_hi = A * ln2_hi - Q * ln3_lo
    assert E_lo > 0

    t75_lo, t75_hi = threshold_log_bounds(75)
    t76_lo, t76_hi = threshold_log_bounds(76)

    # B=75 fails: exp(E)-1 < Q/(3*2^75).
    assert E_hi < t75_lo
    # B=76 succeeds: exp(E)-1 > Q/(3*2^76).
    assert E_lo > t76_hi

    B = 76
    latest_alpha = kappa(B - 1)
    assert latest_alpha == 118
    # Time positions are zero-based, so the 76th odd event occurs by step 119.
    latest_prefix_length = latest_alpha + 1
    assert latest_prefix_length == 119

    count = admissible_odd_prefix_count(B)
    assert count == 15_537_359_898_820_273_235_593_329_305_889

    print("SAFE fixed-resonance buffered-core certificate")
    print("minimal B =", B)
    print("B=75 fails, B=76 succeeds")
    print("latest alpha_76 =", latest_alpha)
    print("first 76 odd events are contained in first", latest_prefix_length, "parity positions")
    print("admissible first-76 odd-position prefixes =", count)
    print("GLOBAL use of this fixed resonance: CONDITIONAL on V33 coverage")


if __name__ == "__main__":
    main()
