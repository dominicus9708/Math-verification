#!/usr/bin/env python3
"""
Exact certificate: terminal 3-adic checkpoint-residue compression.

For a parity word w of length n, odd count q(w), and correction C(w),

    2^n T^n(X) = 3^q X + C(w).

Define the normalized terminal residue

    R_M(w) = 2^(-|w|) C(w) mod 3^M.

If w=uv and the terminal suffix v already contains at least M odd bits,
then

    R_M(uv) = R_M(v) mod 3^M.

Thus every earlier prefix u is exactly annihilated modulo 3^M. For the
current boundary M=28, the checkpoint's 3^28 residue depends only on any
terminal suffix containing at least 28 odd events. The canonical shortest
such suffix starts at the 28th-last odd event.

The same residue has the one-bit recurrence, from R=0:

    bit 0: R' = R/2 mod 3^M
    bit 1: R' = (3R+1)/2 mod 3^M.

IMPORTANT:
- This is exact modular compression, not a claim that the terminal suffix
  language has already been enumerated.
- It preserves a checkpoint endpoint residue only when the word is known
  to terminate at that checkpoint.
- It does not establish same-object coherence with an independently
  counted post-checkpoint dyadic word.
- C4F/global Collatz remain open.
"""

from __future__ import annotations

from itertools import product
from typing import Optional, Sequence, Tuple

M_CURRENT = 28
MOD3_CURRENT = 3 ** M_CURRENT
EXPECTED_MOD3_CURRENT = 22_876_792_454_961


def odd_count(w: Sequence[int]) -> int:
    assert all(bit in (0, 1) for bit in w)
    return sum(w)


def correction(w: Sequence[int]) -> int:
    """C(w) in 2^|w| T^|w|(X)=3^q X+C(w)."""
    C = 0
    for n, bit in enumerate(w):
        assert bit in (0, 1)
        if bit:
            C = 3 * C + (1 << n)
    return C


def concat_correction(u: Sequence[int], v: Sequence[int]) -> int:
    return (3 ** odd_count(v)) * correction(u) + (1 << len(u)) * correction(v)


def terminal_residue(w: Sequence[int], M: int) -> int:
    assert M >= 1
    mod = 3 ** M
    inv_2n = pow(pow(2, len(w), mod), -1, mod)
    return correction(w) * inv_2n % mod


def terminal_residue_stream(w: Sequence[int], M: int) -> int:
    """Compute R_M(w) without materializing C(w)."""
    assert M >= 1
    mod = 3 ** M
    inv2 = pow(2, -1, mod)
    R = 0
    for bit in w:
        assert bit in (0, 1)
        if bit == 0:
            R = R * inv2 % mod
        else:
            R = (3 * R + 1) * inv2 % mod
    return R


def canonical_M_odd_suffix(w: Sequence[int], M: int) -> Optional[Tuple[int, ...]]:
    """
    Shortest terminal suffix containing exactly M odd bits.

    If q(w)<M there is no such suffix. Otherwise it begins at the
    M-th-last odd position, hence its first bit is 1 and its odd count is M.
    """
    assert M >= 1
    if odd_count(w) < M:
        return None

    seen = 0
    start = None
    for i in range(len(w) - 1, -1, -1):
        if w[i] == 1:
            seen += 1
            if seen == M:
                start = i
                break
    assert start is not None
    suffix = tuple(w[start:])
    assert suffix[0] == 1
    assert odd_count(suffix) == M
    if start + 1 < len(w):
        assert odd_count(w[start + 1 :]) == M - 1
    return suffix


def check_composition_identity() -> None:
    for n in range(0, 9):
        for w in product((0, 1), repeat=n):
            for cut in range(n + 1):
                u, v = w[:cut], w[cut:]
                assert correction(w) == concat_correction(u, v)


def check_stream_recurrence() -> None:
    for n in range(0, 11):
        for w in product((0, 1), repeat=n):
            for M in range(1, 5):
                assert terminal_residue(w, M) == terminal_residue_stream(w, M)


def check_terminal_absorption() -> None:
    """Exhaustive small regression of R_M(uv)=R_M(v) when q(v)>=M."""
    for n in range(0, 11):
        for w in product((0, 1), repeat=n):
            for cut in range(n + 1):
                u, v = w[:cut], w[cut:]
                for M in range(1, 5):
                    if odd_count(v) >= M:
                        assert terminal_residue(w, M) == terminal_residue(v, M)


def check_canonical_cut() -> None:
    for n in range(0, 12):
        for w in product((0, 1), repeat=n):
            for M in range(1, 5):
                suffix = canonical_M_odd_suffix(w, M)
                if odd_count(w) < M:
                    assert suffix is None
                else:
                    assert suffix is not None
                    assert odd_count(suffix) == M
                    assert terminal_residue(w, M) == terminal_residue(suffix, M)


def check_symbolic_absorption_factor() -> None:
    """
    From composition:

      R_M(uv)
       = 2^(-|u|-|v|) 3^q(v) C(u) + 2^(-|v|) C(v).

    If q(v)>=M, the first term is divisible by 3^M because powers of 2
    are units modulo 3^M. Check the divisibility factor explicitly.
    """
    for lu in range(0, 8):
        for lv in range(0, 8):
            for qv in range(0, lv + 1):
                for M in range(1, 5):
                    if qv >= M:
                        assert (3 ** qv) % (3 ** M) == 0


def main() -> None:
    assert MOD3_CURRENT == EXPECTED_MOD3_CURRENT
    check_composition_identity()
    check_stream_recurrence()
    check_terminal_absorption()
    check_canonical_cut()
    check_symbolic_absorption_factor()

    print("A0 s=1 TERMINAL TERNARY RESIDUE COMPRESSION CERTIFICATE: PASS")
    print(f"M_current={M_CURRENT}")
    print(f"3^M={MOD3_CURRENT}")
    print("EXACT: R_M(uv)=R_M(v) whenever q(v)>=M")
    print("EXACT: the canonical M-th-last-odd suffix preserves R_M")
    print("EXACT: streaming update is 0:R/2, 1:(3R+1)/2 mod 3^M")
    print("SAFE: pre-checkpoint history before the M-th-last odd event may be dropped for this residue only")
    print("REJECTED: dropping provenance or treating the residue as the full terminal language state")
    print("OPEN: provenance-preserving paired boundary-language construction")
    print("OPEN: C4F/global Collatz conclusion")


if __name__ == "__main__":
    main()
