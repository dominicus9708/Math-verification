#!/usr/bin/env python3

MOD = 1 << 11
LABELS = tuple(range(1024, 1364))


def min_q_survival(k: int) -> int:
    q = 0
    p3 = 1
    while p3 < (1 << k):
        p3 *= 3
        q += 1
    return q


def cumulative_odd_counts_11(n: int):
    x = n
    c = 0
    out = []
    for _ in range(11):
        b = x & 1
        c += b
        out.append(c)
        x = (3 * x + 1) // 2 if b else x // 2
    return tuple(out)


def main():
    required = tuple(min_q_survival(61 + j) for j in range(1, 12))
    cumulative = [cumulative_odd_counts_11(r) for r in range(MOD)]

    expected_classes = {
        39: 2048,
        40: 2048,
        41: 2048,
        42: 2048,
        43: 2048,
        44: 1838,
        45: 341,
        46: 1,
        47: 1,
        48: 1,
        49: 1,
        50: 1,
        51: 1,
        52: 1,
        53: 1,
        54: 1,
        55: 1,
        56: 1,
        57: 1,
        58: 1,
        59: 1,
        60: 1,
        61: 1,
    }

    rows = []
    for q61 in range(39, 62):
        ok = []
        for r in range(MOD):
            cum = cumulative[r]
            survives = all(q61 + cum[j] >= required[j] for j in range(11))
            ok.append(survives)

        mult = pow(3, q61, MOD)
        masks = set()
        counts = []
        for y in range(MOD):
            mask = 0
            count = 0
            for i, a in enumerate(LABELS):
                r = (y + a * mult) & (MOD - 1)
                if ok[r]:
                    mask |= 1 << i
                    count += 1
            masks.add(mask)
            counts.append(count)

        class_count = len(masks)
        assert class_count == expected_classes[q61]
        rows.append((q61, class_count, min(counts), max(counts)))

    # No exact y-residue compression at all in the strongest low-surplus sieve.
    for q in range(39, 44):
        assert expected_classes[q] == MOD

    assert expected_classes[44] == 1838
    assert expected_classes[45] == 341
    for q in range(46, 62):
        assert expected_classes[q] == 1

    print("PASS")
    print("q61 | exact survival-mask right-congruence classes | min labels | max labels")
    for row in rows:
        print(*row)
    print("q61=39..43: all 2048 endpoint residues are pairwise distinguishable")
    print("q61=44: 1838 exact mask classes")
    print("q61=45: 341 exact mask classes")
    print("q61>=46: one trivial class because all 340 labels survive")


if __name__ == "__main__":
    main()
