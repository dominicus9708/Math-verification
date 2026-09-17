#!/usr/bin/env python3
"""MATH-179: exact phase/depth compression for joint r<=21, depth<=41 sweep.

This certificate is a structural regression only.  It does not close any new
Collatz layer.

It verifies two identities used to build the joint paid-count/depth recurrence:

1. For the normalized phase map on (1/2,1], the r-step epsilon sum is

       sum_{j<r} eps_j = m(r) + 1[omega <= tau(r)],

   where m(r)=floor(r*log_2(3/2)) is computed without floating point and

       tau(r)=3^r / 2^(r+m(r)+1).

   Hence a first-return paid cluster with r paid odds has local step length

       h_r = r + 1 + m(r) + 1[omega <= tau(r)].

2. For every global prefix depth 2<=k<=41 and odd count q, coefficient
   survival 3^q >= 2^k is equivalent to nonnegative slack

       u = m(q) - (k-q) >= 0,

   and the exact scale is

       2^k/3^q = 2^(-u) * Omega_q,
       Omega_q = 2^(q+m(q))/3^q.

The local paid-cluster depth h_r and the global prefix depth k are deliberately
kept distinct.  The certificate only shows that both are controlled by the same
Beatty/phase clock; it does not identify their carry states.
"""

from fractions import Fraction

MAX_R = 21
MAX_K = 41


def m(q: int) -> int:
    """Exact floor(q*log2(3/2)) without floating point."""
    if q == 0:
        return 0
    d = 0
    while 3**q > 2 ** (q + d + 1):
        d += 1
    return d


def tau(q: int) -> Fraction:
    assert q >= 1
    return Fraction(3**q, 2 ** (q + m(q) + 1))


def eps_step(omega: Fraction) -> tuple[int, Fraction]:
    assert Fraction(1, 2) < omega <= 1
    eps = 0 if omega > Fraction(3, 4) else 1
    nxt = omega * (Fraction(2, 3) if eps == 0 else Fraction(4, 3))
    assert Fraction(1, 2) < nxt <= 1
    return eps, nxt


def phase_cells() -> list[tuple[Fraction, Fraction]]:
    cuts = {Fraction(1, 2), Fraction(1, 1)}
    for r in range(1, MAX_R + 1):
        cuts.add(tau(r))
    s = sorted(cuts)
    return list(zip(s[:-1], s[1:]))


def audit_phase_clock() -> None:
    # On every cell cut by tau_1..tau_21, all threshold decisions are fixed.
    # A rational midpoint therefore certifies the complete target phase partition.
    for lo, hi in phase_cells():
        omega0 = (lo + hi) / 2
        omega = omega0
        eps_sum = 0

        for r in range(1, MAX_R + 1):
            eps, omega = eps_step(omega)
            eps_sum += eps

            closed_extra = m(r) + (1 if omega0 <= tau(r) else 0)
            assert eps_sum == closed_extra, (
                "epsilon-sum mismatch", lo, hi, r, eps_sum, closed_extra
            )

            # Direct non-iterated phase formula.
            direct = omega0 * Fraction(
                2 ** (r + closed_extra),
                3**r,
            )
            assert omega == direct, (
                "phase mismatch", lo, hi, r, omega, direct
            )

            # Local first-return cluster depth used by the paid-macro executor.
            h_iter = r + 1 + eps_sum
            h_closed = r + 1 + m(r) + (1 if omega0 <= tau(r) else 0)
            assert h_iter == h_closed


def audit_global_depth_slack() -> int:
    valid_states = 0
    for k in range(2, MAX_K + 1):
        for q in range(1, k + 1):
            d = k - q
            u = m(q) - d
            coeff_survives = 3**q >= 2**k
            assert coeff_survives == (u >= 0), (k, q, d, u)

            if not coeff_survives:
                continue

            valid_states += 1
            omega_q = Fraction(2 ** (q + m(q)), 3**q)
            rho = Fraction(2**k, 3**q)
            assert rho == omega_q / (2**u), (k, q, u, rho, omega_q)

    return valid_states


def main() -> None:
    audit_phase_clock()
    valid_states = audit_global_depth_slack()

    print("PASS MATH-179 exact joint phase/depth compression")
    print(f"phase_cells={len(phase_cells())}")
    print(f"paid_count_range=1..{MAX_R}")
    print(f"global_depth_range=2..{MAX_K}")
    print(f"coefficient_valid_(k,q)_states={valid_states}")
    print("local_depth_formula=h_r=r+1+m(r)+I[omega<=tau(r)]")
    print("global_depth_identity=k=q+m(q)-u")
    print("NO NEW LAYER CLOSURE CLAIM")


if __name__ == "__main__":
    main()
