#!/usr/bin/env python3
"""Finite dual-adic bridge semigroup for A0 s=1 Route-B.

At fixed resolution (K,L), let

    M = 2^K 3^L

and map every parity block W to

    S_{K,L}(W) = (A(W), B(W), C(W)) mod M
               = (3^q(W), 2^h(W), C(W)) mod M.

For W = U V,

    A(UV) = A(U) A(V),
    B(UV) = B(U) B(V),
    C(UV) = A(V) C(U) + B(U) C(V)        (mod M).

Hence S_{K,L} is an exact homomorphism from parity-word concatenation into a
finite semigroup.  Equality of these states is therefore a two-sided
congruence at the selected resolution.

When h(W)>=K and q(W)>=L, the state reconstructs both exposed boundaries:

    D_K(W) = -C(W) A(W)^(-1) mod 2^K,
    E_L(W) =  C(W) B(W)^(-1) mod 3^L.

Conversely, D_K and E_L together with A,B recover C mod M by CRT.

This closes a finite correction-sector congruence at every fixed (K,L).  It
does NOT prove that this quotient recognizes the admissible Route-B language:
different interior words may collide at a finite resolution, and ballot /
formation compatibility is additional structure.
"""

from math import gcd

J0 = 10_439_860_591
R0 = 6_586_818_670
MAX_DEPTH = 9

RESOLUTION_CHAIN = (
    (1, 1),
    (2, 2),
    (4, 4),
    (8, 8),
    (16, 16),
    (24, 24),
    (27, 28),
    (32, 32),
    (39, 39),
    (64, 47),
)

PRIMARY_K = 27
PRIMARY_L = 28


def modulus(K, L):
    return (1 << K) * pow(3, L)


def direct_summary(bits):
    h = q = C = 0
    for bit in bits:
        assert bit in (0, 1)
        if bit:
            C = 3 * C + (1 << h)
            q += 1
        h += 1
    return h, q, C


def direct_state(bits, K, L):
    h, q, C = direct_summary(bits)
    M = modulus(K, L)
    return pow(3, q, M), pow(2, h, M), C % M


def compose_state(U, V, M):
    Au, Bu, Cu = U
    Av, Bv, Cv = V
    return (
        Au * Av % M,
        Bu * Bv % M,
        (Av * Cu + Bu * Cv) % M,
    )


def project_state(S, K, L):
    M = modulus(K, L)
    return tuple(x % M for x in S)


def decode_boundaries(S, K, L):
    A, B, C = S
    m2 = 1 << K
    m3 = pow(3, L)
    D = (-(C % m2) * pow(A % m2, -1, m2)) % m2
    E = ((C % m3) * pow(B % m3, -1, m3)) % m3
    return D, E


def correction_from_boundaries(A, B, D, E, K, L):
    """Recover C mod 2^K 3^L from the two boundary residues."""
    m2 = 1 << K
    m3 = pow(3, L)
    M = m2 * m3
    c2 = (-(A % m2) * D) % m2
    c3 = ((B % m3) * E) % m3
    t = ((c3 - c2) * pow(m2, -1, m3)) % m3
    return (c2 + m2 * t) % M


word_checks = 0
split_composition_checks = 0
boundary_decode_checks = 0
crt_roundtrip_checks = 0
projective_refinement_checks = 0

for h in range(1, MAX_DEPTH + 1):
    for address in range(1 << h):
        bits = tuple((address >> i) & 1 for i in range(h))
        hs, qs, Cs = direct_summary(bits)
        word_checks += 1

        states = {}
        for K, L in RESOLUTION_CHAIN:
            S = direct_state(bits, K, L)
            M = modulus(K, L)
            assert S == (
                pow(3, qs, M),
                pow(2, hs, M),
                Cs % M,
            )
            states[(K, L)] = S

            if hs >= K and qs >= L:
                D, E = decode_boundaries(S, K, L)
                assert D == (-Cs * pow(pow(3, qs, 1 << K), -1, 1 << K)) % (1 << K)
                assert E == (Cs * pow(pow(2, hs, pow(3, L)), -1, pow(3, L))) % pow(3, L)
                boundary_decode_checks += 1

                Cback = correction_from_boundaries(S[0], S[1], D, E, K, L)
                assert Cback == Cs % M
                crt_roundtrip_checks += 1

        for (K0, L0), (K1, L1) in zip(RESOLUTION_CHAIN, RESOLUTION_CHAIN[1:]):
            assert K0 <= K1 and L0 <= L1
            assert project_state(states[(K1, L1)], K0, L0) == states[(K0, L0)]
            projective_refinement_checks += 1

        for split in range(1, h):
            Ubits = bits[:split]
            Vbits = bits[split:]
            for K, L in ((1, 1), (2, 2), (4, 4), (8, 8), (27, 28)):
                M = modulus(K, L)
                U = direct_state(Ubits, K, L)
                V = direct_state(Vbits, K, L)
                assert compose_state(U, V, M) == direct_state(bits, K, L)
                split_composition_checks += 1


assert word_checks == 1022
assert split_composition_checks == 7172 * 5
assert projective_refinement_checks == 1022 * (len(RESOLUTION_CHAIN) - 1)


associativity_checks = 0
for hu in range(1, 6):
    for hv in range(1, 6):
        for hw in range(1, 6):
            if hu + hv + hw > 7:
                continue
            for au in range(1 << hu):
                Ubits = tuple((au >> i) & 1 for i in range(hu))
                for av in range(1 << hv):
                    Vbits = tuple((av >> i) & 1 for i in range(hv))
                    for aw in range(1 << hw):
                        Wbits = tuple((aw >> i) & 1 for i in range(hw))
                        K, L = 4, 4
                        M = modulus(K, L)
                        U = direct_state(Ubits, K, L)
                        V = direct_state(Vbits, K, L)
                        W = direct_state(Wbits, K, L)
                        assert compose_state(compose_state(U, V, M), W, M) == compose_state(
                            U, compose_state(V, W, M), M
                        )
                        associativity_checks += 1


def build_stern_brocot_dag(p, q):
    assert 0 <= p <= q and gcd(p, q) == 1
    nodes = [
        {"p": 0, "q": 1, "left": None, "right": None},
        {"p": 1, "q": 1, "left": None, "right": None},
    ]
    left = (0, 1, 0)
    right = (1, 1, 1)
    while True:
        assert left[1] * right[0] - left[0] * right[1] == 1
        mp = left[0] + right[0]
        mq = left[1] + right[1]
        mid = len(nodes)
        nodes.append({"p": mp, "q": mq, "left": left[2], "right": right[2]})
        cmp = p * mq - mp * q
        if cmp == 0:
            return nodes, mid
        if cmp < 0:
            right = (mp, mq, mid)
        else:
            left = (mp, mq, mid)


nodes, root = build_stern_brocot_dag(R0, J0)
assert len(nodes) == 129 and root == 128

M_PRIMARY = modulus(PRIMARY_K, PRIMARY_L)
dag_states = []
dag_composition_checks = 0

for i, node in enumerate(nodes):
    if node["left"] is None:
        h = node["q"]
        q = node["p"]
        C = node["p"]
        S = (
            pow(3, q, M_PRIMARY),
            pow(2, h, M_PRIMARY),
            C % M_PRIMARY,
        )
    else:
        li = node["left"]
        ri = node["right"]
        S = compose_state(dag_states[li], dag_states[ri], M_PRIMARY)
        dag_composition_checks += 1

    assert S[0] == pow(3, node["p"], M_PRIMARY)
    assert S[1] == pow(2, node["q"], M_PRIMARY)
    dag_states.append(S)


assert dag_composition_checks == 127
assert len(set(dag_states)) == 129

root_state = dag_states[root]
root_D27, root_E28 = decode_boundaries(root_state, PRIMARY_K, PRIMARY_L)

assert root_D27 == 87_757_810
assert root_E28 == 2_158_791_402_581

root_C_roundtrip = correction_from_boundaries(
    root_state[0],
    root_state[1],
    root_D27,
    root_E28,
    PRIMARY_K,
    PRIMARY_L,
)
assert root_C_roundtrip == root_state[2]


congruence_collision_pairs = 0
congruence_extension_checks = 0

for K, L in ((1, 1), (2, 2), (3, 2)):
    M = modulus(K, L)
    buckets = {}
    words = []
    for h in range(0, 7):
        for address in range(1 << h):
            bits = tuple((address >> i) & 1 for i in range(h))
            S = direct_state(bits, K, L)
            buckets.setdefault(S, []).append(bits)
            words.append(bits)

    colliding = [group for group in buckets.values() if len(group) >= 2]
    for group in colliding:
        rep = group[0]
        for other in group[1:]:
            congruence_collision_pairs += 1
            for eh in range(0, 4):
                for ea in range(1 << eh):
                    ext = tuple((ea >> i) & 1 for i in range(eh))
                    assert direct_state(rep + ext, K, L) == direct_state(other + ext, K, L)
                    congruence_extension_checks += 1


print("PASS A0 s=1 Route-B finite dual-adic bridge semigroup certificate")
print("arbitrary_word_max_depth", MAX_DEPTH)
print("arbitrary_words", word_checks)
print("split_composition_checks", split_composition_checks)
print("boundary_decode_checks", boundary_decode_checks)
print("crt_roundtrip_checks", crt_roundtrip_checks)
print("projective_refinement_checks", projective_refinement_checks)
print("associativity_checks", associativity_checks)
print("primary_resolution", (PRIMARY_K, PRIMARY_L))
print("primary_modulus", M_PRIMARY)
print("dag_nodes", len(nodes))
print("dag_composition_checks", dag_composition_checks)
print("dag_distinct_primary_states", len(set(dag_states)))
print("root_bridge_state", root_state)
print("root_D27", root_D27)
print("root_E28", root_E28)
print("congruence_collision_pairs", congruence_collision_pairs)
print("congruence_extension_checks", congruence_extension_checks)
print(
    "formation_audit",
    "finite bridge state is formed compositionally from child states with no hidden interior word",
)
print(
    "axis_audit",
    "the state jointly retains start-facing dyadic and end-facing ternary information through one CRT-compatible correction coordinate",
)
print(
    "dsd_audit",
    "fixed-resolution correction congruence is exact; recognition of the admissible long language by that quotient remains open",
)
print(
    "status",
    "G3 fixed-resolution correction congruence CLOSED; G4 adaptive interior language decoder remains OPEN",
)
