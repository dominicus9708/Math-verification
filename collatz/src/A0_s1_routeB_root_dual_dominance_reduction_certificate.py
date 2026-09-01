#!/usr/bin/env python3
"""Exact target-root reduction to two prefix-dominance languages.

The target-specific H/L--Stern-Brocot alignment proves that the long root is
the lower characteristic/threshold word and that its critical cut c is the
record maximum of phi(u)={u log_3(2)} up to the root horizon.

At such a record-max cut c, floor carry across every split c=t+(c-t) is zero:

    f(c)=f(t)+f(c-t),  0<=t<=c.

Therefore the left reverse-low family

    X in L_c,   U=reverse(X)

is exactly the weak prefix-dominance family above the characteristic target

    U_* = TH_c,
    Q_U(t) >= Q_{U_*}(t)=f(t),
    Q_U(c)=f(c).

Conversely every such prefix-dominant U reverses to an L_c word.

The right factor has length s and is already the strict-high language H_s.
Its target is the unique characteristic strict-high word Hchar_s satisfying

    Q_{V_*}(t)=f(t)+1.

Thus H_s is exactly the prefix-dominance family above V_*.

For ANY equal-one-count prefix-dominance pair T,W, write target and candidate
one positions as

    a_1<...<a_q,
    b_1<...<b_q.

Prefix dominance is equivalent to b_r<=a_r for every r.  If W!=T and r0 is
the first shifted one, then

    v_2(C(T)-C(W)) = b_{r0},

which is exactly the first differing bit position.  Hence

    C(W)==C(T) mod 2^K

iff the first K bits of W and T are identical.

Combining this with the existing critical-cut dual-adic factorization gives a
fully target-relative description of the root collision family:

  * LEFT: prefix-dominance + literal/hierarchical prefix equality through K;
  * RIGHT: prefix-dominance + the already-certified ternary suffix-carry test
    through L.

No arbitrary candidate is assumed to be Christoffel.  Christoffel structure is
used only to identify the target characteristic scales.
"""

from fractions import Fraction
from functools import lru_cache

MAX_DEPTH = 11


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


def frac_compare(a: int, b: int):
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


def threshold_word(h):
    return tuple(floor_alpha(u + 1) - floor_alpha(u) for u in range(h))


def high_characteristic_word(h):
    assert h >= 1
    return (1,) + tuple(
        floor_alpha(u + 1) - floor_alpha(u)
        for u in range(1, h)
    )


def correction(bits):
    h = q = C = 0
    for bit in bits:
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return C


def prefix_dominates(W, T):
    if len(W) != len(T) or sum(W) != sum(T):
        return False
    qw = qt = 0
    for wb, tb in zip(W, T):
        qw += wb
        qt += tb
        if qw < qt:
            return False
    return True


def in_L(W):
    q = 0
    for u, bit in enumerate(W, 1):
        q += bit
        if q > floor_alpha(u):
            return False
    return q == floor_alpha(len(W))


def in_H(W):
    if not W:
        return False
    q = 0
    for u, bit in enumerate(W, 1):
        q += bit
        if q < floor_alpha(u) + 1:
            return False
    return q == floor_alpha(len(W)) + 1


def valuation(n, p):
    n = abs(n)
    assert n
    out = 0
    while n % p == 0:
        n //= p
        out += 1
    return out


def first_difference(W, T):
    for i, (a, b) in enumerate(zip(W, T)):
        if a != b:
            return i
    return None


def is_record_max(c, h):
    for u in range(1, h + 1):
        if u != c and frac_compare(c, u) <= 0:
            return False
    return True


left_dominance_checks = 0
right_dominance_checks = 0
dyadic_valuation_checks = 0
dyadic_collision_checks = 0

# Small exact analogues: whenever c is a phase record maximum, reverse(L_c)
# equals the weak dominance family above TH_c.
for c in range(1, MAX_DEPTH + 1):
    if not is_record_max(c, c):
        continue
    T = threshold_word(c)

    for mask in range(1 << c):
        U = tuple((mask >> i) & 1 for i in range(c))
        X = tuple(reversed(U))
        assert in_L(X) == prefix_dominates(U, T)
        left_dominance_checks += 1

        if prefix_dominates(U, T) and U != T:
            delta = correction(T) - correction(U)
            d = first_difference(U, T)
            assert d is not None
            assert valuation(delta, 2) == d
            dyadic_valuation_checks += 1
            for K in range(1, c + 1):
                same_mod = correction(U) % (1 << K) == correction(T) % (1 << K)
                same_prefix = U[:K] == T[:K]
                assert same_mod == same_prefix
                dyadic_collision_checks += 1

# H_h is exactly dominance above the unique high characteristic target.
for h in range(1, MAX_DEPTH + 1):
    T = high_characteristic_word(h)
    assert in_H(T)
    for mask in range(1 << h):
        W = tuple((mask >> i) & 1 for i in range(h))
        assert in_H(W) == prefix_dominates(W, T)
        right_dominance_checks += 1

        if in_H(W) and W != T:
            delta = correction(T) - correction(W)
            d = first_difference(W, T)
            assert d is not None
            assert valuation(delta, 2) == d
            dyadic_valuation_checks += 1


print("PASS A0 s=1 Route-B root dual-dominance reduction certificate")
print("max_depth", MAX_DEPTH)
print("left_dominance_checks", left_dominance_checks)
print("right_dominance_checks", right_dominance_checks)
print("dyadic_valuation_checks", dyadic_valuation_checks)
print("dyadic_collision_checks", dyadic_collision_checks)
print(
    "left",
    "reverse(L_c) at a record-max cut is exactly weak prefix dominance above TH_c",
)
print(
    "right",
    "H_s is exactly prefix dominance above the high characteristic target",
)
print(
    "dyadic",
    "inside either equal-count dominance family v2(target-candidate correction)=first differing bit index",
)
print(
    "dsd_audit",
    "target Christoffel structure identifies only the target/cut; arbitrary family members remain grammar-defined dominance words",
)
print(
    "status",
    "target critical-root collision problem reduced to left prefix equality + right ternary carry on two dominance families",
)
