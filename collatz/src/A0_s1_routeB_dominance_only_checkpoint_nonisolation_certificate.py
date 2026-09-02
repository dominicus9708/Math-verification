#!/usr/bin/env python3
"""Exact audit certificate: dominance-only right-H acceptance cannot isolate Z.

The terminal-28 dominance saturation theorem reduces the complete right-H
H-language existence condition to

    Z mod 3 in {1,2}.

Suppose a dyadic checkpoint observation also fixes

    Z == z2 (mod 2^27).

By CRT these two accepted ternary classes become exactly two residue classes
modulo

    Mweak = 3*2^27.

For one fixed source value X, the independent debit corridor

    75*2^33 < 3X-Z < 112*2^33

is equivalent to the open checkpoint interval

    3X-112*2^33 < Z < 3X-75*2^33,

of exact real width

    W = 37*2^33.

Since

    W = 789*Mweak + 2^27,

an open interval of this integer-endpoint width contains at least 789 integers
from EVERY residue class modulo Mweak.  Consequently the two dominance-accepted
classes contain at least 1578 checkpoint integers before intersection with any
additional global/checkpoint condition.

Thus dominance-only right-H existence plus one 27-bit dyadic residue is not a
checkpoint-singleton mechanism.  The earlier 2^27*3^28 singleton seam remains
valid when a FULL z_H mod 3^28 observation is supplied, but dominance existence
alone does not supply that observation.

This is a method/audit theorem, not a claim that all of these checkpoints meet
the global SAFE Z corridor or the long correction-language/source-control
constraints.
"""

G = 1 << 33
M2 = 1 << 27
MWEAK = 3 * M2
W = 37 * G

assert MWEAK == 402_653_184
assert W == 317_827_579_904
q, r = divmod(W, MWEAK)
assert (q, r) == (789, 134_217_728)
assert r == M2


def count_open_residue(A: int, B: int, residue: int, modulus: int) -> int:
    """Count integers z with A<z<B and z=residue mod modulus."""
    assert A < B and modulus > 0
    residue %= modulus
    lo = A + 1
    hi = B - 1
    if lo > hi:
        return 0
    first = lo + ((residue - lo) % modulus)
    if first > hi:
        return 0
    return (hi - first) // modulus + 1


# Generic phase regression over one full modulus of possible interval starts.
# Translation reduces all phases to A mod MWEAK.  Each residue class must occur
# at least q times because W=q*MWEAK+r with r>0 and endpoints are excluded.
phase_checks = 0
for phase in range(0, MWEAK, 1_048_576):
    A = phase
    B = A + W
    for residue in (0, 1, M2 - 1, M2, MWEAK - 1):
        n = count_open_residue(A, B, residue, MWEAK)
        assert n in {789, 790}
        phase_checks += 1

# Exact CRT: for every z2 there are two distinct accepted classes modulo
# 3*2^27, corresponding to Z mod3=1 and 2.
def crt_class_mod3_m2(z2: int, z3: int) -> int:
    z2 %= M2
    z3 %= 3
    # M2=2^27 == 2 mod3, whose inverse mod3 is 2.
    k = ((z3 - z2) * 2) % 3
    out = z2 + M2 * k
    assert out % M2 == z2
    assert out % 3 == z3
    assert 0 <= out < MWEAK
    return out

crt_checks = 0
for z2 in (0, 1, 2, M2 // 2, M2 - 1):
    c1 = crt_class_mod3_m2(z2, 1)
    c2 = crt_class_mod3_m2(z2, 2)
    assert c1 != c2
    # Any debit interval of width W contains at least 789 points from each.
    for phase in (0, 1, MWEAK - 1, 123_456_789):
        A = phase
        B = A + W
        n1 = count_open_residue(A, B, c1, MWEAK)
        n2 = count_open_residue(A, B, c2, MWEAK)
        assert n1 >= 789 and n2 >= 789
        assert n1 + n2 >= 1_578
        crt_checks += 1

print("PASS A0 s=1 dominance-only checkpoint non-isolation certificate")
print("weak_modulus", MWEAK)
print("debit_checkpoint_interval_width", W)
print("full_weak_periods", q)
print("width_remainder", r)
print("minimum_per_accepted_residue_class", 789)
print("minimum_two_class_candidates_before_other_constraints", 1578)
print("phase_checks", phase_checks)
print("crt_checks", crt_checks)
print(
    "audit_conclusion",
    "dominance-only right-H existence plus Z mod 2^27 cannot expose a unique checkpoint; full z_H or a stronger source/control membership predicate is required",
)
print(
    "scope",
    "candidate counts are before global SAFE-Z and long correction-language/source-control intersections",
)
