#!/usr/bin/env python3
"""Audit the exact prefix/filter-state representation against direct Collatz iteration.

This is a finite implementation audit, not a convergence proof.
"""

from dataclasses import dataclass
from fractions import Fraction
from typing import Optional


def T(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


@dataclass(frozen=True)
class PrefixState:
    k: int
    q: int
    R: int
    theta: Optional[Fraction]  # None = +infinity


def formation_floor(st: PrefixState) -> int:
    if st.k == 0:
        return 2
    mod = 1 << st.k
    inv = pow(3 ** st.q, -1, mod)
    r = (-inv * st.R) % mod
    if r >= 2:
        return r
    if r == 0:
        return mod
    return 1 + mod


def child(st: PrefixState, p: int) -> Optional[PrefixState]:
    k2 = st.k + 1
    q2 = st.q + p
    R2 = (3 if p else 1) * st.R + ((1 << st.k) if p else 0)

    theta2 = st.theta
    if 3 ** q2 < (1 << k2):
        current = Fraction(R2, (1 << k2) - 3 ** q2)
        if theta2 is None or current < theta2:
            theta2 = current

    out = PrefixState(k2, q2, R2, theta2)
    rho = formation_floor(out)
    if theta2 is not None and Fraction(rho, 1) > theta2:
        return None
    return out


def represented_up_to(states: list[PrefixState], limit: int) -> set[int]:
    out: set[int] = set()
    for st in states:
        rho = formation_floor(st)
        step = 1 << st.k if st.k else 1
        n = rho
        while n <= limit:
            if st.theta is None or n <= st.theta:
                out.add(n)
            n += step
    return out


def direct_unresolved(k: int, limit: int) -> set[int]:
    out: set[int] = set()
    for n in range(2, limit + 1):
        x = n
        ok = True
        for _ in range(k):
            x = T(x)
            if x < n:
                ok = False
                break
        if ok:
            out.add(n)
    return out


def run(max_depth: int = 16, limit: int = 20000) -> None:
    states = [PrefixState(0, 0, 0, None)]
    print("k,states,represented,direct,match,frontier")

    for k in range(max_depth + 1):
        represented = represented_up_to(states, limit)
        direct = direct_unresolved(k, limit)
        frontier = min(represented) if represented else ""
        print(
            f"{k},{len(states)},{len(represented)},{len(direct)},"
            f"{represented == direct},{frontier}"
        )

        if represented != direct:
            missing = sorted(direct - represented)[:20]
            extra = sorted(represented - direct)[:20]
            raise AssertionError(f"mismatch at depth {k}: missing={missing}, extra={extra}")

        if k == max_depth:
            break

        nxt: list[PrefixState] = []
        for st in states:
            for p in (0, 1):
                ch = child(st, p)
                if ch is not None:
                    nxt.append(ch)
        states = nxt


if __name__ == "__main__":
    import sys

    K = int(sys.argv[1]) if len(sys.argv) > 1 else 16
    N = int(sys.argv[2]) if len(sys.argv) > 2 else 20000
    run(K, N)
