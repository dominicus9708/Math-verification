#!/usr/bin/env python3
"""Audit single-macroblock periodic closures on the critical h,d line.

A macroblock 1^h 0^d has exact periodic closure
    x = (3^h - 2^h) / (2^(h+d) - 3^h).
For the least noncontracting critical debit
    d = ceil(h * log_2(3/2)),
the script checks exact integer divisibility.

The choice of d is computed by integer comparison, not floating point.
This is a finite audit, not a proof for all h.
"""


def critical_d(h: int) -> int:
    # Least d >= 1 such that 2^(h+d) > 3^h.
    three_h = 3 ** h
    d = 1
    while (1 << (h + d)) <= three_h:
        d += 1
    return d


def run(hmax: int = 5000) -> None:
    hits = []
    for h in range(1, hmax + 1):
        d = critical_d(h)
        D = (1 << (h + d)) - 3 ** h
        N = 3 ** h - (1 << h)
        if N % D == 0:
            hits.append((h, d, N // D))

    print(f"hmax={hmax}")
    print(f"integer_cycle_hits={len(hits)}")
    for h, d, x in hits:
        print(f"h={h},d={d},x={x}")


if __name__ == "__main__":
    import sys
    H = int(sys.argv[1]) if len(sys.argv) > 1 else 5000
    run(H)
