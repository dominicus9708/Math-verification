#!/usr/bin/env python3
"""Finite regression for the exact source-to-macroblock entry partition.

The theorem itself is algebraic and is documented in

    ../theorems/SOURCE_TO_MACROBLOCK_FORMATION_ENTRY_PARTITION.md

This certificate checks:

* the one-macroblock residue formula for a finite H,D grid;
* the affine source-parameter preimage formula;
* actual descriptors on representative points of every certified eight-jump
  A0 s=1 Route-B source cylinder;
* opposite endpoint parity for consecutive m values, hence failure of a
  single cylinder-wide entry descriptor on every non-singleton interval.

This is a finite implementation regression, not a Collatz proof and not a
formation-rank globalization theorem.
"""

from __future__ import annotations

import A0_s1_source_payload_control_factorization_certificate as payload


def v2(n: int) -> int:
    assert n > 0
    return (n & -n).bit_length() - 1


def macroblock_residue(H: int, D: int) -> int:
    """Canonical odd residue x_{H,D} modulo 2^(H+D+1)."""
    assert H >= 1 and D >= 1
    mod_u = 1 << (D + 1)
    u = (pow(pow(3, H), -1, mod_u) * (1 + (1 << D))) % mod_u
    assert u & 1
    mod_x = 1 << (H + D + 1)
    x = ((1 << H) * u - 1) % mod_x
    assert x & 1
    return x


def descriptor(Y: int) -> tuple[int, int, int]:
    """Exact local entry descriptor E=(b,H,D) for a positive endpoint Y."""
    assert Y > 0
    b = v2(Y)
    O = Y >> b
    assert O & 1
    H = v2(O + 1)
    assert H >= 1
    u = (O + 1) >> H
    assert u & 1
    D = v2(pow(3, H) * u - 1)
    assert D >= 1
    return b, H, D


def entry_parameter_residue(st, b: int, H: int, D: int) -> tuple[int, int]:
    """Return (rho,K) with m == rho mod 2^K for descriptor (b,H,D)."""
    K = b + H + D + 1
    M = 1 << K
    x = macroblock_residue(H, D)
    rho = (((1 << b) * x - st.y) * pow(st.A, -1, M)) % M
    return rho, K


def direct_block_check(Y: int, e: tuple[int, int, int]) -> None:
    """Check the exact displayed continuation 0^b 1^H 0^D."""
    b, H, D = e
    z = Y
    for _ in range(b):
        assert (z & 1) == 0
        z //= 2
    assert z & 1

    for _ in range(H):
        assert z & 1
        z = (3 * z + 1) // 2

    for _ in range(D):
        assert (z & 1) == 0
        z //= 2

    # D is maximal: the following state is odd.
    assert z & 1


def verify_local_macroblock_grid(max_H: int = 12, max_D: int = 12) -> None:
    for H in range(1, max_H + 1):
        for D in range(1, max_D + 1):
            x = macroblock_residue(H, D)
            assert descriptor(x) == (0, H, D)

            M = 1 << (H + D + 1)
            # Every lift by the exact modulus retains the same descriptor.
            for t in (0, 1, 2, 5):
                O = x + M * t
                assert descriptor(O) == (0, H, D)
                direct_block_check(O, (0, H, D))


def representative_parameters(st) -> list[int]:
    pts = {st.lo, st.hi, (st.lo + st.hi) // 2}
    if st.lo < st.hi:
        pts.add(st.lo + 1)
        pts.add(st.hi - 1)
    return sorted(m for m in pts if st.lo <= m <= st.hi)


def verify_current_frontier() -> tuple[int, int, int, int]:
    states = payload.states
    assert len(states) == 14_224

    samples = 0
    wide = 0
    singleton = 0

    for st in states:
        for m in representative_parameters(st):
            Y = st.y + st.A * m
            assert Y > 0
            e = descriptor(Y)
            b, H, D = e
            rho, K = entry_parameter_residue(st, b, H, D)
            assert m % (1 << K) == rho
            direct_block_check(Y, e)
            samples += 1

        if st.lo < st.hi:
            wide += 1
            m0 = st.lo
            m1 = st.lo + 1
            Y0 = st.y + st.A * m0
            Y1 = st.y + st.A * m1
            assert (Y0 ^ Y1) & 1
            e0 = descriptor(Y0)
            e1 = descriptor(Y1)
            assert e0[0] != e1[0]
            assert e0 != e1
        else:
            singleton += 1

    return len(states), samples, wide, singleton


def verify_affine_preimage_grid() -> None:
    """Independent small affine-family regression of the residue preimage."""

    class Tiny:
        pass

    for q in range(0, 7):
        A = 3 ** q
        for y in range(1, 18):
            st = Tiny()
            st.y = y
            st.A = A
            for m in range(0, 96):
                Y = y + A * m
                b, H, D = descriptor(Y)
                rho, K = entry_parameter_residue(st, b, H, D)
                assert m % (1 << K) == rho


verify_local_macroblock_grid()
verify_affine_preimage_grid()
frontier_cylinders, sampled_points, wide_cylinders, singleton_cylinders = verify_current_frontier()

print("PASS A0 s=1 source-to-macroblock formation entry partition certificate")
print("frontier_cylinders", frontier_cylinders)
print("sampled_frontier_points", sampled_points)
print("wide_cylinders", wide_cylinders)
print("singleton_cylinders", singleton_cylinders)
print("persistent_state_sufficient_for_local_partition", True)
print("single_cylinder_wide_formation_label_for_wide_intervals", False)
print("global_suffix_formation_rank_bridge_claimed", False)
print("status", "EXACT local entry partition; finite regression only; no independent pruning claimed")
