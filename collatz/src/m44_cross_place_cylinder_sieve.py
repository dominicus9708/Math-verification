#!/usr/bin/env python3
"""Exact verifier for the m=44 cross-place cylinder sieve.

The verifier never enumerates the 2^44 starts individually.  It partitions the
ternary Cantor core by:

  * low ternary selectors a_0,...,a_(Q-1), which fix N mod 3^Q;
  * one dyadic residue N mod 2^(BMAX+1), which fixes every forward parity
    prefix through depth BMAX.

High ternary selector multiplicities are aggregated by a cyclic subset-sum DP.
Each cross-place class is removed only after an exact affine certificate proves
one of:

  1. T^B(N) < N for every N in the class interval; or
  2. a positive integer m < N merges into an odd endpoint T^B(N) through a
     positive odd-to-odd reverse code of depth at most Q.

Default certificate: Q=6, BMAX=18.
"""

from __future__ import annotations

from collections import defaultdict

Q = 6
BMAX = 18
KMAX = 36

N_MIN = 4 * 3**44 + 3
N_MAX = 6 * 3**44 + 1
TOTAL = 1 << 44


def forward_affine_from_residue(r: int, B: int):
    """Return (q,R,endpoint_parity) for the first B time-expanded steps."""
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


def reverse_frontier(z: int, Q: int, KMAX: int):
    """All undominated positive reverse codes from z mod 3^Q.

    State key: (current residue, total binary exponent K).
    For the same key, a larger correction C always gives a smaller ancestor,
    so only maximal C is retained.

    Returns triples (q,K,C) usable in

        m = (2^K y - C) / 3^q.
    """
    states = {(z % (3**Q), 0): 0}
    out = []

    for d in range(Q):
        mod_next = 3 ** (Q - d - 1)
        nxt_states = {}

        for (cur, K), C in states.items():
            r3 = cur % 3
            if r3 == 0:
                continue

            # Need 2^a cur == 1 (mod 3): a even for cur==1, odd for cur==2.
            a0 = 2 if r3 == 1 else 1
            for a in range(a0, KMAX - K + 1, 2):
                numerator = (1 << a) * cur - 1
                assert numerator % 3 == 0

                K2 = K + a
                C2 = (1 << a) * C + 3**d
                residue = numerator // 3
                residue = residue % mod_next if mod_next > 1 else 0

                key = (residue, K2)
                old = nxt_states.get(key)
                if old is None or C2 > old:
                    nxt_states[key] = C2

        states = nxt_states
        q = d + 1

        # At a completed reverse depth, current residue is irrelevant for the
        # affine comparison.  For fixed K retain maximal C over all paths.
        by_K = {}
        for (_residue, K), C in states.items():
            if C > by_K.get(K, -1):
                by_K[K] = C
        out.extend((q, K, C) for K, C in by_K.items())

    return out


def reverse_witness(frontier, qf: int, Rf: int, B: int):
    """Return one class-uniform smaller-ancestor certificate, or None."""
    for qr, K, C in frontier:
        coeff = (1 << K) * 3**qf
        denom = (1 << B) * 3**qr
        const = (1 << K) * Rf - C * (1 << B)

        slope = coeff - denom
        test_N = N_MAX if slope > 0 else N_MIN

        if slope * test_N + const < 0:
            # Final ancestor must be positive.  The numerator is increasing in N.
            ancestor_num = (1 << K) * (3**qf * N_MIN + Rf) - C * (1 << B)
            if ancestor_num > 0:
                return qr, K, C
    return None


def high_selector_counts(Q: int, L: int):
    """Cyclic group-algebra coefficients for selectors a_Q,...,a_43."""
    M = 1 << L
    dp = [0] * M
    dp[0] = 1

    for i in range(Q, 44):
        w = (4 * pow(3, i, M)) % M
        nd = dp[:]
        for r, c in enumerate(dp):
            if c:
                nd[(r + w) % M] += c
        dp = nd

    assert sum(dp) == 1 << (44 - Q)
    return dp


def low_data(mask: int, Q: int, L: int):
    M = 1 << L
    low2 = 0
    low3 = 0
    for i in range(Q):
        if (mask >> i) & 1:
            low2 = (low2 + 4 * pow(3, i, M)) % M
            low3 += 4 * 3**i
    return low2, (low3 + 3) % (3**Q)


def main():
    L = BMAX + 1
    M = 1 << L
    MOD3 = 3**Q

    frontiers = [reverse_frontier(z, Q, KMAX) for z in range(MOD3)]
    high = high_selector_counts(Q, L)
    high_nonzero = [(r, c) for r, c in enumerate(high) if c]

    fixed2 = (4 * pow(3, 44, M) + 3) % M

    # Precompute forward affine maps at every tested dyadic depth.
    fwd = {}
    for B in range(2, BMAX + 1):
        fwd[B] = [forward_affine_from_residue(r, B) for r in range(1 << (B + 1))]

    inv2B = {B: pow(1 << B, -1, MOD3) for B in range(2, BMAX + 1)}
    pow3 = [pow(3, q, MOD3) for q in range(BMAX + 1)]

    excluded_forward = 0
    excluded_reverse = 0
    surviving = 0
    reverse_cache = {}

    for mask in range(1 << Q):
        low2, n3 = low_data(mask, Q, L)

        for high_residue, multiplicity in high_nonzero:
            rL = (fixed2 + low2 + high_residue) % M
            reason = None

            for B in range(2, BMAX + 1):
                rb = rL & ((1 << (B + 1)) - 1)
                qf, Rf, endpoint_odd = fwd[B][rb]

                # Exact forward descent on the whole N interval.
                slope = 3**qf - (1 << B)
                test_N = N_MAX if slope > 0 else N_MIN
                if slope * test_N + Rf < 0:
                    reason = "forward"
                    break

                if not endpoint_odd:
                    continue

                z = ((pow3[qf] * n3 + Rf) * inv2B[B]) % MOD3
                key = (B, rb, z)
                if key not in reverse_cache:
                    reverse_cache[key] = reverse_witness(frontiers[z], qf, Rf, B)

                if reverse_cache[key] is not None:
                    reason = "reverse"
                    break

            if reason == "forward":
                excluded_forward += multiplicity
            elif reason == "reverse":
                excluded_reverse += multiplicity
            else:
                surviving += multiplicity

    excluded = excluded_forward + excluded_reverse

    assert excluded + surviving == TOTAL
    assert excluded_forward == 14_172_856_036_042
    assert excluded_reverse == 2_043_061_564_469
    assert excluded == 16_215_917_600_511
    assert surviving == 1_376_268_443_905

    print("Q:", Q)
    print("BMAX:", BMAX)
    print("total:", TOTAL)
    print("forward excluded:", excluded_forward)
    print("reverse-only excluded:", excluded_reverse)
    print("total excluded:", excluded)
    print("surviving:", surviving)
    print("excluded fraction:", excluded / TOTAL)
    print("surviving fraction:", surviving / TOTAL)
    print("reverse decision cache entries:", len(reverse_cache))


if __name__ == "__main__":
    main()
