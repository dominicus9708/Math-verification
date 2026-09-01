#!/usr/bin/env python3
"""Exact fixed-(h,q) correction-collision frontier theorem for Route-B.

For a word W with length h, one-count q and correction C(W), define

    S_K(W) = -C(W) 3^{-q} mod 2^K,
    E_L(W) =  C(W) 2^{-h} mod 3^L.

If W and T have the same (h,q), then

    C(W) == C(T) mod 2^K  <=>  S_K(W) == S_K(T),
    C(W) == C(T) mod 3^L  <=>  E_L(W) == E_L(T).

By CRT,

    C(W) == C(T) mod 2^K 3^L

iff both normalized boundary coordinates agree.

Combining this with the two-front localization theorem means that, for
same-(h,q) target-aware correction collision, a sufficiently long left
frontier and sufficiently one-rich right frontier decide the ENTIRE correction
collision predicate; the middle is invisible to this predicate.

This does not decide the ballot/critical target metadata or global Route-B
membership.
"""

from itertools import combinations, product


def meta(word):
    C = 0
    q = 0
    for i, bit in enumerate(word):
        if bit:
            C = 3 * C + (1 << i)
            q += 1
    return len(word), q, C


def start(word, K):
    h, q, C = meta(word)
    mod = 1 << K
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod


def end(word, L):
    h, q, C = meta(word)
    mod = 3 ** L
    return (C * pow(pow(2, h, mod), -1, mod)) % mod


def minimal_right_front(word, L):
    """Shortest suffix containing at least L ones; requires L>=1."""
    ones = 0
    for j in range(len(word) - 1, -1, -1):
        ones += word[j]
        if ones >= L:
            return word[j:]
    raise AssertionError("insufficient ones")


pair_checks = 0
frontier_checks = 0
for h in range(1, 8):
    words = list(product((0, 1), repeat=h))
    by_q = {}
    for W in words:
        by_q.setdefault(sum(W), []).append(W)

    for q, family in by_q.items():
        if len(family) < 2:
            continue
        for W, T in combinations(family, 2):
            CW = meta(W)[2]
            CT = meta(T)[2]
            for K in range(1, h + 1):
                dy_raw = (CW - CT) % (1 << K) == 0
                assert dy_raw == (start(W, K) == start(T, K))
                pair_checks += 1

                if q == 0:
                    continue
                for L in range(1, q + 1):
                    ter_raw = (CW - CT) % (3 ** L) == 0
                    assert ter_raw == (end(W, L) == end(T, L))

                    joint_raw = (CW - CT) % ((1 << K) * (3 ** L)) == 0
                    joint_boundary = (
                        start(W, K) == start(T, K)
                        and end(W, L) == end(T, L)
                    )
                    assert joint_raw == joint_boundary
                    pair_checks += 2

                    # Use the first K symbols as a legal left frontier and the
                    # shortest suffix with L ones as a legal right frontier.
                    UW, UT = W[:K], T[:K]
                    VW = minimal_right_front(W, L)
                    VT = minimal_right_front(T, L)
                    assert start(W, K) == start(UW, K)
                    assert start(T, K) == start(UT, K)
                    assert end(W, L) == end(VW, L)
                    assert end(T, L) == end(VT, L)
                    assert joint_raw == (
                        start(UW, K) == start(UT, K)
                        and end(VW, L) == end(VT, L)
                    )
                    frontier_checks += 1

print("PASS A0 s=1 Route-B fixed-(h,q) correction collision frontier certificate")
print("pair_checks", pair_checks)
print("frontier_checks", frontier_checks)
print("exact_equivalence", "same (h,q): raw C collision mod 2^K3^L iff normalized left/right boundary coordinates agree")
print("middle_invisibility", "after legal left/right frontiers, correction collision does not query the middle")
print("scope", "ballot/critical metadata and universal Route-B membership remain separate")
