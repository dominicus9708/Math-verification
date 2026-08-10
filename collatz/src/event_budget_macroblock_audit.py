#!/usr/bin/env python3
"""Exact audit of the odd-event budget identities for accelerated Collatz.

For odd x_j define
    a_j = v_2(3 x_j + 1),
    x_{j+1} = (3 x_j + 1) / 2^{a_j}.

The script checks the exact rational state
    lambda_q = 2^{A_q}/3^q,
    S_q = sum_{i<q} 2^{A_i}/3^{i+1},
    H_q = 1 + S_q/n - lambda_q
        = lambda_q (x_q/n - 1),
and the transition
    H_{q+1}-H_q = lambda_q/3 * (3 + 1/n - 2^{a_q}).

It also checks the run/macroblock identity for ell consecutive a=1 events
followed by b>=2.

This is a finite reproducibility audit of algebraic identities, not a Collatz proof.
"""

from fractions import Fraction


def v2(z: int) -> int:
    c = 0
    while z % 2 == 0:
        z //= 2
        c += 1
    return c


def event_values(n: int, qmax: int):
    assert n > 1 and n % 2 == 1
    x = n
    lam = Fraction(1, 1)
    S = Fraction(0, 1)
    H = Fraction(0, 1)
    vals = []

    for _ in range(qmax):
        a = v2(3 * x + 1)

        assert Fraction(n, 1) + S == lam * x
        assert H == lam * Fraction(x - n, n)

        H2 = H + lam * Fraction(3 * n + 1 - n * (2 ** a), 3 * n)
        S2 = S + lam / 3
        lam2 = lam * Fraction(2 ** a, 3)
        x2 = (3 * x + 1) // (2 ** a)

        assert Fraction(n, 1) + S2 == lam2 * x2
        assert H2 == lam2 * Fraction(x2 - n, n)

        vals.append(a)
        x, lam, S, H = x2, lam2, S2, H2

    return vals


def audit() -> None:
    for n in range(3, 1000, 2):
        event_values(n, 80)

    blocks = 0
    for n in range(3, 500, 2):
        vals = event_values(n, 100)
        x = n
        lam = Fraction(1, 1)
        H = Fraction(0, 1)
        i = 0

        while i < len(vals):
            ell = 0
            while i + ell < len(vals) and vals[i + ell] == 1:
                ell += 1
            if i + ell >= len(vals):
                break

            b = vals[i + ell]
            assert b >= 2

            # A maximal run of ell credit events is exactly a 2-adic alignment.
            assert v2(x + 1) - 1 == ell

            H0 = H
            lam0 = lam
            for t in range(ell + 1):
                a = vals[i + t]
                H += lam * Fraction(3 * n + 1 - n * (2 ** a), 3 * n)
                lam *= Fraction(2 ** a, 3)
                x = (3 * x + 1) // (2 ** a)

            predicted = lam0 * Fraction(1, 3) * (
                Fraction(3 * (n + 1), n)
                - Fraction(2, 3) ** ell * Fraction((2 ** b) * n + 2, n)
            )
            assert H - H0 == predicted

            blocks += 1
            i += ell + 1

    print("identity_audit_ok odd_n=3..999 q<=80")
    print(f"macroblock_audit_ok blocks={blocks}")


if __name__ == "__main__":
    audit()
