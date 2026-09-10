#!/usr/bin/env python3
"""
MATH-054 single-rational S bridge certificate.

Finite exact regression certificate. Collatz remains OPEN.

For a length-k shortcut parity word w with q odd steps and correction C,

    T_w^k(N) = (3^q N + C)/2^k.

Define the exact rational normalized correction

    S(w) = C / 3^q  in Z[1/3].

Then three structures used separately in the proof search are projections of
this same exact rational object:

1. real correction / endpoint:
       T_w^k(N) = (3^q/2^k) * (N + S);

2. dyadic root address:
       N(w) == -S(w) (mod 2^k),
   where odd denominators are inverted modulo 2^k;

3. exact Hensel class at fixed q:
       C(F) == C(E) (mod 3^q)
       iff S(F)-S(E) is an integer.

If S(F)=S(E)+m with integer m, then the canonical roots satisfy
       N(F) == N(E)-m (mod 2^k),
and the affine endpoint is preserved by
       (N,S) -> (N-m,S+m).

This certificate exhaustively regresses these identities on small parity words.
It does not assert an arbitrary-depth Collatz exclusion.
"""
from __future__ import annotations
from fractions import Fraction
from itertools import product


def correction(bits: tuple[int, ...]) -> tuple[int, int, tuple[int, ...]]:
    C = 0
    q = 0
    pos = []
    for p, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << p)
            q += 1
            pos.append(p)
    return C, q, tuple(pos)


def frac_mod_pow2(x: Fraction, k: int) -> int:
    mod = 1 << k
    return (x.numerator * pow(x.denominator, -1, mod)) % mod


def normalized_correction(bits: tuple[int, ...]) -> Fraction:
    C, q, _ = correction(bits)
    return Fraction(C, 3 ** q)


def root_from_S(bits: tuple[int, ...]) -> int:
    k = len(bits)
    S = normalized_correction(bits)
    return (-frac_mod_pow2(S, k)) % (1 << k)


def root_from_odd_positions(bits: tuple[int, ...]) -> int:
    k = len(bits)
    _, _, pos = correction(bits)
    mod = 1 << k
    acc = 0
    for r, p in enumerate(pos):
        acc = (acc + (1 << p) * pow(3, -r - 1, mod)) % mod
    return (-acc) % mod


def simulate(n: int, k: int) -> tuple[tuple[int, ...], int]:
    parity = []
    for _ in range(k):
        parity.append(n & 1)
        n = (3 * n + 1) // 2 if n & 1 else n // 2
    return tuple(parity), n


def selftest() -> None:
    word_checks = 0
    endpoint_checks = 0
    crossing_checks = 0

    # Every finite parity word has one canonical root modulo 2^k.  Verify that
    # the rational-S projection gives exactly that root and that simulation
    # returns the requested parity word.
    for k in range(1, 12):
        for bits in product((0, 1), repeat=k):
            C, q, _ = correction(bits)
            S = Fraction(C, 3 ** q)
            N = root_from_S(bits)
            assert N == root_from_odd_positions(bits)
            got, endpoint = simulate(N, k)
            assert got == bits
            assert Fraction(3 ** q, 2 ** k) * (N + S) == endpoint
            word_checks += 1
            endpoint_checks += 1

            # At a terminal coefficient-deficient prefix, endpoint >= root is
            # exactly the real inequality S >= (2^k/3^q - 1) N.
            if q and 3 ** q < 2 ** k:
                delta = Fraction(2 ** k, 3 ** q) - 1
                assert (endpoint >= N) == (S >= delta * N)
                crossing_checks += 1

    pair_checks = 0
    same_class_checks = 0

    # Same exact 3^q correction class <=> integer translation in S.
    for k in range(2, 11):
        by_q: dict[int, list[tuple[tuple[int, ...], int, Fraction, int]]] = {}
        for bits in product((0, 1), repeat=k):
            C, q, _ = correction(bits)
            S = Fraction(C, 3 ** q)
            N = root_from_S(bits)
            by_q.setdefault(q, []).append((bits, C, S, N))

        for q, rows in by_q.items():
            mod3 = 3 ** q
            for i in range(len(rows)):
                _, C1, S1, N1 = rows[i]
                for j in range(i + 1, len(rows)):
                    _, C2, S2, N2 = rows[j]
                    same_direct = ((C2 - C1) % mod3 == 0)
                    diff = S2 - S1
                    same_S = (diff.denominator == 1)
                    assert same_direct == same_S
                    pair_checks += 1

                    if same_S:
                        m = int(diff)
                        mod2 = 1 << k
                        assert (N2 - (N1 - m)) % mod2 == 0

                        # Endpoint-fiber translation is an exact algebraic
                        # identity, independently of choosing canonical lifts.
                        probe_N = N1 + 3 * mod2
                        left = Fraction(3 ** q, 2 ** k) * (probe_N + S1)
                        right = Fraction(3 ** q, 2 ** k) * ((probe_N - m) + S2)
                        assert left == right
                        same_class_checks += 1

    print(
        "PASS MATH-054 single-rational-S bridge",
        f"words={word_checks}",
        f"pairs={pair_checks}",
        f"same_class={same_class_checks}",
        f"crossing={crossing_checks}",
    )


if __name__ == "__main__":
    selftest()
