#!/usr/bin/env python3
"""MATH-223 exact r=10 prefix Hensel-hard diagnostic through depth 41."""

from collections import Counter
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m206", HERE / "2026_09_19_math206_initial_overshoot_reset_catalogue.py"
)
m206 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m206)

DEPTHS = (13, 22, 26, 31, 35, 41)
EXPECTED_PREFIXES = {13:9, 22:74, 26:246, 31:1043, 35:3240, 41:11817}

def shortcut(n):
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2

def prefix_mask(A, k):
    x = A
    mask = 0
    for p in range(k):
        b = x & 1
        if b:
            mask |= 1 << p
        x = shortcut(x)
    return mask

def blocksum(n, l):
    return (((1 << l) - 1) << (n - l)) if l else 0

def dominated(mask, k):
    bits = [(mask >> i) & 1 for i in range(k)]
    q = sum(bits)
    d = k - q

    gaps = []
    ev = 0
    for pos, b in enumerate(bits):
        if not b:
            gaps.append(pos - ev)
            ev += 1
    assert len(gaps) == d

    cnt = Counter(gaps)
    na = d
    states = {(d, 0)}

    for r in range(q, 0, -1):
        la = cnt.get(r, 0)
        aa = blocksum(na, la)
        na2 = na - la
        out = set()

        for nb, h in states:
            for lb in range(nb + 1):
                bb = blocksum(nb, lb)
                z = h + bb - aa
                if z % 3:
                    continue
                out.add((nb - lb, 2 * (z // 3)))

        states = out
        na = na2

    assert na == 0
    return any(((1 << nb) - 1) + h > 0 for nb, h in states)

def main():
    factors = {(H, Q, A, B) for H, Q, A, B, count in m206.build_frozen_factors()}

    pref = {k:set() for k in DEPTHS}
    for H, Q, A, B in factors:
        for k in DEPTHS:
            if H >= k:
                pref[k].add(prefix_mask(A, k))

    for k in DEPTHS:
        assert len(pref[k]) == EXPECTED_PREFIXES[k], (k, len(pref[k]))
        bad = sum(dominated(mask, k) for mask in pref[k])
        assert bad == 0, (k, bad)
        print("depth", k, "prefixes", len(pref[k]), "hensel_dominated", bad)

    print("PASS MATH-223 r10 prefixes Hensel-hard through depth 41")
    print("NO r10 CLOSURE CLAIM")

if __name__ == "__main__":
    main()
