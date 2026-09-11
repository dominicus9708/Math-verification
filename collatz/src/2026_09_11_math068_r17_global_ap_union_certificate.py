#!/usr/bin/env python3
"""
MATH-068 exact closure certificate for the remaining r=17 medium-multiplicity core.

This continues MATH-067.  The remaining negative-candidate cylinders have
65 <= multiplicity <= 1023.  Instead of continuing each macro lineage
independently, completed macro targets are treated as finite ordinary-integer
sets represented by arithmetic progressions

    P(a,b,m) = {a + b*k : 0 <= k < m},

with b odd.  Once a macro is complete, two representations may be merged only
when they represent the same ordinary target grid and overlapping/adjacent
parameter intervals.  Singleton states are canonicalized to (a,1,1), because
for the one-element set {a} the historical AP step carries no future Collatz
information.

At every shortcut depth the certificate performs the exact set operations:
  1. trim every initial AP segment already <= 2^71;
  2. split parameter k by parity;
  3. apply the shortcut map exactly to each branch;
  4. union overlapping/adjacent intervals on the same (b, a mod b) grid;
  5. canonicalize singleton ordinary integers and merge identical values.

No density or probabilistic inference is used.  The union becomes empty after
all surviving targets reach the frozen verification floor.  Exact maximum
additional shortcut length is 334.

This closes the r=17 paid-count layer only for the current first-cell
minimal-counterexample calculation.  It does not close r<=16, the first
universal Farey cell, later cells, or the Collatz conjecture.
"""
from collections import defaultdict
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
R = 17
MIN_M = 65
MAX_M = 1023


def medium_cylinders():
    total, safe, singleton_cells, critical = m65.classify_cells(R)
    assert (total, len(safe), len(singleton_cells), len(critical)) == (
        1090, 256, 596, 238
    )

    out = []
    branch_nodes = 0
    all_negative = 0
    all_occurrences = 0

    for group in (singleton_cells, critical):
        for cell in group:
            leaves, nodes = m65.negative_candidate_cylinders(cell, R)
            branch_nodes += nodes
            for first, count, tres, mod, yres, coeff in leaves:
                all_negative += 1
                all_occurrences += count
                if not (MIN_M <= count <= MAX_M):
                    continue
                base_s = (first - tres) // mod
                target0 = yres + coeff * base_s
                out.append((target0, coeff, count))

    assert branch_nodes == 42_482_287
    assert all_negative == 1_728_083
    assert all_occurrences == 38_457_239
    assert len(out) == 76_866
    assert sum(m for _, _, m in out) == 14_980_075
    return out


def merge_aps(states):
    """Exact union on identical arithmetic grids.

    A singleton is represented canonically with step 1.  For m>1, write
    a = r + b*k0.  States with the same (b,r) are interval-unioned in k.
    """
    grids = defaultdict(list)
    for a, b, m in states:
        assert b > 0 and m > 0
        if m == 1:
            b = 1
        r = a % b
        k0 = (a - r) // b
        grids[(b, r)].append((k0, k0 + m - 1))

    out = []
    for (b, r), intervals in grids.items():
        intervals.sort()
        lo, hi = intervals[0]
        for a0, a1 in intervals[1:]:
            if a0 <= hi + 1:
                hi = max(hi, a1)
            else:
                out.append((r + b * lo, b, hi - lo + 1))
                lo, hi = a0, a1
        out.append((r + b * lo, b, hi - lo + 1))
    return out


def advance(states):
    children = []
    for a, b, m in states:
        # Since b>0, values <=LO form an initial parameter segment.
        if a <= LO:
            t = (LO - a) // b
            if t >= m - 1:
                continue
            drop = max(0, t + 1)
            a += b * drop
            m -= drop

        # b is odd for every non-singleton state produced by the Collatz
        # affine recursion.  Parameter parity therefore fixes value parity.
        for rho in (0, 1):
            if rho >= m:
                continue
            count = (m - 1 - rho) // 2 + 1
            base = a + b * rho
            if base % 2 == 0:
                a1 = base // 2
                b1 = b
            else:
                a1 = (3 * base + 1) // 2
                b1 = 3 * b
            if count == 1:
                b1 = 1
            children.append((a1, b1, count))

    return merge_aps(children) if children else []


def stats(states):
    if not states:
        return (0, 0, 0, None, None)
    return (
        len(states),
        sum(m for _, _, m in states),
        sum(m == 1 for _, _, m in states),
        min(a for a, _, _ in states),
        max(a + b * (m - 1) for a, b, m in states),
    )


CHECKPOINTS = {
    0: (70_426, 13_995_185, 0,
        2_361_183_794_064_906_256_279,
        6_290_338_245_370_917_570_478),
    1: (140_852, 13_995_185, 0,
        1_180_592_619_018_657_270_055,
        9_435_484_325_167_431_025_232),
    2: (145_410, 7_208_877, 0,
        1_180_592_619_018_657_270_055,
        14_153_220_981_653_974_380_125),
    10: (1_259_308, 1_259_308, 1_259_308,
         1_180_595_215_747_810_745_341,
         362_688_062_596_239_073_743_881),
    120: (1_929, 1_929, 1_929,
          1_188_473_844_486_404_714_020,
          920_812_149_362_291_464_916_543_591),
    307: (2, 2, 2,
          7_890_219_206_343_879_287_219,
          15_713_926_437_629_109_428_662),
    315: (1, 1, 1,
          14_915_953_610_718_256_215_490,
          14_915_953_610_718_256_215_490),
    333: (1, 1, 1,
          3_359_879_092_251_977_200_580,
          3_359_879_092_251_977_200_580),
    334: (1, 1, 1,
          1_679_939_546_125_988_600_290,
          1_679_939_546_125_988_600_290),
    335: (0, 0, 0, None, None),
}


def main():
    raw = medium_cylinders()
    states = merge_aps(raw)

    # Same-grid exact union removes duplicate representations before any
    # dynamical inference.  Cross-grid overlaps need not be guessed here;
    # they are automatically merged when they reach identical singleton values.
    assert stats(states) == CHECKPOINTS[0]

    reached_floor_at = None
    for depth in range(0, 336):
        if depth in CHECKPOINTS:
            assert stats(states) == CHECKPOINTS[depth], (depth, stats(states))
        if depth == 335:
            break
        states = advance(states)
        if not states:
            reached_floor_at = depth + 1
            break

    assert reached_floor_at == 335
    assert stats(states) == CHECKPOINTS[335]

    # The unique depth-334 survivor is already below LO.  It is removed at the
    # next sweep, so the exact maximum number of shortcut maps needed to REACH
    # the floor is 334, not 335.
    assert CHECKPOINTS[333][3] > LO
    assert CHECKPOINTS[334][3] <= LO
    max_descent_steps = 334

    print("r17_medium_raw_cylinders", 76_866)
    print("r17_medium_raw_occurrences", 14_980_075)
    print("r17_initial_same_grid_union", CHECKPOINTS[0][:2])
    print("r17_all_singleton_by_depth", 10)
    print("r17_depth120_unresolved", CHECKPOINTS[120][0])
    print("r17_last_above_floor", CHECKPOINTS[333][3])
    print("r17_first_floor_value_on_last_path", CHECKPOINTS[334][3])
    print("r17_max_descent_steps", max_descent_steps)
    print("PASS MATH-068: r=17 medium core and full r=17 layer closed")


if __name__ == "__main__":
    main()
