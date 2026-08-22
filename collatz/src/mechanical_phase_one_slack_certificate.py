#!/usr/bin/env python3
"""Exact finite regression for the mechanical-phase one-slack lemma.

The theorem is elementary and written in the companion note:
for alpha=log_3(2), b_n=ceil(alpha n), and s,j>=1,

    b_j - 1 <= b_{s+j} - b_s <= b_j.

Hence phase-shifted coefficient-survivor languages satisfy

    S_{0,h}(J) subset S_{s,h}(J) subset S_{0,h+1}(J).

This script checks the integer-power formulation over a large finite grid
without floating point.  It is a regression certificate, not the proof of the
all-s,j ceiling identity.
"""


def barriers(n: int) -> list[int]:
    out = [0] * (n + 1)
    p2 = p3 = 1
    q = 0
    for k in range(1, n + 1):
        p2 *= 2
        while p3 < p2:
            p3 *= 3
            q += 1
        out[k] = q
    return out


def main() -> None:
    S_MAX = 500
    J_MAX = 1000
    b = barriers(S_MAX + J_MAX)

    low_hits = high_hits = 0
    for s in range(1, S_MAX + 1):
        for j in range(1, J_MAX + 1):
            d = b[s + j] - b[s]
            assert d in (b[j] - 1, b[j]), (s, j, d, b[j])
            if d == b[j] - 1:
                low_hits += 1
            else:
                high_hits += 1

    assert low_hits > 0 and high_hits > 0
    print("mechanical phase one-slack regression: PASS")
    print("grid", S_MAX, J_MAX)
    print("lower_choice_count", low_hits)
    print("upper_choice_count", high_hits)


if __name__ == "__main__":
    main()
