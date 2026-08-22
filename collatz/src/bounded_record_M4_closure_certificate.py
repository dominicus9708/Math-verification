#!/usr/bin/env python3
"""Exact finite regression for the eventual M=4 bounded-record closure.

The companion note proves the general result from balanced Beatty factors.
This script checks on a long exact prefix that:

- zero gaps in d_k=ceil(k alpha)-ceil((k-1)alpha) are only 2 or 3;
- gap pair (2,2) never occurs;
- late record-to-record factors of length <=4 are only 10 and 110;
- their record first-passage parity words are uniquely 11 and 111.

It also runs an exact prefix DP from time zero with record gaps <=4 to guard
implementation logic. The all-L proof is in the note, not in this finite scan.
"""


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
D = [0] + [B[k] - B[k - 1] for k in range(1, len(B))]


def record_words(mech: tuple[int, ...]) -> tuple[str, ...]:
    L = len(mech)
    out = []
    for mask in range(1 << L):
        g = 0
        bits = []
        ok = True
        for j, d in enumerate(mech, start=1):
            bit = (mask >> (j - 1)) & 1
            bits.append(bit)
            g += bit - d
            if j < L:
                if g > 0:
                    ok = False
                    break
            elif g != 1:
                ok = False
        if ok:
            out.append("".join(map(str, bits)))
    return tuple(out)


def finite_mechanical_audit() -> None:
    zeros = [k for k in range(1, 4999) if D[k] == 0]
    gaps = [b - a for a, b in zip(zeros, zeros[1:])]
    assert set(gaps) == {2, 3}
    assert all(not (a == 2 and b == 2) for a, b in zip(gaps, gaps[1:]))

    factors = set()
    for a, b in zip(zeros, zeros[1:]):
        if b - a <= 4:
            factors.add(tuple(D[a + 1:b + 1]))
    assert factors == {(1, 0), (1, 1, 0)}, factors
    assert record_words((1, 0)) == ("11",)
    assert record_words((1, 1, 0)) == ("111",)


def exact_prefix_dp(Hmax: int = 120) -> None:
    # State: (odd_count, record_height, age_since_record, parity_prefix).
    # Prefix strings are kept only because the state count remains tiny.
    states = {(0, 0, 0, "")}
    max_count = 1
    for k in range(Hmax):
        nd = set()
        for q, record, age, bits in states:
            for bit in (0, 1):
                q2 = q + bit
                h2 = q2 - B[k + 1]
                if h2 < 0:
                    continue
                if h2 > record:
                    assert h2 == record + 1
                    nd.add((q2, h2, 0, bits + str(bit)))
                else:
                    age2 = age + 1
                    if age2 < 4:
                        nd.add((q2, record, age2, bits + str(bit)))
        states = nd
        max_count = max(max_count, len(states))
        assert states

    # Finite prefixes can branch near the terminal horizon, but every fixed
    # early bit stabilizes to 1 as the horizon is extended. The exact theorem
    # proves the infinite inverse-limit path is eventually all odd.
    common = min(len(s[3]) for s in states)
    prefix_len = 0
    for j in range(common):
        vals = {s[3][j] for s in states}
        if len(vals) == 1:
            prefix_len += 1
        else:
            break
    assert prefix_len >= Hmax - 6, (prefix_len, Hmax)
    assert all(s[3][:prefix_len] == "1" * prefix_len for s in states)
    print("M4 prefix DP max_state_count", max_count)
    print("Hmax", Hmax, "forced_initial_ones", prefix_len)


def main() -> None:
    finite_mechanical_audit()
    exact_prefix_dp()
    print("bounded-record M4 closure regression: PASS")


if __name__ == "__main__":
    main()
