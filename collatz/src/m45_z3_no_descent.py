#!/usr/bin/env python3
"""Exact bit-vector SAT verifier for the m=45 recursively sufficient layer.

Layer:
    N = 4(3^45 + sum_{i=0}^{44} a_i 3^i) + 3,
    a_i in {0,1}.

The script asks whether any selector survives without a strict descent below its
own start through specified accelerated-Collatz depths:

    T(n)=n/2             for even n,
    T(n)=(3n+1)/2        for odd n.

Only the 45 selector bits are free.  The trajectory is a deterministic Z3
bit-vector circuit.  The chosen width is large enough for the mathematical
worst-case growth through MAX_H; Python exact integers independently recheck
any SAT model returned by Z3.

This is a finite computational certificate generator.  SAT means the tested
horizon does not close m=45.  UNSAT at a horizon H proves that no integer in
this finite m=45 layer can avoid descent through H.  This is not by itself a
proof of Collatz outside this layer.
"""

from __future__ import annotations

import argparse
from z3 import Bool, BitVecVal, If, LShR, Solver, UGE, sat, unsat

M = 45
POW3 = [3**i for i in range(M + 1)]
N_MIN = 4 * POW3[M] + 3
N_MAX = 4 * (POW3[M] + (POW3[M] - 1) // 2) + 3


def collatz_step_int(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def first_descent(n: int, limit: int) -> int | None:
    x = n
    for j in range(1, limit + 1):
        x = collatz_step_int(x)
        if x < n:
            return j
    return None


def selector_value(model, selectors) -> tuple[int, int]:
    mask = 0
    y = POW3[M]
    for i, a in enumerate(selectors):
        if bool(model.eval(a, model_completion=True)):
            mask |= 1 << i
            y += POW3[i]
    return 4 * y + 3, mask


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--milestones",
        default="200,300,400,500,600",
        help="comma-separated horizons checked incrementally",
    )
    args = ap.parse_args()
    milestones = sorted({int(x) for x in args.milestones.split(",") if x.strip()})
    if not milestones or milestones[0] <= 0:
        raise SystemExit("positive milestones required")

    max_h = milestones[-1]
    # All-odd accelerated growth is < (3/2)^H plus a geometric correction.
    # max_h extra bits is therefore a deliberately loose rigorous guard.
    width = N_MAX.bit_length() + max_h + 8

    sel = [Bool(f"a_{i}") for i in range(M)]
    zero = BitVecVal(0, width)
    n = BitVecVal(4 * POW3[M] + 3, width)
    for i, a in enumerate(sel):
        n = n + If(a, BitVecVal(4 * POW3[i], width), zero)

    s = Solver()
    x = n
    target_set = set(milestones)

    print("m45 exact Z3 no-descent verifier")
    print("N_min", N_MIN)
    print("N_max", N_MAX)
    print("width", width)

    for j in range(1, max_h + 1):
        odd = LShR(3 * x + BitVecVal(1, width), 1)
        even = LShR(x, 1)
        x = If((x & BitVecVal(1, width)) == BitVecVal(1, width), odd, even)
        s.add(UGE(x, n))

        if j not in target_set:
            continue

        status = s.check()
        print("H", j, "status", status)
        if status == unsat:
            print("first_unsat_milestone", j)
            return
        if status != sat:
            raise RuntimeError(f"unexpected solver status at H={j}: {status}")

        model = s.model()
        nv, mask = selector_value(model, sel)
        assert N_MIN <= nv <= N_MAX
        fd = first_descent(nv, j)
        assert fd is None, (j, nv, fd)
        print("witness_N", nv)
        print("witness_mask", mask)

    print("all requested milestones SAT")


if __name__ == "__main__":
    main()
