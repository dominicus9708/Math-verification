#!/usr/bin/env python3
"""Finite exact regression for the height-excursion macro reduction.

The companion note proves the all-length statements. This script checks them
without floating point on a finite grid of phases, heights, lengths and parity
words.

For alpha=log_3(2), b_n=ceil(n alpha), define
    D_s(L)=b_{s+L}-b_s.
A parity macro W of length L, total odd count Q and incoming height h has
    h_out = h + Q - D_s(L).

Main theorem checked here:
* if W is coefficient-admissible at (s,h) and h_out >= h+1, then
  - W is also admissible at its suffix state (s+L,h_out),
  - Q >= b_L,
  - every later L-step phase displacement is <= Q.
This is the combinatorial part needed for the exact self-prepend/min-plus
transport, and implies nonnegative normalized penalty-minus-rebate for such a
macro.

For height-neutral macros h_out=h, Q=D_s(L) is necessarily one of
    {b_L-1,b_L}.
Thus all neutral excursions lie exactly on the mechanical one-slack boundary.

This is not a proof of coefficient stopping or of the Collatz conjecture.
"""

from itertools import product


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


def admissible(bits: tuple[int, ...], s: int, h: int, b: list[int]) -> bool:
    q = 0
    for j, bit in enumerate(bits, 1):
        q += bit
        if q < b[s + j] - b[s] - h:
            return False
    return True


def main() -> None:
    S_MAX = 40
    H_MAX = 4
    L_MAX = 10
    BRIDGE_J_MAX = 20
    b = barriers(S_MAX + 2 * L_MAX + BRIDGE_J_MAX + 8)

    admissible_count = 0
    gain_count = 0
    neutral_count = 0
    neutral_low = 0
    neutral_high = 0

    for s in range(S_MAX + 1):
        for L in range(1, L_MAX + 1):
            bL = b[L]
            D = b[s + L] - b[s]
            assert D in (bL - 1, bL), (s, L, D, bL)

            for h in range(H_MAX + 1):
                for bits in product((0, 1), repeat=L):
                    if not admissible(bits, s, h, b):
                        continue

                    admissible_count += 1
                    Q = sum(bits)
                    hp = h + Q - D
                    assert hp >= 0

                    if hp >= h + 1:
                        gain_count += 1

                        # One unit of height gain absorbs the possible one-unit
                        # mechanical phase mismatch at every prefix.
                        assert admissible(bits, s + L, hp, b), (
                            s, h, L, bits, Q, hp
                        )

                        # D_s(L) >= b_L-1, so Q=D_s(L)+(hp-h) >= b_L.
                        assert Q >= bL

                        # Later transport across a prepended length-L macro is
                        # safe because every shifted L-step barrier increment is
                        # at most b_L <= Q.
                        A = s + L
                        for j in range(BRIDGE_J_MAX + 1):
                            shifted = b[A + L + j] - b[A + j]
                            assert shifted <= bL <= Q

                    if hp == h:
                        neutral_count += 1
                        assert Q == D
                        assert Q in (bL - 1, bL)
                        if Q == bL - 1:
                            neutral_low += 1
                            # one-slack neutral scale expands, but by < 3
                            assert 3 ** Q < 2 ** L < 3 ** (Q + 1)
                        else:
                            neutral_high += 1
                            # full neutral scale does not expand
                            assert 2 ** L <= 3 ** Q

    assert gain_count > 0
    assert neutral_low > 0 and neutral_high > 0

    print("height-excursion macro regression: PASS")
    print("admissible_macros", admissible_count)
    print("strict_height_gain_macros", gain_count)
    print("height_neutral_macros", neutral_count)
    print("neutral_one_slack", neutral_low)
    print("neutral_full_barrier", neutral_high)


if __name__ == "__main__":
    main()
