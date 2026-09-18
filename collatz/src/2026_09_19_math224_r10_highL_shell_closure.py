#!/usr/bin/env python3
"""MATH-224 exact high-L singleton paid-exit shell closure."""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve().parent
SPEC = spec_from_file_location(
    "m58", HERE / "2026_09_11_paid_macro_transition_certificate.py"
)
m58 = module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(m58)

LO = 1 << 71

EXPECTED = {
    54:(96611,302), 55:(336790,356), 56:(133153,267),
    57:(16754,225), 58:(49968,260), 59:(10699,243),
    60:(6641,176), 61:(5779,212), 62:(676,213),
    63:(1336,212), 64:(667,166), 65:(11,86),
    66:(223,141), 67:(63,142), 68:(18,95),
    69:(27,113), 70:(3,80), 71:(4,79), 72:(2,80),
}

def shortcut(n):
    return n // 2 if n % 2 == 0 else (3*n + 1) // 2

def anchors(L):
    out = set()
    for lo, hi, R, E0, q0 in m58.paid_exit_sources(L):
        tmin, tmax = m58.lift_bounds(L, R, lo, hi)
        stepq = 3**q0
        for t in range(tmin, tmax + 1):
            E = E0 + t * stepq
            if E & 1:
                out.add(R + (1 << L) * t)
    return out

def main():
    cache = {}

    def descent(n):
        x = n
        path = []
        seen = set()
        while x > LO and x not in cache:
            assert x not in seen
            seen.add(x)
            path.append(x)
            x = shortcut(x)
            assert len(path) < 10000
        d = 0 if x <= LO else cache[x]
        for v in reversed(path):
            d += 1
            cache[v] = d
        return cache.get(n, 0)

    total = 0
    for L in range(54, 73):
        ys = anchors(L)
        maxd = max((descent(y) for y in ys), default=0)
        got = (len(ys), maxd)
        assert got == EXPECTED[L], (L, got, EXPECTED[L])
        total += len(ys)
        print("L", L, "anchors", len(ys), "max_descent", maxd)

    assert total == 659425
    print("PASS MATH-224 high-L paid-exit shell closure")
    print("audited_per_L_total", total)
    print("r10 singleton remainder: 13 <= L <= 53, d != 0")
    print("FULL r10 LAYER OPEN")

if __name__ == "__main__":
    main()
