#!/usr/bin/env python3
"""Exact critical-cut product factorization for A0 s=1 Route-B.

For alpha=log_3(2), let f(n)=floor(alpha*n).  Suppose a word W has

    base_min = 0,
    critical_prefix = c,

and split it at that critical prefix:

    W = U V,   |U|=c,   |V|=s.

Then the ballot language factors exactly:

LEFT (reverse-low):
    q(U)=f(c), and every suffix S of U satisfies
        q(S) <= f(|S|).

RIGHT (strict-high):
    every nonempty prefix P of V satisfies
        q(P) >= f(|P|)+1.

Conversely, any concatenation satisfying those two conditions has
base_min=0 and critical_prefix=c.

For the actual long Christoffel root,

    h = 10,439,860,591
    q =  6,586,818,670
    c =  9,809,721,694
    s =    630,138,897

and exact floor arithmetic gives

    f(c) = 6,189,245,290,
    q(V) = 397,573,380 = f(s)+1.

So the right factor is exactly the same strict-high ballot language that was
previously treated as the `critical=None` threshold/dominance sector.

The correction composition

    C(UV)=3^q(V) C(U) + 2^|U| C(V)

then yields a matching dual-adic product factorization.  For two candidates
with the same split lengths and one-counts, whenever K<=|U| and L<=q(V):

    C(UV) == C(U*V*) mod 2^K 3^L

iff simultaneously

    C(U) == C(U*) mod 2^K,
    C(V) == C(V*) mod 3^L.

Thus the critical cut is simultaneously a ballot-family product cut and a
left/right correction-observation cut.

Scope:
  * critical-cut ballot product: CLOSED;
  * dual-adic collision product at supported resolutions: CLOSED;
  * recursive closure of each huge factor: OPEN;
  * Collatz conjecture: OPEN.
"""

from fractions import Fraction
from functools import lru_cache

MAX_DEPTH = 10

ROOT_H = 10_439_860_591
ROOT_Q = 6_586_818_670
ROOT_C = 9_809_721_694


def log_bounds(z: Fraction, n: int = 100):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * z ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * z ** (2 * n + 3) / ((2 * n + 3) * (1 - z * z))
    return s, s + tail


L2, U2 = log_bounds(Fraction(1, 3))
L3, U3 = log_bounds(Fraction(1, 2))
ALPHA_LO = L2 / U3
ALPHA_HI = U2 / L3


@lru_cache(None)
def floor_alpha(n: int) -> int:
    lo = n * ALPHA_LO
    hi = n * ALPHA_HI
    flo = lo.numerator // lo.denominator
    fhi = hi.numerator // hi.denominator
    assert flo == fhi
    return flo


def phase_carry(a: int, b: int) -> int:
    out = floor_alpha(a + b) - floor_alpha(a) - floor_alpha(b)
    assert out in (0, 1)
    return out


def frac_compare(a: int, b: int) -> int:
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


def ballot_summary(bits):
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
    return len(bits), q, base_min, critical


def left_reverse_low(bits) -> bool:
    c = len(bits)
    if sum(bits) != floor_alpha(c):
        return False
    suffix_ones = 0
    for v in range(1, c + 1):
        suffix_ones += bits[c - v]
        if suffix_ones > floor_alpha(v):
            return False
    return True


def right_strict_high(bits) -> bool:
    q = 0
    for v, bit in enumerate(bits, 1):
        q += bit
        if q < floor_alpha(v) + 1:
            return False
    return True


def correction(bits) -> int:
    h = q = C = 0
    for bit in bits:
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return C


# ---------------------------------------------------------------------------
# 1. Exhaustive ballot product equivalence.
# ---------------------------------------------------------------------------

ballot_product_checks = 0
for h in range(2, MAX_DEPTH + 1):
    for mask in range(1 << h):
        bits = tuple((mask >> i) & 1 for i in range(h))
        _, _, base_min, critical = ballot_summary(bits)

        for c in range(1, h):
            product = left_reverse_low(bits[:c]) and right_strict_high(bits[c:])
            direct = base_min == 0 and critical == c
            assert product == direct
            ballot_product_checks += 1


# ---------------------------------------------------------------------------
# 2. Root arithmetic at the actual Christoffel critical cut.
# ---------------------------------------------------------------------------

ROOT_S = ROOT_H - ROOT_C
ROOT_LEFT_Q = floor_alpha(ROOT_C)
ROOT_RIGHT_Q = ROOT_Q - ROOT_LEFT_Q

assert floor_alpha(ROOT_H) == ROOT_Q
assert ROOT_S == 630_138_897
assert ROOT_LEFT_Q == 6_189_245_290
assert floor_alpha(ROOT_S) == 397_573_379
assert ROOT_RIGHT_Q == 397_573_380
assert ROOT_RIGHT_Q == floor_alpha(ROOT_S) + 1
assert phase_carry(ROOT_C, ROOT_S) == 1


# ---------------------------------------------------------------------------
# 3. Exact dual-adic product factorization regression.
# ---------------------------------------------------------------------------

collision_product_checks = 0

# Exhaust over small left/right blocks, comparing pairs with equal component
# one-counts.  This is an implementation regression for the algebraic identity.
for c in range(1, 5):
    for s in range(1, 5):
        left_words = [tuple((m >> i) & 1 for i in range(c)) for m in range(1 << c)]
        right_words = [tuple((m >> i) & 1 for i in range(s)) for m in range(1 << s)]

        for U0 in left_words:
            for U1 in left_words:
                if sum(U0) != sum(U1):
                    continue
            
                for V0 in right_words:
                    for V1 in right_words:
                        qv = sum(V0)
                        if qv != sum(V1) or qv == 0:
                            continue

                        W0 = U0 + V0
                        W1 = U1 + V1
                        C0 = correction(W0)
                        C1 = correction(W1)
                        CU0 = correction(U0)
                        CU1 = correction(U1)
                        CV0 = correction(V0)
                        CV1 = correction(V1)

                        for K in range(1, c + 1):
                            for L in range(1, qv + 1):
                                full = (C0 - C1) % ((1 << K) * (3 ** L)) == 0
                                left = (CU0 - CU1) % (1 << K) == 0
                                right = (CV0 - CV1) % (3 ** L) == 0
                                assert full == (left and right)
                                collision_product_checks += 1


print("PASS A0 s=1 Route-B critical-cut product factorization certificate")
print("ballot_product_checks", ballot_product_checks)
print("collision_product_checks", collision_product_checks)
print("root_h", ROOT_H)
print("root_q", ROOT_Q)
print("root_critical", ROOT_C)
print("root_right_length", ROOT_S)
print("root_left_ones", ROOT_LEFT_Q)
print("root_right_ones", ROOT_RIGHT_Q)
print(
    "ballot_product",
    "critical=c iff left is reverse-low with q=f(c) and right is strict-high",
)
print(
    "dual_adic_product",
    "for K<=c and L<=q(V), full bridge collision iff left dyadic and right ternary collisions both hold",
)
print(
    "formation_audit",
    "the critical coordinate is used as an intrinsic formation cut rather than merely as a stored absolute index",
)
print(
    "axis_audit",
    "left dyadic and right ternary observations factor on the same critical cut as the ballot language",
)
print(
    "dsd_audit",
    "factorization is exact; recursive closure of the two factors is not inferred",
)
print(
    "status",
    "critical-cut family-cover/product lemma CLOSED; factor recursion remains OPEN",
)
