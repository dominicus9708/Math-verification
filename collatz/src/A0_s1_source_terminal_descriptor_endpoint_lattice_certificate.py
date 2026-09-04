#!/usr/bin/env python3
"""Regression certificate for the source terminal-descriptor endpoint lattice.

For an activation channel

    X = r + 2^h k
    Y = y + 3^q k

and a fixed terminal block B of length n, one-count d and correction C_B,
there is one k-residue modulo 2^n realizing B.  Writing

    k = kappa + 2^n t

then gives the exact joint lattice

    X = R_B + 2^(h+n) t
    Z = Z_B + 3^(q+d) t.

At the current late seam h+n=t0 and q+d=j0 with d=28.
Finite examples below are implementation guards only.
"""

from fractions import Fraction


def correction(positions):
    q = len(positions)
    return sum((3 ** (q - 1 - j)) * (1 << a) for j, a in enumerate(positions))


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def compile_terminal(r, y, h, q, k_lo, k_hi, n, positions):
    d = len(positions)
    assert positions == sorted(positions)
    assert len(set(positions)) == d
    assert positions[-1] < n

    C_B = correction(positions)
    mod2 = 1 << n
    power3 = 3 ** (q + d)
    inv = pow(power3 % mod2, -1, mod2)
    kappa = (-(3 ** d * y + C_B) * inv) % mod2

    t_lo = ceil_div(k_lo - kappa, mod2)
    t_hi = (k_hi - kappa) // mod2

    R_B = r + (1 << h) * kappa
    endpoint_num = (3 ** d) * y + C_B + power3 * kappa
    assert endpoint_num % mod2 == 0
    Z_B = endpoint_num // mod2

    return d, C_B, kappa, t_lo, t_hi, R_B, Z_B


CASES = [
    # r, y, h, q, k_lo, k_hi, n, terminal one positions
    (5, 7, 4, 3, -30, 80, 6, [0, 2, 5]),
    (9, 11, 5, 4, 0, 200, 7, [1, 3, 4, 6]),
    (13, 17, 3, 2, -100, 300, 8, [0, 2, 5, 7]),
]

for case in CASES:
    r, y, h, q, k_lo, k_hi, n, positions = case
    d, C_B, kappa, t_lo, t_hi, R_B, Z_B = compile_terminal(*case)

    for t in range(t_lo, t_hi + 1):
        k = kappa + (1 << n) * t
        assert k_lo <= k <= k_hi

        X = r + (1 << h) * k
        Y = y + (3 ** q) * k
        endpoint = (3 ** d) * Y + C_B
        assert endpoint % (1 << n) == 0
        Z = endpoint // (1 << n)

        assert X == R_B + (1 << (h + n)) * t
        assert Z == Z_B + (3 ** (q + d)) * t

    # No omitted k in the parent interval can realize the supplied block.
    for k in range(k_lo, k_hi + 1):
        Y = y + (3 ** q) * k
        realizes = ((3 ** d) * Y + C_B) % (1 << n) == 0
        assert realizes == (k % (1 << n) == kappa)


# Current late-seam identities.  Avoid constructing astronomically large
# 2^t0 or 3^j0; only exponent comparisons are needed for the singleton proof.
T0 = 104_398_605_910
J0 = 65_868_186_701
D = 28
Q = J0 - D

assert Q == 65_868_186_673
assert Q + D == J0
assert T0 > 72

# Certified source corridor upper endpoint is below 2^72:
# (4/3*2^71 + 0.478*2^33) / 2^72
#   = 2/3 + 0.478*2^-39 < 1.
ratio = Fraction(2, 3) + Fraction(239, 500) * Fraction(1, 2 ** 39)
assert ratio < 1

# Therefore the full source corridor has width <2^72, while a fixed complete
# terminal descriptor refines the source lattice with spacing 2^t0 and t0>72.
# The inequality follows from exponent monotonicity; do not materialize 2^t0.
assert T0 > 72

print("PASS source terminal-descriptor endpoint lattice certificate")
print("late_activation_q", Q)
print("terminal_one_count", D)
print("full_odd_count", J0)
print("full_depth", T0)
print("source_corridor_upper_over_2^72_lt_1", True)
print("per_descriptor_physical_source_cardinality", "<= 1")
print("endpoint_consequence", "source-derived terminal descriptor directly exposes provenanced Z")
print("status", "EXACT endpoint lattice; terminal descriptor language remains OPEN")
