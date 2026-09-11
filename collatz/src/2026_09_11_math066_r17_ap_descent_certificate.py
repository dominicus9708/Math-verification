#!/usr/bin/env python3
"""
MATH-066 partial exact audit of the r=17 multi-paid layer.

This continues MATH-065 without materializing every ordinary target.
The r=17 branch is substantially larger than r=18, so completed negative
cylinders are retained as arithmetic progressions

    n = a + b k,  0 <= k < count,

with b an odd power of 3.  The shortcut Collatz map preserves this form after
splitting k by parity.  Thus an entire target progression can be continued
exactly without enumerating every member.

Certified here:
  * exact r=17 workload counts;
  * all singleton negative-candidate cylinders descend to the frozen floor;
  * every negative-candidate cylinder of multiplicity >=1024 descends as an
    exact arithmetic-progression family.

The remaining multiplicity range 2..1023 is OPEN.  Therefore this certificate
does not close r=17, the first universal cell, or Collatz.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math065", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

LO = 1 << 71
BIG = 1024


def ap_descent(a: int, b: int, count: int, max_depth: int = 1000):
    """Exact descent of P={a+b*k:0<=k<count}, with b odd positive.

    At each shortcut step, k parity fixes endpoint parity because b is odd.
    Writing k=r+2s preserves the arithmetic-progression form:

      even branch: (a+b*r)/2 + b*s,
      odd branch : (3(a+b*r)+1)/2 + 3*b*s.

    Values already <=LO form an initial segment because b>0 and are trimmed
    without affecting the remaining lineage.
    """
    states = [(a, b, count)]
    nodes = 0
    max_live = 1

    for depth in range(max_depth + 1):
        nxt = []
        for a0, b0, c0 in states:
            nodes += 1
            if c0 <= 0:
                continue

            if a0 <= LO:
                t = (LO - a0) // b0
                if t >= c0 - 1:
                    continue
                drop = max(0, t + 1)
                a0 += b0 * drop
                c0 -= drop

            for r in (0, 1):
                if r >= c0:
                    continue
                c1 = (c0 - 1 - r) // 2 + 1
                base = a0 + b0 * r
                if base % 2 == 0:
                    a1 = base // 2
                    b1 = b0
                else:
                    a1 = (3 * base + 1) // 2
                    b1 = 3 * b0
                nxt.append((a1, b1, c1))

        if not nxt:
            return True, depth + 1, nodes, max_live
        states = nxt
        max_live = max(max_live, len(states))

    return False, max_depth, nodes, max_live


def singleton_descent(n: int, cache: dict[int, int]):
    x = n
    path = []
    seen = set()
    while x > LO and x not in cache:
        if x in seen:
            return None
        seen.add(x)
        path.append(x)
        x = m65.shortcut(x)
        assert len(path) < 10000

    d = 0 if x <= LO else cache[x]
    for v in reversed(path):
        d += 1
        cache[v] = d
    return cache.get(n, 0)


def main():
    total, safe, singleton_cells, critical = m65.classify_cells(17)
    assert (total, len(safe), len(singleton_cells), len(critical)) == (
        1090, 256, 596, 238
    )

    negative_cylinders = 0
    target_multiplicity = 0
    branch_nodes = 0
    min_target = None
    max_target = 0

    singleton_count = 0
    singleton_cache = {}
    singleton_max_descent = 0

    big_count = 0
    big_multiplicity = 0
    big_nodes = 0
    big_max_depth = 0
    big_max_nodes = 0
    big_max_live = 0

    for group in (singleton_cells, critical):
        for cell in group:
            leaves, nodes = m65.negative_candidate_cylinders(cell, 17)
            branch_nodes += nodes

            for first, count, tres, mod, yres, coeff in leaves:
                negative_cylinders += 1
                target_multiplicity += count
                base_s = (first - tres) // mod
                target0 = yres + coeff * base_s
                target1 = target0 + coeff * (count - 1)
                min_target = target0 if min_target is None else min(min_target, target0)
                max_target = max(max_target, target1)

                if count == 1:
                    singleton_count += 1
                    d = singleton_descent(target0, singleton_cache)
                    assert d is not None
                    singleton_max_descent = max(singleton_max_descent, d)

                if count >= BIG:
                    big_count += 1
                    big_multiplicity += count
                    ok, depth, nodes2, live = ap_descent(target0, coeff, count)
                    assert ok
                    big_nodes += nodes2
                    big_max_depth = max(big_max_depth, depth)
                    big_max_nodes = max(big_max_nodes, nodes2)
                    big_max_live = max(big_max_live, live)

    assert branch_nodes == 42_482_287
    assert negative_cylinders == 1_728_083
    assert target_multiplicity == 38_457_239
    assert min_target == 2_361_183_794_064_906_256_279
    assert max_target == 6_290_338_245_370_917_570_478

    assert singleton_count == 1_013_728
    assert singleton_max_descent == 258

    assert big_count == 4_086
    assert big_multiplicity == 17_143_582
    assert big_nodes == 22_556_393
    assert big_max_depth == 341
    assert big_max_nodes == 130_273
    assert big_max_live == 8_048

    closed_occurrences = singleton_count + big_multiplicity
    remaining_occurrences = target_multiplicity - closed_occurrences
    remaining_cylinders = negative_cylinders - singleton_count - big_count

    assert closed_occurrences == 18_157_310
    assert remaining_occurrences == 20_299_929
    assert remaining_cylinders == 710_269

    print("r17_cells", total, len(safe), len(singleton_cells), len(critical))
    print("r17_branch_nodes", branch_nodes)
    print("r17_negative_cylinders", negative_cylinders)
    print("r17_target_multiplicity", target_multiplicity)
    print("r17_target_range", min_target, max_target)
    print("r17_singletons_closed", singleton_count, "max_descent", singleton_max_descent)
    print("r17_large_AP_closed", big_count, "multiplicity", big_multiplicity)
    print("r17_large_AP_nodes", big_nodes, "max_depth", big_max_depth,
          "max_single_AP_nodes", big_max_nodes, "max_live", big_max_live)
    print("r17_remaining_cylinders", remaining_cylinders)
    print("r17_remaining_occurrences", remaining_occurrences)
    print("OPEN multiplicity range: 2..1023")
    print("PASS MATH-066 partial r=17 AP descent certificate")


if __name__ == "__main__":
    main()
