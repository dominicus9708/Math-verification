#!/usr/bin/env python3
"""MATH-220 exact 13-bit mechanical low-address gate."""

from fractions import Fraction

L = 13

def m(q):
    if q == 0:
        return 0
    return (3**q).bit_length() - 1 - q

def tau(r):
    return Fraction(3**r, 2**(r + m(r) + 1))

def word(omega):
    bits = [0] * L
    r = 0
    while True:
        pos = 0 if r == 0 else r + m(r) + (1 if omega <= tau(r) else 0)
        if pos >= L:
            break
        bits[pos] = 1
        r += 1
    return tuple(bits)

def correction(bits):
    C = q = 0
    for p, b in enumerate(bits):
        if b:
            C = 3 * C + (1 << p)
            q += 1
    return C, q

def residue(bits):
    C, q = correction(bits)
    mod = 1 << L
    return (-C * pow(pow(3, q, mod), -1, mod)) % mod

EXPECTED = {
    673: "1010110110101",
    2721: "1010110110110",
    6969: "1011010110110",
    2553: "1011011010110",
    4089: "1011011011010",
    3179: "1101011011010",
    7275: "1101011011011",
    1915: "1101101011011",
    7163: "1101101101011",
}

def main():
    cuts = sorted({Fraction(1,2), Fraction(1)} |
                  {tau(r) for r in range(1, L+1)})
    got = {}
    for a, b in zip(cuts[:-1], cuts[1:]):
        bits = word((a+b)/2)
        got[residue(bits)] = "".join(map(str, bits))
    for x in cuts:
        if Fraction(1,2) < x <= 1:
            bits = word(x)
            got[residue(bits)] = "".join(map(str, bits))
    assert got == EXPECTED, (got, EXPECTED)
    assert len(got) == 9
    print("PASS MATH-220 13-bit mechanical gate")
    print("residues", sorted(got))
    print("raw_phase_cells", len(cuts)-1)
    print("distinct_words", len(got))
    print("NO r10 LAYER CLOSURE CLAIM")

if __name__ == "__main__":
    main()
