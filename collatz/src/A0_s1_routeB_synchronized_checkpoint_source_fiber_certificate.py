#!/usr/bin/env python3
"""Exact source-fiber cardinality certificate after synchronized checkpoint exposure.

For one retained A0 s=1 Route-B source root

    X = r + 2^h m

and one already-exposed ordinary checkpoint Z, use only the independent
pre-defect debit corridor

    75*2^33 < L_- < 112*2^33,
    L_- = 3X-Z.

Then m lies in one open real interval of width

    37*2^33 / (3*2^h).

Hence its integer cardinality is at most the ceiling of that width.  This file
checks the 14 root-depth values and exact integer endpoint implementation.

Finite sample endpoint checks are implementation guards only.  The general
bound is the elementary interval-lattice argument in the module docstring and
canonical theorem.
"""

G = 1 << 33
L_MINUS_LO = 75 * G
L_MINUS_HI = 112 * G

ROOTS = (2, 5, 8, 10, 13, 16, 18, 21, 24, 27, 29, 32, 35, 37)
EXPECTED = {
    2: 13_242_815_830,
    5: 1_655_351_979,
    8: 206_918_998,
    10: 51_729_750,
    13: 6_466_219,
    16: 808_278,
    18: 202_070,
    21: 25_259,
    24: 3_158,
    27: 395,
    29: 99,
    32: 13,
    35: 2,
    37: 1,
}

Z_MIN = 7_083_549_723_342_395_146_241
Z_MAX = 9_444_732_965_107_363_299_196


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def fiber_cap(first_defect: int) -> int:
    h = first_defect + 1
    return ceil_div(L_MINUS_HI - L_MINUS_LO, 3 * (1 << h))


def exact_fiber_bounds(Z: int, r: int, h: int):
    """Exact integer m bounds from strict debit inequalities."""
    assert 0 <= r < (1 << h)
    den = 3 * (1 << h)

    # den*m > Z + L_MINUS_LO - 3r
    m_lo = (Z + L_MINUS_LO - 3 * r) // den + 1

    # den*m < Z + L_MINUS_HI - 3r
    # The right-hand side is an integer, so m <= (rhs-1)//den.
    m_hi = (Z + L_MINUS_HI - 3 * r - 1) // den
    return m_lo, m_hi


for f in ROOTS:
    assert fiber_cap(f) == EXPECTED[f]

    h = f + 1
    # Endpoint/residue implementation guards.  The theorem itself is not
    # inferred from these samples.
    for Z in (0, 1, 2, Z_MIN, Z_MAX):
        for r in (0, 1, (1 << h) - 1):
            lo, hi = exact_fiber_bounds(Z, r, h)
            count = max(0, hi - lo + 1)
            assert count <= EXPECTED[f]

assert sum(EXPECTED[f] for f in ROOTS if f >= 24) == 3_668
assert sum(EXPECTED[f] for f in ROOTS if f >= 27) == 510
assert sum(EXPECTED[f] for f in ROOTS if f >= 29) == 115
assert sum(EXPECTED[f] for f in ROOTS if f >= 32) == 16
assert sum(EXPECTED[f] for f in ROOTS if f >= 35) == 3
assert sum(EXPECTED[f] for f in ROOTS if f >= 37) == 1

print("PASS A0 s=1 synchronized checkpoint source-fiber certificate")
for f in ROOTS:
    print("root", f, "depth", f + 1, "max_source_parameters_per_Z", EXPECTED[f])
print("deep_suffix_f_ge_24", 3668)
print("deep_suffix_f_ge_27", 510)
print("deep_suffix_f_ge_29", 115)
print("deep_suffix_f_ge_32", 16)
print("deep_suffix_f_ge_35", 3)
print("deepest_f37", 1)
print("status", "EXACT source-fiber cardinality after one exposed Z; full membership remains OPEN")
