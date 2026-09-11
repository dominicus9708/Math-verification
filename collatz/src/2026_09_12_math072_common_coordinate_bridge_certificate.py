#!/usr/bin/env python3
"""MATH-072 regression certificate for the exact common-coordinate bridge.

The universal identities are proved algebraically in the companion note.  This
script is a finite exact regression over all parity words through depth 16.
It checks:

  S = 1 + Sigma - rho,
  rho = 2^{-u} Omega,

and the one-step recurrences for S, rho and Sigma.

Finite regression is not itself the universal proof and does not prove Collatz.
"""
from fractions import Fraction

MAX_DEPTH = 16


def m_of_q(q: int) -> int:
    d = 0
    while 3**q > 2 ** (q + d + 1):
        d += 1
    return d


def data(bits):
    C = 0
    q = 0
    evens = []
    for p, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << p)
            q += 1
        else:
            evens.append(p)

    k = len(bits)
    d = k - q
    S = Fraction(C, 3**q)
    Sigma = sum(
        (Fraction(3**j * 2**e, 3**e) for j, e in enumerate(evens)),
        Fraction(0),
    )
    rho = Fraction(2**k, 3**q)
    m = m_of_q(q)
    u = m - d
    Omega = Fraction(2 ** (q + m), 3**q)
    return k, q, d, S, Sigma, rho, u, Omega


def main():
    checked = 0
    for k in range(MAX_DEPTH + 1):
        for mask in range(1 << k):
            bits = [(mask >> p) & 1 for p in range(k)]
            _, _, _, S, Sigma, rho, u, Omega = data(bits)

            assert S == 1 + Sigma - rho
            if u >= 0:
                assert rho == Omega / (2**u)
            else:
                assert rho == Omega * (2 ** (-u))

            for bit in (0, 1):
                _, _, _, S2, Sigma2, rho2, _, _ = data(bits + [bit])
                if bit == 0:
                    assert S2 == S
                    assert rho2 == 2 * rho
                    assert Sigma2 == Sigma + rho
                else:
                    assert S2 == S + rho / 3
                    assert rho2 == 2 * rho / 3
                    assert Sigma2 == Sigma

            checked += 1

    assert checked == sum(1 << k for k in range(MAX_DEPTH + 1))
    assert checked == 131_071
    print("PASS MATH-072 common-coordinate regression", checked)


if __name__ == "__main__":
    main()
