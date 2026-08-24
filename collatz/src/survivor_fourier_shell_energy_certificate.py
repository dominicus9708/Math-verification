#!/usr/bin/env python3
"""Exact finite regression for the survivor Fourier valuation-shell identity.

The all-depth identity is derived in
  notes/2026-08-24-survivor-fourier-shell-energy.md.

For small H this script independently enumerates every coefficient-surviving
parity word, projects its canonical residue to every lower modulus 2^K, and
compares the sibling-difference Parseval energy with the polynomial-time
prefix/tail DP formula

  E(H,K)=2^(K-1) sum_q C_(K-1)(q) D_(H,K)(q)^2.

No floating point is used. This is a finite regression certificate, not a
proof of Collatz.
"""

from collections import defaultdict


def barriers(H: int) -> list[int]:
    b = [0] * (H + 1)
    q = 0
    p3 = 1
    for j in range(1, H + 1):
        while p3 < (1 << j):
            q += 1
            p3 *= 3
        b[j] = q
    return b


def prefix_levels(H: int, b: list[int]):
    levels = [{0: 1}]
    cur = {0: 1}
    for j in range(1, H + 1):
        th = b[j]
        nxt = defaultdict(int)
        for q, c in cur.items():
            if q >= th:
                nxt[q] += c
            if q + 1 >= th:
                nxt[q + 1] += c
        cur = dict(nxt)
        levels.append(cur)
    return levels


def tail_counts(H: int, K: int, b: list[int]) -> dict[int, int]:
    # Number of admissible continuations from a state immediately after depth K.
    f = {q: 1 for q in range(b[H], H + 1)}
    for j in range(H - 1, K - 1, -1):
        th = b[j + 1]
        nf: dict[int, int] = {}
        for q in range(0, j + 1):
            z = 0
            if q >= th:
                z += f.get(q, 0)
            if q + 1 >= th:
                z += f.get(q + 1, 0)
            if z:
                nf[q] = z
        f = nf
    return f


def dp_energy(H: int, K: int) -> int:
    b = barriers(H)
    levels = prefix_levels(K - 1, b)
    C = levels[K - 1]
    F = tail_counts(H, K, b)
    a = b[K]
    s = 0
    for q, c in C.items():
        even = F.get(q, 0) if q >= a else 0
        odd = F.get(q + 1, 0) if q + 1 >= a else 0
        d = even - odd
        s += c * d * d
    return (1 << (K - 1)) * s


def survivor_words(H: int):
    b = barriers(H)
    level = [((), 0)]
    for j in range(1, H + 1):
        th = b[j]
        nxt = []
        for bits, q in level:
            if q >= th:
                nxt.append((bits + (0,), q))
            if q + 1 >= th:
                nxt.append((bits + (1,), q + 1))
        level = nxt
    return level


def canonical_prefix(bits: tuple[int, ...], K: int) -> int:
    mod = 1 << K
    q = 0
    acc = 0
    for j, bit in enumerate(bits[:K]):
        if bit:
            q += 1
            acc = (acc + (1 << j) * pow(3, -q, mod)) % mod
    return (-acc) % mod


def enumerated_energy(H: int, K: int) -> int:
    words = survivor_words(H)
    M = 1 << K
    counts = [0] * M
    for bits, _ in words:
        counts[canonical_prefix(bits, K)] += 1

    top = 1 << (K - 1)
    diff2 = 0
    for r in range(top):
        d = counts[r] - counts[r + top]
        diff2 += d * d
    return top * diff2


def main() -> None:
    checks = 0
    for H in range(4, 11):
        for K in range(2, H + 1):
            lhs = enumerated_energy(H, K)
            rhs = dp_energy(H, K)
            assert lhs == rhs, (H, K, lhs, rhs)
            checks += 1

    # Terminal-shell regression: plateau gives zero; rise gives 2^(H-1) B_H.
    for H in range(4, 21):
        b = barriers(H)
        E = dp_energy(H, H)
        if b[H] == b[H - 1]:
            assert E == 0
        else:
            levels = prefix_levels(H - 1, b)
            B = levels[H - 1].get(b[H] - 1, 0)
            assert E == (1 << (H - 1)) * B

    print("survivor Fourier shell-energy finite regression: PASS")
    print("enumeration-vs-DP checks:", checks)
    print("terminal plateau/rise shell regression: PASS")


if __name__ == "__main__":
    main()
