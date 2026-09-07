#!/usr/bin/env python3

from collections import defaultdict
from hashlib import sha256

K = 61
MOD = 1 << 11


def min_q_survival(k: int) -> int:
    q = 0
    p3 = 1
    target = 1 << k
    while p3 < target:
        p3 *= 3
        q += 1
    return q


MIN_Q = tuple([0] + [min_q_survival(k) for k in range(1, K + 1)])


def canonical_xy_from_bits(bits):
    """Recover the unique x in [0,2^K) realizing bits, and y=T^K(x)."""
    x = 0
    y = 0
    q = 0
    p3 = 1
    for k, b in enumerate(bits):
        # The two lifts of the current k-bit residue are x and x+2^k.
        # After k steps their endpoints differ by 3^q, which is odd.
        e = b ^ (y & 1)
        z = y + (p3 if e else 0)
        if e:
            x += 1 << k
        if b:
            y = (3 * z + 1) // 2
            q += 1
            p3 *= 3
        else:
            y = z // 2
    return x, y, q


def direct_verify(x: int, bits, expected_q: int, expected_phase: int):
    n = x
    q = 0
    got = []
    for k in range(1, K + 1):
        b = n & 1
        got.append(b)
        q += b
        assert q >= MIN_Q[k]
        n = (3 * n + 1) // 2 if b else n // 2
    assert tuple(got) == tuple(bits)
    assert q == expected_q
    assert (n & (MOD - 1)) == expected_phase
    return n


def iter_valid_words_fixed_q(Q: int):
    """Lexicographic exact generator of all universal-spine words with q61=Q."""
    bits = [0] * K

    def rec(k: int, q: int):
        if k == K:
            if q == Q:
                yield tuple(bits)
            return
        remaining_after = K - (k + 1)
        for b in (0, 1):
            q2 = q + b
            if q2 < MIN_Q[k + 1] or q2 > Q:
                continue
            if q2 + remaining_after < Q:
                continue
            bits[k] = b
            yield from rec(k + 1, q2)

    yield from rec(0, 0)


EXPECTED_FIRST_COMPLETE = {
    39: 14954,
    40: 15131,
    41: 18417,
    42: 13048,
    43: 19853,
    44: 16848,
    45: 15409,
    46: 16130,
    47: 14917,
    48: 18355,
    49: 21604,
    50: 18493,
    51: 20103,
    52: 19877,
    53: 15039,
    54: 18840,
    55: 21077,
    56: 17266,
    57: 14187,
    58: 19822,
}

EXPECTED_HIGH = {
    59: (1708, 1166, "c2d6c693dd3273eae6cea81d34d068df47277b995d2fafb2121564369dd09d8f"),
    60: (59, 58, "7da3ed95ffb1b47a2e85d44029d665acef589ef13767499c3bd31e292743b11c"),
    61: (1, 1, "718127812c05853f0bec61582a4a3840b1c844fe11fe1a004b5b7eb8b8b59846"),
}


def main():
    assert MIN_Q[61] == 39

    rows = []

    # For q=39..58, one exact ordinary-integer witness for every phase proves
    # Reach_61(q) is the full ambient set Z/2048Z. We scan in deterministic
    # lexicographic parity-word order and stop only after all 2048 phases have
    # separately verified witnesses.
    for Q in range(39, 59):
        witness = {}
        scanned = 0
        for bits in iter_valid_words_fixed_q(Q):
            x, y, q = canonical_xy_from_bits(bits)
            scanned += 1
            phase = y & (MOD - 1)
            if phase not in witness:
                y2 = direct_verify(x, bits, Q, phase)
                assert y2 == y
                witness[phase] = x
            if len(witness) == MOD:
                break
        assert len(witness) == MOD
        assert scanned == EXPECTED_FIRST_COMPLETE[Q]
        rows.append((Q, MOD, scanned, "constructive-full"))

    # q=59..61 are small enough to exhaust exactly.
    for Q in range(59, 62):
        phase_to_x = defaultdict(list)
        words = 0
        for bits in iter_valid_words_fixed_q(Q):
            x, y, q = canonical_xy_from_bits(bits)
            phase = y & (MOD - 1)
            y2 = direct_verify(x, bits, Q, phase)
            assert y2 == y
            phase_to_x[phase].append(x)
            words += 1

        phases = sorted(phase_to_x)
        digest = sha256(",".join(map(str, phases)).encode()).hexdigest()
        exp_words, exp_phases, exp_digest = EXPECTED_HIGH[Q]
        assert words == exp_words
        assert len(phases) == exp_phases
        assert digest == exp_digest
        rows.append((Q, len(phases), words, digest))

    # Regression detail for the all-odd word.
    bits = (1,) * K
    x, y, q = canonical_xy_from_bits(bits)
    assert x == (1 << K) - 1
    assert q == 61
    assert (y & (MOD - 1)) == 274

    print("PASS")
    print("q61 | reachable endpoint phases | words scanned/enumerated | certificate")
    for row in rows:
        print(*row)
    print("q61=39..58: every y mod 2048 has an exact ordinary-integer universal-spine witness")
    print("q61=59: 1166/2048 phases reachable (1708 valid words)")
    print("q61=60: 58/2048 phases reachable (59 valid words)")
    print("q61=61: only phase 274 reachable; witness x=2^61-1")
    print("critical consequence: q61=39..45 has full 2048-phase reachability, so")
    print("phase-reachability cannot sharpen the MATH-006 coefficient-only label sieve")


if __name__ == "__main__":
    main()
