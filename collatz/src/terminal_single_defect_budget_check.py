#!/usr/bin/env python3
from fractions import Fraction

Q = 137_528_045_312
SIGMA = 217_976_794_617
NLOG = 40
NDEF_MAX = 285_942_279
D_NEAR = 29_785_654
M19 = 3**19
R19 = 738_416_854

EXPECTED_ZMAX = 167_265_511
EXPECTED_HITS = [
    (51_123_563, 36_788_825_963_355_776_078_158, 5_172_161_310),
    (69_623_881, 36_767_449_656_405_490_789_198, 574_162_590),
    (108_790_195, 36_764_980_509_571_862_422_402, 43_054_293),
    (112_458_389, 36_772_083_750_100_501_999_090, 1_570_946_409),
    (157_121_141, 36_787_219_587_291_159_407_602, 4_826_633_193),
]


def log_ratio_bounds(x: Fraction, n: int):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * x ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * x ** (2 * n + 3) / ((2 * n + 3) * (1 - x * x))
    return s, s + tail


def cantor_values(t: int):
    vals = [0]
    p = 1
    for _ in range(t):
        vals += [v + p for v in vals]
        p *= 3
    return vals


def ceil_fraction(x: Fraction) -> int:
    return (x.numerator + x.denominator - 1) // x.denominator


def strict_integer_lower(x: Fraction) -> int:
    """Smallest integer L certified by L > x."""
    return x.numerator // x.denominator + 1


def main():
    l2, u2 = log_ratio_bounds(Fraction(1, 3), NLOG)
    l3, u3 = log_ratio_bounds(Fraction(1, 2), NLOG)

    lambda_lower = SIGMA * l2 - Q * u3
    assert lambda_lower > 0
    correction_upper = Fraction(Q, 1) / (6 * l2) + Fraction(1, 3)

    # beta = log_2(3/2).  The rational interval certifies the terminal
    # amplitude ceiling from the global run-aware defect-count bound.
    beta_upper = u3 / l2 - 1
    zmax = ceil_fraction(beta_upper * NDEF_MAX)
    assert zmax == EXPECTED_ZMAX
    assert beta_upper < Fraction(117, 200)  # 0.585

    # If the first of the last 20 positions is the only terminal defect,
    # y mod 3^19 is fixed.  Near-return d<=D_NEAR leaves a finite lower
    # Cantor slice.  Compute its exact minimum possible d.
    good_d = []
    for s in cantor_values(19):
        xrem = (4 * s + 3) % M19
        d = (R19 - xrem) % M19
        if d <= D_NEAR:
            good_d.append(d)
    assert len(good_d) == 13_824
    dmin = min(good_d)
    assert dmin == 20_971_503

    # If a terminal run has L nonzero-defect points and reaches amplitude z,
    # then z-1 further level increments must occur across L-1 transitions.
    # Since a +1 increment is possible only at a mechanical gap-2 transition
    # and beta<117/200,
    #
    #   L > 1 + 200(z-2)/117.
    #
    # This point/transition indexing is deliberately one step weaker than the
    # earlier provisional ceil(200(z-1)/117) expression.
    for z, y, shi in EXPECTED_HITS:
        lrun = strict_integer_lower(Fraction(1) + Fraction(200 * (z - 2), 117))
        loss_lower = Fraction(5 * lrun, 48)
        budget_upper = correction_upper - lambda_lower * y - dmin
        assert budget_upper < loss_lower
        print(
            "rejected",
            "z=", z,
            "shi=", shi,
            "run>=", lrun,
            "loss_lower=", float(loss_lower),
            "budget_upper=", float(budget_upper),
        )

    print("terminal single-defect rational budget check: PASS")
    print("certified zmax:", zmax)
    print("lower-19 near-return choices:", len(good_d))
    print("minimum possible d:", dmin)


if __name__ == "__main__":
    main()
