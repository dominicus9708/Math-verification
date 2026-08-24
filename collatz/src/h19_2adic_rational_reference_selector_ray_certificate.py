#!/usr/bin/env python3
"""Exact H19 2-adic rational reference and selector-ray audit.

Purpose
-------
The current R1 mechanical time word begins with repeated copies of

    H19 = 1101101101011011010.

This certificate identifies the unique 2-adic fixed point carrying the infinite
periodic parity word H19^infinity, proves that the first parity defect of an
ordinary start N is exactly the 2-adic valuation of one integer linear form,
and aggregates the recursively-sufficient ternary selector mass along this one
mechanical dyadic ray.

The result is a same-integer coordinate compression.  It does NOT prove that a
first-defect class is dynamically impossible, and the near-balanced selector
child masses must not be promoted to an independence assumption for later
renewal windows.
"""

from collections import defaultdict

H19 = "1101101101011011010"
A = len(H19)
Q = H19.count("1")


def correction(word: str) -> int:
    R = 0
    for i, ch in enumerate(word):
        if ch == "1":
            R = 3 * R + (1 << i)
    return R


R19 = correction(H19)
DEN = 3**Q - 2**A
assert A == 19
assert Q == 12
assert R19 == 1_568_693
assert DEN == 7_153

# The affine H19 map is
#   F(x)=(3^12*x+R19)/2^19.
# Its fixed point is x_* = -R19/DEN in Z_2.
# Since DEN is odd, reduction modulo every 2^L is well defined.


def xstar_mod(L: int) -> int:
    M = 1 << L
    return (-R19 * pow(DEN, -1, M)) % M


def parity_prefix(n: int, L: int) -> str:
    out = []
    for _ in range(L):
        bit = n & 1
        out.append("1" if bit else "0")
        n = (3 * n + 1) // 2 if bit else n // 2
    return "".join(out)


def v2(n: int) -> int:
    assert n != 0
    n = abs(n)
    return (n & -n).bit_length() - 1


# Direct fixed-point / parity audit at several complete H19 periods.
for L in (19, 38, 57, 76):
    xs = xstar_mod(L)
    assert parity_prefix(xs, L) == (H19 * ((L + 18) // 19))[:L]

# Exhaustive low-resolution audit of the first-defect identity on every
# residue N == 3 (mod 4) modulo 2^16.  If the first 16 symbols all agree, the
# linear form is divisible by 2^16; otherwise the first mismatch index equals
# its exact 2-adic valuation.
LTEST = 16
MECH16 = (H19 * 2)[:LTEST]
for N in range(3, 1 << LTEST, 4):
    w = parity_prefix(N, LTEST)
    first = next((i for i, (a, b) in enumerate(zip(w, MECH16)) if a != b), LTEST)
    lam = DEN * N + R19
    val = v2(lam) if lam % (1 << LTEST) else LTEST
    assert min(val, LTEST) == first

# For recursively-sufficient starts N=4Y+3,
#
#   Lambda(N)=7153*N+1568693
#            =4*(7153*Y+397538).
#
# Hence every current core start agrees with the first two mechanical parity
# symbols and
#
#   first defect p = 2 + v2(7153*Y+397538).
assert (3 * DEN + R19) % 4 == 0
SCALED_CONST = (3 * DEN + R19) // 4
assert SCALED_CONST == 397_538


def target_y_residue(kN: int) -> int:
    """Y residue mod 2^(kN-2) giving N=4Y+3 == x_* mod 2^kN."""
    assert kN >= 2
    if kN == 2:
        return 0
    m = kN - 2
    M = 1 << m
    # 7153*Y+397538 == 0 mod 2^(kN-2).
    return (-SCALED_CONST * pow(DEN, -1, M)) % M


def selector_target_count(C: int, selector_bits: int, kN: int) -> int:
    """Count Y=C+sum a_i 3^i lying on the x_* target ray mod 2^kN."""
    if kN == 2:
        return 1 << selector_bits
    m = kN - 2
    M = 1 << m
    target = target_y_residue(kN)
    dp = [0] * M
    dp[0] = 1
    for i in range(selector_bits):
        w = pow(3, i, M)
        nd = dp[:]
        for r, c in enumerate(dp):
            if c:
                nd[(r + w) & (M - 1)] += c
        dp = nd
    return dp[(target - C) & (M - 1)]


def ray_counts(C: int, selector_bits: int, kmax: int = 17):
    return [selector_target_count(C, selector_bits, k) for k in range(2, kmax + 1)]


# Current m=44 core after the exact V33 finite bootstrap:
# full 44-selector layer minus the low subblock a_33=...=a_43=0.
full44 = ray_counts(3**44, 44)
closed_low33 = ray_counts(3**44, 33)
current44 = [a - b for a, b in zip(full44, closed_low33)]

EXPECTED_M44 = [
    17_583_596_109_824,
    8_791_798_054_912,
    4_395_898_994_688,
    2_197_949_497_472,
    1_098_974_748_736,
    549_487_374_364,
    274_743_687_187,
    137_371_843_586,
    68_685_921_612,
    34_342_961_825,
    17_171_477_446,
    8_585_738_741,
    4_292_870_467,
    2_146_434_966,
    1_073_218_845,
    536_607_998,
]
assert current44 == EXPECTED_M44
assert current44[0] == (1 << 44) - (1 << 33)

# The unresolved m=45 range consists of the two 44-selector affine blocks
# C=3^45 and C=3^45+3^44.
m45a = ray_counts(3**45, 44)
m45b = ray_counts(3**45 + 3**44, 44)
m45 = [a + b for a, b in zip(m45a, m45b)]

EXPECTED_M45 = [
    35_184_372_088_832,
    17_592_186_044_416,
    8_796_090_925_056,
    4_398_045_462_528,
    2_199_022_731_248,
    1_099_511_365_622,
    549_755_682_812,
    274_877_841_393,
    137_438_920_476,
    68_719_459_198,
    34_359_726_613,
    17_179_866_734,
    8_589_931_815,
    4_294_970_007,
    2_147_494_113,
    1_073_741_800,
]
assert m45 == EXPECTED_M45
assert m45[0] == 1 << 45


def exact_first_defect_mass(ray, p: int) -> int:
    # ray[j] is C_k for k=2+j; exact p mass is C_p-C_(p+1).
    j = p - 2
    return ray[j] - ray[j + 1]


def child_imbalance(ray, k: int) -> int:
    # Signed target-child minus other-child mass inside target parent at level k.
    j = k - 2
    return 2 * ray[j + 1] - ray[j]


EXPECTED_DEFECT_M44 = {
    2: 8_791_798_054_912,
    5: 1_098_974_748_736,
    8: 137_371_843_601,
    10: 34_342_959_787,
    13: 4_292_868_274,
    16: 536_610_847,
}
EXPECTED_DEFECT_M45 = {
    2: 17_592_186_044_416,
    5: 2_199_022_731_280,
    8: 274_877_841_419,
    10: 68_719_461_278,
    13: 8_589_934_919,
    16: 1_073_752_313,
}
for p, c in EXPECTED_DEFECT_M44.items():
    assert exact_first_defect_mass(current44, p) == c
for p, c in EXPECTED_DEFECT_M45.items():
    assert exact_first_defect_mass(m45, p) == c

EXPECTED_U_M44 = {
    2: 0,
    5: 0,
    8: -15,
    10: 2_038,
    13: 2_193,
    16: -2_849,
}
EXPECTED_U_M45 = {
    2: 0,
    5: -32,
    8: -26,
    10: -2_080,
    13: -3_104,
    16: -10_513,
}
for k, u in EXPECTED_U_M44.items():
    assert child_imbalance(current44, k) == u
for k, u in EXPECTED_U_M45.items():
    assert child_imbalance(m45, k) == u

print("H19 2-adic rational reference / selector ray: PASS")
print("H19", H19)
print("odd_count", Q)
print("R19", R19)
print("x_star", f"-{R19}/{DEN}")
print("linear_label", f"Lambda(N)={DEN}*N+{R19}")
print("scaled_core_label", f"Lambda/4={DEN}*Y+{SCALED_CONST}")
print("m44_current_ray_C2_to_C17", current44)
print("m45_two_block_ray_C2_to_C17", m45)
print("m44_unresolved_channel_masses", EXPECTED_DEFECT_M44)
print("m45_unresolved_channel_masses", EXPECTED_DEFECT_M45)
print("m44_target_child_imbalances", EXPECTED_U_M44)
print("m45_target_child_imbalances", EXPECTED_U_M45)
