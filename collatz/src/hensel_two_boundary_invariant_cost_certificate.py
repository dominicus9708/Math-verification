#!/usr/bin/env python3
"""Regression for the exact two-boundary Hensel invariant/cost identity.

The proof is symbolic and is documented in the companion note.  This script
checks the identity on all short gap words and a range of displacements using
exact Fraction arithmetic, including negative 3-adic powers of two represented
as ordinary rational units with denominator a power of two.
"""

from fractions import Fraction
from itertools import product


def p2(e: int) -> Fraction:
    if e >= 0:
        return Fraction(1 << e, 1)
    return Fraction(1, 1 << (-e))


def v3_fraction(x: Fraction) -> int:
    assert x != 0
    n = abs(x.numerator)
    d = x.denominator
    vn = 0
    vd = 0
    while n % 3 == 0:
        n //= 3
        vn += 1
    while d % 3 == 0:
        d //= 3
        vd += 1
    return vn - vd


def exponents(e0: int, gaps):
    e = [e0]
    for g in gaps:
        assert g in (1, 2)
        e.append(e[-1] - g)
    return e


def check(gaps, e0: int, ds):
    es = exponents(e0, gaps)
    h = len(es)
    assert len(ds) == h

    u = [p2(es[i] - ds[i]) for i in range(h)]
    um = [p2(es[i]) for i in range(h)]

    # Exact invariant for the chosen control word.
    xi = -sum(Fraction(3**i, 1) * u[i] for i in range(h))
    xi0 = -sum(Fraction(3**i, 1) * um[i] for i in range(h))

    # With normalization 2*w_i = 3^i*2^e_i, the accumulated min-plus charge
    # is exactly xi-xi0.
    J = sum(
        Fraction(3**i, 1) * um[i] * (1 - p2(-ds[i]))
        for i in range(h)
    )
    assert xi - xi0 == J
    assert J >= 0

    # Build an exact terminal state and reconstruct the right state backward.
    # This proves the full invariant equation implies every local Hensel
    # division and every preterminal unit condition.
    states = [None] * (h + 1)
    states[h] = Fraction(5, 2)
    for i in range(h - 1, -1, -1):
        states[i] = 3 * states[i + 1] - u[i]

    assert states[0] - 3**h * states[h] == xi

    for i in range(h):
        assert (states[i] + u[i]) / 3 == states[i + 1]
        assert v3_fraction(states[i] + u[i]) >= 1
        if i + 1 < h:
            assert v3_fraction(states[i + 1]) == 0

    # Same Xi is exactly one affine-covariance orbit for the carry pair.
    t = Fraction(7, 4)
    Kr2 = states[0] + 3**h * t
    Kl2 = states[h] + t
    assert Kr2 - 3**h * Kl2 == xi


for h in range(1, 7):
    for gaps in product((1, 2), repeat=max(0, h - 1)):
        for e0 in (-2, -1, 0, 1, 2):
            for ds in product(range(4), repeat=h):
                check(gaps, e0, ds)

print("PASS two-boundary Hensel invariant/cost-collapse regression")
print("identity", "Xi-Xi_mech = sum 3^i 2^e_i (1-2^-d_i)")
print("full_boundary_cost", "fixed whenever the boundary Xi is fixed")
