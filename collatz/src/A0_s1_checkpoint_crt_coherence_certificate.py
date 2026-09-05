#!/usr/bin/env python3
"""
Exact certificate: same-checkpoint CRT coherence for the A0 s=1 Route-B boundary.

This certificate proves only the arithmetic gluing theorem:

  if a pre-checkpoint suffix b and a post-checkpoint prefix v are known to
  belong to the SAME ordinary checkpoint Z, then

      Z == R_M(b) (mod 3^M),
      Z == A_K(v) (mod 2^K),

  where
      R_M(b) = 2^(-|b|) C(b) (mod 3^M)

  whenever q(b) >= M, and A_K is the deterministic parity address.

The pair determines one CRT class modulo 2^K 3^M. At the current
K=27, M=28, this modulus exceeds the full checkpoint corridor span, so
a coherent pair determines at most one ordinary checkpoint Z in the
corridor.

IMPORTANT:
- This does NOT prove that independently counted pre- and post-boundary
  marginals share a common checkpoint.
- Cartesian pairing of unrelated marginals is explicitly not licensed.
- C4F renewal/gap conditions and the global Collatz claim remain open.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence, Tuple

K_CURRENT = 27
M_CURRENT = 28

Z_MIN = 7_083_549_723_369_539_339_554
Z_MAX = 9_444_732_965_739_290_427_391
Z_SPAN = Z_MAX - Z_MIN

MOD2_CURRENT = 1 << K_CURRENT
MOD3_CURRENT = 3 ** M_CURRENT
CRT_MODULUS_CURRENT = MOD2_CURRENT * MOD3_CURRENT

EXPECTED_CRT_MODULUS = 3_070_471_107_232_407_748_608
EXPECTED_Z_SPAN = 2_361_183_242_369_751_087_837
EXPECTED_SLACK = 709_287_864_862_656_660_771


def T(x: int) -> int:
    assert x > 0
    return x // 2 if x % 2 == 0 else (3 * x + 1) // 2


def iterate(x: int, n: int) -> int:
    assert n >= 0
    for _ in range(n):
        x = T(x)
    return x


def parity_word(x: int, n: int) -> Tuple[int, ...]:
    assert x > 0 and n >= 0
    out = []
    for _ in range(n):
        out.append(x & 1)
        x = T(x)
    return tuple(out)


def odd_count(w: Sequence[int]) -> int:
    assert all(bit in (0, 1) for bit in w)
    return sum(w)


def correction(w: Sequence[int]) -> int:
    """C(w) in 2^n T^n(X)=3^q X+C(w)."""
    C = 0
    for n, bit in enumerate(w):
        assert bit in (0, 1)
        if bit:
            C = 3 * C + (1 << n)
    return C


def concat_correction(u: Sequence[int], v: Sequence[int]) -> int:
    """Composition formula C(uv)=3^q(v) C(u)+2^|u| C(v)."""
    return (3 ** odd_count(v)) * correction(u) + (1 << len(u)) * correction(v)


def address_mod(w: Sequence[int], K: int) -> int:
    """
    A_K(w) = -sum_r 2^{a_r} 3^{-r} mod 2^K.

    Only odd positions a_r<K can contribute modulo 2^K, so a word of
    length at least K exposes the K-bit start address.
    """
    assert K >= 1
    assert len(w) >= K
    mod = 1 << K
    total = 0
    rank = 0
    for a, bit in enumerate(w):
        assert bit in (0, 1)
        if bit:
            rank += 1
            if a < K:
                total = (total - (1 << a) * pow(pow(3, rank, mod), -1, mod)) % mod
    return total


def terminal_ternary_residue(w: Sequence[int], M: int) -> int:
    """
    R_M(w)=2^{-|w|} C(w) mod 3^M.

    This is an endpoint residue only when q(w)>=M.
    """
    assert M >= 1
    assert odd_count(w) >= M
    mod = 3 ** M
    return correction(w) * pow(pow(2, len(w), mod), -1, mod) % mod


def crt_pair(z2: int, K: int, z3: int, M: int) -> Tuple[int, int]:
    """Return canonical z mod N satisfying z=z2 mod2^K and z=z3 mod3^M."""
    assert K >= 1 and M >= 1
    m2 = 1 << K
    m3 = 3 ** M
    assert 0 <= z2 < m2
    assert 0 <= z3 < m3
    t = ((z3 - z2) * pow(m2, -1, m3)) % m3
    z = z2 + m2 * t
    N = m2 * m3
    assert 0 <= z < N
    assert z % m2 == z2
    assert z % m3 == z3
    return z, N


def unique_lift_in_interval(residue: int, modulus: int, lo: int, hi: int) -> Optional[int]:
    """Unique lift if interval span < modulus; otherwise reject this API use."""
    assert 0 <= residue < modulus
    assert lo <= hi
    assert hi - lo < modulus
    k = (lo - residue + modulus - 1) // modulus
    z = residue + k * modulus
    if z > hi:
        return None
    assert lo <= z <= hi
    assert z % modulus == residue
    assert z + modulus > hi
    assert z - modulus < lo
    return z


@dataclass(frozen=True)
class BoundarySignature:
    """
    A SAME-CHECKPOINT paired signature.

    The data structure itself does not establish provenance; callers must
    obtain pre_word and post_word from one boundary object / one orbit.
    """

    z2: int
    z3: int
    K: int
    M: int

    @classmethod
    def from_same_checkpoint_words(
        cls,
        pre_terminal_word: Sequence[int],
        post_prefix_word: Sequence[int],
        K: int,
        M: int,
    ) -> "BoundarySignature":
        assert len(post_prefix_word) >= K
        assert odd_count(pre_terminal_word) >= M
        return cls(
            z2=address_mod(post_prefix_word, K),
            z3=terminal_ternary_residue(pre_terminal_word, M),
            K=K,
            M=M,
        )

    def crt(self) -> Tuple[int, int]:
        return crt_pair(self.z2, self.K, self.z3, self.M)


def check_affine_identity() -> None:
    for x in range(1, 200):
        for n in range(0, 12):
            w = parity_word(x, n)
            q = odd_count(w)
            z = iterate(x, n)
            assert (1 << n) * z == (3 ** q) * x + correction(w)


def check_correction_composition() -> None:
    for x in range(1, 100):
        full = parity_word(x, 10)
        for cut in range(0, 11):
            u, v = full[:cut], full[cut:]
            assert correction(full) == concat_correction(u, v)


def check_dyadic_address() -> None:
    for x in range(1, 300):
        for K in range(1, 8):
            w = parity_word(x, K + 3)
            assert address_mod(w, K) == x % (1 << K)


def check_terminal_ternary_locality() -> None:
    for x in range(1, 300):
        for n in range(1, 12):
            full = parity_word(x, n)
            z = iterate(x, n)
            for start in range(0, n):
                suffix = full[start:]
                p = odd_count(suffix)
                for M in range(1, min(p, 4) + 1):
                    assert terminal_ternary_residue(suffix, M) == z % (3 ** M)


def check_same_checkpoint_crt() -> None:
    for x in range(1, 250):
        for n in range(1, 11):
            prefix = parity_word(x, n)
            z = iterate(x, n)
            for start in range(0, n):
                b = prefix[start:]
                p = odd_count(b)
                for M in range(1, min(p, 3) + 1):
                    for K in range(1, 6):
                        v = parity_word(z, K)
                        sig = BoundarySignature.from_same_checkpoint_words(b, v, K, M)
                        residue, N = sig.crt()
                        assert residue == z % N


def check_current_window_uniqueness() -> None:
    assert CRT_MODULUS_CURRENT == EXPECTED_CRT_MODULUS
    assert Z_SPAN == EXPECTED_Z_SPAN
    assert CRT_MODULUS_CURRENT - Z_SPAN == EXPECTED_SLACK
    assert CRT_MODULUS_CURRENT > Z_SPAN

    for z in (
        Z_MIN,
        Z_MIN + 1,
        (Z_MIN + Z_MAX) // 2,
        Z_MAX - 1,
        Z_MAX,
    ):
        residue = z % CRT_MODULUS_CURRENT
        assert unique_lift_in_interval(
            residue, CRT_MODULUS_CURRENT, Z_MIN, Z_MAX
        ) == z

    probe = (Z_MAX + 1) % CRT_MODULUS_CURRENT
    assert unique_lift_in_interval(
        probe, CRT_MODULUS_CURRENT, Z_MIN, Z_MAX
    ) is None


def main() -> None:
    check_affine_identity()
    check_correction_composition()
    check_dyadic_address()
    check_terminal_ternary_locality()
    check_same_checkpoint_crt()
    check_current_window_uniqueness()

    print("A0 s=1 SAME-CHECKPOINT CRT COHERENCE CERTIFICATE: PASS")
    print(f"K={K_CURRENT}")
    print(f"M={M_CURRENT}")
    print(f"2^K={MOD2_CURRENT}")
    print(f"3^M={MOD3_CURRENT}")
    print(f"CRT modulus={CRT_MODULUS_CURRENT}")
    print(f"checkpoint span={Z_SPAN}")
    print(f"uniqueness slack={CRT_MODULUS_CURRENT - Z_SPAN}")
    print("EXACT: coherent (z2,z3) determines at most one Z in the current corridor")
    print("SAFE: preserve same-checkpoint provenance when carrying both marginals")
    print("REJECTED: arbitrary Cartesian pairing of independent marginals")
    print("OPEN: proving/enumerating the actual paired boundary-language relation")
    print("OPEN: C4F/global Collatz conclusion")


if __name__ == "__main__":
    main()
