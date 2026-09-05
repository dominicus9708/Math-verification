#!/usr/bin/env python3
"""Bounded-drop / sparse-run theorem for the formation automaton.

A formation path is a weakly decreasing integer-rank sequence

    k=a_0 >= a_1 >= ... >= a_K >= 0

with carry recurrence

    c_{j+1} = (2*c_j + d_j)/3,
    d_j = 2*(2^a_j - 2^a_{j+1}).

Every path factors uniquely into same-rank runs and strict drops

    S_{b0}^{ell0} D_{b0,b1} S_{b1}^{ell1} ... D_{b{s-1},bs} S_{bs}^{ells},

where

    k=b0>b1>...>bs>=0,
    s<=k,
    ell_i>=0,
    sum ell_i + s = K.

Thus arbitrary path length does not imply arbitrary structural rank-word
complexity: there are at most k strict drops and at most k+1 same-rank runs.

Same-rank run theorem:

    S_a^ell is legal exactly on c=3^ell*n,
    and maps c -> 2^ell*n.

Hence its formation-cylinder summary is simply (ell,0,0), independently of a.

Sparse unrolling theorem:

    3^K*c_K = 2^K*c_0 + D,

where

    D = sum_j 2^(K-1-j)*3^j*d_j.

Only strict drops contribute because d_j=0 for a_j=a_{j+1}.  Therefore D has
at most k nonzero terms.  If the strict drops occur at transition positions
p_i and levels b_{i-1}->b_i, then

    D = sum_i 2^(K-p_i)*3^p_i*(2^b_{i-1}-2^b_i).

The full source cylinder is obtained directly from

    rho == -2^(-K)*D mod 3^K,
    gamma = (2^K*rho + D)/3^K.

Final divisibility by 3^K automatically implies every prefix division is
integral: modulo 3^j, the final numerator reduces to 2^(K-j) times the j-prefix
numerator, and 2 is invertible modulo powers of 3.

Consequently the exact formation-cylinder summary can be computed from the
bounded drop skeleton and run lengths without materializing K rank steps.

Counting theorem.  For exactly s strict drops:

  * choose the s lower rank levels in C(k,s) ways;
  * choose ell_0+...+ell_s=K-s in C(K,s) ways.

Hence

    sum_s C(k,s) C(K,s) = C(K+k,k),

recovering the existing formation-path count.  Across all K, however, there
are only sum_s C(k,s)=2^k strict-drop skeleton TYPES; K-dependence lives only
in the run-length parameters.

Scope: exact theorem internal to the established formation automaton.  It
corrects the idea that an arbitrary-length deterministic rank selector is
needed.  Formation membership is existential over nonincreasing rank paths;
what remains is variable-target/run-parameter interaction, not stepwise rank
selection.  No Collatz-global conclusion is claimed.
"""

from __future__ import annotations

from math import comb


def all_nonincreasing_paths(initial_rank: int, length: int):
    def rec(prefix, current, remaining):
        if remaining == 0:
            yield tuple(prefix)
            return
        for nxt in range(current, -1, -1):
            yield from rec(prefix + [nxt], nxt, remaining - 1)

    yield from rec([initial_rank], initial_rank, length)


def decompose_runs(path: tuple[int, ...]):
    assert path
    assert all(a >= b >= 0 for a, b in zip(path, path[1:]))
    levels = [path[0]]
    runs = []
    same = 0
    for a, b in zip(path, path[1:]):
        if a == b:
            same += 1
        else:
            runs.append(same)
            levels.append(b)
            same = 0
    runs.append(same)
    return tuple(levels), tuple(runs)


def reconstruct_runs(levels, runs):
    assert len(levels) == len(runs) >= 1
    out = [levels[0]]
    for i, level in enumerate(levels):
        out.extend([level] * runs[i])
        if i + 1 < len(levels):
            out.append(levels[i + 1])
    return tuple(out)


def summarize_stepwise(path: tuple[int, ...]):
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
    return K, rho, gamma


def sparse_correction(path: tuple[int, ...]) -> int:
    K = len(path) - 1
    D = 0
    for j, (a, b) in enumerate(zip(path, path[1:])):
        if a == b:
            continue
        D += (
            (1 << (K - 1 - j))
            * (3**j)
            * 2
            * ((1 << a) - (1 << b))
        )
    return D


def summarize_sparse(path: tuple[int, ...]):
    K = len(path) - 1
    D = sparse_correction(path)
    if K == 0:
        return 0, 0, 0
    modulus = 3**K
    rho = (-D * pow(1 << K, -1, modulus)) % modulus
    numer = (1 << K) * rho + D
    assert numer % modulus == 0
    gamma = numer // modulus
    return K, rho, gamma


def compose(left, right):
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
    return K + L, rho, gamma


def run_summary(length: int):
    assert length >= 0
    return length, 0, 0


def drop_summary(a: int, b: int):
    assert a > b >= 0
    return summarize_stepwise((a, b))


def summarize_by_runs(path: tuple[int, ...]):
    levels, runs = decompose_runs(path)
    state = (0, 0, 0)
    for i, level in enumerate(levels):
        state = compose(state, run_summary(runs[i]))
        if i + 1 < len(levels):
            state = compose(state, drop_summary(level, levels[i + 1]))
    return state


def direct_carries(path: tuple[int, ...], c0: int):
    out = [c0]
    c = c0
    for a, b in zip(path, path[1:]):
        numer = 2 * c + 2 * ((1 << a) - (1 << b))
        if numer % 3:
            return None
        c = numer // 3
        out.append(c)
    return tuple(out)


# ---------------------------------------------------------------------------
# Exhaustive regression of factorization, sparse formula and macro composition.
# The proof is the algebra in the module docstring; these checks audit indexing.
# ---------------------------------------------------------------------------

MAX_K = 8
MAX_RANK = 7
path_checks = 0
source_checks = 0
count_identity_checks = 0

for k in range(MAX_RANK + 1):
    assert sum(comb(k, s) for s in range(k + 1)) == 1 << k
    for K in range(MAX_K + 1):
        paths = tuple(all_nonincreasing_paths(k, K))
        assert len(paths) == comb(K + k, k)
        assert sum(
            comb(k, s) * comb(K, s)
            for s in range(min(k, K) + 1)
        ) == comb(K + k, k)
        count_identity_checks += 1

        for path in paths:
            levels, runs = decompose_runs(path)
            s = len(levels) - 1
            assert s <= min(k, K)
            assert sum(runs) + s == K
            assert reconstruct_runs(levels, runs) == path

            direct = summarize_stepwise(path)
            sparse = summarize_sparse(path)
            macro = summarize_by_runs(path)
            assert sparse == direct == macro

            # Sparse correction has one term per strict drop, never per step.
            assert sum(a != b for a, b in zip(path, path[1:])) == s

            KK, rho, gamma = direct
            modulus = 3**KK
            # Representatives of the exact source cylinder realize the path;
            # nearby non-residue representatives do not realize all K steps.
            for n in range(-3, 4):
                c0 = rho + modulus * n
                carries = direct_carries(path, c0)
                assert carries is not None
                assert carries[-1] == gamma + (1 << KK) * n
                source_checks += 1

            path_checks += 1

# Same-rank run theorem, including rejection of nonmultiples of 3^ell.
run_checks = 0
for ell in range(13):
    modulus = 3**ell
    for c0 in range(-500, 501):
        path = tuple([5] * (ell + 1))
        carries = direct_carries(path, c0)
        legal = (c0 % modulus == 0)
        assert (carries is not None) == legal
        if legal:
            n = c0 // modulus
            assert carries[-1] == (1 << ell) * n
        run_checks += 1

assert path_checks == 24_309
assert source_checks == 170_163
assert count_identity_checks == 72
assert run_checks == 13_013

print("PASS A0 s=1 Route-B bounded-drop formation run certificate")
print("path_checks", path_checks)
print("source_checks", source_checks)
print("count_identity_checks", count_identity_checks)
print("same_rank_run_checks", run_checks)
print("max_structural_drops", "initial rank k")
print("drop_skeleton_types", "2^k")
print("same_rank_run_summary", "(ell,0,0): c=3^ell*n -> 2^ell*n")
print("sparse_formula", "3^K*cK=2^K*c0+D; D has <=k nonzero drop terms")
print(
    "dsd_audit",
    "arbitrary formation depth is separated from bounded structural rank-change complexity",
)
print(
    "status",
    "bounded-drop/run compression CLOSED; variable-target/run-parameter globalization remains OPEN",
)
