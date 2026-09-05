#!/usr/bin/env python3
"""Exact finite regression for the 3-adic Hensel parity gate.

This certificate uses modular inverses of 2 modulo powers of 3, so negative
exponents are handled in the correct 3-adic finite quotient.  The symbolic
proof is in:

  collatz/notes/2026-08-27-Hensel-3adic-domain-and-parity-gate.md

Finite regression is not a proof of a global Collatz statement.
"""

from fractions import Fraction
from itertools import product


def pow2_mod_3adic(exponent: int, modulus: int) -> int:
    """2^exponent in (Z/modulus Z)^x; Python uses modular inverse for exp<0."""
    return pow(2, exponent, modulus)


def allowed_parity(K_mod3: int, e: int):
    if K_mod3 == 1:
        return (e + 1) & 1
    if K_mod3 == 2:
        return e & 1
    return None


def greedy_controls(p, gaps):
    out = []
    cur = p
    for g in gaps:
        cur = max(0, cur - g + 1)
        out.append(cur)
    return tuple(out)


def local_cost(weight, d):
    return 2 * weight * (1 - Fraction(1, 2**d))


def inherited_suffix_cost(start_state, gaps, weights, start_index):
    cur = start_state
    total = Fraction(0)
    for i in range(start_index, len(gaps)):
        cur = max(0, cur - gaps[i] + 1)
        total += local_cost(weights[i], cur)
    return total


def theta_h(p, gaps, exponents, h):
    mod = 3**h
    L = greedy_controls(p, gaps)
    total = 0
    for i in range(h):
        total += (3**i) * pow2_mod_3adic(exponents[i] - L[i], mod)
    return (-total) % mod


def check_negative_exponent_parity():
    checks = 0
    for exponent in range(-100, 101):
        expected = 1 if exponent % 2 == 0 else 2
        assert pow2_mod_3adic(exponent, 3) == expected
        checks += 1
    return checks


def check_one_step_gate():
    checks = 0
    for e in range(-8, 9):
        for L in range(16):
            for K in (1, 2):
                pi = allowed_parity(K, e)
                d_star = L if (L & 1) == pi else L + 1

                assert (K + pow2_mod_3adic(e - d_star, 3)) % 3 == 0
                for d in range(L, d_star):
                    assert (K + pow2_mod_3adic(e - d, 3)) % 3 != 0

                # All later admissible controls have the same parity.
                for d in range(d_star, d_star + 12):
                    admissible = (K + pow2_mod_3adic(e - d, 3)) % 3 == 0
                    assert admissible == (((d - d_star) & 1) == 0)

                # Nonunit K has no action.
                for d in range(L, L + 8):
                    assert pow2_mod_3adic(e - d, 3) != 0
                    assert (0 + pow2_mod_3adic(e - d, 3)) % 3 != 0

                checks += 1
    return checks


def check_one_step_bellman_formula():
    checks = 0
    for n in range(1, 6):
        for gaps in product((1, 2), repeat=n):
            weights = tuple(Fraction(i + 2, 19) for i in range(n))
            for p in range(5):
                Ls = greedy_controls(p, gaps)
                L = Ls[0]

                baseline = sum(
                    local_cost(weights[i], Ls[i]) for i in range(n)
                )

                for e in range(-2, 3):
                    for K in (1, 2):
                        pi = allowed_parity(K, e)
                        d_star = L if (L & 1) == pi else L + 1

                        refined = local_cost(weights[0], d_star)
                        refined += inherited_suffix_cost(
                            d_star, gaps, weights, 1
                        )

                        # Exhaustively verify the smallest same-parity action
                        # wins over a generous finite tail of alternatives.
                        candidates = []
                        for d in range(L, L + 18):
                            if (K + pow2_mod_3adic(e - d, 3)) % 3 == 0:
                                val = local_cost(weights[0], d)
                                val += inherited_suffix_cost(d, gaps, weights, 1)
                                candidates.append(val)
                        assert refined == min(candidates)

                        if d_star == L:
                            assert refined == baseline
                        else:
                            assert refined > baseline
                            assert refined - baseline >= weights[0] * Fraction(1, 2**L)

                            # Exact persistence tax formula.
                            perturbed = [d_star]
                            cur = d_star
                            for i in range(1, n):
                                cur = max(0, cur - gaps[i] + 1)
                                perturbed.append(cur)
                            expected_delta = sum(
                                local_cost(weights[i], perturbed[i])
                                - local_cost(weights[i], Ls[i])
                                for i in range(n)
                            )
                            assert refined - baseline == expected_delta

                        checks += 1
    return checks


def check_finite_depth_address():
    checks = 0
    for h in range(1, 6):
        for gaps in product((1, 2), repeat=h):
            for p in range(4):
                L = greedy_controls(p, gaps)
                for exponents in product(range(3), repeat=h):
                    th = theta_h(p, gaps, exponents, h)

                    # Terminal depth-h divisibility implies each prefix
                    # divisibility; check directly in every finite quotient.
                    for r in range(1, h + 1):
                        mod = 3**r
                        prefix = th % mod
                        for i in range(r):
                            prefix += (3**i) * pow2_mod_3adic(
                                exponents[i] - L[i], mod
                            )
                        assert prefix % mod == 0

                    # Nested cylinder property.
                    if h > 1:
                        assert th % (3 ** (h - 1)) == theta_h(
                            p, gaps, exponents, h - 1
                        )

                    checks += 1
    return checks


def main():
    parity_checks = check_negative_exponent_parity()
    gate_checks = check_one_step_gate()
    bellman_checks = check_one_step_bellman_formula()
    address_checks = check_finite_depth_address()

    print("PASS")
    print(f"negative-exponent parity checks: {parity_checks}")
    print(f"one-step parity-gate cases: {gate_checks}")
    print(f"one-step Bellman cases: {bellman_checks}")
    print(f"finite-depth address cases: {address_checks}")


if __name__ == "__main__":
    main()
