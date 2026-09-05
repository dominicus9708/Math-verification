#!/usr/bin/env python3
"""Exact fixed-resolution family DP on the canonical H/L grammar.

Fix a modulus

    M = 2^K 3^L

(or any positive integer).  For each length h define the bidirectional
correction-residue sets

    S_H(h;M) = {(C(W), C(reverse(W))) mod M : W in H_h},
    S_L(h;M) = {(C(W), C(reverse(W))) mod M : W in L_h}.

The exact canonical H/L grammar and the bidirectional correction composition
give recursive equations for these sets using only smaller lengths.

H recurrence.
For every canonical cut c with

    f(c)=f(c-1),
    s=h-c,
    s=0 or phase_carry(c,s)=1,

choose X in L_{c-1} and, if s>0, V in H_s.  Form

    U = 1 reverse(X),
    W = U V.

L recurrence.
For every canonical cut c with

    c=1 or f(c)=f(c-1)+1,
    s=h-c,
    s=0 or phase_carry(c,s)=0,

use U=0 when c=1; otherwise choose X in H_{c-1} and form

    U = 0 reverse(X).

Append V in L_s when s>0.

Because the grammar converse is exact, the resulting residue-set recurrences
are exact: no candidate is omitted and no illegal word is introduced.

STATE BOUND.
At a fixed length h, a bidirectional residue state is one ordered pair in
(Z/MZ)^2.  Therefore

    |S_H(h;M)| <= M^2,
    |S_L(h;M)| <= M^2.

Across all lengths 0<=h<=H the number of distinct typed DP states is at most

    2 (H+1) M^2.

Thus for every fixed observation modulus the H/L ballot families admit a
polynomial-size (indeed linear-in-H state-count) exact correction quotient,
independent of the exponentially or super-exponentially large number of words
represented by the families.

This does NOT make the adaptive/global problem polynomial when K,L themselves
grow with H; that scaling remains a separate gate.
"""

from fractions import Fraction
from functools import lru_cache

MAX_EXHAUSTIVE_H = 9
MODULI = (2, 3, 4, 6, 8, 9, 12, 27, 72)


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


def q_H(h: int) -> int:
    assert h >= 1
    return floor_alpha(h) + 1


def q_L(h: int) -> int:
    assert h >= 0
    return floor_alpha(h)


def correction(bits) -> int:
    h = q = C = 0
    for bit in bits:
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return C


def residue_pair(bits, M):
    return (
        correction(bits) % M,
        correction(tuple(reversed(bits))) % M,
    )


def compose_pair(a, b, h1, q1, h2, q2, M):
    return (
        (pow(3, q2, M) * a[0] + pow(2, h1, M) * b[0]) % M,
        (pow(3, q1, M) * b[1] + pow(2, h2, M) * a[1]) % M,
    )


def primitive_H_pair(x, hx, qx, M):
    return (
        (pow(3, qx, M) + 2 * x[1]) % M,
        (3 * x[0] + pow(2, hx, M)) % M,
    )


def primitive_L_pair(x, M):
    return ((2 * x[1]) % M, x[0] % M)


@lru_cache(None)
def S_H(h: int, M: int):
    assert h >= 1
    out = set()
    for c in range(1, h + 1):
        if floor_alpha(c) != floor_alpha(c - 1):
            continue
        s = h - c
        if s and phase_carry(c, s) != 1:
            continue

        X_states = S_L(c - 1, M)
        V_states = S_H(s, M) if s else frozenset({(0, 0)})
        for x in X_states:
            U = primitive_H_pair(x, c - 1, q_L(c - 1), M)
            for v in V_states:
                out.add(
                    compose_pair(
                        U,
                        v,
                        c,
                        q_H(c),
                        s,
                        q_H(s) if s else 0,
                        M,
                    )
                )
    return frozenset(out)


@lru_cache(None)
def S_L(h: int, M: int):
    assert h >= 0
    if h == 0:
        return frozenset({(0, 0)})

    out = set()
    for c in range(1, h + 1):
        if c > 1 and floor_alpha(c) != floor_alpha(c - 1) + 1:
            continue
        s = h - c
        if s and phase_carry(c, s) != 0:
            continue

        V_states = S_L(s, M) if s else frozenset({(0, 0)})

        if c == 1:
            U_states = ((0, 0),)  # word `0`
        else:
            U_states = tuple(
                primitive_L_pair(x, M) for x in S_H(c - 1, M)
            )

        for U in U_states:
            for v in V_states:
                out.add(
                    compose_pair(
                        U,
                        v,
                        c,
                        q_L(c),
                        s,
                        q_L(s),
                        M,
                    )
                )
    return frozenset(out)


def in_H(bits):
    if not bits:
        return False
    q = 0
    for u, bit in enumerate(bits, 1):
        q += bit
        if q < floor_alpha(u) + 1:
            return False
    return q == q_H(len(bits))


def in_L(bits):
    if not bits:
        return True
    q = 0
    for u, bit in enumerate(bits, 1):
        q += bit
        if q > floor_alpha(u):
            return False
    return q == q_L(len(bits))


def words_of_length(h):
    return tuple(
        tuple((mask >> i) & 1 for i in range(h))
        for mask in range(1 << h)
    )


# ---------------------------------------------------------------------------
# Exhaustive word-vs-family-DP regression.
# ---------------------------------------------------------------------------

H_set_checks = 0
L_set_checks = 0
state_bound_checks = 0

for M in MODULI:
    for h in range(1, MAX_EXHAUSTIVE_H + 1):
        words = words_of_length(h)
        exact_H = {residue_pair(W, M) for W in words if in_H(W)}
        exact_L = {residue_pair(W, M) for W in words if in_L(W)}

        assert exact_H == set(S_H(h, M))
        assert exact_L == set(S_L(h, M))
        H_set_checks += 1
        L_set_checks += 1

        assert len(S_H(h, M)) <= M * M
        assert len(S_L(h, M)) <= M * M
        state_bound_checks += 2

    assert S_L(0, M) == frozenset({(0, 0)})


print("PASS A0 s=1 Route-B H/L fixed-resolution family DP certificate")
print("max_exhaustive_h", MAX_EXHAUSTIVE_H)
print("moduli", MODULI)
print("H_set_checks", H_set_checks)
print("L_set_checks", L_set_checks)
print("state_bound_checks", state_bound_checks)
print(
    "per_length_bound",
    "|S_H(h;M)|, |S_L(h;M)| <= M^2",
)
print(
    "horizon_state_bound",
    "typed correction-pair DP states through H <= 2*(H+1)*M^2",
)
print(
    "formation_audit",
    "every state is generated through the exact canonical grammar converse; no Christoffel assumption is used for arbitrary H/L members",
)
print(
    "dsd_audit",
    "fixed-resolution polynomial state count is separated from the still-open question of how K,L must scale with horizon",
)
print(
    "status",
    "fixed-resolution H/L correction family quotient CLOSED; adaptive-resolution globalization remains OPEN",
)
