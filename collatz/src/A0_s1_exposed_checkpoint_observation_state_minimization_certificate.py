#!/usr/bin/env python3
"""Finite regression for exposed-checkpoint observation state minimization."""

S = 630_138_897
ELL = 28
M3 = 3 ** ELL
M2 = 1 << 27
TWO_S = 12_596_342_295_887
C_H = 2_677_095_985_033
INV_TWO_S = 17_062_811_582_066

assert pow(2, S, M3) == TWO_S
assert (TWO_S * INV_TWO_S) % M3 == 1


def T(x: int) -> int:
    return (3 * x + 1) // 2 if x & 1 else x // 2


def parity_prefix(x: int, n: int):
    bits = []
    for _ in range(n):
        bits.append(x & 1)
        x = T(x)
    return tuple(bits)


def correction(bits) -> int:
    C = 0
    for h, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << h)
    return C


def address(bits) -> int:
    n = len(bits)
    if n == 0:
        return 0
    q = sum(bits)
    mod = 1 << n
    return (-correction(bits) * pow(pow(3, q, mod), -1, mod)) % mod


def rightH(Z: int) -> int:
    return (TWO_S * Z - C_H) % M3


def recover_Z3(zH: int) -> int:
    return (INV_TWO_S * (zH + C_H)) % M3


post_checks = 0
transfer_checks = 0
dominance_checks = 0

# Ordinary post-prefix address regression.
for Z in range(1, 4000):
    for K in (1, 2, 3, 7, 13, 27):
        bits = parity_prefix(Z, K)
        assert address(bits) == Z % (1 << K)
        post_checks += 1

# Ternary affine transfer is bijective. Sample broad representatives plus all
# least ternary classes.
samples = {0, 1, 2, 3, 17, 1000, M3 // 2, M3 - 2, M3 - 1}
for a in range(3):
    for k in range(20):
        samples.add((a + 3 * k) % M3)

for Z3 in samples:
    zH = rightH(Z3)
    assert recover_Z3(zH) == Z3 % M3
    transfer_checks += 1

    # Current terminal-28 saturation criterion from the certified right-H
    # theorem: accepted zH mod 3 are {0,1}, equivalent to Z mod3 in {1,2}.
    accepted_from_h = zH % 3 in {0, 1}
    accepted_from_Z = Z3 % 3 in {1, 2}
    assert accepted_from_h == accepted_from_Z
    dominance_checks += 1

assert post_checks > 20_000
assert transfer_checks > 50
assert dominance_checks == transfer_checks

print("PASS A0 s=1 exposed-checkpoint observation state minimization certificate")
print("post_prefix_address_checks", post_checks)
print("rightH_affine_transfer_checks", transfer_checks)
print("terminal_dominance_equivalence_checks", dominance_checks)
print("derived_z2", "Z mod 2^27")
print("derived_zH", "2^s Z - C(H_s*) mod 3^28")
print("terminal_dominance", "exists iff 3 does not divide Z")
print("state_after_provenanced_Z_exposure", "Z plus only genuinely independent later predicates")
print("rejected", "dropping z2/zH before unique provenance-preserving checkpoint exposure")
print("open", "source-preserving construction of actual Z candidates from current source families")
