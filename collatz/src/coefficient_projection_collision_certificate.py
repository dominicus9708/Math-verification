#!/usr/bin/env python3
"""Exact projection/collision compression for the coefficient-survival language.

Let B_H be the complete set of length-H parity words satisfying

    3^q_j >= 2^j

at every prefix. The first two bits are forced to 11, so use the reduced dyadic
coordinate y=(r-3)/4 and project it modulo 2^rho, 0<=rho<=H-2.

A length-(rho+2) surviving prefix with odd count q has a number of admissible
continuations to H that depends only on (rho+2,q), not on the detailed prefix.
Write

    A[j,q] = number of surviving length-j prefixes with odd count q,
    C[j,q] = number of admissible continuations from state (j,q) to H,
    B_H    = total number of surviving length-H words.

Then the exact collision probability of the projected coefficient-language
probability measure is

    P_{H,rho}
      = sum_q A[rho+2,q] C[rho+2,q]^2 / B_H^2.

Consequently the total normalized Fourier L2 energy at resolution 2^rho is

    E_{H,rho} = 2^rho P_{H,rho},

and the exact-order dyadic shell energy is

    S_{H,rho} = E_{H,rho} - E_{H,rho-1}.

The formula is checked below against brute-force parity-word enumeration at
small H. This is a structural compression lemma/certificate, not a Collatz
proof and not by itself a cross-base transversality bound.
"""

from fractions import Fraction


def qmins_exact(H):
    b = [0] * (H + 1)
    q = 0
    p3 = 1
    for j in range(1, H + 1):
        while p3 < (1 << j):
            q += 1
            p3 *= 3
        b[j] = q
    return b


def forward_backward(H):
    b = qmins_exact(H)

    A = [[0] * (H + 2) for _ in range(H + 1)]
    A[0][0] = 1
    for j in range(H):
        threshold = b[j + 1]
        for q, count in enumerate(A[j]):
            if not count:
                continue
            if q >= threshold:
                A[j + 1][q] += count
            if q + 1 >= threshold:
                A[j + 1][q + 1] += count

    C = [[0] * (H + 2) for _ in range(H + 1)]
    for q in range(H + 2):
        C[H][q] = 1

    for j in range(H - 1, -1, -1):
        threshold = b[j + 1]
        for q in range(j + 1):
            if q >= threshold:
                C[j][q] += C[j + 1][q]
            if q + 1 >= threshold:
                C[j][q] += C[j + 1][q + 1]

    B = C[0][0]
    assert B == sum(A[H])
    return b, A, C, B


def projection_collision_from_tables(H, rho, A, C, B):
    if not (0 <= rho <= H - 2):
        raise ValueError("rho must lie in [0,H-2]")
    j = rho + 2
    num = sum(A[j][q] * C[j][q] * C[j][q] for q in range(H + 2))
    return Fraction(num, B * B)


def projection_collision(H, rho):
    _, A, C, B = forward_backward(H)
    return projection_collision_from_tables(H, rho, A, C, B)


def brute_prefix_counts(H, rho):
    b = qmins_exact(H)
    prefix_depth = rho + 2
    counts = {}

    def rec(bits, q, j):
        if j == H:
            prefix = tuple(bits[:prefix_depth])
            counts[prefix] = counts.get(prefix, 0) + 1
            return

        threshold = b[j + 1]
        if q >= threshold:
            bits.append(0)
            rec(bits, q, j + 1)
            bits.pop()
        if q + 1 >= threshold:
            bits.append(1)
            rec(bits, q + 1, j + 1)
            bits.pop()

    rec([], 0, 0)
    B = sum(counts.values())
    num = sum(c * c for c in counts.values())
    return Fraction(num, B * B), B


def main():
    for H in (8, 10, 12):
        _, A, C, B = forward_backward(H)
        for rho in range(0, H - 1):
            compressed = projection_collision_from_tables(H, rho, A, C, B)
            brute, brute_B = brute_prefix_counts(H, rho)
            assert B == brute_B
            assert compressed == brute, (H, rho, compressed, brute)
        print("bruteforce_projection_match H", H, "PASS")

    H = 28
    _, A, C, B = forward_backward(H)
    print("H", H, "survival_count", B)

    previous_total = Fraction(1, 1)
    for rho in range(1, H - 1):
        P = projection_collision_from_tables(H, rho, A, C, B)
        total = (1 << rho) * P
        shell = total - previous_total
        assert shell >= 0
        if rho in (5, 10, 15, 20, 26):
            print(
                "rho", rho,
                "collision", float(P),
                "total_fourier_energy", float(total),
                "shell_energy", float(shell),
            )
        previous_total = total

    print("coefficient projection collision certificate: PASS")


if __name__ == "__main__":
    main()
