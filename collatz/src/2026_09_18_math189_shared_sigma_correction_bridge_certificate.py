#!/usr/bin/env python3
"""MATH-189 exact finite regression for the shared-Sigma/correction bridge.

This is a regression certificate, not a new Collatz closure claim.

It checks through depth 12 that:
- MATH-051 even-position Sigma equals the normalized-correction Sigma;
- the integer correction recurrence is exact;
- the canonical dyadic residue reproduces the requested parity word;
- every same-(k,q) Hensel-class correction lift shifts the source residue by
  exactly the integer credit and preserves the k-step endpoint;
- the gap coordinate G_j=e_j-j equals the odd count before the j-th even step.
"""

from fractions import Fraction
from itertools import product

MAX_K = 12


def correction(bits):
    C = 0
    q = 0
    for k, b in enumerate(bits):
        if b:
            C = 3 * C + (1 << k)
            q += 1
    return C, q


def sigma_even(bits):
    evens = [i for i, b in enumerate(bits) if not b]
    s = Fraction(0)
    for j, e in enumerate(evens):
        s += (3 ** j) * (Fraction(2, 3) ** e)
    return s


def canonical_residue(C, q, k):
    if k == 0:
        return 0
    mod = 1 << k
    inv = pow(3 ** q, -1, mod)
    return (-C * inv) % mod


def shortcut(n):
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def run_word(n, k):
    bits = []
    x = n
    for _ in range(k):
        bits.append(x & 1)
        x = shortcut(x)
    return tuple(bits), x


def check_word(bits):
    k = len(bits)
    C, q = correction(bits)
    sig = sigma_even(bits)
    rho = Fraction(2 ** k, 3 ** q)

    assert Fraction(C, 3 ** q) == 1 + sig - rho
    assert C == 3 ** q * (1 + sig) - 2 ** k

    # Direct one-step correction recurrence and Sigma update.
    C2 = 0
    q2 = 0
    sig2 = Fraction(0)
    d2 = 0
    for depth, b in enumerate(bits):
        rho2 = Fraction(2 ** depth, 3 ** q2)
        if b == 0:
            sig2 += rho2
            d2 += 1
        else:
            C2 = 3 * C2 + (1 << depth)
            q2 += 1
        assert C2 == 3 ** q2 * (1 + sig2) - 2 ** (depth + 1)
    assert C2 == C and q2 == q and sig2 == sig

    # Canonical source residue plus one positive lift realizes the word.
    a = canonical_residue(C, q, k)
    n = a if a > 0 else a + (1 << k)
    got_bits, endpoint = run_word(n, k)
    assert got_bits == tuple(bits)
    assert endpoint * (1 << k) == (3 ** q) * n + C

    # Gap coordinate equals odd count before each even event.
    odd_seen = 0
    even_rank = 0
    for e, b in enumerate(bits):
        if b:
            odd_seen += 1
        else:
            G = e - even_rank
            assert G == odd_seen
            even_rank += 1


def main():
    words = 0
    class_pairs = 0

    for k in range(1, MAX_K + 1):
        groups = {}
        for bits in product((0, 1), repeat=k):
            check_word(bits)
            C, q = correction(bits)
            key = (q, C % (3 ** q))
            groups.setdefault(key, []).append((C, bits))
            words += 1

        for (q, _), arr in groups.items():
            arr.sort()
            for i in range(len(arr)):
                C, bits = arr[i]
                a = canonical_residue(C, q, k)
                for j in range(i + 1, len(arr)):
                    Cstar, _ = arr[j]
                    diff = Cstar - C
                    assert diff > 0 and diff % (3 ** q) == 0
                    t = diff // (3 ** q)
                    astar = canonical_residue(Cstar, q, k)
                    assert astar == (a - t) % (1 << k)

                    # Equal-endpoint identity is exact algebraically.
                    # Use a positive lift large enough that N-t is positive.
                    N = a + 2 * (1 << k)
                    Nstar = N - t
                    assert Nstar > 0
                    lhs = (3 ** q) * Nstar + Cstar
                    rhs = (3 ** q) * N + C
                    assert lhs == rhs
                    class_pairs += 1

    print("PASS MATH-189 shared Sigma / correction / Hensel bridge regression")
    print(f"depth_range=1..{MAX_K}")
    print(f"parity_words_checked={words}")
    print(f"hensel_class_pairs_checked={class_pairs}")
    print("NO NEW LAYER CLOSURE CLAIM")


if __name__ == "__main__":
    main()
