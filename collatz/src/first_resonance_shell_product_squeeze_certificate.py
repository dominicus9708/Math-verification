#!/usr/bin/env python3
"""Exact arithmetic certificate for the first-resonance shell-product squeeze.

For the odd-event orbit x_j with dyadic shell displacement d_j,
    x_j > 2^d_j N,
and the first-resonance product identity gives a lower bound on
    sum 2^(-d_j).

This certificate proves the numerical lower bound using exact Fraction
logarithm intervals.  It does not prove the Collatz conjecture.
"""

from fractions import Fraction

A = 114_208_327_604
Q = 72_057_431_991
B = 1 << 71
NLOG = 70


def log_bounds(z: Fraction, n: int = NLOG):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


l2, u2 = log_bounds(Fraction(1, 3))   # ln 2
l3, u3 = log_bounds(Fraction(1, 2))   # ln 3

# Lambda = A ln2 - Q ln3.  Use the directed lower interval.
lambda_lo = A * l2 - Q * u3
lambda_hi = A * u2 - Q * l3
assert 0 < lambda_lo < lambda_hi

# Product identity + ln(1+u)<u + x_j > 2^d_j N and N>B imply
#     sum_j 2^(-d_j) > 3 B Lambda.
moment_lo = 3 * B * lambda_lo
assert moment_lo > 39_036_664_018
assert moment_lo / Q > Fraction(5417, 10_000)

print("PASS first-resonance shell product squeeze")
print("lambda_lower", float(lambda_lo))
print("lambda_upper", float(lambda_hi))
print("shell_moment_lower", float(moment_lo))
print("shell_moment_fraction_lower", float(moment_lo / Q))
