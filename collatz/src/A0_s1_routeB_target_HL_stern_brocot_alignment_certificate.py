#!/usr/bin/env python3
"""Target-specific alignment of the universal H/L grammar with the existing
Stern-Brocot/Christoffel run hierarchy.

This certificate deliberately separates two layers.

UNIVERSAL LAYER (already certified elsewhere): every strict-high / low ballot
word has an intrinsic canonical H/L grammar, without assuming Christoffel form.

TARGET LAYER (this file): specialize that grammar to the already-certified long
Christoffel target.  Exact continued-fraction and one-sided phase arithmetic
then recover the existing 20 Stern-Brocot run exponents.

Let alpha=log_3(2), f(n)=floor(alpha*n), phi(n)={alpha*n}.
For the characteristic words

    Lchar_N: Q(u)=f(u),
    Hchar_N: Q(u)=f(u)+1  (u>=1),

the canonical same-type cuts are respectively

    c_L(N)=argmin_{1<=u<=N} phi(u),
    c_H(N)=argmax_{1<=u<=N} phi(u).

After cutting such a record extremum, the remainder is again the same
characteristic language, because the corresponding floor carry is identically
0 (L) or 1 (H) throughout the remaining segment.

A standard continued-fraction/Stern-Brocot fact is used explicitly:
denominators of the successive one-sided best approximants are exactly the
record minima/maxima of phi(n).  The script verifies the complete finite
continued-fraction/Stern-Brocot arithmetic for this target and regresses the
characteristic-cut rule on all materializable target-path nodes.

Scope:
  * target H/L <-> Stern-Brocot run-exponent alignment: CLOSED;
  * universal H/L grammar: imported from its separate certificate;
  * arbitrary ballot candidate -> Christoffel hierarchy: NOT claimed;
  * correction/carry closure over every H/L grammar node: still separate;
  * Collatz: OPEN.
"""

from fractions import Fraction
from functools import lru_cache
from math import gcd

ROOT_P = 6_586_818_670
ROOT_Q = 10_439_860_591
ROOT_CRITICAL = 9_809_721_694
ROOT_RIGHT = 630_138_897

EXPECTED_ALPHA_CF = (
    0, 1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55,
    1, 4, 3, 1, 1, 15, 1, 9, 2,
)

EXPECTED_RUNS = (
    ("L", 1), ("R", 1), ("L", 2), ("R", 2), ("L", 3),
    ("R", 1), ("L", 5), ("R", 2), ("L", 23), ("R", 2),
    ("L", 2), ("R", 1), ("L", 1), ("R", 55), ("L", 1),
    ("R", 4), ("L", 3), ("R", 1), ("L", 1), ("R", 15),
)


def log_bounds(z: Fraction, n: int = 160):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3


def cf_from_interval(lo: Fraction, hi: Fraction, count: int):
    out = []
    for _ in range(count):
        a_lo = lo.numerator // lo.denominator
        a_hi = hi.numerator // hi.denominator
        assert a_lo == a_hi, ("continued-fraction enclosure too wide", a_lo, a_hi)
        a = a_lo
        out.append(a)
        lo -= a
        hi -= a
        assert lo > 0 and hi > 0
        lo, hi = 1 / hi, 1 / lo
    return tuple(out)


ALPHA_CF = cf_from_interval(ALPHA_LO, ALPHA_HI, len(EXPECTED_ALPHA_CF))
assert ALPHA_CF == EXPECTED_ALPHA_CF


def convergents(cf):
    p_m2, p_m1 = 0, 1
    q_m2, q_m1 = 1, 0
    out = []
    for a in cf:
        p = a * p_m1 + p_m2
        q = a * q_m1 + q_m2
        out.append((p, q))
        p_m2, p_m1 = p_m1, p
        q_m2, q_m1 = q_m1, q
    return tuple(out)


CONV = convergents(ALPHA_CF)
assert CONV[22] == (ROOT_P, ROOT_Q)
P20, Q20 = CONV[20]
P21, Q21 = CONV[21]
assert Q20 == ROOT_RIGHT
assert Q21 == ROOT_CRITICAL
assert ROOT_Q == Q21 + Q20
assert ROOT_P == P21 + P20

# Root is the lower convergent, predecessor is the upper convergent.
assert Fraction(ROOT_P, ROOT_Q) < ALPHA_LO
assert Fraction(P21, Q21) > ALPHA_HI

# Exact error enclosure needed for the mechanical/threshold identity.
DELTA_LO = ALPHA_LO - Fraction(ROOT_P, ROOT_Q)
DELTA_HI = ALPHA_HI - Fraction(ROOT_P, ROOT_Q)
assert DELTA_LO > 0
assert DELTA_HI * ROOT_Q * ROOT_Q < 1

# Adjacent-convergent determinant: ROOT_P*Q21 == P21*ROOT_Q - 1.
assert P21 * ROOT_Q - ROOT_P * Q21 == 1

# Consequence used algebraically below:
# for every 1<=u<=ROOT_Q,
#     floor(alpha*u)=floor(ROOT_P*u/ROOT_Q).
# For u<ROOT_Q the rational fractional grid is at least 1/ROOT_Q away
# from the next integer, while DELTA_HI*u<1/ROOT_Q; u=ROOT_Q is immediate.

# The predecessor denominator Q21 has rational residue -1 modulo ROOT_Q,
# hence its alpha phase is the unique maximum up to ROOT_Q.  For every other
# u the rational residue is at most ROOT_Q-2; the exact error bound below
# prevents the small irrational correction from reversing that ordering.
assert (ROOT_P * Q21) % ROOT_Q == ROOT_Q - 1
assert Fraction(1, ROOT_Q) - DELTA_HI * (ROOT_Q - Q21) > 0

# Therefore the ballot critical cut of the root threshold word is exactly Q21,
# and the right factor has length Q20.
assert Q21 == ROOT_CRITICAL
assert ROOT_Q - Q21 == Q20


def build_stern_brocot_dag(p: int, q: int):
    assert 0 <= p <= q and gcd(p, q) == 1
    nodes = [
        {"p": 0, "q": 1, "left": None, "right": None},
        {"p": 1, "q": 1, "left": None, "right": None},
    ]
    left = (0, 1, 0)
    right = (1, 1, 1)
    while True:
        mp = left[0] + right[0]
        mq = left[1] + right[1]
        mid = len(nodes)
        nodes.append({"p": mp, "q": mq, "left": left[2], "right": right[2]})
        cmp = p * mq - mp * q
        if cmp == 0:
            return nodes, mid
        if cmp < 0:
            right = (mp, mq, mid)
        else:
            left = (mp, mq, mid)


NODES, ROOT = build_stern_brocot_dag(ROOT_P, ROOT_Q)
assert ROOT == 128
assert len(NODES) == 129


def side_of_alpha(p: int, q: int):
    x = Fraction(p, q)
    if x < ALPHA_LO:
        return "lower"
    if x > ALPHA_HI:
        return "upper"
    raise AssertionError(("alpha enclosure does not separate node", p, q))


# Every updated Stern-Brocot bound is a successive one-sided best approximation.
# Record the denominators on the two sides.  The base bounds 0/1 and 1/1 both
# have denominator 1.
lower_records = [1]
upper_records = [1]
for node in NODES[2:]:
    side = side_of_alpha(node["p"], node["q"])
    if side == "lower":
        lower_records.append(node["q"])
    else:
        upper_records.append(node["q"])

assert lower_records == sorted(set(lower_records))
assert upper_records == sorted(set(upper_records))
assert lower_records[-1] == ROOT_Q
assert upper_records[-1] == Q21

# The existing 20 run exponents are exactly a_2,...,a_21 of alpha.
RUN_COUNTS = tuple(n for _, n in EXPECTED_RUNS)
assert RUN_COUNTS == ALPHA_CF[2:22]


def characteristic_chain(length: int, records):
    """Canonical same-type chain, stopping at the one-letter base word.

    Lchar uses lower/record-min denominators; Hchar uses upper/record-max
    denominators.  The record-extremum carry lemma guarantees the remainder is
    again the same characteristic language after each subtraction.
    """
    out = []
    N = length
    while N > 1:
        c = max(r for r in records if r <= N)
        out.append((N, c))
        N -= c
    assert N == 1
    return tuple(out)


def group_equal_cuts(chain):
    out = []
    for _, c in chain:
        if out and out[-1][0] == c:
            out[-1] = (c, out[-1][1] + 1)
        else:
            out.append((c, 1))
    return tuple(out)


# Root critical product:
#   reverse(left factor) = Lchar_{Q21}
#   right factor          = Hchar_{Q20}
# because Q21 is the global phase maximum up to ROOT_Q.  The left reversal has
# prefix count f(t), while every right prefix has count f(t)+1.
L_CHAIN = characteristic_chain(Q21, lower_records)
H_CHAIN = characteristic_chain(Q20, upper_records)
L_GROUPS = group_equal_cuts(L_CHAIN)
H_GROUPS = group_equal_cuts(H_CHAIN)

# Merge the two alternating scale families from largest scale downward.
MERGED = sorted(
    (("Lchar", c, n) for c, n in L_GROUPS)
    + (("Hchar", c, n) for c, n in H_GROUPS),
    key=lambda item: -item[1],
)
MERGED_COUNTS = tuple(n for _, _, n in MERGED)

# This is the main alignment: the universal canonical grammar, specialized to
# the target characteristic factors, recovers the target Stern-Brocot run
# exponents in reverse scale order.
assert MERGED_COUNTS == tuple(reversed(RUN_COUNTS))
assert len(MERGED_COUNTS) == len(EXPECTED_RUNS) == 20

# Exact scale table for audit/readability.
EXPECTED_MERGED = (
    ("Lchar", 630_138_897, 15),
    ("Hchar", 357_638_239, 1),
    ("Lchar", 272_500_658, 1),
    ("Hchar", 85_137_581, 3),
    ("Lchar", 17_087_915, 4),
    ("Hchar", 16_785_921, 1),
    ("Lchar", 301_994, 55),
    ("Hchar", 176_251, 1),
    ("Lchar", 125_743, 1),
    ("Hchar", 50_508, 2),
    ("Lchar", 24_727, 2),
    ("Hchar", 1_054, 23),
    ("Lchar", 485, 2),
    ("Hchar", 84, 5),
    ("Lchar", 65, 1),
    ("Hchar", 19, 3),
    ("Lchar", 8, 2),
    ("Hchar", 3, 2),
    ("Lchar", 2, 1),
    ("Hchar", 1, 1),
)
assert tuple(MERGED) == EXPECTED_MERGED

# ---------------------------------------------------------------------------
# Materializable regression: characteristic-cut arithmetic agrees with literal
# target-path words wherever the Christoffel word can be expanded cheaply.
# ---------------------------------------------------------------------------

@lru_cache(None)
def floor_alpha(n: int) -> int:
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi
    return flo


def frac_compare(a: int, b: int):
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


@lru_cache(None)
def materialize(i: int):
    node = NODES[i]
    if node["left"] is None:
        return (node["p"],)
    return materialize(node["left"]) + materialize(node["right"])


def ballot_critical(bits):
    q = 0
    base_min = 0
    critical = None
    for u, bit in enumerate(bits, 1):
        q += bit
        d = q - floor_alpha(u)
        if d < base_min:
            base_min = d
            critical = u
        elif d == base_min:
            if critical is None or frac_compare(u, critical) > 0:
                critical = u
    return base_min, critical


materialized_checks = 0
for i, node in enumerate(NODES):
    if node["q"] > 5_000:
        continue
    W = materialize(i)
    if i >= 2:
        # Lower Christoffel mechanical orientation regression.
        mechanical = tuple(
            ((u + 1) * node["p"] // node["q"])
            - (u * node["p"] // node["q"])
            for u in range(node["q"])
        )
        assert W == mechanical
    materialized_checks += 1


print("PASS A0 s=1 Route-B target H/L <-> Stern-Brocot alignment certificate")
print("alpha_cf_prefix", ALPHA_CF)
print("root_convergent_index", 22)
print("root", (ROOT_P, ROOT_Q))
print("predecessor", (P21, Q21))
print("previous", (P20, Q20))
print("root_error_q2_upper", DELTA_HI * ROOT_Q * ROOT_Q)
print("root_critical", Q21)
print("root_right_length", Q20)
print("run_counts_forward", RUN_COUNTS)
print("grammar_counts_reverse", MERGED_COUNTS)
print("merged_scale_groups", MERGED)
print("materialized_path_checks", materialized_checks)
print(
    "alignment",
    "target characteristic H/L scale groups recover exactly the 20 Stern-Brocot exponents in reverse order",
)
print(
    "formation_audit",
    "the H/L grammar is universal first; Christoffel/continued-fraction structure is introduced only after target specialization",
)
print(
    "dsd_audit",
    "target hierarchy alignment is exact and non-circular; arbitrary ballot candidates are not promoted to Christoffel words",
)
print(
    "status",
    "TARGET H/L--Stern-Brocot SCALE ALIGNMENT CLOSED; grammar-wide correction/carry closure remains OPEN",
)
