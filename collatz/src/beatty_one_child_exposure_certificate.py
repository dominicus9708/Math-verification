#!/usr/bin/env python3
"""Exact finite audit for the Beatty one-child exposure lower bound.

The coefficient-survivor language uses
  b_L = min{q : 3^q >= 2^L} = ceil(L log_3 2).
At a rise b_{L+1}=b_L+1, the one-child parent set is exactly the endpoint
boundary q_L=b_L.

The algebraic theorem in the companion note proves
  |D_L|/|R_L| >= ((2 b_L + 1 - L)/(b_L+1))/L > 2/(5L).

This script independently computes the exact survivor slack DP and checks the
finite inequalities through MAX_L without floating-point barrier decisions.
"""

from fractions import Fraction

MAX_L = 1500


def barriers(n: int):
    out = [0] * (n + 2)
    q = 0
    p3 = 1
    p2 = 1
    for L in range(1, n + 2):
        p2 <<= 1
        while p3 < p2:
            q += 1
            p3 *= 3
        out[L] = q
    return out


def main() -> None:
    b = barriers(MAX_L)

    # slack distribution A[s] after the current length, relative to b_L.
    A = [1]
    prev_b = 0
    rises = 0
    min_ratio = None
    min_scaled = None

    for L in range(1, MAX_L + 1):
        eps = b[L] - prev_b
        assert eps in (0, 1)

        if eps == 0:
            # plateau: append 0 preserves slack, append 1 raises it.
            B = [0] * (len(A) + 1)
            for s, cnt in enumerate(A):
                B[s] += cnt
                B[s + 1] += cnt
        else:
            # rise: append 1 preserves new slack; append 0 lowers old slack
            # by one, so old slack s+1 contributes to new slack s.
            B = [0] * len(A)
            for s in range(len(A)):
                B[s] += A[s]
                if s + 1 < len(A):
                    B[s] += A[s + 1]
            while len(B) > 1 and B[-1] == 0:
                B.pop()

        A = B
        prev_b = b[L]

        if b[L + 1] == b[L] + 1:
            rises += 1
            R = sum(A)
            D = A[0]
            frac = Fraction(D, R)

            # Exact phase-dependent lower bound from the binomial tail and
            # cycle-minimum boundary estimate.
            phase = Fraction(2 * b[L] + 1 - L, b[L] + 1)
            assert frac * L >= phase

            # Elementary universal bound: alpha=log_3 2 > 5/8 because
            # 3^5=243 < 2^8=256, hence phase > 2/5.
            assert frac * L > Fraction(2, 5)

            if min_ratio is None or frac < min_ratio[1]:
                min_ratio = (L, frac)
            scaled = frac * L
            if min_scaled is None or scaled < min_scaled[1]:
                min_scaled = (L, scaled)

    print("max_L", MAX_L)
    print("rise_steps", rises)
    print("min_raw_rise_ratio_at", min_ratio[0], float(min_ratio[1]))
    print("min_L_times_ratio_at", min_scaled[0], float(min_scaled[1]))
    print("universal_bound 2/(5L): PASS")
    print("Beatty one-child exposure certificate: PASS")


if __name__ == "__main__":
    main()
