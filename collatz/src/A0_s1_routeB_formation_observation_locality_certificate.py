#!/usr/bin/env python3
"""Exact projective observation-locality theorem for formation cylinders.

For a weakly decreasing rank path

    a_0 >= ... >= a_K,

let rho_K be its exact formation source residue modulo 3^K.  Writing strict
rank drops at transition positions p_i and levels b_{i-1}->b_i, the sparse
formula gives

    rho_K == - sum_i 3^p_i * 2^(-p_i) * (2^b_{i-1}-2^b_i)  (mod 3^K).

Therefore, for every m<=K,

    rho_K mod 3^m = rho_m,

where rho_m is the source residue of the length-m prefix.  Drops at p_i>=m
vanish modulo 3^m, and the total future depth K cancels from every earlier
term.

Equivalently every deeper cylinder is an exact ternary refinement of its
prefix cylinder:

    rho_K = rho_m + 3^m * nu,   0<=nu<3^(K-m),

and

    rho_K + 3^K*n
      = rho_m + 3^m*(nu + 3^(K-m)*n).

Thus increasing formation observation depth cannot invalidate already exposed
ternary source information.  It only refines it.

Important scope distinction:
* projective residue information is nested exactly;
* this does NOT say rho_m alone is a future right-congruence state, because
  future composition also depends on the boundary rank and outgoing carry;
* it does NOT prove the physical variable target has a uniformly bounded
  required ternary depth.

The theorem is algebraic.  The exhaustive checks below audit indexing and the
implementation of sparse residues.
"""

from math import comb


def all_nonincreasing_paths(initial_rank: int, length: int):
    def rec(prefix, current, remaining):
        if remaining == 0:
            yield tuple(prefix)
            return
        for nxt in range(current, -1, -1):
            yield from rec(prefix + [nxt], nxt, remaining - 1)

    yield from rec([initial_rank], initial_rank, length)


def sparse_summary(path: tuple[int, ...]):
    assert path
    assert all(a >= b >= 0 for a, b in zip(path, path[1:]))
    K = len(path) - 1
    if K == 0:
        return 0, 0, 0

    D = 0
    for j, (a, b) in enumerate(zip(path, path[1:])):
        if a == b:
            continue
        D += (
            (1 << (K - j))
            * (3**j)
            * ((1 << a) - (1 << b))
        )

    modulus = 3**K
    rho = (-D * pow(1 << K, -1, modulus)) % modulus
    numer = (1 << K) * rho + D
    assert numer % modulus == 0
    gamma = numer // modulus
    return K, rho, gamma


def drop_local_residue(path: tuple[int, ...], m: int) -> int:
    """Compute rho mod 3^m directly from only drop events before m."""
    assert 0 <= m <= len(path) - 1
    if m == 0:
        return 0
    modulus = 3**m
    out = 0
    for p, (a, b) in enumerate(zip(path, path[1:])):
        if p >= m:
            break
        if a == b:
            continue
        delta = (1 << a) - (1 << b)
        out -= (3**p) * pow(1 << p, -1, modulus) * delta
    return out % modulus


MAX_INITIAL_RANK = 7
MAX_DEPTH = 9
path_checks = 0
projection_checks = 0
nesting_checks = 0
local_formula_checks = 0

for k in range(MAX_INITIAL_RANK + 1):
    for K in range(MAX_DEPTH + 1):
        paths = tuple(all_nonincreasing_paths(k, K))
        assert len(paths) == comb(K + k, k)

        for path in paths:
            _, rho_K, _ = sparse_summary(path)
            path_checks += 1

            for m in range(K + 1):
                _, rho_m, _ = sparse_summary(path[: m + 1])
                modulus = 3**m

                assert rho_K % modulus == rho_m
                projection_checks += 1

                assert drop_local_residue(path, m) == rho_m
                local_formula_checks += 1

                if m == K:
                    continue

                assert (rho_K - rho_m) % modulus == 0
                nu = (rho_K - rho_m) // modulus
                assert 0 <= nu < 3 ** (K - m)

                # The deep source family is literally a sub-cylinder of the
                # prefix source family under the displayed parameter change.
                for n in range(-2, 3):
                    c0_deep = rho_K + (3**K) * n
                    n_prefix = nu + 3 ** (K - m) * n
                    c0_prefix = rho_m + (3**m) * n_prefix
                    assert c0_deep == c0_prefix
                    nesting_checks += 1

assert path_checks == 43_757
assert projection_checks == 388_960
assert local_formula_checks == 388_960
assert nesting_checks == 1_726_015

print("PASS A0 s=1 Route-B formation observation locality certificate")
print("path_checks", path_checks)
print("projection_checks", projection_checks)
print("local_formula_checks", local_formula_checks)
print("nesting_checks", nesting_checks)
print("projection", "rho_K mod 3^m = rho_m(prefix)")
print("locality", "drops at positions >=m are invisible modulo 3^m")
print("nesting", "deep cylinder is an exact sub-cylinder of every prefix cylinder")
print(
    "dsd_audit",
    "unbounded arithmetic resolution is projectively consistent and does not retroactively alter described ternary information",
)
print(
    "status",
    "formation observation locality CLOSED; variable physical-target projective compatibility remains OPEN",
)
