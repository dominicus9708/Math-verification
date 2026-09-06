#!/usr/bin/env python3
"""Exact regression examples for the 17-state Collatz FSM in Nwankpa v6.

The paper's Lemma 30 parametrizes several transient states, including
  S3 = {18m+2 : m>=1},
  S9 = {18k+16 : k>=0},
  S12 = {18k+17 : k>=0},
and states S3 -> S1 or S2 and S9 -> S11 or S12.

This certificate shows:
1) the quotient state does not determine a unique successor state;
2) a state cycle need not be an integer Collatz cycle.
"""


def C(n: int) -> int:
    return n // 2 if n % 2 == 0 else 3 * n + 1


def coarse_state_from_parametric_cases(n: int) -> str:
    # Only cases needed by the certificate, taken directly from Lemma 30.
    if n >= 20 and (n - 2) % 18 == 0:
        return "S3"
    if n >= 16 and (n - 16) % 18 == 0:
        return "S9"
    if n >= 17 and (n - 17) % 18 == 0:
        return "S12"
    # S1 = I, residue 1, even; in particular 10=9*1+1 with odd multiplier.
    if n == 10:
        return "S1"
    # S2 includes 19=18*1+1.
    if n == 19:
        return "S2"
    # S11 includes 8=18*0+8.
    if n == 8:
        return "S11"
    raise ValueError(f"state not encoded for n={n}")


# Same coarse state, different coarse successors.
x1, x2 = 20, 38
assert coarse_state_from_parametric_cases(x1) == "S3"
assert coarse_state_from_parametric_cases(x2) == "S3"
y1, y2 = C(x1), C(x2)
assert (y1, y2) == (10, 19)
assert coarse_state_from_parametric_cases(y1) == "S1"
assert coarse_state_from_parametric_cases(y2) == "S2"
assert coarse_state_from_parametric_cases(y1) != coarse_state_from_parametric_cases(y2)

# A quotient-state loop that is not an integer cycle.
a = 34
b = C(a)
c = C(b)
assert (a, b, c) == (34, 17, 52)
assert coarse_state_from_parametric_cases(a) == "S9"
assert coarse_state_from_parametric_cases(b) == "S12"
assert coarse_state_from_parametric_cases(c) == "S9"
assert c != a

print("SAFE FSM quotient regression")
print("20 and 38 are both S3, but successors are 10 in S1 and 19 in S2.")
print("34 -> 17 -> 52 gives S9 -> S12 -> S9 while 34 != 52.")
print("Therefore: integer determinism != quotient-state determinism,")
print("and a quotient-state cycle != an integer Collatz cycle.")
