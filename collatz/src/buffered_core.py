#!/usr/bin/env python3
"""Exact buffered-core bound for first coefficient-crossing Collatz classes.

Accelerated map: T(n)=n/2 if n even, (3n+1)/2 if n odd.
For q odd entries at the first coefficient crossing let
    sigma = ceil(q log_2 3),
    M = 2**sigma,
    P = 3**q,
    D = M-P > 0.

For an admissible odd-position vector alpha=(alpha_1,...,alpha_q),
    R(alpha)=sum_{i=1}^q 3**(q-i) 2**alpha_i,
    M y = P x + R,
    z = x-y,
so
    M z = D x - R.

If two admissible vectors share their first B odd positions, every remaining
position is >= B. Hence Delta R is divisible by 2**B. Also, from the first-
coefficient-crossing bound alpha_i <= floor((i-1)log_2 3),
    |Delta R| < (q-B) 3**(q-1) <= q 3**(q-1).
Therefore, if
    D 2**B > q 3**(q-1),
then Delta x is a nonzero multiple of 2**B and
    sign(Delta z) = sign(Delta x)
for every pair in the same B-core fiber.

The same threshold also bounds any paradoxical first-crossing canonical start:
    x < q 3**(q-1)/D < 2**B.
Thus its first B parity bits determine x exactly; the remaining tail is not an
independent search axis for such a candidate.

All threshold computations below use integer arithmetic only.
"""

from __future__ import annotations
import argparse


def sigma_exact(q: int) -> int:
    if q < 1:
        raise ValueError("q must be positive")
    # 3**q is never a power of two.
    return (3 ** q).bit_length()


def buffered_core(q: int) -> tuple[int, int, int]:
    """Return (B, sigma, D), minimal B>=0 with D*2**B > q*3**(q-1)."""
    sigma = sigma_exact(q)
    D = (1 << sigma) - 3 ** q
    rhs = q * 3 ** (q - 1)
    B = 0
    while D * (1 << B) <= rhs:
        B += 1
    return B, sigma, D


def dangerous_dimension(q: int) -> int:
    """Exact earlier local dangerous-axis count h(q)."""
    sigma = sigma_exact(q)
    D = (1 << sigma) - 3 ** q
    h = 0
    p = 3 ** (q - 1)
    for _i in range(1, q + 1):
        if p >= D:
            h += 1
            p //= 3
        else:
            break
    return h


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("q", nargs="*", type=int,
                    default=[10, 15, 17, 20, 29, 41, 253, 306, 8951,
                             13606, 15601, 47468, 79335])
    args = ap.parse_args()

    print("q,sigma,h_local,B_buffer,D_bits")
    for q in args.q:
        B, sigma, D = buffered_core(q)
        h = dangerous_dimension(q)
        print(f"{q},{sigma},{h},{B},{D.bit_length()}")


if __name__ == "__main__":
    main()
