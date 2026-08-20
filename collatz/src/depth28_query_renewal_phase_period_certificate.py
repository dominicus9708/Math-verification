#!/usr/bin/env python3
"""
Algebraic certificate for the phase periods of depth-28 renewal query shifts.

Existing depth-28 Hensel renewal translations have the form
    d_p = 2^p * 3^{-(q_before(p)+1)} mod 2^28.
After scaling a ternary syndrome state by 3^{-a}, the cyclic-query shift is
    delta_p(a) = 2^p * 3^{-(a+q_before(p)+1)} mod 2^28.

Because the factor 2^p is fixed, the a-dependence lives modulo 2^(28-p).
For 28-p >= 3, ord_{2^(28-p)}(3) = 2^(26-p).
"""

L = 28
MOD = 1 << L
MASK = MOD - 1
H19 = "1101101101011011010"
POSITIONS = (2, 5, 8, 10, 13, 16, 18, 21, 24, 27)


def mechanical():
    s = (H19 * ((L + len(H19) - 1) // len(H19)))[:L]
    return s


def q_before(p, m):
    return sum(1 for ch in m[:p] if ch == "1")


def invmod_odd(a, mod):
    return pow(a, -1, mod)


def delta(p, a, m):
    e = a + q_before(p, m) + 1
    return ((1 << p) * pow(pow(3, e, MOD), -1, MOD)) & MASK


def v2(x):
    if x == 0:
        return 99
    n = 0
    while (x & 1) == 0:
        n += 1
        x >>= 1
    return n


def expected_period(p):
    k = L - p
    if k <= 1:
        return 1
    if k == 2:
        return 2
    return 1 << (k - 2)


def main():
    m = mechanical()
    rows = []
    for p in POSITIONS:
        per = expected_period(p)
        d0 = delta(p, 0, m)
        assert v2(d0) == p
        assert delta(p, per, m) == d0
        if per > 1:
            assert delta(p, per // 2, m) != d0
        rows.append((p, q_before(p, m), per, d0))

    print("p,q_before,a_period,delta_p(0)")
    for row in rows:
        print(",".join(map(str, row)))
    print("depth28 query-renewal phase-period certificate: PASS")


if __name__ == "__main__":
    main()
