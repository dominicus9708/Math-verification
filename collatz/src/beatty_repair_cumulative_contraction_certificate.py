#!/usr/bin/env python3
"""Exact finite certificate for the Beatty + selector-repair contraction bridge.

This certificate combines two previously separated facts:

1. At every Beatty rise, the coefficient one-child boundary obeys
       |D_L| / |R_L| > 2/(5L).
2. If a selector child multiplicity satisfies a <= C(x) <= b and rho=a/b>1/3,
   then the one-child repair lemma loses at least
       delta(rho) = (3 rho - 1)/(4 rho)
   of the selector mass carried by the one-child parent set.

Since selector mass on D relative to R is at least rho |D|/|R|, the total
normalized candidate-mass loss at a rise is at least

       (3 rho - 1)/(10 L).

The asymptotic theorem remains conditional on a horizon-independent selector
min/max lower bound rho >= rho0 > 1/3 on the exact candidate fibre.  This file
only certifies the algebra and the declared finite diagnostics.
"""

from fractions import Fraction

MAX_L = 1500

STATS = {
    "H24_full": (4_188_525, 4_199_983),
    "H25_full": (2_092_917, 2_102_038),
    "H24_Q7_high": (32_039, 33_523),
    "H24_Q8_high": (15_871, 16_878),
    "H24_Q9_high": (7_826, 8_584),
    "H25_Q7_high": (15_828, 16_923),
}


def barriers(n: int):
    """Return b_L=min{q:3^q>=2^L} without floating-point decisions."""
    out = [0] * (n + 2)
    q = 0
    p3 = 1
    p2 = 1
    for L in range(1, n + 2):
        p2 <<= 1
        while p3 < p2:
            q += 1
            p3 *= 3
        out[L] = q
    return out


def main() -> None:
    b = barriers(MAX_L)

    rise_harmonic = Fraction(0, 1)
    harmonic = Fraction(0, 1)
    rise_steps = 0

    # Elementary alpha=log_3(2)>5/8 because 3^5 < 2^8.
    # The Beatty discrepancy then gives the finite check target
    #   sum_{rise L<=N} 1/L >= (5/8) H_N - 3/8.
    for L in range(1, MAX_L + 1):
        harmonic += Fraction(1, L)
        if b[L + 1] == b[L] + 1:
            rise_steps += 1
            rise_harmonic += Fraction(1, L)
        assert rise_harmonic >= Fraction(5, 8) * harmonic - Fraction(3, 8)

    print("max_L", MAX_L)
    print("rise_steps", rise_steps)
    print("rise_harmonic", float(rise_harmonic))
    print("elementary_harmonic_floor", float(Fraction(5, 8) * harmonic - Fraction(3, 8)))

    for name, (a, B) in STATS.items():
        assert 0 < a <= B
        rho = Fraction(a, B)
        assert 3 * a > B

        delta = Fraction(3 * rho - 1, 4 * rho)
        kappa = Fraction(3 * rho - 1, 10)
        assert delta > 0
        assert kappa > 0

        product = Fraction(1, 1)
        for L in range(1, MAX_L + 1):
            if b[L + 1] != b[L] + 1:
                continue

            # Existing coefficient-exposure theorem gives >2/(5L).
            # Min/max selector weighting transfers at least a factor rho.
            weighted_exposure_floor = rho * Fraction(2, 5 * L)
            total_loss_floor = delta * weighted_exposure_floor

            # Exact cancellation of rho:
            # delta * rho * 2/(5L) = (3rho-1)/(10L).
            assert total_loss_floor == kappa / L
            assert 0 < total_loss_floor < 1
            product *= 1 - total_loss_floor

        print(name)
        print("  rho", float(rho))
        print("  per_rise_kappa", float(kappa))
        print("  exact_product_through_MAX_L", float(product))

    print("Beatty + selector-repair cumulative contraction bridge: PASS")
    print("ASYMPTOTIC STATUS: conditional on inf rho_L > 1/3 on exact candidate fibres")


if __name__ == "__main__":
    main()
