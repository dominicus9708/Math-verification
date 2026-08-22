#!/usr/bin/env python3
"""Entropy certificate for the q>=4 / q<=3 aligned five-block split.

Among the 32 five-bit parity words, six have q>=4 and 26 have q<=3.
If at most rho*n of n aligned blocks are low-q, the crude language count is

    sum_{j<=rho n} binom(n,j) 26^j 6^(n-j).

For rho <= 26/32 its asymptotic binary entropy per parity bit is

    e(rho) = [H2(rho)+rho log2 26 +(1-rho) log2 6]/5.

The script computes the rho at which the exclusion 1-e(rho) equals the
coefficient-only exclusion 1-H2(log_3 2).

This is an entropy-budget split only; it is not a cross-base transversality
theorem and not a proof of the Collatz conjecture.
"""

import math
from math import comb


def H2(p: float) -> float:
    if p == 0.0 or p == 1.0:
        return 0.0
    return -p * math.log2(p) - (1.0 - p) * math.log2(1.0 - p)


def block_entropy(rho: float) -> float:
    return (
        H2(rho)
        + rho * math.log2(26.0)
        + (1.0 - rho) * math.log2(6.0)
    ) / 5.0


def main() -> None:
    alpha = math.log(2.0) / math.log(3.0)
    eta_coeff = 1.0 - H2(alpha)
    target_entropy = 1.0 - eta_coeff

    lo = 0.0
    hi = 13.0 / 16.0  # 26/32, where the high/low language is unrestricted.
    for _ in range(100):
        mid = (lo + hi) / 2.0
        if block_entropy(mid) < target_entropy:
            lo = mid
        else:
            hi = mid

    rho_star = (lo + hi) / 2.0
    eta_split = 1.0 - block_entropy(rho_star)

    print("alpha", repr(alpha))
    print("eta_coeff", repr(eta_coeff))
    print("rho_star", repr(rho_star))
    print("entropy_at_rho_star", repr(block_entropy(rho_star)))
    print("eta_split", repr(eta_split))

    assert abs(eta_split - eta_coeff) < 1e-13
    assert abs(rho_star - 0.5547058790629843) < 1e-12

    # Small exact finite-count regression.
    n = 20
    m = math.floor(rho_star * n)
    count = sum(comb(n, j) * 26**j * 6 ** (n - j) for j in range(m + 1))
    total = 32**n
    assert 0 < count < total
    print("finite_n20_low_cap", m)
    print("finite_n20_count", count)
    print("finite_n20_fraction", count / total)

    print("high/low five-block entropy split certificate: PASS")


if __name__ == "__main__":
    main()
