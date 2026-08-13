#!/usr/bin/env python3
"""Exact certificates for Euclidean triangular correction-collision credits.

This file verifies two non-enumerative witnesses in the fixed one-slack
fibre (Sigma,M)=(-1,-1):

* U8 = U7 U6, length 46, q=28, credit 35;
* U9 = U7 U6 U6, length 65, q=40, credit 47.

The witnesses were found with the triangular composition congruence

    3^t R_Ah - R_Al + 2^|A| D_B == 0 (mod 3^(q-r)),

where D_B=(R_Bh-R_Bl)/3^r.  The checks below use Python integers only.
"""

U6 = "1010110110101101101"
U7 = "011011011010110110101101101"
U8 = U7 + U6
U9 = U7 + U6 + U6


def correction(word: str) -> int:
    R = 0
    for i, bit in enumerate(word):
        if bit == "1":
            R = 3 * R + (1 << i)
    return R


def rel_state(word: str, mechanical: str) -> tuple[int, int]:
    h = 0
    m = 0
    for a, b in zip(word, mechanical):
        h += int(a) - int(b)
        m = min(m, h)
    return h, m


# Level 8 = U7 U6.
L8_Ah = "001110011010111010101101101"   # U7 state (-1,-1), q=16
L8_Al = "111111110100101110111000111"   # U7 state (+2,0),  q=19
L8_Bh = "1010110110101110101"           # U6 state (0,0),   q=12
L8_Bl = "1010101101010100100"           # U6 state (-3,-3), q=9

W8_h = L8_Ah + L8_Bh
W8_l = L8_Al + L8_Bl

assert len(W8_h) == len(W8_l) == len(U8) == 46
assert W8_h.count("1") == W8_l.count("1") == 28
assert rel_state(W8_h, U8) == rel_state(W8_l, U8) == (-1, -1)

R8_Ah = correction(L8_Ah)
R8_Al = correction(L8_Al)
R8_Bh = correction(L8_Bh)
R8_Bl = correction(L8_Bl)

assert (R8_Bh - R8_Bl) % (3**9) == 0
D8_B = (R8_Bh - R8_Bl) // (3**9)
assert D8_B == 134

B8 = 27 * R8_Ah - R8_Al + (2**27) * D8_B
assert B8 % (3**19) == 0
assert B8 // (3**19) == 35

R8_h = correction(W8_h)
R8_l = correction(W8_l)
assert R8_h - R8_l == 35 * (3**28)


# Level 9 = U7 U6 U6.  First form the U8 prefix quotient D_C,
# then apply the same triangular step once more.
L9_Ah = "001101101011010110110101110"   # U7 state (-1,-1), q=16
L9_Al = "110111110011111010110101011"   # U7 state (+2,0),  q=19
L9_Ch = "1010111010101101110"           # U6 neutral, q=12
L9_Cl = "1111110000111100101"           # U6 neutral, q=12
L9_Bh = "1010110111001111001"           # U6 neutral, q=12
L9_Bl = "1101101010101010000"           # U6 state (-3,-3), q=9

W9_h = L9_Ah + L9_Ch + L9_Bh
W9_l = L9_Al + L9_Cl + L9_Bl

assert len(W9_h) == len(W9_l) == len(U9) == 65
assert W9_h.count("1") == W9_l.count("1") == 40
assert rel_state(W9_h, U9) == rel_state(W9_l, U9) == (-1, -1)

R9_Ah = correction(L9_Ah)
R9_Al = correction(L9_Al)
R9_Ch = correction(L9_Ch)
R9_Cl = correction(L9_Cl)
R9_Bh = correction(L9_Bh)
R9_Bl = correction(L9_Bl)

assert (R9_Bh - R9_Bl) % (3**9) == 0
D9_B = (R9_Bh - R9_Bl) // (3**9)
assert D9_B == 128

C9 = 27 * R9_Ch - R9_Cl + (2**19) * D9_B
assert C9 % (3**12) == 0
D9_C = C9 // (3**12)
assert D9_C == 260

B9 = 27 * R9_Ah - R9_Al + (2**27) * D9_C
assert B9 % (3**19) == 0
assert B9 // (3**19) == 47

R9_h = correction(W9_h)
R9_l = correction(W9_l)
assert R9_h - R9_l == 47 * (3**40)

print("level8_credit", 35)
print("level8_q", 28)
print("level8_diff", R8_h - R8_l)
print("level9_credit", 47)
print("level9_q", 40)
print("level9_diff", R9_h - R9_l)
