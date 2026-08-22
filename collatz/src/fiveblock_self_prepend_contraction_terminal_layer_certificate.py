#!/usr/bin/env python3
"""Exact finite regression for the five-block self-prepend and terminal-floor lemmas.

The analytic note proves the lemmas. This script checks the finite combinatorial
components used there:

* every admissible q>=4 five-word is again admissible at its suffix phase-height
  state over a large exact phase/slack window;
* the exact five-word correction maxima and the sharp low-q threshold 76/5;
* q_j(x)<=j/2+2 for 1<=x<=15 until entry into the 1<->2 accelerated cycle;
* the exact rational comparison log_3(2)>5/8 via 2^8>3^5.

This is a regression certificate, not a proof of coefficient stopping and not a
proof of the Collatz conjecture.
"""

from itertools import product


def barriers(n: int) -> list[int]:
    b = [0] * (n + 1)
    p3 = 1
    q = 0
    for k in range(1, n + 1):
        while p3 < (1 << k):
            p3 *= 3
            q += 1
        b[k] = q
    return b


def canonical_word(bits: tuple[int, ...]):
    r = 1
    y = 1
    q = 0
    qs: list[int] = []
    for k, bit in enumerate(bits):
        if bit ^ (y & 1):
            r += 1 << k
            y += 3**q
        if bit == 0:
            y //= 2
        else:
            y = (3 * y + 1) // 2
            q += 1
        qs.append(q)
    R = 32 * y - 3**q * r
    return r, y, q, R, qs


WORDS = [canonical_word(bits) for bits in product((0, 1), repeat=5)]


def admissible(s: int, h: int, w, b: list[int]) -> bool:
    _, _, _, _, qs = w
    return all(
        qs[j - 1] >= b[s + j] - b[s] - h
        for j in range(1, 6)
    )


def phase_transfer_regression() -> None:
    b = barriers(5020)
    for s in range(0, 5001):
        d5 = b[s + 5] - b[s]
        assert d5 in (3, 4)
        for h in range(13):
            for w in WORDS:
                r, _, q, _, _ = w
                if not admissible(s, h, w, b) or q < 4:
                    continue
                hp = h + q - d5
                assert hp >= 0
                assert admissible(s + 5, hp, w, b), (s, h, r, q, hp)
    print("high-q suffix self-admissibility regression: PASS")


def correction_constants() -> None:
    by_q: dict[int, int] = {}
    low_ratio = []
    for r, _, q, R, _ in WORDS:
        by_q[q] = max(by_q.get(q, 0), R)
        if q <= 3:
            low_ratio.append((R / (32 - 3**q), r, q, R))

    expected = {0: 0, 1: 16, 2: 40, 3: 76, 4: 130, 5: 211}
    assert by_q == expected, by_q

    ratio, r, q, R = max(low_ratio)
    assert (ratio, r, q, R) == (76 / 5, 28, 3, 76)

    print("max correction by q:", by_q)
    print("max low-q expansion threshold: 76/5 at r=28 q=3")


def small_floor_bound() -> None:
    # For 1<=x<=15, verify 2*q_j-j <= 4 until entry into {1,2}.
    # Once in the 1<->2 accelerated cycle, the same inequality persists.
    worst = (-10**9, None, None)

    for x0 in range(1, 16):
        x = x0
        q = 0
        for j in range(1, 100):
            if x & 1:
                q += 1
                x = (3 * x + 1) // 2
            else:
                x //= 2

            score = 2 * q - j
            worst = max(worst, (score, x0, j))
            assert score <= 4, (x0, j, score)

            if x in (1, 2):
                # Explicitly cross the cycle boundary as a regression guard.
                y = x
                qq = q
                for jj in range(j + 1, j + 5):
                    if y & 1:
                        qq += 1
                        y = (3 * y + 1) // 2
                    else:
                        y //= 2
                    assert 2 * qq - jj <= 4
                break
        else:
            raise AssertionError(("no cycle entry", x0))

    assert worst[0] == 4, worst

    # Exact rational comparison alpha=log_3(2)>5/8.
    assert 2**8 > 3**5

    print("small-floor q_j <= j/2+2 certificate: PASS")
    print("worst 2*q_j-j =", worst[0])
    print("therefore J >= 8(h+3) forces mu_{s,h}(J) >= 16")


def main() -> None:
    phase_transfer_regression()
    correction_constants()
    small_floor_bound()
    print("five-block self-prepend/terminal-layer certificate: PASS")


if __name__ == "__main__":
    main()
