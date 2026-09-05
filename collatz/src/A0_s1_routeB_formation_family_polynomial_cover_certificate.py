#!/usr/bin/env python3
"""Exact polynomial-size family cover for fixed-initial-rank formation gates.

Fix an initial formation rank k and a horizon K. Every admissible rank path is
weakly decreasing,

    k=a_0 >= a_1 >= ... >= a_K >= 0.

There are exactly

    binom(K+k, k)

such paths. For each fixed path P, the formation-cylinder theorem gives one
source family

    c_0 = rho_P + 3^K n,

and every intermediate carry is affine in the same n with positive
coefficient. Therefore any finite conjunction of integer interval constraints
on the carry path reduces to one integer interval

    n in [Nmin(P), Nmax(P)] intersect Z.

Consequently an existential formation gate over all nonincreasing rank paths
is represented exactly by a union of at most

    binom(K+k,k) = O(K^k)   (fixed k)

arithmetic-cylinder interval pieces. Different paths may give the same piece;
this is an upper bound, not a disjointness claim.

Equivalently, using the bounded-drop factorization, there are at most 2^k
strict-drop skeleton types, and each skeleton has at most k+1 run-length
parameters. Thus arbitrary formation depth is parameter growth, not
exponential rank-word branching, when k is fixed.

Scope: formation-side existential semantics only. This does not generate the
candidate Collatz parity block and does not prove Route-B closure.
"""

from math import comb


def ceil_div(a: int, b: int) -> int:
    assert b > 0
    return -((-a) // b)


def all_paths(k: int, K: int):
    def rec(prefix, current, remaining):
        if remaining == 0:
            yield tuple(prefix)
            return
        for nxt in range(current, -1, -1):
            yield from rec(prefix + [nxt], nxt, remaining - 1)

    yield from rec([k], k, K)


def formation_step(c: int, a: int, b: int):
    numer = 2 * c + 2 * ((1 << a) - (1 << b))
    if numer % 3:
        return None
    return numer // 3


def summarize(path):
    K = len(path) - 1
    rho = 0
    gamma = 0
    for j, (a, b) in enumerate(zip(path, path[1:])):
        d = 2 * ((1 << a) - (1 << b))
        coeff = 1 << (j + 1)
        tau = (-(2 * gamma + d) * pow(coeff, -1, 3)) % 3
        rho += (3**j) * tau
        gamma = (2 * gamma + d + coeff * tau) // 3
    return K, rho, gamma


def intermediate_affine(path):
    K, rho_K, _ = summarize(path)
    out = []
    for j in range(K + 1):
        _, rho_j, gamma_j = summarize(path[: j + 1])
        assert (rho_K - rho_j) % (3**j) == 0
        nu_j = (rho_K - rho_j) // (3**j)
        beta_j = gamma_j + (1 << j) * nu_j
        coeff_j = (1 << j) * 3 ** (K - j)
        out.append((beta_j, coeff_j))
    return tuple(out)


def corridor_piece(path, lower: int, upper: int):
    """Exact source-cylinder piece whose every carry lies in [lower,upper]."""
    K, rho, _ = summarize(path)
    affine = intermediate_affine(path)
    n_lo = max(ceil_div(lower - beta, coeff) for beta, coeff in affine)
    n_hi = min((upper - beta) // coeff for beta, coeff in affine)
    return K, rho, n_lo, n_hi


def symbolic_accept(c0: int, pieces):
    for K, rho, n_lo, n_hi in pieces:
        modulus = 3**K
        if (c0 - rho) % modulus:
            continue
        n = (c0 - rho) // modulus
        if n_lo <= n <= n_hi:
            return True
    return False


def direct_accept(c0: int, paths, lower: int, upper: int):
    for path in paths:
        c = c0
        carries = [c]
        legal = True
        for a, b in zip(path, path[1:]):
            c = formation_step(c, a, b)
            if c is None:
                legal = False
                break
            carries.append(c)
        if legal and all(lower <= x <= upper for x in carries):
            return True
    return False


MAX_RANK = 4
MAX_DEPTH = 5
LOWER = -8
UPPER = 12
membership_checks = 0
symbolic_path_pieces = 0
count_checks = 0

for k in range(MAX_RANK + 1):
    assert sum(comb(k, s) for s in range(k + 1)) == 1 << k
    for K in range(MAX_DEPTH + 1):
        paths = tuple(all_paths(k, K))
        assert len(paths) == comb(K + k, k)
        assert sum(
            comb(k, s) * comb(K, s)
            for s in range(min(k, K) + 1)
        ) == comb(K + k, k)
        count_checks += 1

        pieces = tuple(corridor_piece(path, LOWER, UPPER) for path in paths)
        assert len(pieces) == comb(K + k, k)
        symbolic_path_pieces += len(pieces)

        for c0 in range(-150, 151):
            assert symbolic_accept(c0, pieces) == direct_accept(
                c0, paths, LOWER, UPPER
            )
            membership_checks += 1

assert count_checks == 30
assert symbolic_path_pieces == 461
assert membership_checks == 9_030

print("PASS A0 s=1 Route-B formation family polynomial cover certificate")
print("max_initial_rank", MAX_RANK)
print("max_depth", MAX_DEPTH)
print("count_checks", count_checks)
print("symbolic_path_pieces", symbolic_path_pieces)
print("membership_checks", membership_checks)
print("exact_piece_bound", "binom(K+k,k) arithmetic-cylinder intervals")
print("fixed_rank_complexity", "O(K^k) symbolic formation pieces")
print("skeleton_types", "at most 2^k strict-drop skeletons")
print(
    "dsd_audit",
    "formation-side long depth is polynomial family growth for fixed initial rank; deterministic parity-block generation remains separate",
)
