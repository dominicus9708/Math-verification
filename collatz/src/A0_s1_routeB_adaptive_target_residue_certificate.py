#!/usr/bin/env python3
"""Adaptive target-residue oracle for A0 s=1 Route-B.

Once a physical source integer X is fixed, a candidate parity block W of
length h and odd-count q has correction C(W) and canonical source residue

    r_W = -C(W) * (3^q)^(-1) mod 2^h.

Hence W is exactly the length-h parity cylinder followed by X iff

    C(W) == -3^q X  (mod 2^h).

At partial dyadic resolution K<=h define the target residue

    tau_K(X,q) = -3^q X mod 2^K.

Then C(W) mod 2^K == tau_K(X,q) is an exact K-bit screening condition.
For two distinct candidates U,V with the same (h,q), put

    Delta = C(U)-C(V).

Their correction residues agree through exactly v_2(Delta) dyadic bits, so

    K_* = v_2(Delta)+1

is the exact first resolution that distinguishes them.  Since distinct
same-(h,q) parity cylinders have different full source residues mod 2^h,
K_*<=h.

This closes a target-aware adaptive dyadic oracle.  Full K=h congruence is
exact parity-cylinder identification for fixed X and q.  Lower K is screening
only.  The oracle does not by itself establish Route-B ballot, first-passage,
renewal, or universal language membership conditions.
"""

from itertools import combinations

MAX_DEPTH = 11
LIFTS = (1, 2, 4)


def T(x: int) -> int:
    assert x >= 0
    return (3 * x + 1) // 2 if x & 1 else x // 2


def correction_summary(bits):
    h = q = C = 0
    for bit in bits:
        assert bit in (0, 1)
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return h, q, C


def canonical_source_residue(h: int, q: int, C: int) -> int:
    modulus = 1 << h
    return (-C * pow(pow(3, q, modulus), -1, modulus)) % modulus


def target_residue(X: int, q: int, K: int) -> int:
    assert K >= 1
    modulus = 1 << K
    return (-pow(3, q, modulus) * (X % modulus)) % modulus


def valuation2(n: int) -> int:
    assert n != 0
    n = abs(n)
    out = 0
    while n % 2 == 0:
        n //= 2
        out += 1
    return out


word_count = 0
direct_orbit_checks = 0
target_resolution_checks = 0
same_hq_pair_checks = 0
adaptive_first_separation_checks = 0
full_resolution_unique_groups = 0
max_observed_v2 = -1

for h in range(1, MAX_DEPTH + 1):
    groups = {}

    for address in range(1 << h):
        bits = tuple((address >> i) & 1 for i in range(h))
        hh, q, C = correction_summary(bits)
        assert hh == h
        r = canonical_source_residue(h, q, C)
        groups.setdefault(q, []).append((bits, C, r))
        word_count += 1

        # Every lift X=r+2^h*n has exactly this first h-bit parity cylinder,
        # and its target congruence is correct at every partial resolution.
        for n in LIFTS:
            X = r + (1 << h) * n
            z = X
            got = []
            for _ in range(h):
                got.append(z & 1)
                z = T(z)
            assert tuple(got) == bits
            direct_orbit_checks += 1

            for K in range(1, h + 1):
                assert C % (1 << K) == target_residue(X, q, K)
                target_resolution_checks += 1

    for q, items in groups.items():
        # Full target/correction residue is injective inside every fixed
        # (h,q) class.  Equivalently, distinct candidates cannot survive all
        # h dyadic target bits.
        full_residues = [C % (1 << h) for _bits, C, _r in items]
        assert len(full_residues) == len(set(full_residues))
        full_resolution_unique_groups += 1

        for (U, CU, rU), (V, CV, rV) in combinations(items, 2):
            assert U != V
            Delta = CU - CV
            assert Delta != 0
            v2 = valuation2(Delta)
            assert v2 < h
            max_observed_v2 = max(max_observed_v2, v2)
            K_star = v2 + 1
            assert 1 <= K_star <= h
            same_hq_pair_checks += 1

            # Use a positive source integer in U's cylinder.  U and V are
            # indistinguishable to the target oracle below K_star, then V is
            # rejected exactly at K_star while U survives.
            X = rU + (1 << h)
            for K in range(1, K_star):
                modulus = 1 << K
                tau = target_residue(X, q, K)
                assert CU % modulus == CV % modulus == tau

            modulus = 1 << K_star
            tau = target_residue(X, q, K_star)
            assert CU % modulus == tau
            assert CV % modulus != tau
            adaptive_first_separation_checks += 1


assert word_count == 4_094
assert direct_orbit_checks == 12_282
assert target_resolution_checks == 122_886
assert same_hq_pair_checks == 476_145
assert adaptive_first_separation_checks == 476_145
assert full_resolution_unique_groups == 77
assert max_observed_v2 == 9

print("PASS A0 s=1 Route-B adaptive target-residue certificate")
print("max_depth", MAX_DEPTH)
print("word_count", word_count)
print("direct_orbit_checks", direct_orbit_checks)
print("target_resolution_checks", target_resolution_checks)
print("same_hq_pair_checks", same_hq_pair_checks)
print("adaptive_first_separation_checks", adaptive_first_separation_checks)
print("full_resolution_unique_groups", full_resolution_unique_groups)
print("max_observed_v2", max_observed_v2)
print(
    "formation_audit",
    "after source X and odd-count q are fixed, tau_K(X,q) is a determined target coordinate; no candidate interior materialization is required to form it",
)
print(
    "axis_audit",
    "K is an external dyadic observation/refinement axis; increasing K refines target discrimination without changing intrinsic X or q",
)
print(
    "dsd_audit",
    "full K=h target congruence exactly identifies the deterministic parity cylinder inside a fixed-(h,q) class; partial K remains screening only",
)
print(
    "status",
    "G4 adaptive target-cylinder oracle CLOSED; non-correction long-membership gates and universal Route-B membership remain OPEN",
)
