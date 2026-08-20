#!/usr/bin/env python3
"""Certificate for the frequency/slack rank-one cocycle of the coefficient
Fourier transfer.

Let b_j=ceil(j log_3 2) and e=q-b_j>=0 be the ordinary global coefficient
slack.  For a fixed final Fourier modulus, write T_j(t) for the one-step
weighted transfer on slack states.  Let S be the unilateral shift

    S e_a = e_(a+1),

and P0 the rank-one projection onto slack zero.

The exact local identities are

    T_j(3t) S = S T_j(t)                  if b_(j+1)=b_j,
    T_j(3t) S = S T_j(t) + P0             if b_(j+1)=b_j+1.

The reason is the exact phase covariance

    3 t * 3^(-(b_(j+1)+e))
      == t * 3^(-(b_(j+1)+e-1))  (mod 2^n)

for e>=1.  At a rise, the shifted input has one additional even transition
from slack 1 to slack 0; that single transition is P0.

The product identity is the corresponding discrete Duhamel formula: every
failure of 3-frequency covariance is a sum of rank-one slack-zero boundary
insertions at Beatty rises.

The all-j phase congruence checks below are exact integer arithmetic.  A small
complex-matrix regression independently checks both local and product forms.
"""

from __future__ import annotations

import cmath
import math
import numpy as np


def barriers(k: int) -> list[int]:
    b = [0] * (k + 1)
    p2 = p3 = 1
    q = 0
    for j in range(1, k + 1):
        p2 *= 2
        while p3 < p2:
            p3 *= 3
            q += 1
        b[j] = q
    return b


def phase_residue(k: int, j: int, t: int, q: int) -> tuple[int, int]:
    mod = 1 << (k - j)
    return (t * pow(3, -q, mod)) % mod, mod


def exact_phase_covariance() -> None:
    for k in range(2, 65):
        b = barriers(k)
        for j in range(k):
            for t in (1, 3, 5, 17, 41):
                for e in range(1, 20):
                    q = b[j + 1] + e
                    lhs = phase_residue(k, j, 3 * t, q)
                    rhs = phase_residue(k, j, t, q - 1)
                    assert lhs == rhs, (k, j, t, e, lhs, rhs)


def step_matrix(k: int, j: int, t: int, E: int) -> tuple[np.ndarray, int]:
    b = barriers(k)
    d = b[j + 1] - b[j]
    rem = k - j
    mod = 1 << rem
    T = np.zeros((E, E), dtype=np.complex128)

    for e in range(E):
        # even bit: e' = e-d
        ep = e - d
        if 0 <= ep < E:
            T[ep, e] += 1.0

        # odd bit: e' = e+1-d
        ep = e + 1 - d
        if 0 <= ep < E:
            qnew = b[j + 1] + ep
            residue = (t * pow(3, -qnew, mod)) % mod
            phase = cmath.exp(-2j * math.pi * residue / mod)
            T[ep, e] += phase

    return T, d


def shift(E: int) -> np.ndarray:
    S = np.zeros((E, E), dtype=np.complex128)
    for e in range(E - 1):
        S[e + 1, e] = 1.0
    return S


def proj0(E: int) -> np.ndarray:
    P = np.zeros((E, E), dtype=np.complex128)
    P[0, 0] = 1.0
    return P


def local_matrix_regression() -> None:
    E = 36
    S = shift(E)
    P = proj0(E)
    worst = 0.0

    for k in (10, 15, 22, 31):
        for j in range(k):
            for t in (1, 3, 5, 17):
                A, d = step_matrix(k, j, 3 * t, E)
                B, _ = step_matrix(k, j, t, E)
                target = S @ B + (P if d else 0.0)
                # Ignore the top two artificial truncation rows/columns.
                err = float(np.max(np.abs((A @ S - target)[: E - 2, : E - 2])))
                worst = max(worst, err)
                assert err < 1e-11, (k, j, t, d, err)

    print("local_matrix_worst_error", worst)


def product_regression() -> None:
    # Verify the Duhamel expansion for several small horizons.  A larger slack
    # truncation than the horizon prevents top-boundary artifacts in the tested
    # columns.
    for k in (6, 9, 12):
        E = k + 8
        S = shift(E)
        P = proj0(E)
        b = barriers(k)
        for t in (1, 5):
            A = [step_matrix(k, j, 3 * t, E)[0] for j in range(k)]
            B = [step_matrix(k, j, t, E)[0] for j in range(k)]

            def product(seq):
                X = np.eye(E, dtype=np.complex128)
                for M in seq:
                    X = M @ X
                return X

            left = product(A) @ S
            right = S @ product(B)

            for j in range(k):
                if b[j + 1] != b[j] + 1:
                    continue
                after = product(A[j + 1 :])
                before = product(B[:j])
                right += after @ P @ before

            err = float(np.max(np.abs((left - right)[: k + 2, : k + 2])))
            assert err < 2e-11, (k, t, err)

    print("product_duhamel_regression", "PASS")


def main() -> None:
    exact_phase_covariance()
    local_matrix_regression()
    product_regression()
    print("frequency-slack rank-one cocycle: PASS")


if __name__ == "__main__":
    main()
