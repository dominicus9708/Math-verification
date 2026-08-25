#!/usr/bin/env python3
"""Exact coefficient-survival SAT verifier for the m=45 selector layer.

For the current m=45 layer, the separately certified coherent-ballot theorem
proves through H=301,993 that no-descent implies coefficient survival at every
prefix. The converse is immediate from

    2^j T^j(N) = 3^{q_j} N + R_j,   R_j >= 0.

Hence, throughout the certified range,

    T^j(N) >= N for all j<=H

is equivalent to

    3^{q_j} >= 2^j for all j<=H.

This script therefore removes every large unsigned comparison T^j(N)>=N from
the SAT circuit. It keeps only the exact selector construction, deterministic
parity evolution, and prefix odd-count thresholds. A SAT model is rechecked by
Python exact integer arithmetic.

UNSAT at H<=301,993 proves that every integer in this finite m=45 layer has a
strict descent by H. This is not a proof of Collatz outside the layer.
"""

from __future__ import annotations

import argparse

from z3 import Bool, BitVecVal, If, LShR, PbGe, Solver, sat, unsat, unknown

M = 45
H_EQUIV_MAX = 301_993
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


def coefficient_survives_int(n: int, H: int) -> bool:
    x = n
    q = 0
    p3 = 1
    p2 = 1
    for _ in range(H):
        b = x & 1
        if b:
            q += 1
            p3 *= 3
        p2 *= 2
        if p3 < p2:
            return False
        x = collatz_step_int(x)
    return True


def exact_safe_width(max_h: int) -> int:
    # Monotone all-odd affine branch dominates both accelerated branches and
    # also bounds every pre-shift 3*x+1 numerator used by the bit-vector circuit.
    x = N_MAX
    peak = x
    for _ in range(max_h):
        numerator = 3 * x + 1
        peak = max(peak, numerator)
        x = numerator // 2
    return peak.bit_length() + 1


def qmin_table(H: int) -> list[int]:
    out = [0] * (H + 1)
    q = 0
    p3 = 1
    p2 = 1
    for h in range(1, H + 1):
        p2 *= 2
        while p3 < p2:
            p3 *= 3
            q += 1
        out[h] = q
    return out


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
    ap.add_argument("--milestones", default="74,84,112,140,168,196,200")
    ap.add_argument("--timeout-ms", type=int, default=60_000)
    args = ap.parse_args()

    milestones = sorted({int(x) for x in args.milestones.split(",") if x.strip()})
    if not milestones or milestones[0] <= 0:
        raise SystemExit("positive milestones required")
    max_h = milestones[-1]
    if max_h > H_EQUIV_MAX:
        raise SystemExit("requested horizon exceeds coherent-ballot equivalence certificate")

    qmin = qmin_table(max_h)
    width = exact_safe_width(max_h)
    target = set(milestones)

    selectors = [Bool(f"a_{i}") for i in range(M)]
    zero = BitVecVal(0, width)
    n = BitVecVal(4 * POW3[M] + 3, width)
    for i, a in enumerate(selectors):
        n = n + If(a, BitVecVal(4 * POW3[i], width), zero)

    s = Solver()
    s.set(timeout=args.timeout_ms)
    x = n
    odd_bits = []

    print("m45 exact coefficient-survival Z3 verifier", flush=True)
    print("equivalence_certified_through", H_EQUIV_MAX, flush=True)
    print("N_min", N_MIN, flush=True)
    print("N_max", N_MAX, flush=True)
    print("width", width, flush=True)

    for j in range(1, max_h + 1):
        odd = (x & BitVecVal(1, width)) == BitVecVal(1, width)
        odd_bits.append(odd)
        odd_value = LShR(3 * x + BitVecVal(1, width), 1)
        even_value = LShR(x, 1)
        x = If(odd, odd_value, even_value)

        # q_min rises only by 0 or 1. Between rises q_j is nondecreasing while
        # the required threshold is constant, so it is sufficient and exact to
        # impose a prefix cardinality constraint only at each rise.
        if qmin[j] > qmin[j - 1]:
            s.add(PbGe([(b, 1) for b in odd_bits], qmin[j]))

        if j not in target:
            continue

        status = s.check()
        print("H", j, "status", status, flush=True)
        if status == sat:
            model = s.model()
            nv, mask = selector_value(model, selectors)
            assert N_MIN <= nv <= N_MAX
            assert coefficient_survives_int(nv, j)
            assert first_descent(nv, j) is None
            print("witness_N", nv, flush=True)
            print("witness_mask", mask, flush=True)
        elif status == unsat:
            print("first_unsat_milestone", j, flush=True)
            return
        elif status == unknown:
            print("reason_unknown", s.reason_unknown(), flush=True)
        else:
            raise RuntimeError(status)


if __name__ == "__main__":
    main()
