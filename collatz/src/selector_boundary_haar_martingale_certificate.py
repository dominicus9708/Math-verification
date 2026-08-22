#!/usr/bin/env python3
"""Exact finite certificate for the selector/Beatty-boundary Haar reduction.

This verifies, on small exact dyadic quotients, the identities used in the
Stage-4 martingale reformulation:

  ||Delta_r g_m||_2^2 = 2^r e_r(m),
  e_r(m) = 2 p_(r+1)(m) - p_r(m),
  sum_{s<R} 2^s e_s(m) = 2^R p_R(m) - 1,

and at a Beatty barrier rise from parent length L to child length L+1,
with r=L-2,

  K_L / 2^m = <h_L, Delta_r g_m>,
  ||h_L||_2^2 = B_L / 2^r.

Therefore

  (K_L/2^m)^2 / (B_L/2^r) <= 2^r e_r(m)

and summing over distinct rise levels gives the global square-budget bound.

The file also certifies two exact counterexamples to the discarded trial bound
2^m e_r(m) <= 5/4.  This is a structural certificate, not a Collatz proof.
"""

from fractions import Fraction


def qmins_exact(k: int) -> list[int]:
    b = [0] * (k + 1)
    q = 0
    p3 = 1
    for j in range(1, k + 1):
        target = 1 << j
        while p3 < target:
            p3 *= 3
            q += 1
        b[j] = q
    return b


def coefficient_survivors_reduced(L: int) -> list[int]:
    """Indicator on y mod 2^(L-2) for N=4y+3 coefficient survival to L."""
    assert L >= 2
    M = 1 << (L - 2)
    b = qmins_exact(L)
    out = [0] * M
    for y in range(M):
        x = 4 * y + 3
        q = 0
        ok = True
        for k in range(1, L + 1):
            if x & 1:
                q += 1
                x = (3 * x + 1) // 2
            else:
                x //= 2
            if q < b[k]:
                ok = False
                break
        out[y] = int(ok)
    return out


def selector_counts_shifted(m: int, r: int) -> list[int]:
    """Multiplicity of 3^m + sum a_i 3^i modulo 2^r."""
    if r == 0:
        return [1 << m]
    M = 1 << r
    dp = [0] * M
    dp[pow(3, m, M)] = 1
    for i in range(m):
        w = pow(3, i, M)
        nd = dp[:]
        for x, v in enumerate(dp):
            if v:
                nd[(x + w) & (M - 1)] += v
        dp = nd
    assert sum(dp) == 1 << m
    return dp


def collision(m: int, r: int) -> Fraction:
    c = selector_counts_shifted(m, r)
    total = 1 << m
    return Fraction(sum(v * v for v in c), total * total)


def energy(m: int, r: int) -> Fraction:
    return 2 * collision(m, r + 1) - collision(m, r)


def small_exact_regression(m: int = 8, R: int = 7) -> None:
    p = [collision(m, r) for r in range(R + 1)]
    e = [2 * p[r + 1] - p[r] for r in range(R)]
    assert all(x >= 0 for x in e)

    # Exact dyadic martingale telescope.
    for rr in range(1, R + 1):
        lhs = sum((1 << s) * e[s] for s in range(rr))
        rhs = (1 << rr) * p[rr] - 1
        assert lhs == rhs

    square_budget = Fraction(0)
    l1_budget = Fraction(0)
    boundary_norm_sum = Fraction(0)

    for L in range(2, R + 2):
        b = qmins_exact(L + 1)
        if b[L + 1] != b[L] + 1:
            continue

        r = L - 2
        M = 1 << r
        cnt = selector_counts_shifted(m, r + 1)
        parent = coefficient_survivors_reduced(L)
        child = coefficient_survivors_reduced(L + 1)

        B = 0
        K = 0
        D = 0
        for x in range(M):
            if not parent[x]:
                continue
            c0, c1 = cnt[x], cnt[x + M]
            b0, b1 = child[x], child[x + M]
            if b0 + b1 == 1:
                B += 1
                D += c0 + c1
                K += (b0 - b1) * (c0 - c1)

        assert B > 0
        hnorm = Fraction(B, M)
        dnorm = (1 << r) * e[r]
        knorm = Fraction(K, 1 << m)

        # Exact per-level Haar/Cauchy bound.
        assert knorm * knorm <= hnorm * dnorm

        square_budget += knorm * knorm / hnorm
        l1_budget += abs(knorm)
        boundary_norm_sum += hnorm

        print(
            "rise",
            "L", L,
            "r", r,
            "B", B,
            "D", D,
            "K", K,
            "hnorm", hnorm,
            "delta_norm_sq", dnorm,
        )

    total_energy = sum((1 << s) * e[s] for s in range(R))
    assert square_budget <= total_energy
    assert l1_budget * l1_budget <= boundary_norm_sum * total_energy

    print("square_budget", square_budget)
    print("selector_energy_budget", total_energy)
    print("partial_boundary_norm_sum", boundary_norm_sum)
    print("partial_abs_K_budget", l1_budget)


def discarded_constant_counterexamples() -> None:
    # Exact counterexamples found after extending the middle-band scan.
    r2616 = (1 << 26) * energy(26, 16)
    r2917 = (1 << 29) * energy(29, 17)

    assert r2616 == Fraction(14_419_123, 8_388_608)
    assert r2917 == Fraction(436_843_091, 134_217_728)
    assert r2616 > Fraction(5, 4)
    assert r2917 > Fraction(5, 4)

    print("discarded_bound_counterexample_26_16", r2616, float(r2616))
    print("discarded_bound_counterexample_29_17", r2917, float(r2917))


def main() -> None:
    small_exact_regression()
    discarded_constant_counterexamples()
    print("selector-boundary Haar martingale certificate: PASS")


if __name__ == "__main__":
    main()
