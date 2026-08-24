#!/usr/bin/env python3
"""Exact finite regression for Beatty plateau annihilation / rise boundary support.

The all-depth proof is in
  notes/2026-08-24-beatty-plateau-zero-and-boundary-factorization.md.

This script performs an independent integer-set audit through depth 24.
It does not use floating point or evaluate Fourier sums.

For each depth k it enumerates the exact coefficient-surviving parity words,
computes their canonical residues mod 2^k, and verifies:

* plateau b_k=b_{k-1}: the survivor residue set is invariant under adding
  2^(k-1), so every odd Fourier character cancels identically;
* rise b_k=b_{k-1}+1: all two-child parent pairs cancel, and the one-child
  parents are exactly the length-(k-1) survivors with q=b_k-1; their unique
  surviving child is odd.

The canonical residue is computed from the exact inverse affine formula

  r == -sum_{odd j} 2^j 3^{-q_j} (mod 2^k).

This is a finite regression certificate, not a proof of Collatz.
"""


def qmins_exact(kmax: int) -> list[int]:
    b = [0] * (kmax + 1)
    q = 0
    p3 = 1
    for k in range(1, kmax + 1):
        target = 1 << k
        while p3 < target:
            q += 1
            p3 *= 3
        b[k] = q
    return b


def canonical(bits: tuple[int, ...]) -> int:
    k = len(bits)
    mod = 1 << k
    q = 0
    s = 0
    for j, bit in enumerate(bits):
        if bit:
            q += 1
            s = (s + (1 << j) * pow(3, -q, mod)) % mod
    return (-s) % mod


def survivor_words(kmax: int, b: list[int]):
    levels: list[list[tuple[tuple[int, ...], int]]] = [[((), 0)]]
    for k in range(1, kmax + 1):
        nxt: list[tuple[tuple[int, ...], int]] = []
        threshold = b[k]
        for bits, q in levels[-1]:
            if q >= threshold:
                nxt.append((bits + (0,), q))
            if q + 1 >= threshold:
                nxt.append((bits + (1,), q + 1))
        levels.append(nxt)
    return levels


def main() -> None:
    KMAX = 24
    b = qmins_exact(KMAX)
    levels = survivor_words(KMAX, b)

    # Selected exact total counts already certified elsewhere.
    expected = {
        7: 13,
        13: 367,
        14: 734,
        20: 27_328,
        24: 286_581,
    }
    for k, n in expected.items():
        assert len(levels[k]) == n, (k, len(levels[k]), n)

    plateau_count = 0
    rise_count = 0

    for k in range(2, KMAX + 1):
        top = 1 << (k - 1)
        residues = {canonical(bits) for bits, _ in levels[k]}
        assert len(residues) == len(levels[k])

        # Group children by their low-(k-1)-bit parent address.
        children: dict[int, list[int]] = {}
        for r in residues:
            children.setdefault(r & (top - 1), []).append(r)

        if b[k] == b[k - 1]:
            plateau_count += 1
            # Every parent has exactly the two top-bit lifts.
            for low, rs in children.items():
                assert len(rs) == 2
                assert set(rs) == {low, low + top}
            # Equivalent global top-bit translation invariance.
            assert {r ^ top for r in residues} == residues
        else:
            rise_count += 1
            assert b[k] == b[k - 1] + 1

            boundary_parents = {
                canonical(bits)
                for bits, q in levels[k - 1]
                if q == b[k] - 1
            }

            one_child_lows = {
                low for low, rs in children.items() if len(rs) == 1
            }
            two_child_lows = {
                low for low, rs in children.items() if len(rs) == 2
            }

            # Parent canonical addresses are exactly low-bit addresses at the
            # next lift.  The one-child support is the Beatty boundary.
            assert one_child_lows == boundary_parents
            assert one_child_lows.isdisjoint(two_child_lows)

            # Every boundary parent has exactly one surviving parity child and
            # it is the odd child.  Check this directly in parity-word space.
            boundary_words = {
                bits for bits, q in levels[k - 1] if q == b[k] - 1
            }
            level_k_words = {bits for bits, _ in levels[k]}
            for bits in boundary_words:
                assert bits + (1,) in level_k_words
                assert bits + (0,) not in level_k_words

            # Every nonboundary parent has two surviving children.
            for bits, q in levels[k - 1]:
                if q >= b[k]:
                    assert bits + (0,) in level_k_words
                    assert bits + (1,) in level_k_words

    assert plateau_count + rise_count == KMAX - 1

    print("depth<=24 exact dyadic sibling audit: PASS")
    print("plateau depths checked:", plateau_count)
    print("rise depths checked:", rise_count)
    print("plateau top-bit invariance: PASS")
    print("rise one-child support == Beatty boundary: PASS")
    print("odd-frequency annihilation/factorization finite regression: PASS")


if __name__ == "__main__":
    main()
