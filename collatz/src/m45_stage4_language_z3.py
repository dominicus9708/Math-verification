#!/usr/bin/env python3
"""Exact SAT audit for the current m=45 Stage-4 minimal-counterexample core.

Current necessary conditions:
- m=45 recursively sufficient selector layer;
- exact coefficient survival q_j >= ceil(j log_3 2) at every prefix;
- every complete aligned 7-step block is one of the 69 full-Hensel
  residue-maximal L7 words used by the Stage-4 coarse language;
- at depth 28 the first defect from the exact mechanical boundary is in
  p in {2,5,8,10}, the ordinary m=45 channels left after the previously
  certified first-defect closures.

For this m=45 layer, the coherent-ballot certificate proves through H=301,993
that no-descent implies coefficient survival. The converse follows immediately
from the positive affine correction. Therefore coefficient survival and
no-descent are equivalent throughout every horizon used here, and no separate
UGE(T^j(N),N) solver is required.

SAT means a candidate remains after these necessary minimal-counterexample
filters. UNSAT closes this already-pruned m=45 core through the tested horizon,
when combined with the previously certified first-defect closures. UNKNOWN is
non-conclusive. This is finite computation, not a proof of Collatz globally.
"""

from __future__ import annotations

import argparse
from collections import defaultdict

from z3 import And, Bool, BitVecVal, If, LShR, Not, Or, PbGe, Solver, sat, unsat, unknown

M = 45
H_EQUIV_MAX = 301_993
POW3 = [3**i for i in range(M + 1)]
N_MIN = 4 * POW3[M] + 3
N_MAX = 4 * (POW3[M] + (POW3[M] - 1) // 2) + 3
REMAINING_FIRST_DEFECTS = (2, 5, 8, 10)


def collatz_step_int(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def first_descent(n: int, limit: int) -> int | None:
    x = n
    for j in range(1, limit + 1):
        x = collatz_step_int(x)
        if x < n:
            return j
    return None


def parity_prefix_int(n: int, H: int) -> list[int]:
    x = n
    out = []
    for _ in range(H):
        b = x & 1
        out.append(b)
        x = collatz_step_int(x)
    return out


def exact_safe_width(max_h: int) -> int:
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


def mechanical_bits(H: int) -> list[int]:
    qmin = qmin_table(H)
    return [qmin[h + 1] - qmin[h] for h in range(H)]


def correction(bits: tuple[int, ...]) -> tuple[int, int]:
    R = 0
    q = 0
    for k, b in enumerate(bits):
        if b:
            R = 3 * R + (1 << k)
            q += 1
    return q, R


def l7_residue_maximal_words() -> tuple[tuple[int, ...], ...]:
    groups: dict[tuple[int, int], list[tuple[int, tuple[int, ...]]]] = defaultdict(list)
    for mask in range(1 << 7):
        bits = tuple((mask >> k) & 1 for k in range(7))
        q, R = correction(bits)
        groups[(q, R % (3**q))].append((R, bits))
    out = []
    counts = [0] * 8
    for (q, _), arr in groups.items():
        _R, bits = max(arr)
        out.append(bits)
        counts[q] += 1
    assert tuple(counts) == (1, 2, 6, 15, 21, 16, 7, 1)
    assert len(out) == 69
    return tuple(out)


def selector_value(model, selectors) -> tuple[int, int]:
    mask = 0
    y = POW3[M]
    for i, a in enumerate(selectors):
        if bool(model.eval(a, model_completion=True)):
            mask |= 1 << i
            y += POW3[i]
    return 4 * y + 3, mask


def word_constraint(bits, allowed_words):
    choices = []
    for word in allowed_words:
        choices.append(And(*[(b if bit else Not(b)) for b, bit in zip(bits, word)]))
    return Or(*choices)


def first_defect_constraint(bits, mechanical):
    choices = []
    for p in REMAINING_FIRST_DEFECTS:
        prefix = [bits[i] if mechanical[i] else Not(bits[i]) for i in range(p)]
        defect = Not(bits[p]) if mechanical[p] else bits[p]
        choices.append(And(*prefix, defect))
    return Or(*choices)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--milestones", default="28,74,84,112")
    ap.add_argument("--timeout-ms", type=int, default=60_000)
    args = ap.parse_args()

    milestones = sorted({int(x) for x in args.milestones.split(",") if x.strip()})
    if not milestones or milestones[0] < 28:
        raise SystemExit("milestones must start at H>=28")
    max_h = milestones[-1]
    if max_h > H_EQUIV_MAX:
        raise SystemExit("requested horizon exceeds coherent-ballot equivalence certificate")
    target = set(milestones)

    qmin = qmin_table(max_h)
    mechanical = mechanical_bits(max_h)
    allowed_l7 = l7_residue_maximal_words()
    width = exact_safe_width(max_h)

    expected28 = "1101101101011011010110110110"
    assert "".join(map(str, mechanical[:28])) == expected28

    selectors = [Bool(f"a_{i}") for i in range(M)]
    zero = BitVecVal(0, width)
    n = BitVecVal(4 * POW3[M] + 3, width)
    for i, a in enumerate(selectors):
        n = n + If(a, BitVecVal(4 * POW3[i], width), zero)

    x = n
    odd_bits = []
    solver = Solver()
    solver.set(timeout=args.timeout_ms)

    print("m45 Stage-4 necessary-language Z3 verifier", flush=True)
    print("equivalence_certified_through", H_EQUIV_MAX, flush=True)
    print("N_min", N_MIN, flush=True)
    print("N_max", N_MAX, flush=True)
    print("width", width, flush=True)
    print("L7_words", len(allowed_l7), flush=True)
    print("remaining_first_defects", REMAINING_FIRST_DEFECTS, flush=True)

    for j in range(1, max_h + 1):
        odd = (x & BitVecVal(1, width)) == BitVecVal(1, width)
        odd_bits.append(odd)
        odd_value = LShR(3 * x + BitVecVal(1, width), 1)
        even_value = LShR(x, 1)
        x = If(odd, odd_value, even_value)

        # Exact coefficient-survival constraints are required only at Beatty
        # rises: q_j is nondecreasing and q_min is constant between rises.
        if qmin[j] > qmin[j - 1]:
            solver.add(PbGe([(b, 1) for b in odd_bits], qmin[j]))

        if j % 7 == 0:
            solver.add(word_constraint(odd_bits[j - 7 : j], allowed_l7))

        if j == 28:
            solver.add(first_defect_constraint(odd_bits[:28], mechanical[:28]))

        if j not in target:
            continue

        status = solver.check()
        print("H", j, "status", status, flush=True)
        if status == sat:
            model = solver.model()
            nv, mask = selector_value(model, selectors)
            bits = parity_prefix_int(nv, j)
            assert all(sum(bits[:h]) >= qmin[h] for h in range(1, j + 1))
            assert first_descent(nv, j) is None
            print("witness_N", nv, flush=True)
            print("witness_mask", mask, flush=True)
        elif status == unsat:
            print("first_unsat_milestone", j, flush=True)
            return
        elif status == unknown:
            print("reason_unknown", solver.reason_unknown(), flush=True)
        else:
            raise RuntimeError(status)


if __name__ == "__main__":
    main()
