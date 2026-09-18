#!/usr/bin/env python3
"""MATH-202 exact phase-summed surplus certificate.

For every r=2..21:
- partitions normalized phase by the exact MATH-179 tau cuts;
- evaluates interval infima and all cut points using Fraction;
- certifies the exact lower bound on
    (1/6) sum_j varpi_j - (19/503) h_r;
- derives the necessary singleton-overshoot depth z_min.

The structural implication uses MATH-186 and MATH-193.
Finite exact arithmetic only. Collatz remains open.
"""

from fractions import Fraction

LAM = Fraction(19, 503)


def m(n: int) -> int:
    # floor(n log2(3/2)) = floor(log2(3^n)) - n
    return (3**n).bit_length() - 1 - n


def tau(n: int) -> Fraction:
    return Fraction(3**n, 2 ** (n + m(n) + 1))


def phase_coeff(w: Fraction, j: int) -> Fraction:
    if j == 0:
        return Fraction(1)
    return Fraction(
        2 ** (j + m(j) + (1 if w <= tau(j) else 0)),
        3**j,
    )


def h_r(w: Fraction, r: int) -> int:
    return r + 1 + m(r) + (1 if w <= tau(r) else 0)


def point_surplus(w: Fraction, r: int) -> Fraction:
    paid_lb = sum((w * phase_coeff(w, j) / 6 for j in range(r)), Fraction(0))
    return paid_lb - LAM * h_r(w, r)


def exact_bound(r: int):
    cuts = sorted(
        set([Fraction(1, 2), Fraction(1)] + [tau(j) for j in range(1, r + 1)])
    )

    best = None
    witness = None

    # Exact cut points. Phase 1/2 is excluded from the domain.
    for w in cuts:
        if w <= Fraction(1, 2):
            continue
        val = point_surplus(w, r)
        if best is None or val < best:
            best = val
            witness = ("point", w)

    # On each open cell every indicator is fixed and the lower-bound
    # expression is affine increasing in w, so its infimum is at the
    # left endpoint. The endpoint need not belong to the cell: an infimum
    # is enough for a rigorous global lower bound.
    for a, b in zip(cuts[:-1], cuts[1:]):
        if b <= Fraction(1, 2):
            continue
        mid = (a + b) / 2
        coeff_sum = sum((phase_coeff(mid, j) for j in range(r)), Fraction(0))
        paid_inf = a * coeff_sum / 6
        val = paid_inf - LAM * h_r(mid, r)
        if best is None or val < best:
            best = val
            witness = ("interval", a, b, paid_inf, h_r(mid, r))

    assert best is not None
    ratio = best / LAM
    zmin = (ratio.numerator + ratio.denominator - 1) // ratio.denominator
    return best, ratio, zmin, witness


EXPECTED = {
    2:  (Fraction(101,18108), Fraction(101,684), 1),
    3:  (Fraction(3643,48288), Fraction(3643,1824), 2),
    4:  (Fraction(16081,144864), Fraction(16081,5472), 3),
    5:  (Fraction(80435,386304), Fraction(80435,14592), 6),
    6:  (Fraction(282521,1158912), Fraction(282521,43776), 7),
    7:  (Fraction(1262159,4400244), Fraction(1262159,166212), 8),
    8:  (Fraction(4115809,11733984), Fraction(4115809,443232), 10),
    9:  (Fraction(13808611,35201952), Fraction(726769,69984), 11),
    10: (Fraction(45390185,93871872), Fraction(45390185,3545856), 13),
    11: (Fraction(147860027,281615616), Fraction(147860027,10637568), 14),
    12: (Fraction(640820381,1069259292), Fraction(640820381,40389516), 16),
    13: (Fraction(1873261075,2851358112), Fraction(1873261075,107705376), 18),
    14: (Fraction(6640308193,9493807104), Fraction(6640308193,358612992), 19),
    15: (Fraction(19551818603,25316818944), Fraction(19551818603,956301312), 21),
    16: (Fraction(61356587585,75950456832), Fraction(61356587585,2868903936), 22),
    17: (Fraction(183985818883,202534551552), Fraction(183985818883,7650410496), 25),
    18: (Fraction(722233984561,768998375424), Fraction(722233984561,29047652352), 25),
    19: (Fraction(2262462108307,2306995126272), Fraction(2262462108307,87142957056), 26),
    20: (Fraction(6444835761809,6151987003392), Fraction(6444835761809,232381218816), 28),
    21: (Fraction(20100588522419,18455961010176), Fraction(20100588522419,697143656448), 29),
}


def main():
    for r in range(2, 22):
        got = exact_bound(r)
        assert got[:3] == EXPECTED[r], (r, got[:3], EXPECTED[r])
        lb, ratio, zmin, witness = got
        # None of the ratios is integral, so danger needs z >= ordinary ceil.
        assert ratio.denominator != 1
        assert lb > 0

        print(
            "r", r,
            "epsilon_lb", f"{lb.numerator}/{lb.denominator}",
            "ratio", f"{ratio.numerator}/{ratio.denominator}",
            "zmin", zmin,
            "witness", witness,
        )

    assert exact_bound(10)[2] == 13
    print("PASS MATH-202 exact phase-summed multi-paid surplus certificate")


if __name__ == "__main__":
    main()
