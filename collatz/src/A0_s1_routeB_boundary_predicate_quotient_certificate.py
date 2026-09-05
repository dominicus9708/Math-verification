#!/usr/bin/env python3
"""Exact predicate-relative quotient for nested Route-B boundary gates.

For a binary word W of length h with q ones and correction C(W), define

    D_K(W) = -C(W) * (3^q)^(-1) mod 2^K,
    E_L(W) =  C(W) * (2^h)^(-1) mod 3^L.

These are projective boundary observations:

    K1 <= K2  => D_K2 mod 2^K1 = D_K1,
    L1 <= L2  => E_L2 mod 3^L1 = E_L1.

Therefore any conjunction of compatible target equalities on ONE block,

    D_K(W)=d_K  (K in Kset),
    E_L(W)=e_L  (L in Lset),

where the target residues are reductions of the largest requested residues,
is equivalent to the two maximal-resolution tests only.

Thus

    Omega_{K*,L*}(W) = (D_{K*}(W), E_{L*}(W))

is an exact predicate-relative quotient for this boundary-gate subsystem.
It may identify states whose full future source/parity semantics differ.
That is legal because only the explicitly defined boundary predicate is being
preserved.

Scope:
* exact for nested equality gates on the same block;
* does not preserve correction-language membership, ballot, formation, or an
  undefined C4F predicate;
* does not by itself give a renewable long-orbit state.

The finite enumeration below is only an implementation/indexing regression.
"""

from itertools import product


def correction(bits):
    C = 0
    q = 0
    for i, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << i)
            q += 1
    return C, q


def start_dyadic(bits, K):
    C, q = correction(bits)
    assert 1 <= K <= len(bits)
    mod = 1 << K
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod


def end_ternary(bits, L):
    C, q = correction(bits)
    assert 1 <= L <= q
    mod = 3**L
    return (C * pow(pow(2, len(bits), mod), -1, mod)) % mod


MAX_H = 7
nested_dyadic_checks = 0
nested_ternary_checks = 0
compatible_conjunction_pair_checks = 0

for h in range(1, MAX_H + 1):
    groups = {}
    for bits in product((0, 1), repeat=h):
        _, q = correction(bits)
        groups.setdefault(q, []).append(bits)

        for K2 in range(1, h + 1):
            d2 = start_dyadic(bits, K2)
            for K1 in range(1, K2 + 1):
                assert d2 % (1 << K1) == start_dyadic(bits, K1)
                nested_dyadic_checks += 1

        for L2 in range(1, q + 1):
            e2 = end_ternary(bits, L2)
            for L1 in range(1, L2 + 1):
                assert e2 % (3**L1) == end_ternary(bits, L1)
                nested_ternary_checks += 1

    # Audit the conjunction collapse on all pairs in each fixed-(h,q) class.
    for q, words in groups.items():
        for target in words:
            target_d = {K: start_dyadic(target, K) for K in range(1, h + 1)}
            target_e = {L: end_ternary(target, L) for L in range(1, q + 1)}

            for candidate in words:
                all_d = all(
                    start_dyadic(candidate, K) == target_d[K]
                    for K in target_d
                )
                max_d = start_dyadic(candidate, h) == target_d[h]
                assert all_d == max_d

                if q:
                    all_e = all(
                        end_ternary(candidate, L) == target_e[L]
                        for L in target_e
                    )
                    max_e = end_ternary(candidate, q) == target_e[q]
                    assert all_e == max_e

                compatible_conjunction_pair_checks += 1

assert nested_dyadic_checks == 5_630
assert nested_ternary_checks == 1_792
assert compatible_conjunction_pair_checks == 4_706

print("PASS A0 s=1 Route-B boundary predicate quotient certificate")
print("max_word_length", MAX_H)
print("nested_dyadic_checks", nested_dyadic_checks)
print("nested_ternary_checks", nested_ternary_checks)
print("compatible_conjunction_pair_checks", compatible_conjunction_pair_checks)
print(
    "exact_quotient",
    "compatible nested boundary equalities on one block reduce to maximal D_K and E_L coordinates",
)
print(
    "predicate_scope",
    "boundary equality subsystem only; interior language/ballot/formation semantics are not silently merged",
)
print(
    "dsd_audit",
    "different full source states may be identified only after the preserved predicate has been explicitly specified",
)
