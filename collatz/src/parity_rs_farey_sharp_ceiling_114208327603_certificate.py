#!/usr/bin/env python3
"""Exact rational certificate for the sharp constant-wall parity-RS gate.

External input (not reverified here): every positive integer below 2^71
converges under the shortcut Collatz map, as reported by Barina.

The script proves, with Fraction arithmetic and rigorous atanh-series bounds,
that the chosen rational wall is valid for the adjusted multiplier
3 + 2^-71, that it and an upper Farey neighbour straddle log_3(2), and
that their mediant lies strictly between the adjusted and exact critical
slopes.  Consequently the coefficient-survival gate through Q-1 is sharp
for every single constant rational parity-RS wall derived only from B=2^71.
"""

from fractions import Fraction

B = 1 << 71
TERMS = 35

# Valid lower wall r=p/d < beta := log_{3+1/B}(2).
p = 6_586_818_670
d = 10_439_860_591

# Farey neighbour above alpha := log_3(2).
u = 65_470_613_321
v = 103_768_467_013

# First rational between beta and alpha.
P = p + u
Q = d + v


def log_bounds(num: int, den: int, terms: int = TERMS) -> tuple[Fraction, Fraction]:
    """Rigorous lower/upper bounds for log(num/den), num>den>0.

    With z=(x-1)/(x+1),
        log x = 2*sum_{k>=0} z^(2k+1)/(2k+1).
    The positive tail after `terms` terms is bounded by replacing every
    remaining denominator by 2*terms+1 and summing the geometric series.
    """
    assert num > den > 0
    z = Fraction(num - den, num + den)
    z2 = z * z
    zpow = z
    s = Fraction(0)

    for k in range(terms):
        s += zpow / (2 * k + 1)
        zpow *= z2

    lower = 2 * s
    tail_upper = 2 * zpow / Fraction(2 * terms + 1) / (1 - z2)
    upper = lower + tail_upper
    return lower, upper


def main() -> None:
    L2, U2 = log_bounds(2, 1)
    L3, U3 = log_bounds(3, 1)
    LA, UA = log_bounds(3 * B + 1, B)

    # 1) Valid parity-RS lower wall: p/d < beta=log_A(2).
    #    Sufficient exact comparison: p*upper(log A) < d*lower(log 2).
    assert p * UA < d * L2

    # 2) Exact critical slope is below u/v: alpha=log_3(2) < u/v.
    assert u * L3 > v * U2

    # 3) Farey-neighbour determinant.
    assert u * d - p * v == 1

    # 4) Mediant lies below alpha.
    assert P * U3 < Q * L2

    # 5) Mediant lies above beta.
    assert P * LA > Q * U2

    # 6) Exact mediant identities.
    assert P == 72_057_431_991
    assert Q == 114_208_327_604
    assert P * d - p * Q == 1
    assert u * Q - P * v == 1

    print("PASS sharp constant-wall parity-RS coefficient gate")
    print(f"published_base=2^71={B}")
    print(f"series_terms={TERMS}")
    print(f"valid_lower_wall={p}/{d}")
    print(f"farey_upper={u}/{v}")
    print(f"first_beta_alpha_rational={P}/{Q}")
    print(f"coefficient_survival_forced_through={Q-1}")
    print(f"sharp_constant_wall_failure_depth={Q}")


if __name__ == "__main__":
    main()
