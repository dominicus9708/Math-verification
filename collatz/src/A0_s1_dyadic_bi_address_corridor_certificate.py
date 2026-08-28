#!/usr/bin/env python3
"""Exact finite certificate for the s=1 dyadic bi-address corridor.

Inputs inherited from companion SAFE certificates on the reset A0 branch:

    2^71 < X < 2^72,
    2^72 < Z < 2^73,
    (7581/100) G < L_minus=3X-Z < (2721/25) G,
    G=2^33.

The certificate records three exact consequences.

(1) A length-h parity word for the accelerated Collatz map

        T(n)=n/2              (n even),
             (3n+1)/2         (n odd)

    determines exactly one starting residue modulo 2^h.

(2) Because X and Z lie in the displayed shells, their first 72 and 73
    parity bits respectively expose the complete ordinary integers X and Z.

(3) Since 0<L_minus<2^40, the first 40 parity bits at X and at Z already
    expose the complete ordinary debit via

        L_minus = (3*(X mod 2^40) - (Z mod 2^40)) mod 2^40,

    where the right side is the least nonnegative residue; zero is excluded
    by the strict lower corridor.

This is an exposure/corridor theorem.  It is NOT a theorem that arbitrary
locally admissible 40-bit addresses extend through the long t0-step pre
block, and it does not use independence of the two marginal address sets.
This is not a proof of Collatz.
"""

from fractions import Fraction
from itertools import product

G = 1 << 33
M40 = 1 << 40
B = 1 << 71

L_LO = Fraction(7581, 100) * G
L_HI = Fraction(2721, 25) * G

# Integer corridor induced by the strict rational bounds.
L_MIN = (7581 * G) // 100 + 1
L_MAX = (2721 * G - 1) // 25

assert 0 < L_LO < L_HI < M40
assert L_MIN <= L_MAX < M40
assert Fraction(L_MIN, 1) > L_LO
assert Fraction(L_MAX, 1) < L_HI
assert Fraction(L_MIN - 1, 1) <= L_LO
assert Fraction(L_MAX + 1, 1) >= L_HI

# Reset-strip X shell used by the current Route-B audit.
# N < (4/3)2^71 and d < 0.478G imply X=N+d<2^72; N>2^71 and d>=0 imply X>2^71.
X_UPPER = Fraction(4, 3) * B + Fraction(478, 1000) * G
assert X_UPPER < 2 * B


def parity_address(bits):
    """Unique start residue mod 2^h for a prescribed parity word."""
    h = len(bits)
    qh = sum(bits)
    qprefix = 0
    correction = 0
    for i, eps in enumerate(bits):
        qprefix += eps
        if eps:
            correction += (1 << i) * (3 ** (qh - qprefix))
    modulus = 1 << h
    return (-correction * pow(3 ** qh, -1, modulus)) % modulus


def actual_parity_word(x, h):
    out = []
    for _ in range(h):
        eps = x & 1
        out.append(eps)
        x = (3 * x + 1) // 2 if eps else x // 2
    return tuple(out)


# Finite regression only: the algebraic identity in the companion note is the proof.
# Exhaustively verify bijection and word realization through depth 12.
for h in range(1, 13):
    residues = set()
    for bits in product((0, 1), repeat=h):
        x = parity_address(bits)
        assert actual_parity_word(x, h) == bits
        residues.add(x)
    assert len(residues) == (1 << h)

# Exact modular corridor identity regression on representative ordinary pairs.
# If L=3X-Z lies in (0,2^40), reduction mod 2^40 returns L itself.
for X0, L in [
    ((1 << 71) + 123456789, L_MIN),
    ((1 << 71) + (1 << 40) + 987654321, (L_MIN + L_MAX) // 2),
    ((1 << 72) - 1, L_MAX),
]:
    Z0 = 3 * X0 - L
    assert (3 * (X0 % M40) - (Z0 % M40)) % M40 == L

# High/low carry form of the same identity.
# Writing 3X=H*2^40+r and 0<L<2^40, floor(Z/2^40) is H or H-1.
for r in [0, L_MIN - 1, L_MIN, (L_MIN + L_MAX) // 2, L_MAX, M40 - 1]:
    for L in [L_MIN, (L_MIN + L_MAX) // 2, L_MAX]:
        H = 17
        value = H * M40 + r - L
        hz = value // M40
        assert hz in (H - 1, H)
        low_z = value % M40
        assert (r - low_z) % M40 == L

print("PASS A0 s=1 dyadic bi-address corridor certificate")
print("X_shell", "2^71 < X < 2^72")
print("Z_shell", "2^72 < Z < 2^73")
print("L_integer_min", L_MIN)
print("L_integer_max", L_MAX)
print("L_over_2^40_lower", float(L_LO / M40))
print("L_over_2^40_upper", float(L_HI / M40))
print("low_dyadic_meet_bits", 40)
print("parity_address_regression_depth", 12)
print("independence_product_used", False)
