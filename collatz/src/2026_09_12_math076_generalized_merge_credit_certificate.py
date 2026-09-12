#!/usr/bin/env python3
"""MATH-076: generalized cross-layer merge-credit regression.

For two coefficient-surviving canonical states at the same depth k with the
same endpoint y, order them so q_H >= q_L and put d=q_H-q_L.  Define

    rho = 2^k / 3^q,
    S   = rho*y-r.

Then endpoint equality implies the exact identity

    G_d := r_L - 3^d r_H = 3^d S_H - S_L.

Using Sigma=S+rho-1 and rho_L=3^d rho_H, this is equivalently

    G_d = (3^d-1) + 3^d Sigma_H - Sigma_L.

This finite certificate enumerates the coefficient-surviving canonical tree
through depth 26, detects true first merges using the corrected predecessor
criterion from the integrated DSD audit, and regression-checks the identities.
It does NOT prove G_d>0 globally.
"""

from collections import defaultdict
from fractions import Fraction

MAX_DEPTH = 26


def main() -> None:
    # state = (r, y, q, actual_predecessor, final_parity)
    states = [(0, 0, 0, 0, 0)]
    total = 0
    hist = defaultdict(int)
    sign = defaultdict(lambda: [0, 0, 0])  # negative, zero, positive
    min_g = {}
    max_g = {}
    identity_failures = 0
    sigma_failures = 0
    congruence_failures = 0

    for parent_depth in range(MAX_DEPTH):
        v = 1 << parent_depth
        nxt = []
        for r, y, q, _pre0, _p0 in states:
            u = 3 ** q
            for p in (0, 1):
                lift = p ^ (y & 1)
                r2 = r + lift * v
                pre = y + lift * u
                y2 = (3 * pre + 1) // 2 if p else pre // 2
                q2 = q + p
                # Child depth is parent_depth+1, hence modulus coefficient 2*v.
                if 3 ** q2 >= 2 * v:
                    nxt.append((r2, y2, q2, pre, p))
        states = nxt

        classes = defaultdict(list)
        for st in states:
            classes[st[1]].append(st)

        k = parent_depth + 1
        pow2 = 1 << k
        for arr in classes.values():
            if len(arr) < 2:
                continue
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    a, b = arr[i], arr[j]
                    # Same actual predecessor means they were already merged.
                    if a[3] == b[3]:
                        continue
                    total += 1
                    lo, hi = (a, b) if a[2] <= b[2] else (b, a)
                    d = hi[2] - lo[2]
                    hist[d] += 1

                    rL, yL, qL, _, _ = lo
                    rH, yH, qH, _, _ = hi
                    assert yL == yH
                    assert qH - qL == d

                    rhoL = Fraction(pow2, 3 ** qL)
                    rhoH = Fraction(pow2, 3 ** qH)
                    SL = rhoL * yL - rL
                    SH = rhoH * yH - rH
                    sigmaL = SL + rhoL - 1
                    sigmaH = SH + rhoH - 1

                    G = rL - (3 ** d) * rH
                    if Fraction(G, 1) != (3 ** d) * SH - SL:
                        identity_failures += 1
                    if Fraction(G, 1) != (3 ** d - 1) + (3 ** d) * sigmaH - sigmaL:
                        sigma_failures += 1

                    expected_mod4 = 2 if d % 2 else 0
                    if G % 4 != expected_mod4:
                        congruence_failures += 1

                    if G < 0:
                        sign[d][0] += 1
                    elif G == 0:
                        sign[d][1] += 1
                    else:
                        sign[d][2] += 1
                    min_g[d] = G if d not in min_g else min(min_g[d], G)
                    max_g[d] = G if d not in max_g else max(max_g[d], G)

    assert total == 388
    assert dict(hist) == {1: 243, 2: 136, 3: 9}
    assert identity_failures == 0
    assert sigma_failures == 0
    assert congruence_failures == 0
    assert dict(sign) == {1: [0, 0, 243], 2: [0, 0, 136], 3: [0, 0, 9]}
    assert min_g == {1: 2, 2: 8, 3: 26}
    assert max_g == {1: 6, 2: 12, 3: 26}

    print("depth", MAX_DEPTH)
    print("true_first_merges", total)
    for d in sorted(hist):
        print("d", d, "count", hist[d], "sign", sign[d],
              "G_range", min_g[d], max_g[d])
    print("identity_failures", identity_failures)
    print("sigma_failures", sigma_failures)
    print("congruence_failures", congruence_failures)
    print("PASS MATH-076 generalized merge-credit regression")


if __name__ == "__main__":
    main()
