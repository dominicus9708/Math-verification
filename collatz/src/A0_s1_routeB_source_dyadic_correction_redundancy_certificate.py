#!/usr/bin/env python3
"""Exact source-prefix / full-correction dyadic redundancy certificate.

Let a fixed-total-count correction word split as

    W = A B,
    |A| = K,
    q(A) = p,
    q(B) = Q-p,

with affine correction C(.).  Exact block composition is

    C(W) = 3^(Q-p) C(A) + 2^K C(B).

Hence modulo 2^K,

    C(W) == 3^(Q-p) C(A).

If W is required to connect ordinary source X to an endpoint under total
one-count Q, then the full required correction obeys

    C_req == -3^Q X (mod 2^K)

because the endpoint term is multiplied by the full power 2^|W| and K<=|W|.
Since 3 is a unit modulo 2^K, equality of the two dyadic observations is
exactly

    C(A) == -3^p X (mod 2^K).

But this is precisely the ordinary prefix-channel condition

    2^K T^K(X) = 3^p X + C(A).

Therefore, conditional on an exact source parity prefix A, the dyadic residue
of the full required correction contains no independent checkpoint/membership
information.  Conversely, for a supplied binary prefix A, the congruence has
one unique X residue modulo 2^K, namely the canonical prefix cylinder.

This theorem does NOT say that full correction equality is redundant.  Future
one-count/formation constraints and the endpoint/checkpoint remain unresolved.
The dyadic residue can still be useful as an alternate decoder when the source
prefix itself is not already carried.

Finite exhaustive checks below are implementation guards only.
"""

from itertools import product


def correction(bits):
    C = 0
    q = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << h)
            q += 1
    return C, q


def T(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def orbit_prefix(x: int, h: int):
    bits = []
    for _ in range(h):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits), x


checks = 0
unique_prefix_checks = 0

for H in range(1, 9):
    for W in product((0, 1), repeat=H):
        CW, Q = correction(W)

        for K in range(H + 1):
            A = W[:K]
            B = W[K:]
            CA, p = correction(A)
            CB, qB = correction(B)

            assert Q == p + qB
            assert CW == (3 ** qB) * CA + (1 << K) * CB

            if K == 0:
                checks += 1
                continue

            mod = 1 << K
            assert CW % mod == ((3 ** qB) * CA) % mod

            # Unique source residue represented by prefix A.
            x_res = (-CA * pow(3, -p, mod)) % mod
            actual_bits, endpoint = orbit_prefix(x_res, K)
            assert actual_bits == A
            assert (3 ** p) * x_res + CA == (1 << K) * endpoint

            # Full-total-count dyadic observation is the same condition after
            # multiplication by the future odd unit 3^qB.
            assert CW % mod == (-pow(3, Q, mod) * x_res) % mod

            # No second source residue modulo 2^K can satisfy the same prefix
            # correction congruence because 3^p is invertible modulo 2^K.
            for delta in (1, mod // 2 if mod > 2 else 1):
                x2 = (x_res + delta) % mod
                if x2 != x_res:
                    assert ((3 ** p) * x2 + CA) % mod != 0
                    unique_prefix_checks += 1

            checks += 1

assert checks == 4_096
assert unique_prefix_checks > 0

print("PASS A0 s=1 source dyadic correction redundancy certificate")
print("exhaustive_total_lengths", 8)
print("split_checks", checks)
print("unique_prefix_checks", unique_prefix_checks)
print(
    "exact_identity",
    "C(W) mod 2^K = 3^(Q-p) C(A); full required dyadic correction reduces exactly to the ordinary source-prefix congruence",
)
print(
    "state_consequence",
    "when exact source prefix/control A is already carried, do not add C_req mod 2^K as an independent pruning coordinate",
)
print(
    "scope",
    "full correction equality, future formation/count constraints, endpoint Z, and Route-B membership remain OPEN",
)
