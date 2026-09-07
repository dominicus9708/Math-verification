#!/usr/bin/env python3

MOD = 1 << 11
BLOCK_LABELS = range(1024, 1364)  # 340 surviving top-11-bit labels


def min_q_survival(k: int) -> int:
    q = 0
    p3 = 1
    target = 1 << k
    while p3 < target:
        p3 *= 3
        q += 1
    return q


def parity_word_11(n: int):
    # The first 11 shortcut-map parity bits depend only on n mod 2^11.
    x = n
    out = []
    for _ in range(11):
        b = x & 1
        out.append(b)
        x = (3 * x + 1) // 2 if b else x // 2
    return tuple(out)


def tail_survives(bits, q61: int) -> bool:
    q = q61
    for j, b in enumerate(bits, start=1):
        q += b
        if q < min_q_survival(61 + j):
            return False
    return True


def main():
    words = [parity_word_11(r) for r in range(MOD)]
    assert len(set(words)) == MOD  # exact parity-vector bijection mod 2^11

    q61_min = min_q_survival(61)
    assert q61_min == 39

    # For N=a*2^61+x, with the canonical lower-prefix endpoint y=T^61(x),
    # T^61(N)=y+a*3^q. Hence the final 11 parity bits depend on
    # (y+a*3^q) mod 2^11. Enumerate every possible y residue, so the bounds
    # below are uniform over all lower-61-bit prefix realizations.
    expected = {
        39: (36, 47),
        40: (124, 141),
        41: (221, 235),
        42: (288, 303),
        43: (320, 333),
        44: (336, 340),
        45: (339, 340),
        46: (340, 340),
        47: (340, 340),
        48: (340, 340),
        49: (340, 340),
        50: (340, 340),
        51: (340, 340),
        52: (340, 340),
        53: (340, 340),
        54: (340, 340),
        55: (340, 340),
        56: (340, 340),
        57: (340, 340),
        58: (340, 340),
        59: (340, 340),
        60: (340, 340),
        61: (340, 340),
    }

    rows = []
    for q61 in range(q61_min, 62):
        multiplier = pow(3, q61, MOD)
        assert multiplier & 1
        ok = [tail_survives(words[r], q61) for r in range(MOD)]

        counts = []
        for y in range(MOD):
            c = 0
            for a in BLOCK_LABELS:
                r = (y + a * multiplier) & (MOD - 1)
                c += int(ok[r])
            counts.append(c)

        mn, mx = min(counts), max(counts)
        assert (mn, mx) == expected[q61]
        rows.append((q61, multiplier, mn, mx))

    # High-value uniform caps for the lowest-surplus depth-61 states.
    assert expected[39][1] == 47
    assert expected[40][1] == 141
    assert expected[41][1] == 235
    assert expected[42][1] == 303
    assert expected[43][1] == 333

    print("PASS")
    print("q61_min =", q61_min)
    print("q61 | 3^q mod 2048 | min surviving labels | max surviving labels")
    for row in rows:
        print(*row)
    print("uniform cap at q61=39: at most 47 of 340 block labels survive to depth72")
    print("uniform cap at q61=40: at most 141 of 340 block labels survive to depth72")
    print("uniform cap at q61=41: at most 235 of 340 block labels survive to depth72")


if __name__ == "__main__":
    main()
