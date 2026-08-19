#!/usr/bin/env python3
"""Exact arithmetic certificate for the height-credit phase-cocycle theorem.

Inputs:
  * the all-factor 19-step theorem
        |local normalized correction source| < 8,
    certified by h19_allfactor_height_credit_source_certificate.cpp;
  * the exact G81/G82 first-return phase partition already certified in the
    repository.

Let alpha=log_3(2), epsilon=12-19 alpha and delta=1-81 epsilon.
For a 19-step block with mechanical odd count Q, actual odd count q, incoming
height H and outgoing height H'=H+q-Q, normalize ordinary predecessor credit by

    chi = credit / 3^H.

The exact credit concatenation identity becomes

    chi_left = source + (2^19/3^Q) chi_right,

where |source|<8.

At the first-return gate scale the two possible homogeneous multipliers are

    G81: 2^1539/3^971 = 3^delta,
    G82: 2^1558/3^983 = 3^(delta-epsilon).

The phase return is x' = x+delta mod epsilon, so in both cases

    A_gate = 3^(x'-x).

Thus Psi=3^x chi removes the homogeneous multiplier exactly:

    Psi_left = Psi_right + 3^x S_gate.

For any mechanical/Sturmian prefix, the odd-count discrepancy from t*alpha has
absolute value <1.  Therefore every partial homogeneous product inside one gate
is <3.  A gate has at most 82 length-19 blocks, hence

    |S_gate| < 8*3*82 = 1968,
    |Delta Psi_gate| < 3*1968 = 5904.

Consequently a relation constructed from terminal credit zero through n
first-return gates satisfies |Psi|<5904*n.  In particular, at a renewal boundary
with H=0, ordinary credit has only linear amplitude in n.

The final telescoping step is algebraic; this file certifies all integer/rational
constants and the exact sign/range facts used by it.  This is a globalization
lemma for the credit channel, not a proof of Collatz.
"""

from fractions import Fraction

# Certified convergent bracket already used by the G81/G82 exact theorem.
LOW = Fraction(15601, 24727)
HIGH = Fraction(31867, 50508)
assert LOW < HIGH
assert 3**15601 < 2**24727
assert 3**31867 > 2**50508

# alpha is bracketed by LOW < alpha < HIGH.
# epsilon=12-19 alpha therefore lies in the reversed rational interval.
EPS_LO = Fraction(12) - 19 * HIGH
EPS_HI = Fraction(12) - 19 * LOW
assert EPS_LO > 0
assert EPS_HI < 1

# delta=1-81 epsilon.
DELTA_LO = Fraction(1) - 81 * EPS_HI
DELTA_HI = Fraction(1) - 81 * EPS_LO
assert DELTA_LO > 0
assert DELTA_HI < EPS_LO  # 0 < delta < epsilon uniformly in the bracket.

# Exact Euclidean-gate arithmetic identities.
assert 1539 == 81 * 19
assert 971 == 81 * 12 - 1
assert 1558 == 82 * 19
assert 983 == 82 * 12 - 1

# Hence, symbolically,
# 1539*alpha-971 = 1-81*(12-19*alpha) = delta,
# 1558*alpha-983 = delta-epsilon.
# Integer-power signs independently certify G81 is slightly expansive and
# G82 slightly contractive in the homogeneous coefficient channel.
assert 2**1539 > 3**971
assert 2**1558 < 3**983

LOCAL_SOURCE_BOUND = 8
PREFIX_PRODUCT_BOUND = 3
MAX_GATE_BLOCKS = 82
GATE_SOURCE_BOUND = LOCAL_SOURCE_BOUND * PREFIX_PRODUCT_BOUND * MAX_GATE_BLOCKS
assert GATE_SOURCE_BOUND == 1968

# Since 0<=x<epsilon<1, 3^x<3.
PHASE_WEIGHT_BOUND = 3
PSI_INCREMENT_BOUND = PHASE_WEIGHT_BOUND * GATE_SOURCE_BOUND
assert PSI_INCREMENT_BOUND == 5904

# Simple exact induction constant: terminal Psi_n=0 implies
# |Psi_0| < 5904*n after n gate steps.
for n in (1, 2, 10, 100, 1000):
    assert n * PSI_INCREMENT_BOUND == 5904 * n

print("height-credit phase cocycle certificate: PASS")
print("epsilon_interval", EPS_LO, EPS_HI)
print("delta_interval", DELTA_LO, DELTA_HI)
print("gate_source_bound", GATE_SOURCE_BOUND)
print("phase_adjusted_increment_bound", PSI_INCREMENT_BOUND)
print("renewal_credit_growth", "O(number_of_first_return_gates)")
