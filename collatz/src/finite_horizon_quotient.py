#!/usr/bin/env python3
"""Exact finite-horizon quotient for coefficient-surviving Collatz prefixes.

Accelerated map:
    T(n)=n/2          if n is even
    T(n)=(3n+1)/2     if n is odd

Canonical prefix state at depth k:
    (r,q,y)
where r is the canonical start residue in [0,2^k), q is the odd-count,
and y=T^k(r).

For a fixed target depth K and remaining horizon m=K-k, the proved quotient is:

    same q,
    y1 == y2 (mod 2^m),
    r1 <= r2

=> state 1 dominates state 2 for this target horizon.

Reason: every common future parity suffix of length m produces the same
canonical lift/carry bits, hence the same additive start increment.  Future
coefficient-barrier decisions also coincide because q evolves identically.

This program:
  1. reproduces the exact counterexample to the older all-future same-endpoint
     dominance claim;
  2. performs small exhaustive tests of the finite-horizon signature;
  3. computes mu(K) by the exact target-specific quotient.

All arithmetic is Python arbitrary-precision integer arithmetic.  The program
is a verifier for the derived lemma, not a proof of Collatz convergence.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from dataclasses import dataclass
from itertools import product


@dataclass(frozen=True)
class State:
    r: int
    q: int
    y: int


def qmins(K: int) -> list[int]:
    """a[k] = least q with 3**q >= 2**k, exactly."""
    out = [0] * (K + 1)
    p3 = 1
    q = 0
    for k in range(1, K + 1):
        while p3 < (1 << k):
            p3 *= 3
            q += 1
        out[k] = q
    return out


def pow3s(K: int) -> list[int]:
    out = [1] * (K + 2)
    for q in range(1, K + 2):
        out[q] = 3 * out[q - 1]
    return out


def child(state: State, k: int, b: int, p3: list[int]) -> State:
    """Canonical child with requested next parity b in {0,1}."""
    c = b ^ (state.y & 1)
    r = state.r + c * (1 << k)
    y = state.y + c * p3[state.q]
    q = state.q
    if b == 0:
        y //= 2
    else:
        y = (3 * y + 1) // 2
        q += 1
    return State(r, q, y)


def descendants(
    state: State,
    k: int,
    m: int,
    qmin: list[int],
    p3: list[int],
) -> dict[str, State]:
    """All coefficient-surviving length-m descendants, keyed by suffix."""
    cur: dict[str, State] = {"": state}
    for j in range(m):
        nxt: dict[str, State] = {}
        for path, s in cur.items():
            for b in (0, 1):
                t = child(s, k + j, b, p3)
                if t.q >= qmin[k + j + 1]:
                    nxt[path + str(b)] = t
        cur = nxt
    return cur


def generate_levels(K: int) -> list[list[State]]:
    qmin = qmins(K)
    p3 = pow3s(K)
    levels: list[list[State]] = [[State(0, 0, 0)]]
    for k in range(K):
        nxt: list[State] = []
        for s in levels[-1]:
            for b in (0, 1):
                t = child(s, k, b, p3)
                if t.q >= qmin[k + 1]:
                    nxt.append(t)
        levels.append(nxt)
    return levels


def endpoint_counterexample() -> None:
    """Reproduce the k=10, horizon-5 failure of global endpoint dominance."""
    k = 10
    m = 5
    qmin = qmins(k + m)
    p3 = pow3s(k + m)
    s1 = State(127, 8, 820)
    s2 = State(383, 7, 820)

    d1 = descendants(s1, k, m, qmin, p3)
    d2 = descendants(s2, k, m, qmin, p3)
    p1, t1 = min(d1.items(), key=lambda kv: kv[1].r)
    p2, t2 = min(d2.items(), key=lambda kv: kv[1].r)

    assert (p1, t1.r, t1.q, t1.y) == ("01101", 2175, 11, 11765)
    assert (p2, t2.r, t2.q, t2.y) == ("11111", 1407, 12, 22841)
    assert t2.r < t1.r

    print("endpoint_counterexample=PASS")
    print(f"S1_best={t1.r},suffix={p1},q={t1.q},y={t1.y}")
    print(f"S2_best={t2.r},suffix={p2},q={t2.q},y={t2.y}")


def exhaustive_signature_test(max_k: int = 8, max_m: int = 4) -> None:
    """Exhaustively test the proved same-q finite-horizon signature."""
    levels = generate_levels(max_k + max_m)
    tested_pairs = 0

    for k in range(1, max_k + 1):
        for m in range(1, max_m + 1):
            qmin = qmins(k + m)
            p3 = pow3s(k + m)
            modulus = 1 << m
            states = levels[k]

            groups: dict[tuple[int, int], list[State]] = defaultdict(list)
            for s in states:
                groups[(s.q, s.y % modulus)].append(s)

            for group in groups.values():
                if len(group) < 2:
                    continue
                group.sort(key=lambda s: s.r)
                base = group[0]
                A = descendants(base, k, m, qmin, p3)
                for other in group[1:]:
                    B = descendants(other, k, m, qmin, p3)
                    assert A.keys() == B.keys()
                    for path in A:
                        assert A[path].r <= B[path].r
                        assert B[path].r - A[path].r == other.r - base.r
                    tested_pairs += 1

    print(f"finite_horizon_signature=PASS,tested_pairs={tested_pairs}")


def quotient_mu(K: int) -> tuple[int, list[int]]:
    """Compute mu(K) with the exact same-q finite-horizon quotient.

    At the end of depth k, remaining horizon is m=K-k.  Group by
        (q, y mod 2^m)
    and retain the state with smallest r in each group.
    """
    if K < 1:
        raise ValueError("K must be positive")

    qmin = qmins(K)
    p3 = pow3s(K)
    current = [State(0, 0, 0)]
    counts: list[int] = []

    for k in range(K):
        remaining = K - (k + 1)
        modulus = 1 << remaining if remaining else 1
        groups: dict[tuple[int, int], State] = {}

        for s in current:
            for b in (0, 1):
                t = child(s, k, b, p3)
                if t.q < qmin[k + 1]:
                    continue
                key = (t.q, t.y % modulus if remaining else 0)
                old = groups.get(key)
                if old is None or t.r < old.r:
                    groups[key] = t

        current = list(groups.values())
        counts.append(len(current))

    return min(s.r for s in current), counts


def known_small_checks() -> None:
    """Cross-check target-specific quotient against exact known mu plateaus."""
    expected = {
        5: 7,
        6: 7,
        7: 27,
        10: 27,
        20: 27,
        25: 27,
    }
    for K, want in expected.items():
        got, counts = quotient_mu(K)
        assert got == want, (K, got, want)
        print(f"K={K},mu={got},max_quotient_states={max(counts)}")
    print("known_small_mu=PASS")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--K", type=int, default=0,
                    help="also compute target-specific quotient mu(K)")
    ap.add_argument("--skip-self-test", action="store_true")
    args = ap.parse_args()

    if not args.skip_self_test:
        endpoint_counterexample()
        exhaustive_signature_test()
        known_small_checks()

    if args.K:
        mu, counts = quotient_mu(args.K)
        print(f"target_K={args.K},mu={mu},max_quotient_states={max(counts)}")
        print("depth,state_count")
        for k, n in enumerate(counts, 1):
            print(f"{k},{n}")


if __name__ == "__main__":
    main()
