#!/usr/bin/env python3
"""MATH-191 exhaustive small-depth regression for exact CanFwd.

For every candidate parity word through depth 9, compare:

- direct search over all same-(k,d) competitor words using exact Sigma;
- forward block viability recursion CanFwd.

The two decisions must agree exactly.

Finite implementation regression only.  No new Hensel depth or Collatz claim.
"""

from fractions import Fraction
from functools import lru_cache
from itertools import product

MAX_K = 9


def gap_blocks(bits: tuple[int, ...]) -> tuple[int, ...]:
    q = 0
    a = [0]
    for bit in bits:
        if bit == 0:
            a[q] += 1
        else:
            q += 1
            a.append(0)
    return tuple(a)


def sigma_blocks(a: tuple[int, ...]) -> Fraction:
    p = 0
    out = Fraction(0)
    for r, block in enumerate(a):
        power_sum = 2**p * (2**block - 1)
        out += power_sum * Fraction(2**r, 3**r)
        p += block
    return out


def can_fwd(a: tuple[int, ...]) -> bool:
    Q = len(a) - 1
    D = sum(a)

    pA_prefix = [0] * (Q + 1)
    p = 0
    A = [0] * (Q + 1)
    for r, block in enumerate(a):
        pA_prefix[r] = p
        A[r] = 2**p * (2**block - 1)
        p += block

    @lru_cache(maxsize=None)
    def can(r: int, pB: int, W: int) -> bool:
        if r == Q + 1:
            return pB == D and W > 0 and W % (3**Q) == 0

        # MATH-190 optimistic upper bound after the current level is processed
        # is deliberately omitted here; this regression tests the core exact
        # recursion independently of any pruning optimization.
        for b in range(D - pB + 1):
            B = 2**pB * (2**b - 1)
            W2 = 3 * W + 2**r * (B - A[r])
            if can(r + 1, pB + b, W2):
                return True
        return False

    return can(0, 0, 0)


def main() -> None:
    candidates = 0
    direct_pairs = 0

    for k in range(MAX_K + 1):
        words = [tuple(x) for x in product((0, 1), repeat=k)]
        by_q: dict[int, list[tuple[int, ...]]] = {}
        for w in words:
            by_q.setdefault(sum(w), []).append(w)

        for q, group in by_q.items():
            sig = {w: sigma_blocks(gap_blocks(w)) for w in group}
            for cand in group:
                candidates += 1
                direct = False
                for comp in group:
                    direct_pairs += 1
                    diff = sig[comp] - sig[cand]
                    if diff.denominator == 1 and diff > 0:
                        direct = True
                        break

                got = can_fwd(gap_blocks(cand))
                assert got == direct, (k, q, cand, got, direct)

    print("PASS MATH-191 exact CanFwd regression")
    print(f"max_depth={MAX_K}")
    print(f"candidates_checked={candidates}")
    print(f"direct_pair_tests={direct_pairs}")
    print("NO NEW HENSEL DEPTH OR COLLATZ CLOSURE CLAIM")


if __name__ == "__main__":
    main()
