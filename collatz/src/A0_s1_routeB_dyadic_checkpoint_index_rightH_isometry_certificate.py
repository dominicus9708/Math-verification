#!/usr/bin/env python3
"""Exact certificate for the dyadic checkpoint-index / right-H 3-adic isometry.

Fix z2 = Z mod 2^27 and write

    Z = z2 + 2^27 n.

The synchronized right-H observation is

    zH = 2^s Z - C_H (mod 3^28)
       = A(z2) + u*n (mod 3^28),

where u=2^(s+27) is a unit.  Hence every zH cylinder modulo 3^ell
pulls back to exactly one n cylinder modulo 3^ell.

The proof is algebraic; finite loops below are implementation guards only.
"""

from math import gcd

S = 630_138_897
M2 = 1 << 27
M3 = 3 ** 28
C_H = 2_677_095_985_033
POW2S = pow(2, S, M3)
U = pow(2, S + 27, M3)
U_INV = pow(U, -1, M3)

Z_MIN = 7_083_549_723_342_395_146_241
Z_MAX = 9_444_732_965_107_363_299_196
Z_SPAN = Z_MAX - Z_MIN

EXPECTED_POW2S = 12_596_342_295_887
EXPECTED_U = 15_139_992_122_704
EXPECTED_U_INV = 13_299_776_895_097
EXPECTED_MAX_SLICE = 17_592_186_046_876


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def slice_bounds(z2: int):
    assert 0 <= z2 < M2
    lo = ceil_div(Z_MIN - z2, M2)
    hi = (Z_MAX - z2) // M2
    return lo, hi


def A(z2: int, modulus: int = M3) -> int:
    return (pow(2, S, modulus) * z2 - C_H) % modulus


def zH_from_index(z2: int, n: int, modulus: int = M3) -> int:
    return (A(z2, modulus) + pow(2, S + 27, modulus) * n) % modulus


def pullback_residue(z2: int, c: int, ell: int) -> int:
    assert 1 <= ell <= 28
    mod = 3 ** ell
    u = pow(2, S + 27, mod)
    return (pow(u, -1, mod) * (c - A(z2, mod))) % mod


assert POW2S == EXPECTED_POW2S
assert U == EXPECTED_U
assert U_INV == EXPECTED_U_INV
assert gcd(U, M3) == 1
assert (U * U_INV) % M3 == 1

max_slice = Z_SPAN // M2 + 1
assert max_slice == EXPECTED_MAX_SLICE
assert max_slice < M3

# Every full dyadic slice has fewer than 3^28 possible n values.
for z2 in (0, 1, Z_MIN % M2, Z_MAX % M2, M2 - 1):
    lo, hi = slice_bounds(z2)
    count = max(0, hi - lo + 1)
    assert count <= max_slice
    assert count < M3

# Implementation guards for the exact residue pullback identity at several
# precisions.  The theorem itself follows from invertibility of U modulo 3^ell.
for ell in (1, 2, 5, 12, 18, 24, 28):
    mod = 3 ** ell
    u = pow(2, S + 27, mod)
    assert gcd(u, mod) == 1

    for z2 in (0, 1, 17, Z_MIN % M2, Z_MAX % M2, M2 - 1):
        for c in (0, 1, 2, mod // 2, mod - 1):
            rho = pullback_residue(z2, c, ell)
            assert zH_from_index(z2, rho, mod) == c % mod

            # Any translated representative by 3^ell has the same zH cylinder.
            assert zH_from_index(z2, rho + mod, mod) == c % mod

# Full 28-trit injectivity on a SAFE slice follows algebraically from
# |n1-n2| < 3^28.  Check the relevant uniform inequality exactly.
assert Z_SPAN < M2 * M3
assert max_slice <= M3 - 1

print("PASS A0 s=1 dyadic checkpoint-index/right-H isometry certificate")
print("2^s_mod_3^28", POW2S)
print("u_2^(s+27)_mod_3^28", U)
print("u_inverse_mod_3^28", U_INV)
print("max_checkpoint_index_slice", max_slice)
print("3^28", M3)
print("uniform_slice_lt_3^28", True)
print("status", "EXACT residue pullback at fixed dyadic checkpoint address; right-H path construction remains OPEN")
