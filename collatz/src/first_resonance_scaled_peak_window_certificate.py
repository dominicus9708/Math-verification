#!/usr/bin/env python3
"""Exact rational certificate for the first-resonance scaled interface peak.

For the repaired first global resonance, split the anchored Christoffel root
into its supercritical left child U and finite-base RS-safe right child S.
If x_j is the actual odd state and d_j its left displacement from the
mechanical odd position, define z_j=x_j/2^d_j.  Along any block with q odd
steps and total mechanical time A_b,

    3^q/2^A_b < z_out/z_in <= (3+1/B)^q/2^A_b

for B=2^71, because every odd state on a minimal-counterexample prefix is >B.
The safe suffix therefore forces a strict peak at the U|S interface.

All numerical assertions below use Fraction arithmetic and positive-series
log enclosures.  No floating-point comparison is used in a proof assertion.
"""

from fractions import Fraction

B = 1 << 71
GAP = 1 << 33

# Root first resonance.
A = 114_208_327_604
Q = 72_057_431_991

# Ordered root split U . S.
A_U = 103_768_467_013
Q_U = 65_470_613_321
A_S = 10_439_860_591
Q_S = 6_586_818_670

LOW_GAP = 21_706_947_634
UP_GAP = 31_870_071_812
NLOG = 120


def log_bounds(z: Fraction, n: int = NLOG):
    """Bounds log((1+z)/(1-z)) by a positive atanh series."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / (
        (2 * n + 3) * (1 - z * z)
    )
    return s, s + tail


def main() -> None:
    # Exact split arithmetic.
    assert A_U + A_S == A
    assert Q_U + Q_S == Q
    assert A_U * Q_S - Q_U * A_S == 1

    # ln 2 and ln 3.
    l2, u2 = log_bounds(Fraction(1, 3))
    l3, u3 = log_bounds(Fraction(1, 2))

    # ln(3+1/B).
    X = Fraction(3 * B + 1, B)
    z = (X - 1) / (X + 1)
    lA, uA = log_bounds(z)

    # S is strictly RS-safe:
    #   (3+1/B)^Q_S / 2^A_S < 1.
    theta_safe_lo = A_S * l2 - Q_S * uA
    assert theta_safe_lo > 0

    # If r_S <= exp(-theta_safe), then
    #   z_mid > y*exp(theta_safe).
    # Since exp(t)-1 > t and y>B,
    #   z_mid-y > B*theta_safe_lo.
    lower_peak_gap = Fraction(B) * theta_safe_lo
    assert lower_peak_gap > LOW_GAP

    # True-3 lower ratio on S:
    #   z_end/z_mid > 3^Q_S/2^A_S = exp(-theta_true).
    # Hence z_mid < y*exp(theta_true).
    theta_true_hi = A_S * u2 - Q_S * l3
    assert 0 < theta_true_hi < 1

    # First-resonance endpoint bound:
    #   y < (4/3)2^71 + 2^33.
    YMAX = Fraction(4 * B, 3) + GAP

    # exp(t)-1 <= t/(1-t) for 0<t<1.
    upper_peak_gap = YMAX * theta_true_hi / (1 - theta_true_hi)
    assert upper_peak_gap < UP_GAP

    # Sanity: U is genuinely supercritical under the true coefficient.
    theta_U_lo = Q_U * l3 - A_U * u2
    assert theta_U_lo > 0

    print("PASS first-resonance scaled peak window")
    print("root=(A,Q)", A, Q)
    print("U=(A,Q)", A_U, Q_U)
    print("S=(A,Q)", A_S, Q_S)
    print("lower_peak_gap>", LOW_GAP)
    print("upper_peak_gap<", UP_GAP)
    print("exact_lower_orientation", float(lower_peak_gap))
    print("exact_upper_orientation", float(upper_peak_gap))
    print("interface window: y+LOW_GAP < z_mid < y+UP_GAP")


if __name__ == "__main__":
    main()
