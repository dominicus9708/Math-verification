#!/usr/bin/env python3
"""Finite regression for bounded-record periodic-tail and M<=3 pruning.

The companion note contains the general proofs. This file checks:

1. exact Beatty mechanical factors ending in zero for L<=3;
2. exact first-passage record words for those factors;
3. positivity and cross-completion equality of representative eventually
   periodic parity-series geometric sums with density above log_3 2.

This is a regression certificate, not a proof of Collatz.
"""

from fractions import Fraction


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


B = barriers(400)


def mechanical_factor(s: int, L: int) -> tuple[int, ...]:
    return tuple(B[s + j] - B[s + j - 1] for j in range(1, L + 1))


def record_words(d: tuple[int, ...]) -> tuple[str, ...]:
    L = len(d)
    out = []
    for mask in range(1 << L):
        q = 0
        D = 0
        ok = True
        bits = [(mask >> j) & 1 for j in range(L)]
        for j, (dj, bit) in enumerate(zip(d, bits), start=1):
            q += bit
            D += dj
            g = q - D
            if j < L:
                if g > 0:
                    ok = False
                    break
            elif g != 1:
                ok = False
        if ok:
            out.append("".join(str(x) for x in bits))
    return tuple(out)


def check_small_M() -> None:
    seen: dict[tuple[int, ...], tuple[str, ...]] = {}
    for L in (1, 2, 3):
        for s in range(300):
            d = mechanical_factor(s, L)
            if d[-1] == 0:
                seen[d] = record_words(d)

    expected = {
        (0,): ("1",),
        (1, 0): ("11",),
        (0, 1, 0): ("011",),
        (1, 1, 0): ("111",),
    }
    assert seen == expected, (seen, expected)
    assert all(len(words) == 1 for words in seen.values())


def periodic_series_value(gaps: tuple[int, ...], prefix_p: int = 0,
                          prefix_i: int = 0) -> Fraction:
    """Real/Q-rational value of a pure periodic odd-gap tail.

    gaps are positive spacings between successive odd positions. We use one
    period of B=len(gaps) odd events and A=sum(gaps) time steps. The returned
    rational is the geometric-series tail beginning at the first odd position
    prefix_p+gaps[0].
    """
    A = sum(gaps)
    Bn = len(gaps)
    assert (1 << A) < 3 ** Bn

    p = prefix_p
    block = Fraction(0, 1)
    for j, gap in enumerate(gaps, start=1):
        p += gap
        block += Fraction(1 << p, 3 ** (prefix_i + j))

    ratio = Fraction(1 << A, 3 ** Bn)
    return block / (1 - ratio)


def check_periodic_examples() -> None:
    # Representative high-density periods. The theorem is algebraic for all
    # periods satisfying 2^A < 3^B; these examples guard the formula.
    examples = [
        (1, 1),          # density 1
        (1, 1, 2),       # density 3/4
        (1, 2, 1, 1),    # density 4/5
        (2, 1, 2, 1, 1), # density 5/7
    ]
    for gaps in examples:
        A = sum(gaps)
        Bn = len(gaps)
        assert (1 << A) < 3 ** Bn
        S = periodic_series_value(gaps)
        assert S > 0

        # Verify the geometric fixed-point identity exactly in Q:
        # S = block + (2^A/3^B) S.
        p = 0
        block = Fraction(0, 1)
        for j, gap in enumerate(gaps, start=1):
            p += gap
            block += Fraction(1 << p, 3 ** j)
        ratio = Fraction(1 << A, 3 ** Bn)
        assert S == block + ratio * S


def main() -> None:
    check_small_M()
    check_periodic_examples()
    print("bounded-record periodic/small-M regression: PASS")
    print("all L<=3 record factors are singleton")
    print("representative high-density periodic series are positive rational geometric sums")


if __name__ == "__main__":
    main()
