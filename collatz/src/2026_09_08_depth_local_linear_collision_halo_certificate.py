#!/usr/bin/env python3
"""MATH-021: exact depth-local linear collision-halo certificate.

This certificate proves the finite-prefix inputs used by the algebraic reduction:

1. the published-floor coefficient threshold for depths 1..61 agrees exactly
   with the simpler q_min(k)=min{q:3^q>=2^k};
2. for a right-hand internal-boundary start b*2^61+r, the first 61 parity
   bits depend only on r;
3. no r in [0,702] satisfies the full coefficient-survival prefix through
   depth 61, while r=703 does.

Together with the already-audited MATH-004 correction bound
0 < d = S_L-S_R < Q/3 <= k/3 for a same-endpoint cross-boundary pair,
this yields no internal adjacent-block endpoint collision for 61<=k<=2109.

Finite computation is not promoted to a universal Collatz proof.
"""

B_PUB = 1 << 71
A_NUM = 3 * B_PUB + 1
K_ANCHOR = 61
R_MIN = 703
K_EXCLUSION_MAX = 3 * R_MIN  # 2109


def qmin_three(k: int) -> int:
    q = 0
    p = 1
    target = 1 << k
    while p < target:
        p *= 3
        q += 1
    return q


def qmin_published_floor(k: int) -> int:
    """Exact strict threshold for (3+1/B_pub)^q > 2^k."""
    q = 0
    ap = 1
    bp = 1
    target = 1 << k
    while not (ap > target * bp):
        q += 1
        ap *= A_NUM
        bp *= B_PUB
    return q


QMIN = [0] + [qmin_three(k) for k in range(1, K_ANCHOR + 1)]


def survives_anchor_offset(r: int) -> bool:
    """Candidate-language coefficient survival for every prefix 1..61.

    For N=b*2^61+r, the first 61 shortcut parity bits depend only on
    N mod 2^61 = r, so it is sufficient to iterate the canonical residue r.
    """
    n = r
    q = 0
    for k in range(1, K_ANCHOR + 1):
        odd = n & 1
        q += odd
        n = (3 * n + 1) // 2 if odd else n // 2
        if q < QMIN[k]:
            return False
    return True


def main() -> None:
    # Exact baseline-threshold regression in the only prefix range used to
    # establish the local right-offset obstruction.
    for k in range(1, K_ANCHOR + 1):
        assert qmin_published_floor(k) == qmin_three(k)

    assert QMIN[61] == 39

    survivors = [r for r in range(R_MIN + 1) if survives_anchor_offset(r)]
    assert survivors == [R_MIN]

    # Integer consequence of d < k/3: for k <= 3*703, d < 703 and hence
    # every right offset in a collision must satisfy r <= 702.
    assert K_EXCLUSION_MAX == 2109
    assert (K_EXCLUSION_MAX - 1) // 3 == 702
    assert K_EXCLUSION_MAX // 3 == 703
    assert (K_EXCLUSION_MAX + 1 - 1) // 3 == 703  # depth 2110 admits r=703

    print("PASS")
    print("published-floor q_min agrees with 3^q>=2^k for k=1..61")
    print("q_min(61) =", QMIN[61])
    print("smallest nonnegative right offset surviving every prefix through 61 =", R_MIN)
    print("all right offsets 0..702 fail by or before depth61")
    print("linear collision-halo consequence: no internal cross-boundary endpoint collision")
    print("for every depth 61 <= k <=", K_EXCLUSION_MAX)
    print("scope = candidate-language internal adjacent-block endpoint coupling only")
    print("COLLATZ STATUS = OPEN")


if __name__ == "__main__":
    main()
