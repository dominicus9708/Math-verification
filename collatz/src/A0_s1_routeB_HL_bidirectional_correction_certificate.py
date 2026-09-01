#!/usr/bin/env python3
"""Exact bidirectional correction state for the canonical H/L grammar.

For a binary word W let

    C+(W) = C(W),
    C-(W) = C(reverse(W)),

where C is the ordinary Route-B correction

    C(W)=sum_{r=1}^q 3^(q-r) 2^(a_r)

for one-positions a_1<...<a_q.

The reversal appearing in the canonical H/L grammar means C+ alone is not a
closed recursive coordinate.  The pair (C+,C-) is.

For W=UV:

    C+(UV)=3^q(V) C+(U) + 2^|U| C+(V),

    C-(UV)=3^q(U) C-(V) + 2^|V| C-(U).

For the H primitive block

    U_H = 1 reverse(X),

one has

    C+(U_H)=3^q(X) + 2 C-(X),
    C-(U_H)=3 C+(X) + 2^|X|.

For the L primitive block

    U_L = 0 reverse(X),

one has

    C+(U_L)=2 C-(X),
    C-(U_L)=C+(X).

Thus the exact state

    R(W)=(|W|, q(W), C+(W), C-(W))

is closed under concatenation, reversal-sensitive H/L primitive formation, and
therefore under the complete canonical H/L grammar.

At any fixed modulus M the same formulas hold after reducing C+, C-, and all
powers modulo M.  This supplies the correction arithmetic needed for a
family-DP over grammar nodes without materializing their bit strings.

Scope:
  * exact bidirectional correction arithmetic on the H/L grammar: CLOSED;
  * finite-modulus version: algebraically CLOSED;
  * polynomial/global bound on the number of reachable grammar states: OPEN;
  * Collatz: OPEN.
"""

MAX_DEPTH = 11


def correction(bits) -> int:
    h = q = C = 0
    for bit in bits:
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return C


def state(bits):
    return (
        len(bits),
        sum(bits),
        correction(bits),
        correction(tuple(reversed(bits))),
    )


def compose(a, b):
    h1, q1, Cp1, Cm1 = a
    h2, q2, Cp2, Cm2 = b
    return (
        h1 + h2,
        q1 + q2,
        (3 ** q2) * Cp1 + (1 << h1) * Cp2,
        (3 ** q1) * Cm2 + (1 << h2) * Cm1,
    )


def primitive_H(x_state):
    h, q, Cp, Cm = x_state
    return (
        h + 1,
        q + 1,
        (3 ** q) + 2 * Cm,
        3 * Cp + (1 << h),
    )


def primitive_L(x_state):
    h, q, Cp, Cm = x_state
    return (
        h + 1,
        q,
        2 * Cm,
        Cp,
    )


def primitive_H_word(X):
    return (1,) + tuple(reversed(X))


def primitive_L_word(X):
    return (0,) + tuple(reversed(X))


# ---------------------------------------------------------------------------
# 1. Exact concatenation / reversal composition.
# ---------------------------------------------------------------------------

composition_checks = 0
for n in range(MAX_DEPTH + 1):
    for mask in range(1 << n):
        W = tuple((mask >> i) & 1 for i in range(n))
        direct = state(W)
        for cut in range(n + 1):
            assert compose(state(W[:cut]), state(W[cut:])) == direct
            composition_checks += 1


# ---------------------------------------------------------------------------
# 2. Primitive H/L transformations.
# ---------------------------------------------------------------------------

H_primitive_checks = 0
L_primitive_checks = 0
for n in range(MAX_DEPTH + 1):
    for mask in range(1 << n):
        X = tuple((mask >> i) & 1 for i in range(n))
        sx = state(X)

        UH = primitive_H_word(X)
        UL = primitive_L_word(X)

        assert primitive_H(sx) == state(UH)
        assert primitive_L(sx) == state(UL)
        H_primitive_checks += 1
        L_primitive_checks += 1


# ---------------------------------------------------------------------------
# 3. Associativity of the bidirectional state composition.
# ---------------------------------------------------------------------------

associativity_checks = 0
for n in range(9):
    for mask in range(1 << n):
        W = tuple((mask >> i) & 1 for i in range(n))
        direct = state(W)
        for i in range(n + 1):
            for j in range(i, n + 1):
                a = state(W[:i])
                b = state(W[i:j])
                c = state(W[j:])
                assert compose(compose(a, b), c) == direct
                assert compose(a, compose(b, c)) == direct
                associativity_checks += 1


# ---------------------------------------------------------------------------
# 4. Fixed-modulus regression.
# ---------------------------------------------------------------------------

modular_checks = 0
for M in (2, 4, 8, 3, 9, 27, 72, 216):
    for n in range(8):
        for mask in range(1 << n):
            W = tuple((mask >> i) & 1 for i in range(n))
            h, q, Cp, Cm = state(W)
            for cut in range(n + 1):
                h2, q2, Cp2, Cm2 = compose(state(W[:cut]), state(W[cut:]))
                assert h2 == h and q2 == q
                assert Cp2 % M == Cp % M
                assert Cm2 % M == Cm % M
                modular_checks += 1


print("PASS A0 s=1 Route-B H/L bidirectional correction certificate")
print("state", "(|W|,q,C(W),C(reverse(W)))")
print("composition_checks", composition_checks)
print("H_primitive_checks", H_primitive_checks)
print("L_primitive_checks", L_primitive_checks)
print("associativity_checks", associativity_checks)
print("modular_checks", modular_checks)
print(
    "H_primitive",
    "C+=(3^q)+2*C-, C-=3*C+ + 2^h",
)
print(
    "L_primitive",
    "C+=2*C-, C-=C+",
)
print(
    "dsd_audit",
    "reversal is represented explicitly rather than silently assumed to preserve the ordinary correction coordinate",
)
print(
    "status",
    "exact grammar-wide correction arithmetic CLOSED; reachable-state growth / global family closure remains OPEN",
)
