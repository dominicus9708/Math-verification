#!/usr/bin/env python3
"""High-precision one-sided CF audit for the R1 slope strip.

This is a reproducibility/diagnostic script, not a formal interval certificate.
It enumerates convergents and intermediate convergents of gamma=log_2(3)
and finds the first upper approximation p/q satisfying

    0 < p/q - gamma < 1 / (3 * 2^71 * ln 2).

For publication-grade certification, replace mpmath comparisons by directed
interval arithmetic or exact rational enclosures for ln(2), ln(3).
"""

import mpmath as mp

mp.mp.dps = 120

GAMMA = mp.log(3) / mp.log(2)
EPS = 1 / (3 * mp.mpf(2) ** 71 * mp.log(2))


def continued_fraction_data(limit_terms=40):
    x = GAMMA
    p_nm2, p_nm1 = 0, 1
    q_nm2, q_nm1 = 1, 0
    rows = []

    for n in range(limit_terms):
        a = int(mp.floor(x))
        p = a * p_nm1 + p_nm2
        q = a * q_nm1 + q_nm2

        # Intermediate convergents between C_{n-2} and C_n:
        # (m p_{n-1}+p_{n-2})/(m q_{n-1}+q_{n-2}), 1<=m<=a.
        inter = []
        for m in range(1, a + 1):
            pi = m * p_nm1 + p_nm2
            qi = m * q_nm1 + q_nm2
            err = mp.mpf(pi) / qi - GAMMA
            inter.append((m, pi, qi, err))

        rows.append((n, a, p, q, inter))
        p_nm2, p_nm1 = p_nm1, p
        q_nm2, q_nm1 = q_nm1, q
        x = 1 / (x - a)

    return rows


def main():
    best = None
    all_upper = []

    for n, a, p, q, inter in continued_fraction_data():
        for m, pi, qi, err in inter:
            if err <= 0:
                continue
            all_upper.append((qi, pi, err, n, m))
            if err < EPS and (best is None or qi < best[0]):
                best = (qi, pi, err, n, m)

    all_upper.sort()

    print("gamma =", mp.nstr(GAMMA, 80))
    print("epsilon =", mp.nstr(EPS, 40))
    print()

    if best is None:
        raise SystemExit("No qualifying upper semiconvergent in searched CF range")

    q, p, err, n, m = best
    print("first qualifying upper convergent/semiconvergent by denominator:")
    print(f"A={p}")
    print(f"H={q}")
    print(f"CF stage n={n}, intermediate multiplier m={m}")
    print("error =", mp.nstr(err, 40))
    print()

    print("nearby upper approximants by denominator:")
    nearby = [row for row in all_upper if row[0] <= q]
    for qi, pi, ei, ni, mi in nearby[-8:]:
        print(
            f"A={pi} H={qi} err={mp.nstr(ei, 18)} "
            f"n={ni} m={mi} qualifies={ei < EPS}"
        )

    assert p == 114_208_327_604
    assert q == 72_057_431_991
    assert err < EPS


if __name__ == "__main__":
    main()
