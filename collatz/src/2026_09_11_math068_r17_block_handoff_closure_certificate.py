#!/usr/bin/env python3
"""
MATH-068 exact closure certificate for the remaining r=17 medium-multiplicity core.

MATH-067 leaves exactly the negative-candidate cylinders with 65<=m<=1023:
  76,866 cylinders representing 14,980,075 target occurrences.

This certificate does not materialize those 14.98 million targets initially.
Instead it uses the universal 8-step shortcut block determined by n mod 2^8.
For an AP

    n = a + b k,  0 <= k < m,

with odd b, each k residue modulo 2^8 fixes n mod 2^8 and hence the next
8 parity bits.  Writing k=r+2^8 s gives another exact AP after eight shortcut
steps.  Values <=2^71 are trimmed exactly.

Certified result:
- first 8-step block: 9,587,872 occurrences descend; 5,392,203 remain;
- every surviving AP then has multiplicity <=4;
- second 8-step block: 2,777,528 more occurrences descend;
- 2,614,675 singleton occurrences remain, representing 1,826,810 unique ints;
- every unique singleton descends to <=2^71, with at most 318 additional
  shortcut steps after the 16-step block handoff.

Therefore the complete r=17 layer is closed for the current first-cell
minimal-counterexample calculation.  r<=16, the first universal cell, later
Farey cells, and Collatz remain open.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from collections import Counter

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "math065", HERE / "2026_09_11_math065_paid_count_18plus_closure_certificate.py"
)
m65 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m65)

LO = 1 << 71
H = 8
MOD = 1 << H


def pow3_exponent(n: int) -> int:
    q = 0
    while n > 1:
        assert n % 3 == 0
        n //= 3
        q += 1
    return q


def block_table():
    """Return (3^q,C) for T^8(n)=(3^q n+C)/256 on each n mod256."""
    out = []
    for residue in range(MOD):
        x = residue
        A = 1
        C = 0
        for t in range(H):
            if x & 1:
                A *= 3
                C = 3 * C + (1 << t)
                x = (3 * x + 1) // 2
            else:
                x //= 2
        out.append((A, C))
    return out


BLOCK = block_table()


def block_split(a: int, b: int, count: int):
    """Exact 8-step images of one AP, still as APs.

    Because b is odd, k modulo 256 is equivalent to n modulo 256.
    For k=k0+256*s the 8-step image is

        a' + b' s,

    where b'=3^q b for the parity word selected by n mod256.
    """
    out = []
    for k0 in range(min(count, MOD)):
        c = (count - 1 - k0) // MOD + 1
        n0 = a + b * k0
        A, C = BLOCK[n0 & (MOD - 1)]
        y0 = (A * n0 + C) // MOD
        out.append((y0, A * b, c))
    return out


def trim_floor(a: int, b: int, count: int):
    if count <= 0:
        return a, b, 0, 0
    dropped = 0
    if a <= LO:
        t = (LO - a) // b
        dropped = min(count, max(0, t + 1))
        a += b * dropped
        count -= dropped
    return a, b, count, dropped


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def descent(n: int, cache: dict[int, int]):
    x = n
    path = []
    seen = set()
    while x > LO and x not in cache:
        if x in seen:
            return None
        seen.add(x)
        path.append(x)
        x = shortcut(x)
        assert len(path) < 10000
    d = 0 if x <= LO else cache[x]
    for v in reversed(path):
        d += 1
        cache[v] = d
    return cache.get(n, 0)


def medium_cylinders():
    total, safe, singleton, critical = m65.classify_cells(17)
    assert (total, len(safe), len(singleton), len(critical)) == (1090, 256, 596, 238)

    out = []
    for group in (singleton, critical):
        for cell in group:
            leaves, _ = m65.negative_candidate_cylinders(cell, 17)
            for first, count, tres, mod, yres, coeff in leaves:
                if not (65 <= count <= 1023):
                    continue
                base_s = (first - tres) // mod
                target0 = yres + coeff * base_s
                out.append((target0, coeff, count))
    return out


def main():
    cylinders = medium_cylinders()
    assert len(cylinders) == 76_866
    assert sum(c for _, _, c in cylinders) == 14_980_075

    coeff_counts = Counter(pow3_exponent(b) for _, b, _ in cylinders)
    assert coeff_counts == Counter({38: 8_268, 39: 19_445, 40: 49_153})

    low8_classes = {(a & 255, b & 255) for a, b, _ in cylinders}
    assert len(low8_classes) == 768

    closed1 = 0
    closed2 = 0
    survivors = []
    max_after_first = 0

    for a, b, count in cylinders:
        for a1, b1, c1 in block_split(a, b, count):
            a1, b1, c1, drop1 = trim_floor(a1, b1, c1)
            closed1 += drop1
            if not c1:
                continue
            max_after_first = max(max_after_first, c1)

            for a2, b2, c2 in block_split(a1, b1, c1):
                a2, b2, c2, drop2 = trim_floor(a2, b2, c2)
                closed2 += drop2
                if c2:
                    assert c2 == 1
                    survivors.append(a2)

    assert closed1 == 9_587_872
    assert max_after_first == 4
    assert closed2 == 2_777_528
    assert len(survivors) == 2_614_675
    assert closed1 + closed2 + len(survivors) == 14_980_075

    unique = set(survivors)
    assert len(unique) == 1_826_810

    cache = {}
    max_tail = 0
    for n in unique:
        d = descent(n, cache)
        assert d is not None
        max_tail = max(max_tail, d)
    assert max_tail == 318

    print("r17_medium_cylinders", len(cylinders))
    print("r17_medium_occurrences", 14_980_075)
    print("r17_low8_affine_classes", len(low8_classes))
    print("after_8_closed", closed1)
    print("after_8_remaining", 14_980_075 - closed1)
    print("after_8_max_family_multiplicity", max_after_first)
    print("after_16_additional_closed", closed2)
    print("after_16_singleton_occurrences", len(survivors))
    print("after_16_unique_singletons", len(unique))
    print("post_handoff_max_descent", max_tail)
    print("original_target_safe_step_bound", 16 + max_tail)
    print("PASS MATH-068: complete r=17 layer closed")


if __name__ == "__main__":
    main()
