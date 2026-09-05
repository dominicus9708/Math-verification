#!/usr/bin/env python3
"""Exact global first-resonance handoff after the sharp constant parity-RS gate.

External inputs/theorems:
- convergence below 2^71 (Barina 2025),
- the mechanical first-crossing remainder envelope,
- Worley--Dujella's adjacent-convergent classification.

All arithmetic and candidate enumeration in this file is exact Fraction/integer
arithmetic.  No ternary selector or repeated L7/L14 pullback is used.
"""

from fractions import Fraction
from math import gcd

B = 1 << 71
Q0 = 72_057_431_991
A0 = 114_208_327_604
Q1 = 137_528_045_312
NLOG = 60


def log_ratio_bounds(x: Fraction, n: int):
    s = Fraction(0)
    for k in range(n + 1):
        s += Fraction(2) * x ** (2 * k + 1) / (2 * k + 1)
    tail = Fraction(2) * x ** (2 * n + 3) / ((2 * n + 3) * (1 - x * x))
    return s, s + tail


def interval_cf(lo: Fraction, hi: Fraction, n: int):
    out = []
    for _ in range(n):
        a0 = lo.numerator // lo.denominator
        a1 = hi.numerator // hi.denominator
        assert a0 == a1
        out.append(a0)
        lo -= a0
        hi -= a0
        assert lo > 0
        lo, hi = 1 / hi, 1 / lo
    return out


def convergents(cf):
    p2, p1 = 0, 1
    q2, q1 = 1, 0
    out = []
    for a in cf:
        p = a * p1 + p2
        q = a * q1 + q2
        out.append((p, q))
        p2, p1 = p1, p
        q2, q1 = q1, q
    return out


def main() -> None:
    # Rigorous log intervals.
    l2, u2 = log_ratio_bounds(Fraction(1, 3), NLOG)  # ln 2
    l3, u3 = log_ratio_bounds(Fraction(1, 2), NLOG)  # ln 3
    gamma_lo = l3 / u2
    gamma_hi = u3 / l2

    cf = interval_cf(gamma_lo, gamma_hi, 26)
    cv = convergents(cf)

    # Mechanical-envelope Worley constant over Q0 < q <= Q1, with only the
    # globally published floor B=2^71.
    kmax = (
        Fraction(Q1 * Q1, 1) / (6 * B * l2 * l2)
        + Fraction(Q1, 1) / (3 * B * l2)
    )
    assert kmax < Fraction(2779, 1000)

    # Therefore rs < 2*kmax < 5.558, hence integral rs <= 5.
    pairs = [(1, 0), (0, 1)]
    for r in range(1, 6):
        for s in range(1, 6):
            if r * s <= 5:
                pairs.append((r, s))

    cmax = (
        Fraction(1, 1) / (6 * B * l2 * l2)
        + Fraction(1, 1) / (3 * B * (Q0 + 1) * l2)
    )

    worley = {}
    for j in range(len(cv) - 1):
        p0, b0 = cv[j]
        p1, b1 = cv[j + 1]
        for r, s in pairs:
            for sign in (-1, 1):
                pp = r * p1 + sign * s * p0
                bb = r * b1 + sign * s * b0
                if pp <= 0 or bb <= 0:
                    continue
                g = gcd(pp, bb)
                a, b = pp // g, bb // g
                if b > Q1:
                    continue

                gmin = Q0 // b + 1
                gmax = Q1 // b
                if gmin > gmax:
                    continue

                err_lo = Fraction(a, b) - gamma_hi
                err_hi = Fraction(a, b) - gamma_lo
                if err_hi <= 0:
                    continue
                assert err_lo > 0
                if err_lo >= kmax / (b * b):
                    continue

                worley[(a, b)] = (j, r, s, sign, gmin, gmax, err_lo, err_hi)

    survivors = []
    fails = []
    for (a, b), meta in worley.items():
        err_lo = meta[-2]
        if err_lo < cmax:
            survivors.append((a, b, meta))
        else:
            fails.append((err_lo / cmax, a, b))

    assert len(worley) == 41
    assert len(survivors) == 1
    a1, q1, meta = survivors[0]
    assert (a1, q1) == (217_976_794_617, 137_528_045_312)
    assert meta[4] == 1 and meta[5] == 1

    # The first sharp-wall boundary cell itself is not eliminated by the
    # interval scan above.  But its mechanical ceiling is rigorously < 4B/3.
    # ln(P)=A0 ln2-Q0 ln3, and P-1 >= ln(P).
    gap_lower = A0 * l2 - Q0 * u3
    assert gap_lower > 0
    s_upper = Fraction(Q0, 1) / (6 * l2) + Fraction(1, 3)
    start_ceiling_upper = s_upper / gap_lower
    assert start_ceiling_upper < Fraction(4 * B, 3)
    assert Fraction(4 * B, 3) < (1 << 72)

    nearest_fail = min(fails)

    print("PASS global first-resonance post-constant-gate certificate")
    print(f"published_floor=2^71={B}")
    print(f"first_boundary=(A,q)=({A0},{Q0})")
    print("first_boundary_start_ceiling < (4/3)*2^71 < 2^72")
    print(f"post-boundary_q_interval=({Q0},{Q1}]")
    print(f"Worley_rs_product_bound<=5")
    print(f"primitive_superset_count={len(worley)}")
    print(f"unique_later_candidate=(A,q)=({a1},{q1})")
    print(f"nearest_rejected_primitive=(A,q)=({nearest_fail[1]},{nearest_fail[2]})")


if __name__ == "__main__":
    main()
