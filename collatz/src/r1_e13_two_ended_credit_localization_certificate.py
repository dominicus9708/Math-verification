#!/usr/bin/env python3
"""Two-ended E=13 formation localization for bounded G13 entrance credits.

This certificate consumes the cutoff-free terminal automaton and the exact
G13 transition parent-credit identity

    Delta_gate = k * 2^(F-h),  F=5245.

For any bounded credit d<=397 that can pass the terminal E=13 3-adic filter,
a transition-section realization at width h must therefore satisfy

    2^(F-h) | d.

The exact surviving-credit counts collapse to the last nine transition widths:

    h=5237..5245 -> 1,3,6,10,16,31,64,125,247 credits.

No bounded terminally-admissible credit exists at h=5233..5236.  Across all
last-nine width/credit fibres only 503 labelled classes remain.

A separate exact left-end identity says that for two same-q E=13 pre-gate
paths with original-root difference Delta and entrance difference d,

    3^1526 Delta = 2^1539 d + C(P') - C(P).

If r is the earliest even-position symmetric difference between P and P',
then v2(C(P')-C(P))=r<1539, so v2(Delta)=r.  The independently established
root-credit bound 1<=Delta<=256 therefore forces r<=8.  Thus the left end is
also confined to the first nine accelerated positions.

This file certifies the finite width/credit intersections and records the
algebraic two-ended localization.  It is not a closure of E=13 or Collatz.
"""

from functools import lru_cache

MAX_CREDIT = 397
F = 5245


def block_sum(after: int, before: int) -> int:
    return (1 << (5 + before)) - (1 << (5 + after))


@lru_cache(maxsize=None)
def terminal_accepts(a: int, b: int, carry: int) -> bool:
    if carry == 0:
        return True
    if carry % 3 == 0:
        c2 = 2 * (carry // 3)
        if terminal_accepts(a, b, c2):
            return True
    for a2 in range(a + 1):
        aa = block_sum(a2, a)
        for b2 in range(b + 1):
            if a2 == a and b2 == b:
                continue
            bb = block_sum(b2, b)
            z = carry + bb - aa
            if z % 3 == 0 and terminal_accepts(a2, b2, 2 * (z // 3)):
                return True
    return False


def v2(n: int) -> int:
    r = 0
    while n % 2 == 0:
        n //= 2
        r += 1
    return r


def main() -> None:
    pre = [d for d in range(1, MAX_CREDIT + 1)
           if terminal_accepts(8, 8, (1 << 13) * d)]
    assert len(pre) == 247

    # Positive k upper bounds from the exact G13 survival-conditioned
    # transition theorem, widths h=5233,...,5245.
    kmax = {
        5233: 1, 5234: 3, 5235: 6, 5236: 13, 5237: 26,
        5238: 53, 5239: 107, 5240: 214, 5241: 428,
        5242: 856, 5243: 1713, 5244: 3428, 5245: 6859,
    }

    rows = []
    total = 0
    for h in range(5233, 5246):
        r = F - h
        vals = [
            d for d in pre
            if d % (1 << r) == 0 and d // (1 << r) <= kmax[h]
        ]
        rows.append((h, r, vals))
        total += len(vals)

    expected_counts = [0, 0, 0, 0, 1, 3, 6, 10, 16, 31, 64, 125, 247]
    assert [len(v) for _, _, v in rows] == expected_counts
    assert total == 503
    assert rows[4][2] == [256]
    assert rows[5][2] == [128, 256, 384]
    assert rows[6][2] == [64, 128, 192, 256, 320, 384]

    # The bounded-credit region can only appear once F-h<=8.
    assert all(len(v) == 0 for h, r, v in rows if r >= 9)
    assert all(h >= 5237 for h, r, v in rows if v)

    # Independent left-end consequence of 1<=Delta<=256:
    # the first symmetric event-position defect has r=v2(Delta)<=8.
    assert max(v2(delta) for delta in range(1, 257)) == 8

    print("E13 two-ended bounded-credit localization: PASS")
    print("h F-h surviving_terminal_credits")
    for h, r, vals in rows:
        print(h, r, len(vals), vals if len(vals) <= 16 else "")
    print("total width-credit fibres =", total)
    print("bounded transition repair requires h>=5237 (F-h<=8)")
    print("left pre-gate parity defect requires r_left<=8")


if __name__ == "__main__":
    main()
