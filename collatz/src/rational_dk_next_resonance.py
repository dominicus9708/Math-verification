#!/usr/bin/env python3
"""Exact rational verifier for the next unresolved Collatz resonance.

Scope:
- no floating point;
- certifies a Denjoy--Koksma-based magnitude bound using rational
  atanh-series intervals for ln 2 and ln 3;
- certifies the resulting m=46 ternary-prefix restriction and candidate count;
- certifies rational defect-count bounds.

This is a finite verifier, not a Collatz/CST proof.
"""

from fractions import Fraction

Q = 137_528_045_312
SIGMA = 217_976_794_617
N = 40

EXPECTED_UCERT = 36_797_925_187_243_805_015_225
EXPECTED_TOTAL = 62_672_162_783_232
EXPECTED_N1 = 14_516_878_922
EXPECTED_N2 = 9_677_919_281
EXPECTED_N3 = 8_295_359_384


def log_ratio_bounds(x: Fraction, n: int):
    """Bounds log((1+x)/(1-x)) by a positive atanh series."""
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * x ** (2 * k + 1) / (2 * k + 1)
    tail = (
        Fraction(2)
        * x ** (2 * n + 3)
        / (2 * n + 3)
        / (1 - x * x)
    )
    return s, s + tail


def count_allowed_top4(smax: int):
    allowed = []
    max_tail = (3**40 - 1) // 2
    for mask in range(16):
        bits = [(mask >> (3 - j)) & 1 for j in range(4)]
        base = sum(bits[j] * 3 ** (43 - j) for j in range(4))
        if base + max_tail <= smax:
            allowed.append(tuple(bits))
    return allowed


def main():
    l2, u2 = log_ratio_bounds(Fraction(1, 3), N)  # ln 2
    l3, u3 = log_ratio_bounds(Fraction(1, 2), N)  # ln 3

    lambda_lower = SIGMA * l2 - Q * u3
    lambda_upper = SIGMA * u2 - Q * l3
    assert lambda_lower > 0
    assert lambda_lower <= lambda_upper

    # DK: S*(q) <= q/(6 ln2) + 1/3.
    correction_upper = Fraction(Q, 1) / (6 * l2) + Fraction(1, 3)

    # delta=e^Lambda-1 >= Lambda >= lambda_lower.
    x_upper = correction_upper / lambda_lower
    ucert = (x_upper.numerator + x_upper.denominator - 1) // x_upper.denominator

    assert ucert == EXPECTED_UCERT
    assert x_upper < 2**75
    assert ucert < 2**75

    # Integer x satisfies x < ucert.
    # In m=46: x=4(3^46+S)+3.
    smax = (ucert - 4) // 4 - 3**46
    allowed = count_allowed_top4(smax)
    expected_patterns = {
        (0, 0, 0, 0),
        (0, 0, 0, 1),
        (0, 0, 1, 0),
        (0, 0, 1, 1),
        (0, 1, 0, 0),
        (0, 1, 0, 1),
        (0, 1, 1, 0),
        (0, 1, 1, 1),
        (1, 0, 0, 0),
    }
    assert set(allowed) == expected_patterns

    m46_count = len(allowed) * 2**40
    total_count = 3 * 2**44 + m46_count
    assert total_count == EXPECTED_TOTAL

    # Rational defect-density certificate at the minimal m=46 start.
    x46 = 4 * 3**46 + 3
    deficit_upper = correction_upper - lambda_lower * x46
    assert deficit_upper > 0

    n1 = (12 * deficit_upper.numerator) // deficit_upper.denominator
    n2_bound = 8 * deficit_upper  # 6/(1-1/4)=8
    n2 = n2_bound.numerator // n2_bound.denominator
    n3_bound = Fraction(48, 7) * deficit_upper  # 6/(1-1/8)=48/7
    n3 = n3_bound.numerator // n3_bound.denominator

    assert n1 == EXPECTED_N1
    assert n2 == EXPECTED_N2
    assert n3 == EXPECTED_N3

    print("exact rational certificate: PASS")
    print("lambda_lower > 0:", True)
    print("certified integer upper endpoint:", ucert)
    print("margin below 2^75:", 2**75 - ucert)
    print("allowed m=46 high-four prefixes:", ["".join(map(str, p)) for p in allowed])
    print("m=46 candidate count:", m46_count)
    print("total four-block candidate count:", total_count)
    print("N_{>0} <=", n1)
    print("N_{>=2} <=", n2)
    print("N_{>=3} <=", n3)
    print("certified cap fraction >=", float(Fraction(Q - n1, Q)))


if __name__ == "__main__":
    main()
