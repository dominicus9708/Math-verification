#!/usr/bin/env python3
"""MATH-077 exact source-resolution certificate for the pure u=0 boundary word.

Pure boundary policy:
  * at u=0 take the odd shortcut;
  * if epsilon=1 raises u to 1, take one even shortcut immediately;
  * never take an odd shortcut at positive slack.

The script computes the exact parity-cylinder source residue and counts ordinary
source anchors in the strict first-cell window 2^71 < N < 1364*2^61.
"""

LO = 1 << 71
HI = 1364 * (1 << 61)


def m(q: int) -> int:
    if q == 0:
        return 0
    return pow(3, q).bit_length() - 1 - q


def boundary_word(k: int):
    q = d = 0
    out = []
    for _ in range(k):
        u = m(q) - d
        assert u in (0, 1)
        if u == 0:
            out.append(1)
            q += 1
        else:
            out.append(0)
            d += 1
    return out


def correction_q(bits):
    C = q = 0
    for pos, bit in enumerate(bits):
        if bit:
            C = 3 * C + (1 << pos)
            q += 1
    return C, q


def cylinder(k: int):
    bits = boundary_word(k)
    C, q = correction_q(bits)
    mod = 1 << k
    residue = (-C * pow(pow(3, q, mod), -1, mod)) % mod
    first = LO + 1 + ((residue - (LO + 1)) % mod)
    count = 0 if first >= HI else (HI - 1 - first) // mod + 1
    return count, first if count else None, residue, q


def main():
    expected = {
        65: 21,
        66: 10,
        67: 5,
        68: 2,
        69: 1,
        70: 0,
    }
    for k, want in expected.items():
        count, first, residue, q = cylinder(k)
        assert count == want, (k, count, want)
        print(k, "count", count, "q", q, "residue", residue,
              "first", first)

    # Nesting check: each longer pure-boundary cylinder is the exact child of
    # the previous one, so surviving ordinary anchors can only decrease.
    prev = None
    for k in range(1, 71):
        count, first, residue, q = cylinder(k)
        if prev is not None:
            pcount, pfirst, pres, pq = prev
            assert residue % (1 << (k - 1)) == pres
            assert count <= pcount
        prev = (count, first, residue, q)

    assert cylinder(69)[0] == 1
    assert cylinder(70)[0] == 0
    print("PASS MATH-077 pure boundary source cylinder empty by depth 70")


if __name__ == "__main__":
    main()
