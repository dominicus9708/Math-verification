#!/usr/bin/env python3
"""Exact certificate: consecutive v2(3n+1)=1 runs are unbounded.

For odd n ≡ 3 (mod 4), define the single-halving odd-to-odd step
    S(n) = (3n+1)/2
when v2(3n+1)=1.
One has the exact countdown identity
    v2(S(n)+1) = v2(n+1)-1.
Hence n0 = 2^r-1 has r-1 consecutive single-halving steps.
This refutes any universal fixed-K claim that every K consecutive accelerated
odd Collatz steps must contain one with v2(3n+1) >= 2.
"""


def v2(n: int) -> int:
    c = 0
    while n % 2 == 0:
        n //= 2
        c += 1
    return c


def single_step(n: int) -> int:
    assert n % 2 == 1
    a = v2(3*n + 1)
    assert a == 1
    return (3*n + 1) // 2


def check(r: int):
    n = (1 << r) - 1
    start = n
    rows = []
    for j in range(r - 1):
        assert v2(n + 1) == r - j
        assert v2(3*n + 1) == 1
        nxt = single_step(n)
        assert v2(nxt + 1) == v2(n + 1) - 1
        rows.append((j, n, nxt))
        n = nxt
    # After r-1 single-halving steps the countdown reaches v2(n+1)=1;
    # the next accelerated odd step has at least two halving factors.
    assert v2(n + 1) == 1
    assert v2(3*n + 1) >= 2
    return start, n, rows


def main():
    # K=21 is defeated by r=22 already: there are r-1=21 consecutive
    # accelerated odd steps with valuation exactly 1.
    r = 22
    start, last, rows = check(r)
    assert len(rows) == 21
    print("SAFE exact counterexample to any fixed K=21 valuation-window lemma")
    print("start n = 2^22 - 1 =", start)
    print("consecutive v2(3n+1)=1 steps =", len(rows))
    print("state after run =", last)
    print("next valuation =", v2(3*last + 1))

    # Regression: arbitrary longer runs.
    for r in range(2, 41):
        _, _, rr = check(r)
        assert len(rr) == r - 1
    print("unbounded-run family verified for r=2..40; algebra proves all r>=2")


if __name__ == "__main__":
    main()
