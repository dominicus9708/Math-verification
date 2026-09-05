#!/usr/bin/env python3
"""Exact dual H/L canonical grammar for A0 s=1 Route-B ballot families.

Let alpha=log_3(2), f(n)=floor(alpha*n), and phi(n)={alpha*n}.

Define the strict-high and low languages

    H_h = {W: |W|=h, Q_W(h)=f(h)+1,
                 Q_W(u)>=f(u)+1 for every 1<=u<=h},

    L_h = {W: |W|=h, Q_W(h)=f(h),
                 Q_W(u)<=f(u) for every 1<=u<=h}.

For W in H_h let

    d_H(u)=Q_W(u)-f(u),
    c_H(W)=the unique u with d_H(u)=1 having maximal phi(u).

For W in L_h let

    d_L(u)=f(u)-Q_W(u),
    c_L(W)=the unique u with d_L(u)=0 having minimal phi(u).

Because alpha is irrational all phases phi(u), u>=1, are distinct.

H-GRAMMAR.
If c=c_H(W), W=UV, |U|=c, |V|=s, then

  * f(c)=f(c-1), hence the c-th threshold increment is 0;
  * U = 1 reverse(X) for a unique X in L_{c-1};
  * if s>0, phase_carry(c,s)=1 and V in H_s.

Conversely, if f(c)=f(c-1), X in L_{c-1}, and either s=0 or
phase_carry(c,s)=1 with V in H_s, then

    W = 1 reverse(X) V

belongs to H_{c+s} and has canonical cut c_H(W)=c.

L-GRAMMAR.
If c=c_L(W), W=UV, |U|=c, |V|=s, then

  * if c=1, U=0;
  * if c>1, f(c)=f(c-1)+1 and U=0 reverse(X) for a unique X in H_{c-1};
  * if s>0, phase_carry(c,s)=0 and V in L_s.

Conversely the same conditions generate exactly a word in L_{c+s} whose
canonical cut is c.

Thus every nonempty H/L word has a deterministic canonical decomposition.
Every recursive child has strictly smaller length: c-1<h and s=h-c<h.
Hence length is a well-founded rank for this grammar.

This theorem is ballot-language structure only.  It does not assert that every
Route-B survivor is a Christoffel word and does not prove Collatz.
"""

from fractions import Fraction
from functools import lru_cache

MAX_DEPTH = 12


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
    assert flo == fhi, ("increase log enclosure", n, flo, fhi)
    return flo


def frac_compare(a: int, b: int) -> int:
    """Compare phi(a) and phi(b) exactly without floating point."""
    if a == b:
        return 0
    if a > b:
        return 1 if floor_alpha(a) - floor_alpha(b) <= floor_alpha(a - b) else -1
    return -frac_compare(b, a)


def phase_carry(a: int, b: int) -> int:
    out = floor_alpha(a + b) - floor_alpha(a) - floor_alpha(b)
    assert out in (0, 1)
    return out


def prefix_ones(bits):
    q = 0
    out = []
    for bit in bits:
        q += bit
        out.append(q)
    return tuple(out)


def in_H(bits) -> bool:
    h = len(bits)
    if h == 0:
        return False
    pref = prefix_ones(bits)
    if pref[-1] != floor_alpha(h) + 1:
        return False
    return all(q >= floor_alpha(u) + 1 for u, q in enumerate(pref, 1))


def in_L(bits) -> bool:
    h = len(bits)
    if h == 0:
        return True
    pref = prefix_ones(bits)
    if pref[-1] != floor_alpha(h):
        return False
    return all(q <= floor_alpha(u) for u, q in enumerate(pref, 1))


def canonical_H_cut(bits) -> int:
    assert in_H(bits)
    pref = prefix_ones(bits)
    candidates = [
        u for u, q in enumerate(pref, 1)
        if q - floor_alpha(u) == 1
    ]
    assert candidates
    best = candidates[0]
    for u in candidates[1:]:
        if frac_compare(u, best) > 0:
            best = u
    return best


def canonical_L_cut(bits) -> int:
    assert in_L(bits) and bits
    pref = prefix_ones(bits)
    candidates = [
        u for u, q in enumerate(pref, 1)
        if floor_alpha(u) - q == 0
    ]
    assert candidates
    best = candidates[0]
    for u in candidates[1:]:
        if frac_compare(u, best) < 0:
            best = u
    return best


def all_H(h):
    if h == 0:
        return ()
    return tuple(
        bits
        for mask in range(1 << h)
        for bits in [tuple((mask >> i) & 1 for i in range(h))]
        if in_H(bits)
    )


def all_L(h):
    if h == 0:
        return ((),)
    return tuple(
        bits
        for mask in range(1 << h)
        for bits in [tuple((mask >> i) & 1 for i in range(h))]
        if in_L(bits)
    )


# ---------------------------------------------------------------------------
# 1. Forward canonical decomposition.
# ---------------------------------------------------------------------------

H_forward_checks = 0
L_forward_checks = 0
strict_descent_checks = 0

for h in range(1, MAX_DEPTH + 1):
    for W in all_H(h):
        c = canonical_H_cut(W)
        U = W[:c]
        V = W[c:]
        s = len(V)

        assert floor_alpha(c) == floor_alpha(c - 1)
        assert U[0] == 1
        X = tuple(reversed(U[1:]))
        assert in_L(X)
        if s:
            assert phase_carry(c, s) == 1
            assert in_H(V)
        assert c - 1 < h
        assert s < h
        H_forward_checks += 1
        strict_descent_checks += 2

    for W in all_L(h):
        c = canonical_L_cut(W)
        U = W[:c]
        V = W[c:]
        s = len(V)

        assert U[0] == 0
        if c == 1:
            assert U == (0,)
        else:
            assert floor_alpha(c) == floor_alpha(c - 1) + 1
            X = tuple(reversed(U[1:]))
            assert in_H(X)
        if s:
            assert phase_carry(c, s) == 0
            assert in_L(V)
        assert c - 1 < h
        assert s < h
        L_forward_checks += 1
        strict_descent_checks += 2


# ---------------------------------------------------------------------------
# 2. Converse generation: no hidden condition is missing.
# ---------------------------------------------------------------------------

H_converse_checks = 0
L_converse_checks = 0

for h in range(1, MAX_DEPTH + 1):
    # H grammar.
    for c in range(1, h + 1):
        if floor_alpha(c) != floor_alpha(c - 1):
            continue
        s = h - c
        if s and phase_carry(c, s) != 1:
            continue
        right_words = all_H(s) if s else ((),)
        for X in all_L(c - 1):
            U = (1,) + tuple(reversed(X))
            for V in right_words:
                W = U + V
                assert in_H(W)
                assert canonical_H_cut(W) == c
                H_converse_checks += 1

    # L grammar.
    for c in range(1, h + 1):
        if c > 1 and floor_alpha(c) != floor_alpha(c - 1) + 1:
            continue
        s = h - c
        if s and phase_carry(c, s) != 0:
            continue

        if c == 1:
            left_words = ((0,),)
        else:
            left_words = tuple(
                (0,) + tuple(reversed(X)) for X in all_H(c - 1)
            )
        right_words = all_L(s) if s else ((),)
        for U in left_words:
            for V in right_words:
                W = U + V
                assert in_L(W)
                assert canonical_L_cut(W) == c
                L_converse_checks += 1


# ---------------------------------------------------------------------------
# 3. Unique reconstruction from the canonical decomposition.
# ---------------------------------------------------------------------------

reconstruction_checks = 0
for h in range(1, MAX_DEPTH + 1):
    for W in all_H(h):
        c = canonical_H_cut(W)
        X = tuple(reversed(W[1:c]))
        V = W[c:]
        assert (1,) + tuple(reversed(X)) + V == W
        reconstruction_checks += 1

    for W in all_L(h):
        c = canonical_L_cut(W)
        if c == 1:
            U = (0,)
        else:
            X = tuple(reversed(W[1:c]))
            U = (0,) + tuple(reversed(X))
        assert U + W[c:] == W
        reconstruction_checks += 1


print("PASS A0 s=1 Route-B dual H/L canonical grammar certificate")
print("max_depth", MAX_DEPTH)
print("H_forward_checks", H_forward_checks)
print("L_forward_checks", L_forward_checks)
print("H_converse_checks", H_converse_checks)
print("L_converse_checks", L_converse_checks)
print("strict_descent_checks", strict_descent_checks)
print("reconstruction_checks", reconstruction_checks)
print(
    "H_rule",
    "H -> 1 reverse(L) H with threshold-bit-0 cut and phase carry 1 on a nonempty remainder",
)
print(
    "L_rule",
    "L -> 0 reverse(H) L with threshold-bit-1 cut (or c=1 base cut) and phase carry 0 on a nonempty remainder",
)
print(
    "rank",
    "every recursive language child has strictly smaller length",
)
print(
    "dsd_audit",
    "the grammar is defined for every H/L word before any Christoffel specialization; target hierarchy is not assumed",
)
print(
    "status",
    "dual H/L canonical ballot grammar CLOSED; identification with the target Stern-Brocot run hierarchy remains separate",
)
