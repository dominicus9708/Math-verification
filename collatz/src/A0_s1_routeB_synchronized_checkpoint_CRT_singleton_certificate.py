#!/usr/bin/env python3
"""Exact synchronized checkpoint CRT singleton certificate for A0 s=1 Route-B.

This closes the checkpoint exposure interface used before the 14-root
forward/backward join.

Upstream SAFE inputs are deliberately restricted to the pre-defect
40-bit debit/credit corridor chain:

    2^71 < X < (4/3) 2^71 + 0.478 2^33,
    75 2^33 < L_- < 112 2^33,
    L_- = 3X-Z.

No later defect-derived X bound is used here.

These give one SAFE integer checkpoint corridor [Z_MIN,Z_MAX].  A dyadic
observation

    Z == z2 (mod 2^27)

and the synchronized right-H ternary observation

    z_H == 2^s Z - C(H_s^*) (mod 3^28)

jointly determine one residue class modulo 2^27*3^28.  Since the certified
checkpoint corridor has span smaller than that modulus, every observation pair
(z2,z_H) has at most one ordinary integer Z in the corridor.

This is deterministic CRT arithmetic.  It is NOT multiplication of marginal
residue densities and does not assume dyadic/ternary independence.

Finite sample checks below are implementation guards only.  The proof kernel is
(1) the certified upstream strict intervals, (2) exact characteristic-word
correction arithmetic, (3) coprime CRT, and (4) corridor span < CRT modulus.
"""

from fractions import Fraction

J0 = 10_439_860_591
R0 = 6_586_818_670
S = 630_138_897

B = 1 << 71
G = 1 << 33

M2 = 1 << 27
M3 = 3 ** 28
M = M2 * M3


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def floor_fraction(x: Fraction) -> int:
    return x.numerator // x.denominator


def ceil_fraction(x: Fraction) -> int:
    return -((-x.numerator) // x.denominator)


# ---------------------------------------------------------------------------
# 1. SAFE checkpoint corridor from the independent pre-defect corridor chain.
# ---------------------------------------------------------------------------
X_LO = Fraction(B, 1)
X_HI = Fraction(4, 3) * B + Fraction(478, 1000) * G
LM_LO = Fraction(75 * G, 1)
LM_HI = Fraction(112 * G, 1)

# Strict upstream inequalities:
# X_LO < X < X_HI, LM_LO < L_- < LM_HI, Z = 3X-L_-.
Z_LO_REAL = 3 * X_LO - LM_HI
Z_HI_REAL = 3 * X_HI - LM_LO

Z_MIN = floor_fraction(Z_LO_REAL) + 1
Z_MAX = ceil_fraction(Z_HI_REAL) - 1
Z_SPAN = Z_MAX - Z_MIN

assert Z_MIN == 7_083_549_723_342_395_146_241
assert Z_MAX == 9_444_732_965_107_363_299_196
assert Z_SPAN == 2_361_183_241_764_968_152_955
assert (1 << 72) < Z_MIN <= Z_MAX < (1 << 73)

# ---------------------------------------------------------------------------
# 2. Exact terminal right-H affine observation modulo 3^28.
# ---------------------------------------------------------------------------
QH = (R0 * S) // J0 + 1
assert QH == 397_573_380


def target_one_position(r: int) -> int:
    """0-based bit position of ranked one r in H_s^*."""
    assert 1 <= r <= QH
    if r == 1:
        return 0
    # q_H(u)=floor((R0/J0)u)+1 for u>0.  The r-th jump occurs at
    # bit i=ceil((r-1)J0/R0)-1.
    return ceil_div((r - 1) * J0, R0) - 1


# Modulo 3^28 only the final 28 ranked-one correction terms survive.
CH28 = 0
for r in range(QH - 28 + 1, QH + 1):
    a = target_one_position(r)
    CH28 = (CH28 + pow(3, QH - r, M3) * pow(2, a, M3)) % M3

A28 = pow(2, S, M3)
INV_A28 = pow(A28, -1, M3)

assert M3 == 22_876_792_454_961
assert A28 == 12_596_342_295_887
assert CH28 == 2_677_095_985_033
assert INV_A28 == 17_062_811_582_066


def z3_from_right_carry(z_h: int) -> int:
    """Recover Z mod 3^28 from z_H=2^S Z-C(H_s^*) mod 3^28."""
    return (INV_A28 * ((z_h + CH28) % M3)) % M3


# ---------------------------------------------------------------------------
# 3. Synchronized CRT with the 27-bit dyadic checkpoint observation.
# ---------------------------------------------------------------------------
INV_M2_MOD_M3 = pow(M2, -1, M3)
assert INV_M2_MOD_M3 == 664_903_189_592
assert M == 3_070_471_107_232_407_748_608
assert Z_SPAN < M
assert M - Z_SPAN == 709_287_865_467_439_595_653


def crt_class(z2: int, z3: int) -> int:
    """Unique representative in [0,M) satisfying both coprime residues."""
    z2 %= M2
    z3 %= M3
    k = ((z3 - z2) * INV_M2_MOD_M3) % M3
    z0 = z2 + M2 * k
    assert 0 <= z0 < M
    assert z0 % M2 == z2
    assert z0 % M3 == z3
    return z0


def corridor_candidate(z2: int, z_h: int):
    """Return the unique checkpoint in the SAFE corridor, or None."""
    z3 = z3_from_right_carry(z_h)
    z0 = crt_class(z2, z3)

    k_lo = ceil_div(Z_MIN - z0, M)
    k_hi = (Z_MAX - z0) // M

    # Exact singleton theorem: corridor span is strictly less than M.
    assert k_lo > k_hi or k_lo == k_hi
    if k_lo > k_hi:
        return None

    z = z0 + k_lo * M
    assert Z_MIN <= z <= Z_MAX
    return z


# ---------------------------------------------------------------------------
# 4. Finite implementation guards only.
# ---------------------------------------------------------------------------
# Constructive synchronization: ordinary Z -> two observations -> same Z.
samples = (
    Z_MIN,
    Z_MIN + 1,
    (Z_MIN + Z_MAX) // 2,
    Z_MAX - 1,
    Z_MAX,
)
for z in samples:
    z2 = z % M2
    z_h = (A28 * z - CH28) % M3
    assert z3_from_right_carry(z_h) == z % M3
    assert corridor_candidate(z2, z_h) == z

# Generic observation-pair guard.
for z2 in (0, 1, 17, M2 - 1):
    for z_h in (0, 1, 19, M3 - 1):
        z = corridor_candidate(z2, z_h)
        if z is not None:
            assert z % M2 == z2
            assert (A28 * z - CH28) % M3 == z_h

print("PASS A0 s=1 Route-B synchronized checkpoint CRT singleton certificate")
print("Z_MIN", Z_MIN)
print("Z_MAX", Z_MAX)
print("Z_SPAN", Z_SPAN)
print("CRT_MODULUS", M)
print("CRT_MARGIN", M - Z_SPAN)
print("M3", M3)
print("A28", A28)
print("CH28", CH28)
print("INV_A28", INV_A28)
print("INV_2POW27_MOD_3POW28", INV_M2_MOD_M3)
print(
    "exact",
    "each synchronized (Z mod 2^27, right-H carry mod 3^28) pair admits at most one ordinary Z in the SAFE checkpoint corridor",
)
print(
    "dependency_audit",
    "uses only the pre-defect X/debit corridor inputs; no later defect-derived X bound is used retroactively",
)
print(
    "rejected_inference",
    "no dyadic/ternary marginal-density multiplication and no independence assumption",
)
print(
    "status",
    "synchronized checkpoint exposure CLOSED; 14-root source/P_min join remains OPEN",
)
