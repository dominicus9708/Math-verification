#!/usr/bin/env python3
"""Exact finite regression for the bounded-record renewal diamond.

The companion note gives the all-phase finite-state argument.  This script
checks the mechanical gap facts, the relative-state transition, exact diamond
reunion, and the critical dyadic sibling relation over a large finite grid.
It is a regression certificate, not the final bounded-tail Hensel theorem and
not a proof of Collatz.
"""

from __future__ import annotations


def barriers(nmax: int) -> list[int]:
    out = [0] * (nmax + 1)
    p3 = 1
    q = 0
    for k in range(1, nmax + 1):
        while p3 < (1 << k):
            p3 *= 3
            q += 1
        out[k] = q
    return out


B = barriers(5000)


def mech(k: int) -> int:
    return B[k] - B[k - 1]


def step(state: tuple[int, int], m: int, eps: int, M: int) -> tuple[int, int] | None:
    d, age = state
    if d == 0 and m == 0 and eps == 1:
        return (0, 0)
    d2 = d + m - eps
    age2 = age + 1
    if d2 < 0 or d2 > age2 or age2 >= M:
        return None
    return (d2, age2)


def canonical_residue(bits: list[int]) -> int:
    L = len(bits)
    q = sum(bits)
    R = 0
    odd_positions = [j for j, bit in enumerate(bits) if bit]
    for i, p in enumerate(odd_positions, start=1):
        R += (3 ** (q - i)) * (1 << p)
    mod = 1 << L
    return (-R * pow(3, -q, mod)) % mod


def next_plateaus(s: int) -> tuple[int, int]:
    hits = []
    k = s + 1
    while len(hits) < 2:
        if mech(k) == 0:
            hits.append(k)
        k += 1
    return hits[0], hits[1]


def diamond_words(s: int) -> tuple[list[int], list[int], int]:
    p1, p2 = next_plateaus(s)
    delayed = []
    early = []
    for k in range(s + 1, p2 + 1):
        m = mech(k)
        if k == p1:
            delayed.append(0)
            early.append(1)
        elif k == p2:
            delayed.append(1)
            early.append(1)
        else:
            # Between plateaus all mechanical bits are rises, so odd parity
            # keeps relative deficit zero.
            assert m == 1
            delayed.append(1)
            early.append(1)
    return delayed, early, p1 - s


def run_word(bits: list[int], s: int, M: int) -> tuple[int, int]:
    state = (0, 0)
    for j, eps in enumerate(bits, start=1):
        state2 = step(state, mech(s + j), eps, M)
        assert state2 is not None, (s, j, state, eps)
        state = state2
    return state


def main() -> None:
    # Mechanical word contains neither 00 nor 111.
    w = "".join(str(mech(k)) for k in range(1, 4000))
    assert "00" not in w
    assert "111" not in w

    checked = 0
    for s in range(0, 3000):
        # Every actual record time after the initial state is a mechanical
        # plateau.  The local diamond itself only needs the reset state and
        # the future two plateaus, so the check is valid for every phase s.
        delayed, early, first_pos = diamond_words(s)
        assert len(delayed) == len(early) <= 6
        assert sum(a != b for a, b in zip(delayed, early)) == 1
        assert delayed[first_pos - 1] == 0
        assert early[first_pos - 1] == 1
        assert run_word(delayed, s, 6) == (0, 0)
        assert run_word(early, s, 6) == (0, 0)

        # At the critical bit, the two canonical cylinders are dyadic
        # siblings: residues differ by 2^(first_pos-1) modulo 2^first_pos.
        rd = canonical_residue(delayed[:first_pos])
        re = canonical_residue(early[:first_pos])
        mod = 1 << first_pos
        want = 1 << (first_pos - 1)
        assert (re - rd) % mod == want, (s, first_pos, rd, re)
        checked += 1

    # Concatenate six diamonds using both choices.  Every one of the 2^6
    # words is valid and ends at reset; parity words are distinct.
    paths = [(0, [])]
    s0 = 0
    current_phase = s0
    # Use a fixed sequence of six mechanical diamond blocks.  Because both
    # choices have the same length and reunion phase, the next block is shared.
    blocks = []
    s = s0
    for _ in range(6):
        d, e, _ = diamond_words(s)
        blocks.append((s, d, e))
        s += len(d)

    words = [([], s0)]
    for phase, delayed, early in blocks:
        nw = []
        for bits, start in words:
            assert start == phase
            for choice in (delayed, early):
                merged = bits + choice
                nw.append((merged, phase + len(choice)))
        words = nw

    assert len(words) == 64
    assert len({tuple(bits) for bits, _ in words}) == 64
    for bits, _ in words:
        assert run_word(bits, s0, 6) == (0, 0)

    print("bounded-record renewal diamond regression: PASS")
    print("single_phase_checks", checked)
    print("six_diamond_words", len(words))


if __name__ == "__main__":
    main()
