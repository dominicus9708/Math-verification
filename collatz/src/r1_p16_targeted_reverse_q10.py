#!/usr/bin/env python3
"""Exact targeted reverse audit for the isolated-R1 p=16 hard sector.

Input facts certified elsewhere:
  * depth-27 Hensel hard prefixes at first mismatch p=16 collapse mod 2^19
    to the three residues 89083, 220155, 351227;
  * current unresolved starts are in the m=44 Cantor core above V_33.

This script raises only the reverse depth Q while keeping BMAX=18.  It proves
that Q=6 and Q=8 remove no low ternary selector cylinders, whereas Q=10
removes exactly five low-seven cylinders, independently of the three dyadic
residues and independently of a_7,a_8,a_9.
"""

from functools import lru_cache

R19 = (89083, 220155, 351227)
BMAX = 18
N_MIN = 4 * (3**44 + 3**33) + 3
N_MAX = 6 * 3**44 + 1


def forward_affine(r, B):
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


def reverse_frontier(z, Q, KMAX):
    states = {(z % (3**Q), 0): 0}
    out = []
    for d in range(Q):
        mod_next = 3 ** (Q - d - 1)
        nxt = {}
        for (cur, K), C in states.items():
            r3 = cur % 3
            if r3 == 0:
                continue
            a0 = 2 if r3 == 1 else 1
            for a in range(a0, KMAX - K + 1, 2):
                numerator = (1 << a) * cur - 1
                assert numerator % 3 == 0
                K2 = K + a
                C2 = (1 << a) * C + 3**d
                residue = numerator // 3
                residue = residue % mod_next if mod_next > 1 else 0
                key = (residue, K2)
                if C2 > nxt.get(key, -1):
                    nxt[key] = C2
        states = nxt
        byK = {}
        for (_residue, K), C in states.items():
            if C > byK.get(K, -1):
                byK[K] = C
        out.extend((d + 1, K, C) for K, C in byK.items())
    return out


def reverse_witness(frontier, qf, Rf, B):
    for qr, K, C in frontier:
        coeff = (1 << K) * 3**qf
        denom = (1 << B) * 3**qr
        const = (1 << K) * Rf - C * (1 << B)
        slope = coeff - denom
        testN = N_MAX if slope > 0 else N_MIN
        if slope * testN + const < 0:
            ancestor_num = (1 << K) * (3**qf * N_MIN + Rf) - C * (1 << B)
            if ancestor_num > 0:
                return qr, K, C
    return None


def n_mod_3q(mask, Q):
    n = 4 * 3**44 + 3
    for i in range(Q):
        if (mask >> i) & 1:
            n += 4 * 3**i
    return n % (3**Q)


def audit(Q, KMAX):
    MOD3 = 3**Q

    @lru_cache(None)
    def frontier(z):
        return tuple(reverse_frontier(z, Q, KMAX))

    survivor_sets = []
    for r19 in R19:
        survivors = []
        for mask in range(1 << Q):
            n3 = n_mod_3q(mask, Q)
            excluded = False
            for B in range(2, BMAX + 1):
                rb = r19 & ((1 << (B + 1)) - 1)
                qf, Rf, endpoint_odd = forward_affine(rb, B)

                slope = 3**qf - (1 << B)
                testN = N_MAX if slope > 0 else N_MIN
                if slope * testN + Rf < 0:
                    excluded = True
                    break

                if endpoint_odd:
                    z = ((3**qf * n3 + Rf) * pow(1 << B, -1, MOD3)) % MOD3
                    if reverse_witness(frontier(z), qf, Rf, B) is not None:
                        excluded = True
                        break

            if not excluded:
                survivors.append(mask)
        survivor_sets.append(set(survivors))

    assert survivor_sets[0] == survivor_sets[1] == survivor_sets[2]
    return survivor_sets[0]


def main():
    s6 = audit(6, 36)
    s8 = audit(8, 48)
    s10 = audit(10, 60)

    assert len(s6) == 64
    assert len(s8) == 256
    assert len(s10) == 984

    excluded10 = sorted(set(range(1 << 10)) - s10)
    low7 = sorted({m & 127 for m in excluded10})

    assert low7 == [6, 8, 14, 35, 78]
    assert excluded10 == sorted(base + 128 * hi for base in low7 for hi in range(8))

    print("Q6 survivors:", len(s6), "/ 64")
    print("Q8 survivors:", len(s8), "/ 256")
    print("Q10 survivors:", len(s10), "/ 1024")
    print("Q10 excluded:", len(excluded10))
    print("permanent low-seven forbidden masks:", low7)


if __name__ == "__main__":
    main()
