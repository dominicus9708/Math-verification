#!/usr/bin/env python3
"""MATH-187 exact regression for the joint parity/address recurrence.

Checks two independent parts:

1. all abstract parity words through depth 12 against the direct affine
   correction definitions for k,q,d,u,rho,Omega,S,Sigma;
2. the exact same-integer address-cylinder recurrence through depth 8 starting
   from all integers 0..255, comparing every child cylinder with direct
   shortcut-map filtering.

Finite regression only.  The recurrence identities are algebraic.  This file
makes no first-cell or Collatz closure claim.
"""
from fractions import Fraction


def m(q: int) -> int:
    if q == 0:
        return 0
    # floor(q*log2(3/2)) = floor(log2(3^q)) - q exactly.
    return (3**q).bit_length() - 1 - q


def shortcut(n: int) -> int:
    return n // 2 if n % 2 == 0 else (3 * n + 1) // 2


def audit_analytic(depth_max: int = 12) -> int:
    states = [dict(
        k=0, q=0, d=0, u=0,
        rho=Fraction(1), Omega=Fraction(1),
        S=Fraction(0), Sigma=Fraction(0), C=0,
        P=Fraction(0), c=0,
    )]
    checks = 0

    for _ in range(depth_max):
        nxt = []
        for st in states:
            for b in (0, 1):
                k, q, d, u = st["k"], st["q"], st["d"], st["u"]
                delta = m(q + 1) - m(q)
                assert delta in (0, 1)

                k2 = k + 1
                q2 = q + b
                d2 = d + 1 - b
                u2 = u - 1 + b * (1 + delta)

                rho2 = Fraction(2, 3**b) * st["rho"]
                Omega2 = st["Omega"] * (Fraction(2 ** (1 + delta), 3) ** b)
                S2 = st["S"] + b * st["rho"] / 3
                Sigma2 = st["Sigma"] + (1 - b) * st["rho"]

                C2 = st["C"] if b == 0 else 3 * st["C"] + (1 << k)
                P2 = st["P"] + b * (st["Omega"] - st["rho"]) / 3
                c2 = st["c"] + (1 if (b == 1 and u > 0) else 0)

                assert d2 == k2 - q2
                assert u2 == m(q2) - d2
                assert rho2 == Fraction(2**k2, 3**q2)
                assert Omega2 == Fraction(2 ** (q2 + m(q2)), 3**q2)
                assert S2 == Fraction(C2, 3**q2)
                assert Sigma2 == S2 + rho2 - 1

                nxt.append(dict(
                    k=k2, q=q2, d=d2, u=u2,
                    rho=rho2, Omega=Omega2,
                    S=S2, Sigma=Sigma2, C=C2,
                    P=P2, c=c2,
                ))
                checks += 1
        states = nxt

    assert len(states) == 1 << depth_max
    return checks


def audit_address(depth_max: int = 8, initial_size: int = 256) -> int:
    states = [dict(
        A=0, H=0, B=0, Q=0, M=initial_size,
        starts=list(range(initial_size)),
        endpoints=list(range(initial_size)),
    )]
    checks = 0

    for _ in range(depth_max):
        nxt = []
        for st in states:
            for b in (0, 1):
                A, H, B, Q, M = (
                    st["A"], st["H"], st["B"], st["Q"], st["M"]
                )

                eta = (b - B) & 1
                M2 = (M + 1 - eta) // 2

                direct = [
                    (n, y)
                    for n, y in zip(st["starts"], st["endpoints"])
                    if (y & 1) == b
                ]
                assert len(direct) == M2
                if M2 == 0:
                    continue

                A2 = A + (1 << H) * eta
                H2 = H + 1
                Q2 = Q + b
                B2 = (3**b * (B + 3**Q * eta) + b) // 2

                starts2 = [n for n, _ in direct]
                endpoints2 = [shortcut(y) for _, y in direct]

                assert starts2 == [A2 + (1 << H2) * t for t in range(M2)]
                assert endpoints2 == [B2 + 3**Q2 * t for t in range(M2)]

                nxt.append(dict(
                    A=A2, H=H2, B=B2, Q=Q2, M=M2,
                    starts=starts2, endpoints=endpoints2,
                ))
                checks += 1
        states = nxt

    assert len(states) == initial_size
    return checks


def main() -> None:
    analytic = audit_analytic()
    address = audit_address()
    print(f"analytic_transition_checks={analytic}")
    print(f"address_transition_checks={address}")
    print("PASS MATH-187 joint parity/address recurrence regression")
    print("NO FIRST-CELL OR COLLATZ CLOSURE CLAIM")


if __name__ == "__main__":
    main()
