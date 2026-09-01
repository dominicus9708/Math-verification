#!/usr/bin/env python3
"""Exact two-front middle-invisibility theorem for A0 s=1 Route-B.

For an ordinary binary Collatz parity word W define

    C(W) by 2^h T^h(x) = 3^q x + C(W),

and boundary projections

    S_K(W) = -C(W) * 3^{-q(W)} mod 2^K,
    E_L(W) =  C(W) * 2^{-h(W)} mod 3^L.

For any decomposition W = U M V,

    |U| >= K  => S_K(W) = S_K(U),
    q(V) >= L => E_L(W) = E_L(V).

Hence when both capacities hold, the complete middle block M is invisible to
both boundary coordinates.  This is a necessary-boundary localization result,
not correction-language membership.
"""

from itertools import product


def meta(word):
    C = 0
    q = 0
    for h, bit in enumerate(word):
        if bit:
            C = 3 * C + (1 << h)
            q += 1
    return len(word), q, C


def compose(U, V):
    hU, qU, CU = meta(U)
    hV, qV, CV = meta(V)
    return hU + hV, qU + qV, (3 ** qV) * CU + (1 << hU) * CV


def start(word, K):
    h, q, C = meta(word)
    assert 1 <= K <= h
    mod = 1 << K
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod


def end(word, L):
    h, q, C = meta(word)
    assert 1 <= L <= q
    mod = 3 ** L
    return (C * pow(pow(2, h, mod), -1, mod)) % mod


# Composition identity guard.
composition_checks = 0
for a in range(0, 5):
    for b in range(0, 5):
        for U in product((0, 1), repeat=a):
            for V in product((0, 1), repeat=b):
                assert meta(U + V) == compose(U, V)
                composition_checks += 1

# Exhaustive small two-front localization regression.
# The algebraic proof is independent of these finite checks.
left_checks = 0
right_checks = 0
two_front_checks = 0
for a in range(1, 5):
    for mlen in range(0, 5):
        for c in range(1, 5):
            for U in product((0, 1), repeat=a):
                for M in product((0, 1), repeat=mlen):
                    for V in product((0, 1), repeat=c):
                        W = U + M + V
                        for K in range(1, a + 1):
                            assert start(W, K) == start(U, K)
                            left_checks += 1

                        qV = sum(V)
                        for L in range(1, qV + 1):
                            assert end(W, L) == end(V, L)
                            right_checks += 1

                        if qV:
                            for K in range(1, a + 1):
                                for L in range(1, qV + 1):
                                    assert (
                                        start(W, K), end(W, L)
                                    ) == (
                                        start(U, K), end(V, L)
                                    )
                                    two_front_checks += 1

print("PASS A0 s=1 Route-B two-front middle-invisibility certificate")
print("composition_checks", composition_checks)
print("left_localization_checks", left_checks)
print("right_localization_checks", right_checks)
print("two_front_checks", two_front_checks)
print("exact_left", "|U|>=K => S_K(UMV)=S_K(U)")
print("exact_right", "q(V)>=L => E_L(UMV)=E_L(V)")
print("scope", "middle is invisible only to these two boundary predicates; long correction-language membership remains open")
