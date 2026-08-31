#!/usr/bin/env python3
"""Exact formation-cylinder macrostate for A0 s=1 Route-B.

For one valid nonincreasing formation-rank path

    a_0 >= a_1 >= ... >= a_K,

use the existing formation carry recurrence

    c_{j+1} = 2(c_j + 2^a_j - 2^a_{j+1}) / 3.

Equivalently, with

    d_j = 2(2^a_j - 2^a_{j+1}),

    c_{j+1} = (2*c_j + d_j)/3.

THEOREM (formation cylinder).
There is a unique pair (rho_K,gamma_K), with 0<=rho_K<3^K, such that

    c_0 = rho_K + 3^K n

is exactly the full incoming-carry family for which every one of the first K
formation divisions is integral, and for that same integer parameter n,

    c_K = gamma_K + 2^K n.

The pair is built inductively.  If after j steps

    c_0 = rho_j + 3^j n,
    c_j = gamma_j + 2^j n,

then the next integrality condition determines one ternary digit tau_j:

    tau_j == -(2*gamma_j+d_j)*(2^(j+1))^(-1) mod 3,

and after n=tau_j+3*n',

    rho_{j+1}   = rho_j + 3^j*tau_j,
    gamma_{j+1} = (2*gamma_j+d_j+2^(j+1)*tau_j)/3.

INTERMEDIATE CARRIES.
For the final cylinder c_0=rho_K+3^K n, let

    nu_j   = (rho_K-rho_j)/3^j,
    beta_j = gamma_j + 2^j*nu_j.

Then every intermediate carry is affine in the same family parameter:

    c_j = beta_j + 2^j 3^(K-j) n.

Hence any finite conjunction of fixed interval/sign constraints on the whole
carry path reduces exactly to one integer interval in n.

COMPOSITION.
If a left formation block P has summary (K,rho_P,gamma_P) and a right block Q
with matching boundary rank has summary (L,rho_Q,gamma_Q), then there is one
ternary bridge digit block tau modulo 3^L:

    tau = (rho_Q-gamma_P)*(2^K)^(-1) mod 3^L.

Writing the left family parameter as n=tau+3^L m gives an exact composed
summary

    rho_PQ = rho_P + 3^K*tau,
    eta    = (gamma_P + 2^K*tau - rho_Q)/3^L,
    gamma_PQ = gamma_Q + 2^L*eta.

Thus formation blocks compose as arithmetic cylinders without enumerating
individual incoming carries.

Scope: this is an exact theorem internal to the established formation
automaton for a fixed nonincreasing rank path.  It does NOT prove that every
remaining deterministic Route-B trajectory selects a globally renewable rank
path, and it is not a Collatz proof.
"""

from __future__ import annotations


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def formation_step(c: int, a: int, b: int):
    assert a >= b >= 0
    d = 2 * ((1 << a) - (1 << b))
    numer = 2 * c + d
    if numer % 3:
        return None
    return numer // 3


def summarize(path: tuple[int, ...]) -> tuple[int, int, int]:
    assert path
    assert all(a >= b >= 0 for a, b in zip(path, path[1:]))
    K = len(path) - 1
    rho = 0
    gamma = 0
    for j, (a, b) in enumerate(zip(path, path[1:])):
        d = 2 * ((1 << a) - (1 << b))
        coeff = 1 << (j + 1)
        tau = (-(2 * gamma + d) * pow(coeff, -1, 3)) % 3
        rho += (3**j) * tau
        numer = 2 * gamma + d + coeff * tau
        assert numer % 3 == 0
        gamma = numer // 3
    assert 0 <= rho < 3**K
    return K, rho, gamma


def compose(
    left: tuple[int, int, int],
    right: tuple[int, int, int],
) -> tuple[int, int, int]:
    K, rho_p, gamma_p = left
    L, rho_q, gamma_q = right
    modulus = 3**L
    tau = 0 if L == 0 else (
        (rho_q - gamma_p) * pow(1 << K, -1, modulus)
    ) % modulus
    rho = rho_p + (3**K) * tau
    eta_num = gamma_p + (1 << K) * tau - rho_q
    assert eta_num % modulus == 0
    eta = eta_num // modulus
    gamma = gamma_q + (1 << L) * eta
    assert 0 <= rho < 3 ** (K + L)
    return K + L, rho, gamma


def all_nonincreasing_paths(initial_rank: int, length: int):
    assert initial_rank >= 0 and length >= 0

    def rec(prefix, current, remaining):
        if remaining == 0:
            yield tuple(prefix)
            return
        for nxt in range(current, -1, -1):
            yield from rec(prefix + [nxt], nxt, remaining - 1)

    yield from rec([initial_rank], initial_rank, length)


def intermediate_betas(path: tuple[int, ...]):
    K, rho_K, _ = summarize(path)
    out = []
    for j in range(K + 1):
        _, rho_j, gamma_j = summarize(path[: j + 1])
        assert (rho_K - rho_j) % (3**j) == 0
        nu_j = (rho_K - rho_j) // (3**j)
        beta_j = gamma_j + (1 << j) * nu_j
        out.append(beta_j)
    return tuple(out)


# ---------------------------------------------------------------------------
# Exact finite regression of the theorem and implementation/indexing.
# The theorem itself is the induction/composition algebra above.
# ---------------------------------------------------------------------------

MAX_INITIAL_RANK = 6
MAX_PATH_LENGTH = 6

path_checks = 0
raw_carry_checks = 0
composition_checks = 0
sign_checks = 0
interval_checks = 0

for initial_rank in range(MAX_INITIAL_RANK + 1):
    for K in range(MAX_PATH_LENGTH + 1):
        for path in all_nonincreasing_paths(initial_rank, K):
            path_checks += 1
            summary = summarize(path)
            KK, rho, gamma = summary
            assert KK == K
            betas = intermediate_betas(path)
            coeffs = tuple(
                (1 << j) * 3 ** (K - j)
                for j in range(K + 1)
            )

            # Full-cylinder family and every intermediate carry.
            for n in range(-10, 11):
                c = rho + (3**K) * n
                carries = [c]
                for j in range(K):
                    c = formation_step(c, path[j], path[j + 1])
                    assert c is not None
                    carries.append(c)
                assert c == gamma + (1 << K) * n
                for j, cj in enumerate(carries):
                    assert cj == betas[j] + coeffs[j] * n

            # Raw-source audit: integrality through all K steps is equivalent
            # to one residue class c0=rho mod 3^K.
            modulus = 3**K
            for c0 in range(-300, 301):
                c = c0
                integral = True
                for j in range(K):
                    nxt = formation_step(c, path[j], path[j + 1])
                    if nxt is None:
                        integral = False
                        break
                    c = nxt

                assert integral == ((c0 - rho) % modulus == 0)
                if integral:
                    n = (c0 - rho) // modulus
                    assert c == gamma + (1 << K) * n
                raw_carry_checks += 1

            # Every binary split of a fixed rank path composes to the same
            # direct formation-cylinder summary.
            for split in range(K + 1):
                left = summarize(path[: split + 1])
                right = summarize(path[split:])
                assert compose(left, right) == summary
                composition_checks += 1

            # All-intermediate sign constraints reduce to one n half-line.
            upper_nonpositive = min(
                (-beta) // coeff
                for beta, coeff in zip(betas, coeffs)
            )
            lower_nonnegative = max(
                ceil_div(-beta, coeff)
                for beta, coeff in zip(betas, coeffs)
            )

            # A representative arbitrary two-sided carry corridor.
            L_BOUND = -10
            U_BOUND = 15
            corridor_lo = max(
                ceil_div(L_BOUND - beta, coeff)
                for beta, coeff in zip(betas, coeffs)
            )
            corridor_hi = min(
                (U_BOUND - beta) // coeff
                for beta, coeff in zip(betas, coeffs)
            )

            for n in range(-20, 21):
                carries = tuple(
                    beta + coeff * n
                    for beta, coeff in zip(betas, coeffs)
                )
                assert all(c <= 0 for c in carries) == (n <= upper_nonpositive)
                assert all(c >= 0 for c in carries) == (n >= lower_nonnegative)
                sign_checks += 2

                assert all(
                    L_BOUND <= c <= U_BOUND for c in carries
                ) == (corridor_lo <= n <= corridor_hi)
                interval_checks += 1


assert path_checks == 3_431
assert raw_carry_checks == 2_062_031
assert composition_checks == 21_021
assert sign_checks == 281_342
assert interval_checks == 140_671

print("PASS A0 s=1 Route-B formation cylinder macrostate certificate")
print("summary", "(length,rho mod 3^length,gamma)")
print("source_family", "c0=rho+3^K*n")
print("output_family", "cK=gamma+2^K*n")
print("intermediate_family", "cj=beta_j+2^j*3^(K-j)*n")
print("path_checks", path_checks)
print("raw_carry_checks", raw_carry_checks)
print("composition_checks", composition_checks)
print("sign_checks", sign_checks)
print("interval_checks", interval_checks)
print(
    "compression_consequence",
    "fixed-rank-path formation semantics transports whole arithmetic carry families and composes by macroblocks",
)
print(
    "dsd_audit",
    "integrality, outgoing carry, and all finite intermediate carry corridors share one explicitly defined family parameter",
)
print(
    "status",
    "formation fixed-rank-path macrostate CLOSED; deterministic Route-B rank-path renewal remains OPEN",
)
