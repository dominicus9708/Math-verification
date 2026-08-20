#!/usr/bin/env python3
"""
Exact certificate for the normalized ternary-syndrome penalty recurrence.

The small-horizon part is independently brute-forced over ordinary integers.
The K=200 table is an exact arithmetic cross-check of values already produced
by the branch/syndrome best-first certificates in this proof branch.

This is not a proof of coefficient stopping or Collatz.
"""

from fractions import Fraction


def barrier_table(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        p2 = 1 << k
        while p3 < p2:
            p3 *= 3
            q += 1
        out[k] = q
    return out


BARRIER = barrier_table(256)


def T(x: int) -> int:
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def survives(x: int, s: int, h: int, J: int) -> bool:
    y = x
    q = 0
    for j in range(1, J + 1):
        bit = y & 1
        q += bit
        y = T(y)
        if q < BARRIER[s + j] - BARRIER[s] - h:
            return False
    return True


def brute_min(s: int, h: int, J: int, modulus: int = 1, residue: int = 0,
              limit: int = 2_000_000) -> int:
    target = residue % modulus
    for x in range(1, limit + 1):
        if x % modulus == target and survives(x, s, h, J):
            return x
    raise RuntimeError("increase brute-force limit")


# First five coefficient-surviving branches:
# r, q, c=T^5(r), R, outgoing h
BRANCHES = (
    (7, 4, 20, 73, 0),
    (15, 4, 40, 65, 0),
    (27, 4, 71, 85, 0),
    (31, 5, 242, 211, 1),
)


def normalized_suffix(x: int, q: int) -> Fraction:
    # Initial split is s=0,a=0,B=5, so suffix normalization is 2^5/3^q.
    return Fraction(32 * x, 3 ** q)


def branch_start_from_suffix(r: int, q: int, c: int, nu: int) -> int:
    delta = nu - c
    assert delta >= 0 and delta % (3 ** q) == 0
    return r + 32 * (delta // (3 ** q))


def check_small_horizons() -> None:
    expected_global = {10: 27, 20: 27, 30: 27}

    for J in (10, 20, 30):
        branch_starts = []
        print(f"suffix_horizon={J}")
        for r, q, c, R, hp in BRANCHES:
            mu = brute_min(5, hp, J)
            nu = brute_min(5, hp, J, 3 ** q, c)
            P = normalized_suffix(nu - mu, q)
            E = Fraction(R, 3 ** q)
            branch_start = branch_start_from_suffix(r, q, c, nu)

            # Exact normalized recurrence for this branch:
            # x_hat = mu_hat + P - E.  Initial normalization is identity.
            rhs = normalized_suffix(mu, q) + P - E
            assert rhs.denominator == 1
            assert rhs.numerator == branch_start
            assert P >= 0
            branch_starts.append(branch_start)

            print(
                f"  r={r:2d} q={q} mu={mu} nu={nu} "
                f"P={P} E={E} branch_min={branch_start}"
            )

        global_min = min(branch_starts)
        direct = brute_min(0, 0, J + 5)
        assert global_min == direct == expected_global[J]
        print(f"  global_mu({J+5})={global_min}")


def check_k200_calibration() -> None:
    # Existing exact syndrome solver values for suffix horizon 195.
    mu_h0 = 837_799
    mu_h1 = 837_799
    rows = (
        # r,q,c,R,hp,nu,expected branch minimum
        (7, 4, 20, 73, 0, 15_388_886, 6_079_559),
        (15, 4, 40, 65, 0, 10_259_257, 4_053_039),
        (27, 4, 71, 85, 0, 16_786_430, 6_631_675),
        (31, 5, 242, 211, 1, 8_550_683, 1_126_015),
    )

    print("K=200 exact normalized penalty calibration")
    starts = []
    for r, q, c, R, hp, nu, want in rows:
        mu = mu_h0 if hp == 0 else mu_h1
        P = normalized_suffix(nu - mu, q)
        E = Fraction(R, 3 ** q)
        rhs = normalized_suffix(mu, q) + P - E
        branch_start = branch_start_from_suffix(r, q, c, nu)
        assert rhs == branch_start == want
        assert P > E
        starts.append(branch_start)
        print(
            f"  r={r:2d}: mu_hat={normalized_suffix(mu,q)} "
            f"P={P} E={E} branch_min={branch_start}"
        )

    assert min(starts) == 1_126_015
    print("  global_mu(200)=1126015")


def main() -> None:
    check_small_horizons()
    check_k200_calibration()
    print("normalized syndrome penalty recurrence certificate: PASS")


if __name__ == "__main__":
    main()
