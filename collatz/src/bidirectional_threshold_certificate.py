#!/usr/bin/env python3
"""Bidirectional certificate for a proposed lower bound mu(K) >= X.

Forward side:
  propagate the exact target-specific quotient to split depth k, retaining the
  minimum canonical start r for each (q, y mod 2^(K-k)) signature.  States with
  r>=X are discarded because future lift costs are nonnegative.

Backward side:
  for each r<X, dangerous high-bit lifts are
      J = 0,...,ceil((X-r)/2^k)-1.
  The exact transformed interval-count recursion certifies whether any such
  lift survives the remaining coefficient barrier.

If all dangerous intervals are empty, mu(K)>=X is certified.  If a dangerous
interval is nonempty, the verifier locates the first admissible lift and returns
an explicit start n<X that survives through K.

Run from collatz/src so sibling modules are importable.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass

from finite_horizon_quotient import State, child, qmins, pow3s
from interval_count_certificate import IntervalCounter


@dataclass(frozen=True)
class FailureWitness:
    split_r: int
    q: int
    eta: int
    J: int
    n: int


def forward_representatives(K: int, ksplit: int, X: int) -> list[State]:
    """Exact D_k representatives relevant to starts below X."""
    qmin = qmins(K)
    p3 = pow3s(K)
    current = [State(0, 0, 0)]

    for k in range(ksplit):
        remaining = K - (k + 1)
        modulus = 1 << remaining if remaining else 1
        groups: dict[tuple[int, int], State] = {}

        for s in current:
            for b in (0, 1):
                t = child(s, k, b, p3)
                if t.q < qmin[k + 1]:
                    continue
                if t.r >= X:
                    continue
                key = (t.q, t.y % modulus if remaining else 0)
                old = groups.get(key)
                if old is None or t.r < old.r:
                    groups[key] = t

        current = list(groups.values())

    return current


def first_point(counter: IntervalCounter, k: int, q: int, m: int, xi: int, L: int) -> int:
    """Least J in [0,L) with a transformed admissible point at xi+J."""
    assert L > 0
    assert counter.count(k, q, m, xi, L) > 0

    lo, hi = 0, L
    # count(xi,t)>0 is monotone in t.
    while lo + 1 < hi:
        mid = (lo + hi) // 2
        if counter.count(k, q, m, xi, mid) > 0:
            hi = mid
        else:
            lo = mid

    # hi is the first positive interval length, so the point offset is hi-1.
    if counter.count(k, q, m, xi, 1) > 0:
        return 0
    return hi - 1


def survives_K(n: int, K: int) -> bool:
    x = n
    q = 0
    for j in range(1, K + 1):
        if x & 1:
            q += 1
            x = (3 * x + 1) // 2
        else:
            x //= 2
        if 3 ** q < 1 << j:
            return False
    return True


def certify(K: int, X: int, ksplit: int) -> tuple[bool, list[State], FailureWitness | None]:
    if not (0 <= ksplit <= K):
        raise ValueError("require 0 <= split <= K")
    if X < 1:
        raise ValueError("X must be positive")

    reps = forward_representatives(K, ksplit, X)
    m = K - ksplit
    M = 1 << m
    counter = IntervalCounter(K + 4)

    for s in sorted(reps, key=lambda z: z.r):
        # ceil((X-r)/2^k), with positive numerator because r<X.
        den = 1 << ksplit
        L = (X - s.r + den - 1) // den
        if L <= 0:
            continue

        eta = s.y % M
        inv = 1 if m == 0 else pow(3 ** s.q, -1, M)
        xi = 0 if m == 0 else (inv * eta) % M
        cnt = counter.count(ksplit, s.q, m, xi, L)
        if cnt > 0:
            J = first_point(counter, ksplit, s.q, m, xi, L)
            n = s.r + den * J
            assert n < X
            assert survives_K(n, K)
            return False, reps, FailureWitness(s.r, s.q, eta, J, n)

    return True, reps, None


def self_test() -> None:
    tests = [
        (30, 27, 15, True, None),
        (30, 28, 15, False, 27),
        (100, 10087, 15, True, None),
        (100, 10088, 15, False, 10087),
    ]
    for K, X, k, want_ok, want_n in tests:
        ok, reps, witness = certify(K, X, k)
        assert ok == want_ok, (K, X, ok, want_ok)
        if want_n is not None:
            assert witness is not None
            assert witness.n == want_n, (K, X, witness.n, want_n)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("K", type=int, nargs="?", default=100)
    ap.add_argument("X", type=int, nargs="?", default=10087)
    ap.add_argument("--split", type=int, default=None)
    ap.add_argument("--self-test", action="store_true")
    args = ap.parse_args()

    if args.self_test:
        self_test()
        print("self_test=PASS")
        return

    k = args.split
    if k is None:
        # Natural threshold-certificate split: expose enough low bits that a
        # candidate below X has at most a one-point dangerous high-lift interval.
        k = min(args.K, max(0, (args.X - 1).bit_length()))

    ok, reps, witness = certify(args.K, args.X, k)
    print(f"K={args.K},X={args.X},split={k},forward_representatives={len(reps)}")
    if ok:
        print(f"CERTIFIED: mu({args.K}) >= {args.X}")
    else:
        assert witness is not None
        print("FAILED: explicit coefficient-surviving witness below X")
        print(
            f"n={witness.n},split_r={witness.split_r},q={witness.q},"
            f"eta={witness.eta},J={witness.J}"
        )


if __name__ == "__main__":
    main()
