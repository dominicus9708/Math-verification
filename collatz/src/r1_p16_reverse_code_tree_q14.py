#!/usr/bin/env python3
"""Exact reverse-code prefix-tree verifier for the isolated-R1 p=16 hard sector.

This version generates admissible reverse exponent codes directly, indexes each
code by the endpoint residue it requires, and audits Q=6,8,10,11,12,13,14 for
the three depth-27 hard dyadic residues.  It avoids constructing frontiers for
all 3^Q endpoint residues.
"""

from collections import defaultdict
from itertools import product

R19 = (89083, 220155, 351227)
BMAX = 18
N_MIN = 4 * (3**44 + 3**33) + 3
N_MAX = 6 * 3**44 + 1

EXPECTED = {
    6: 64,
    8: 256,
    10: 984,
    11: 1960,
    12: 3896,
    13: 7776,
    14: 15440,
}

EXPECTED_MINIMAL = {
    10: [(6, 14), (7, 6), (7, 8), (7, 35)],
    11: [(6, 14), (7, 6), (7, 8), (7, 35), (9, 148), (9, 461)],
    12: [
        (6, 14), (7, 6), (7, 8), (7, 35),
        (9, 135), (9, 148), (9, 254), (9, 461), (9, 494),
    ],
    13: [
        (6, 14), (7, 6), (7, 8), (7, 35),
        (9, 135), (9, 148), (9, 254), (9, 461), (9, 494),
        (11, 1143), (11, 1869), (11, 1940), (11, 1961),
    ],
}


def forward_affine(r: int, B: int):
    n = r
    q = 0
    R = 0
    for k in range(B):
        if n & 1:
            R = 3 * R + (1 << k)
            q += 1
            n = (3 * n + 1) // 2
        else:
            n //= 2
    return q, R, n & 1


def correction_from_exponents(exponents):
    C = 0
    for d, a in enumerate(exponents):
        C = (1 << a) * C + 3**d
    return C


def positive_compositions(total, length, prefix=()):
    if length == 1:
        yield prefix + (total,)
        return
    for a in range(1, total - length + 2):
        yield from positive_compositions(total - a, length - 1, prefix + (a,))


def valid_reverse_code(exponents):
    q = len(exponents)
    K = sum(exponents)
    C = correction_from_exponents(exponents)
    mod = 3**q
    z = (C * pow(1 << K, -1, mod)) % mod

    cur = z
    for a in exponents:
        if cur % 3 == 0:
            return None
        num = (1 << a) * cur - 1
        if num % 3:
            return None
        cur = num // 3

    return z, K, C


def useful_kmax(qr: int) -> int:
    best = 0
    for r in R19:
        for B in range(2, BMAX + 1):
            qf, _Rf, _odd = forward_affine(r & ((1 << (B + 1)) - 1), B)
            K = 0
            while (1 << (K + 1)) * 3**qf < (1 << B) * 3**qr:
                K += 1
            best = max(best, K)
    return best


def build_codes(QMAX=14):
    table = [None] + [defaultdict(dict) for _ in range(QMAX)]
    for q in range(1, QMAX + 1):
        kmax = useful_kmax(q)
        for K in range(q, kmax + 1):
            for exponents in positive_compositions(K, q):
                valid = valid_reverse_code(exponents)
                if valid is None:
                    continue
                z, K2, C = valid
                old = table[q][z].get(K2)
                if old is None or C > old[0]:
                    table[q][z][K2] = (C, exponents)
    return table


def n_mod_3q(mask: int, Q: int) -> int:
    n = 4 * 3**44 + 3
    for i in range(Q):
        if (mask >> i) & 1:
            n += 4 * 3**i
    return n % (3**Q)


def audit_mask(r19: int, mask: int, Q: int, codes):
    modQ = 3**Q
    n3 = n_mod_3q(mask, Q)

    for B in range(2, BMAX + 1):
        rb = r19 & ((1 << (B + 1)) - 1)
        qf, Rf, endpoint_odd = forward_affine(rb, B)

        # Whole-class forward descent.
        slope = 3**qf - (1 << B)
        testN = N_MAX if slope > 0 else N_MIN
        if slope * testN + Rf < 0:
            return ("forward", B)

        if not endpoint_odd:
            continue

        zQ = ((3**qf * n3 + Rf) * pow(1 << B, -1, modQ)) % modQ

        for qr in range(1, Q + 1):
            z = zQ % (3**qr)
            bucket = codes[qr].get(z)
            if not bucket:
                continue

            for K, (C, exponents) in bucket.items():
                coeff = (1 << K) * 3**qf
                denom = (1 << B) * 3**qr
                const = (1 << K) * Rf - C * (1 << B)
                slope = coeff - denom
                testN = N_MAX if slope > 0 else N_MIN
                if slope * testN + const >= 0:
                    continue

                ancestor_num = (1 << K) * (3**qf * N_MIN + Rf) - C * (1 << B)
                if ancestor_num > 0:
                    return ("reverse", B, qf, Rf, qr, K, C, exponents)

    return None


def minimal_cylinders(excluded, Q):
    out = []

    def walk(base, k):
        descendants = (base + (hi << k) for hi in range(1 << (Q - k)))
        if all(x in excluded for x in descendants):
            out.append((k, base))
            return
        if k == Q:
            return
        walk(base, k + 1)
        walk(base + (1 << k), k + 1)

    walk(0, 0)
    return sorted(out)


def main():
    codes = build_codes(14)

    for Q in (6, 8, 10, 11, 12, 13, 14):
        survivor_sets = []
        witness_maps = []

        for r in R19:
            survivors = set()
            witnesses = {}
            for mask in range(1 << Q):
                witness = audit_mask(r, mask, Q, codes)
                if witness is None:
                    survivors.add(mask)
                else:
                    witnesses[mask] = witness
            survivor_sets.append(survivors)
            witness_maps.append(witnesses)

        assert survivor_sets[0] == survivor_sets[1] == survivor_sets[2]
        survivors = survivor_sets[0]
        assert len(survivors) == EXPECTED[Q]

        excluded = set(range(1 << Q)) - survivors
        mins = minimal_cylinders(excluded, Q)
        if Q in EXPECTED_MINIMAL:
            assert mins == EXPECTED_MINIMAL[Q]

        print(
            "Q", Q,
            "survivors", len(survivors),
            "excluded", len(excluded),
            "minimal_cylinders", len(mins),
        )
        print("  ", mins)

        # Print one exact witness for every minimal cylinder using the first
        # dyadic hard residue and zero higher selector bits.
        if Q >= 10:
            for k, base in mins:
                print("   witness", (k, base), witness_maps[0][base])


if __name__ == "__main__":
    main()
