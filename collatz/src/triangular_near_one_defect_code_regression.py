#!/usr/bin/env python3
"""
Triangular Beatty near-one defect-code regression.

This file accompanies the algebraic lemma recorded in
collatz/notes/2026-08-26-triangular-near-one-defect-code-lemma.md.

It checks:
  * exact dyadic phase transport;
  * centered defect-code integrality;
  * the global short-edge near-one threshold delta=1/60074;
  * uniqueness of the newly appended dyadic chunk when the defect is zero;
  * the explicit combinatorial constants used in the frequency-count bound.

The theorem is algebraic.  The finite loops below are regression checks, not
the proof and not a proof of the Collatz conjecture.
"""

from fractions import Fraction
from math import cos, pi, log2

D_SHORT = 10
DELTA = Fraction(1, 2**D_SHORT + 3**D_SHORT + 1)  # 1/60074
RHO = Fraction(1, 100)

assert DELTA == Fraction(1, 60074)
for d in range(1, D_SHORT + 1):
    for s in range(1, d + 1):
        assert DELTA * (2**d + 3**s) < 1


def centered(r: int, modulus: int) -> int:
    r %= modulus
    if r > modulus // 2:
        r -= modulus
    return r


def phase_centered(k: int, m: int, ell: int) -> int:
    M = 1 << m
    a = pow(3, -ell, M)
    return centered((k % M) * a, M)


def transition(k: int, m: int, ell: int, d: int, s: int):
    assert 1 <= d < m and 1 <= s <= d
    M2 = 1 << (m - d)
    c = phase_centered(k, m, ell)
    cp = phase_centered(k, m - d, ell + s)

    # Exact transport modulo the lower dyadic resolution.
    assert (c - (3**s) * cp) % M2 == 0
    z = (c - (3**s) * cp) // M2

    near = abs(c) * DELTA.denominator <= (1 << m)
    nearp = abs(cp) * DELTA.denominator <= (1 << (m - d))
    if near and nearp:
        # |z| <= delta(2^d+3^s) < 1, hence z=0.
        assert z == 0
    return c, cp, z


# Exhaustive small-modulus transport regression.
checks = 0
for m in range(3, 11):
    for d in range(1, min(D_SHORT, m - 1) + 1):
        for s in range(1, d + 1):
            for ell in range(1, 7):
                for k in range(1 << m):
                    transition(k, m, ell, d, s)
                    checks += 1

# Zero defect fixes at most one newly appended d-bit chunk.
uniqueness_checks = 0
for m in range(4, 13):
    for d in range(1, min(D_SHORT, m - 1) + 1):
        for s in range(1, d + 1):
            for ell in range(1, 7):
                low_mod = 1 << (m - d)
                # Sample every low state for small lower resolutions; cap larger
                # cases to keep this regression portable.
                lows = range(low_mod) if low_mod <= 256 else range(256)
                for klow in lows:
                    hits = 0
                    for h in range(1 << d):
                        k = klow + h * low_mod
                        _, _, z = transition(k, m, ell, d, s)
                        if z == 0:
                            hits += 1
                    assert hits <= 1
                    uniqueness_checks += 1

# Explicit counting constants used in the note.
# n >= L/10 and long gaps are d>=11, so there are at least n/11 - 1
# short edges.  If at most n/100 vertices are far, at most 2n/100
# short edges are spoiled.
zero_edge_density = Fraction(1, 11) - 2 * RHO  # 39/550
bit_saving_density = 2 * zero_edge_density    # 39/275
assert zero_edge_density == Fraction(39, 550)
assert bit_saving_density == Fraction(39, 275)

# Standard binary entropy at rho=0.01; diagnostic decimal only.
rho = float(RHO)
H2 = -rho * log2(rho) - (1-rho) * log2(1-rho)
assert H2 < 0.081
net_code_exponent = float(bit_saving_density) - H2
assert net_code_exponent > 0.060

kappa = cos(pi / DELTA.denominator)
far_bit_rate = -log2(kappa)
eta_per_mixed_coordinate = far_bit_rate / 100.0
eta_per_boundary_length = far_bit_rate / 1000.0

print("triangular near-one defect-code regression: PASS")
print("transport checks =", checks)
print("zero-defect uniqueness checks =", uniqueness_checks)
print("delta = 1/%d" % DELTA.denominator)
print("zero-edge density >= 39/550 (up to O(1/n))")
print("bit-saving density >= 39/275 (up to O(1/n))")
print("H2(0.01) =", H2)
print("net sparse-code exponent >", net_code_exponent, "bits/mixed-coordinate")
print("-log2(cos(pi/60074)) =", far_bit_rate)
print("typical-fibre product rate >=", eta_per_mixed_coordinate,
      "bits/mixed-coordinate")
print("using n>=L/10 gives >=", eta_per_boundary_length,
      "bits/boundary-step")
