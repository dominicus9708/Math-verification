#!/usr/bin/env python3
"""Exact finite certificate for the forced-OO resonant forward-correction identity.

For every coefficient-surviving boundary word at each Beatty rise depth
2 <= K <= 20, the first two parity bits are 11.  Write N=4Y+3, L=K-2,
q'=Q-2 and let R_tail be the ordinary affine correction of the remaining
L-bit tail.  The exact identity is

    9*3^q' * Y + 8*3^q' + R_tail == 0 (mod 2^L),

or equivalently

    3^q' Y + 8*9^{-1}3^q' + 9^{-1}R_tail == 0 (mod 2^L).

The second congruence proves that at Fourier frequency h*3^q' (h odd), the
canonical Hensel inverse disappears and the variable phase is the ordinary
forward correction multiplied by the fixed dyadic unit 9^{-1}.

The script uses only exact integer arithmetic.  It is a finite regression for
an all-depth algebraic identity, not a proof of Collatz.
"""


def qmins_exact(kmax: int) -> list[int]:
    b = [0] * (kmax + 1)
    q = 0
    p3 = 1
    for k in range(1, kmax + 1):
        while p3 < (1 << k):
            q += 1
            p3 *= 3
        b[k] = q
    return b


def survivors(kmax: int, barrier: list[int]):
    levels: list[list[tuple[tuple[int, ...], int]]] = [[((), 0)]]
    for k in range(1, kmax + 1):
        out = []
        th = barrier[k]
        for bits, q in levels[-1]:
            if q >= th:
                out.append((bits + (0,), q))
            if q + 1 >= th:
                out.append((bits + (1,), q + 1))
        levels.append(out)
    return levels


def canonical(bits: tuple[int, ...]) -> int:
    k = len(bits)
    mod = 1 << k
    q = 0
    s = 0
    for j, bit in enumerate(bits):
        if bit:
            q += 1
            s = (s + (1 << j) * pow(3, -q, mod)) % mod
    return (-s) % mod


def tail_correction(tail: tuple[int, ...]) -> tuple[int, int]:
    q = 0
    R = 0
    for j, bit in enumerate(tail):
        if bit:
            R = 3 * R + (1 << j)
            q += 1
    return q, R


def main() -> None:
    KMAX = 20
    barrier = qmins_exact(KMAX)
    levels = survivors(KMAX, barrier)

    rise_depths = 0
    checked_words = 0

    for K in range(2, KMAX + 1):
        if barrier[K] != barrier[K - 1] + 1:
            continue
        rise_depths += 1

        Q = barrier[K]
        parent_q = Q - 1
        boundary_parents = [
            bits for bits, q in levels[K - 1] if q == parent_q
        ]

        for parent in boundary_parents:
            bits = parent + (1,)  # unique surviving child at the rise
            assert bits[:2] == (1, 1)
            assert sum(bits) == Q

            N = canonical(bits)
            assert N % 4 == 3
            Y = (N - 3) // 4

            tail = bits[2:]
            L = K - 2
            qprime, Rtail = tail_correction(tail)
            assert qprime == Q - 2

            mod = 1 << L
            lhs = (pow(3, qprime, mod) * ((9 * Y + 8) % mod) + Rtail) % mod
            assert lhs == 0

            inv9 = pow(9, -1, mod)
            resonant = (
                pow(3, qprime, mod) * Y
                + 8 * inv9 * pow(3, qprime, mod)
                + inv9 * Rtail
            ) % mod
            assert resonant == 0

            # Check several odd multipliers h.  This is the exponent congruence
            # underlying equality of the corresponding complex characters.
            for h in (1, 3, 5, 7, 15):
                assert (h * resonant) % mod == 0

            checked_words += 1

    assert rise_depths > 0
    assert checked_words > 0

    print("forced-OO resonant forward-correction finite audit: PASS")
    print("rise depths checked:", rise_depths)
    print("boundary words checked:", checked_words)
    print("all resonant exponent congruences exact: PASS")


if __name__ == "__main__":
    main()
