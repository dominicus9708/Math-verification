#!/usr/bin/env python3
"""Exact coordinate audit for the m=45 p=8 depth-28 renewal credit.

This certificate fixes a subtle normalization issue in the closure program.
The number 290 produced by the p=8 immediate-return calculation is NOT the
ordinary integer predecessor credit used by the G81/G82 credit recursion.
It is a projective/common-suffix normalized credit.

For a common suffix of length s with r odd symbols, a state difference of the
form

    Delta_in = 2^s * c

is sent to

    Delta_out = 3^r * c.

Thus c is invariant after stripping the common dyadic/ternary coefficient.
For the mechanical depth-28 word and its p=8 adjacent 01->10 excursion the
exact invariant is c=290, with (s,r)=(18,11).

The ordinary credit recursion in the repository is

    delta_left = (R_u-R_w + 2^L delta_right) / 3^q,

so its delta variables are ordinary integer differences, not c.

For a front-loaded gate cube with J pair coordinates, the normalized Hensel
target for ordinary credit delta is

    target = -2^(2J+1) delta (mod 3^q).

If delta=3^b*c with 3 not dividing c, the first b balanced-Hensel digits are
forced zero.  After those b zero lifts, the primitive credit is 4^b*c, not c.
For the p=8 endpoint ordinary difference this is 4^11*290=1,216,348,160.
Therefore the old bounded-credit audit 1<=delta<=397 cannot be applied by
simply substituting 290.

This is a coordinate theorem/diagnostic, not a Collatz proof.
"""

L = 28
H19 = "1101101101011011010"
MECH = (H19 + H19)[:L]


def canonical(bits: str):
    r = 0
    y = 0
    q = 0
    for k, ch in enumerate(bits):
        b = int(ch)
        carry = b ^ (y & 1)
        if carry:
            r += 1 << k
            y += 3**q
        if b:
            y = (3*y + 1)//2
            q += 1
        else:
            y //= 2
    return r, y, q


def run_prefix(n: int, bits: str):
    x = n
    for ch in bits:
        b = x & 1
        assert b == int(ch)
        x = (3*x + 1)//2 if b else x//2
    return x


# p=8 is a mechanical 01 pair.  The positive-height immediate return is 10.
p = 8
assert MECH[p:p+2] == "01"
EXC = list(MECH)
EXC[p], EXC[p+1] = "1", "0"
EXC = "".join(EXC)

rm, ym, qm = canonical(MECH)
re, ye, qe = canonical(EXC)
assert (qm, qe) == (18, 18)
assert (rm, re) == (163_470_331, 199_065_339)
assert (ym, ye) == (235_929_181, 287_301_811)

ret = p + 2
s = L - ret
r_suffix = sum(int(c) for c in MECH[ret:])
assert (s, r_suffix) == (18, 11)
assert MECH[ret:] == EXC[ret:]

xm = run_prefix(rm, MECH[:ret])
xe = run_prefix(re, EXC[:ret])
Delta_in = xe - xm
Delta_out = ye - ym

assert Delta_in == 76_021_760
assert Delta_out == 51_372_630
assert Delta_in % (1 << s) == 0
c = Delta_in >> s
assert c == 290
assert Delta_out == 3**r_suffix * c
assert Delta_in == 2**s * c

# Generic Hensel normalization identity.  In a gate cube
# 2^(2J+1) = 8*4^(J-1), so after multiplying by 4^(-(J-1))
# the initial balanced residual is -8*delta.  If delta=3^b*c,
# b zero trits turn this into -8*4^b*c.
b = r_suffix
reduced_primitive = 4**b * c
assert reduced_primitive == 1_216_348_160
assert reduced_primitive > 397

# The two ordinary boundary differences are likewise not the bounded credit.
assert Delta_in != c and Delta_out != c
assert Delta_in > 397 and Delta_out > 397

print("m45 p8 projective-credit alignment: PASS")
print("return_difference", Delta_in)
print("endpoint_difference", Delta_out)
print("common_suffix", (s, r_suffix))
print("projective_credit", c)
print("gate_reduced_primitive_after_11_zero_trits", reduced_primitive)
print("direct_290_to_bounded_gate_credit", "INVALID")
