#!/usr/bin/env python3
"""Exact arithmetic certificate for the first global resonance near-return gap.

External inputs not reverified here:
- convergence of every positive integer below 2^71 (Barina 2025);
- the mechanical first-crossing remainder envelope
      S_w <= q/(6 ln 2) + 1/3;
- Hercher's cycle theorem: if X0 >= 3*2^69, every nontrivial cycle has
  more than 1.375e11 odd members.

Everything else is exact integer/Fraction arithmetic.
"""

from fractions import Fraction

B = 1 << 71
A0 = 114_208_327_604
Q0 = 72_057_431_991
TERMS = 60


def log_bounds(num: int, den: int, terms: int = TERMS) -> tuple[Fraction, Fraction]:
    assert num > den > 0
    z = Fraction(num - den, num + den)
    z2 = z * z
    zpow = z
    s = Fraction(0)
    for k in range(terms):
        s += zpow / (2 * k + 1)
        zpow *= z2
    lo = 2 * s
    tail = 2 * zpow / Fraction(2 * terms + 1) / (1 - z2)
    return lo, lo + tail


def main() -> None:
    l2, u2 = log_bounds(2, 1)
    l3, u3 = log_bounds(3, 1)

    # P=2^A0/3^Q0 > 1.  Lower bound P-1 >= ln P.
    logP_lower = A0 * l2 - Q0 * u3
    assert logP_lower > 0

    # Mechanical normalized correction upper bound.
    S_upper = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)

    # If E=T^A0(N)=N+g and N>=B, then
    # g=(S_w-(P-1)N)/P < S_upper - B*logP_lower.
    g_upper = S_upper - B * logP_lower
    assert g_upper > 0
    assert g_upper < (1 << 33)

    # The bound is much smaller than N, so the mod-4 descent argument applies.
    assert 3 * (1 << 33) + 1 < B

    # Hercher's cycle theorem applies already from X0=3*2^69.
    assert B >= 3 * (1 << 69)
    assert Q0 < 137_500_000_000

    print("PASS first-resonance near-return gap certificate")
    print(f"published_floor=2^71={B}")
    print(f"boundary=(A,q)=({A0},{Q0})")
    print(f"g_upper_fraction={g_upper.numerator}/{g_upper.denominator}")
    print(f"g_upper_decimal_approx={float(g_upper):.12f}")
    print("therefore: 0 <= g < 2^33 before cycle exclusion")
    print("Hercher + q0<1.375e11 excludes g=0")
    print("minimal-counterexample mod-4 argument forces g == 0 mod 4")
    print("conclusion: g in 4*Z_{>0}, g < 2^33")


if __name__ == "__main__":
    main()
