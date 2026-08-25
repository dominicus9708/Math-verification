#!/usr/bin/env python3
"""Exact rational certificate for the min/max child-repair lemma.

If a selector count function C on the child modulus satisfies a<=C(x)<=b,
then for every signed one-child parent set D,

    |K| / S_D <= (b-a)/(2a),

where K=sum_D v(r)(C(r)-C(r+M)) and
S_D=sum_D (C(r)+C(r+M)).

The same statement applies to every translated low-ternary cylinder when its
high-selector multiplicity function has the stated min/max values.

The multiplicity extrema below are imported from the already independent exact
selector-DP certificates in the repository; this file certifies the derived
rational repair/contraction constants.
"""

from fractions import Fraction

STATS = {
    "H24_full": (4_188_525, 4_199_983),
    "H25_full": (2_092_917, 2_102_038),
    "H24_Q7_high": (32_039, 33_523),
    "H24_Q8_high": (15_871, 16_878),
    "H24_Q9_high": (7_826, 8_584),
    "H25_Q7_high": (15_828, 16_923),
}


def main() -> None:
    for name, (a, b) in STATS.items():
        assert 0 < a <= b
        rho = Fraction(a, b)
        beta = Fraction(b - a, 2 * a)
        loss = Fraction(1, 2) * (1 - beta)
        retained = Fraction(1, 2) * (1 + beta)

        # Positive contraction is equivalent to min/max ratio > 1/3.
        assert 3 * a > b
        assert beta < 1
        assert loss > 0
        assert retained < 1

        print(name)
        print("  minmax_ratio", float(rho))
        print("  relative_repair_bound", float(beta))
        print("  one_child_retained_bound", float(retained))
        print("  one_child_loss_floor", float(loss))

    print("selector minmax child-repair bound: PASS")


if __name__ == "__main__":
    main()
