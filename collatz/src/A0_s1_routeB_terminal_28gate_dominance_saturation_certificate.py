#!/usr/bin/env python3
"""Exact terminal-28 target-dominance saturation certificate.

For the current right-H terminal window, index the last L=28 ranked one-events
from the right by t=0..27.  Let

    z_t + 2^A_t - 2^B_t == 0 (mod 3)

be the one-gate carry condition, with

    z_(t+1) = (z_t + 2^A_t - 2^B_t)/3  (mod 3^(m-1)),
    B_t = base_t + s_t,
    0 <= s_(t+1) <= s_t <= D_t.

The local mod-3 obstruction is immediate.  Since 2^n mod 3 depends only on
parity, for one fixed A_t an incoming carry z_t is locally admissible iff

    z_t mod 3 in G(A_t),

where

    G(A) = {0,1} for A even,
           {0,2} for A odd.

The nontrivial point is that every locally admissible z_t lifts through the
entire remaining suffix when the ordering cap is sufficiently large.

Inductive slack threshold:

    T_(L-1) = 1,
    T_t = T_(t+1) + 3.

Why +3 is enough: fix an arbitrary z_t mod 9, A_t mod 6, base_t mod 6,
next-target parity, and lower slack threshold T mod 6.  Among the four
consecutive integers

    T, T+1, T+2, T+3

there is always at least one slack s such that

* the current numerator is divisible by 3; and
* the successor carry lies in G(A_(t+1)) modulo 3.

This is a finite residue lemma modulo 6/9, checked exhaustively below.  Once
that s is chosen with s>=T_(t+1), the induction continues.

For L=28 the maximum required cap is

    T_0 = 1 + 3*27 = 82.

The actual target capacities satisfy

    D_t >= 232,565,502 >> 82

for every terminal rank.  Hence the complete 28-gate target-dominance
acceptance set is exactly the local first-gate set:

    z_H mod 3 in G(A_0).

Here A_0=630,138,896 is even, so

    z_H mod 3 in {0,1}.

Using z_H = 2^S Z - C(H_s^*) mod 3^28, with S odd and C(H_s^*) == 1 mod 3,
this is equivalent to

    Z mod 3 in {1,2},

i.e. 3 does not divide Z.

This closes ONLY target-dominance suffix existence at terminal precision 28.
Any additional H/L grammar boundary/control predicate and full pre-bridge
membership remain separate.
"""

J0 = 10_439_860_591
R0 = 6_586_818_670
S = 630_138_897
QH = (R0 * S) // J0 + 1
L = 28


def ceil_div(a: int, b: int) -> int:
    return -((-a) // b)


def target_one_position(r: int) -> int:
    assert 1 <= r <= QH
    if r == 1:
        return 0
    return ceil_div((r - 1) * J0, R0) - 1


def good_classes(A: int):
    return {0, 1} if A % 2 == 0 else {0, 2}


# ---------------------------------------------------------------------------
# 1. Exact current capacities and threshold budget.
# ---------------------------------------------------------------------------
rows = []
for t in range(L):
    r = QH - t
    A = target_one_position(r)
    base = QH - t - 1
    D = A - base
    rows.append((t, A, base, D))

assert rows[0] == (0, 630_138_896, 397_573_379, 232_565_517)
assert rows[-1] == (27, 630_138_854, 397_573_352, 232_565_502)

T = [0] * L
T[-1] = 1
for t in range(L - 2, -1, -1):
    T[t] = T[t + 1] + 3

assert T[0] == 82
assert all(D >= T[t] for t, _A, _base, D in rows)

# ---------------------------------------------------------------------------
# 2. Base gate: cap >=1 contains both slack parities.
# ---------------------------------------------------------------------------
for A in range(6):
    for base in range(6):
        for z in range(3):
            direct = []
            for s in (0, 1):
                B = base + s
                if (z + pow(2, A, 3) - pow(2, B, 3)) % 3 == 0:
                    direct.append(s)
            assert bool(direct) == (z in good_classes(A))

# ---------------------------------------------------------------------------
# 3. Universal induction residue lemma.
# ---------------------------------------------------------------------------
# We need only residues A/base/T mod 6 and z mod 9.  The next accepted set
# depends only on the parity of A_next.
local_checks = 0
for A in range(6):
    for base in range(6):
        for A_next_parity in (0, 1):
            G_next = {0, 1} if A_next_parity == 0 else {0, 2}
            for z9 in range(9):
                if z9 % 3 not in good_classes(A):
                    continue
                for T0 in range(6):
                    found = False
                    # Any absolute threshold congruent to T0 mod 6 behaves
                    # identically, so use T0+12 to keep all samples positive.
                    lower = T0 + 12
                    for s in range(lower, lower + 4):
                        B = base + s
                        numer = (
                            z9
                            + pow(2, A, 9)
                            - pow(2, B, 9)
                        ) % 9
                        if numer % 3:
                            continue
                        z_next_mod3 = (numer // 3) % 3
                        if z_next_mod3 in G_next:
                            found = True
                            break
                    assert found
                    local_checks += 1

assert local_checks == 1_728

# Span 2 is not universally sufficient; this guards that +3 is not silently
# replaced by a stronger unproved claim.
span2_failures = 0
for A in range(6):
    for base in range(6):
        for A_next_parity in (0, 1):
            G_next = {0, 1} if A_next_parity == 0 else {0, 2}
            for z9 in range(9):
                if z9 % 3 not in good_classes(A):
                    continue
                for T0 in range(6):
                    lower = T0 + 12
                    found = False
                    for s in range(lower, lower + 3):
                        B = base + s
                        numer = (
                            z9
                            + pow(2, A, 9)
                            - pow(2, B, 9)
                        ) % 9
                        if numer % 3:
                            continue
                        if (numer // 3) % 3 in G_next:
                            found = True
                            break
                    if not found:
                        span2_failures += 1

assert span2_failures > 0

# ---------------------------------------------------------------------------
# 4. Current first-gate and checkpoint corollary.
# ---------------------------------------------------------------------------
A0 = rows[0][1]
assert A0 % 2 == 0
assert good_classes(A0) == {0, 1}

# z_H = 2^S Z - C(H*) mod 3.  S is odd, so 2^S == 2 mod3.
# The last ranked-one term is the whole target correction mod3; A0 is even,
# so C(H*) == 2^A0 == 1 mod3.
assert S % 2 == 1
assert pow(2, S, 3) == 2
assert pow(2, A0, 3) == 1

accepted_Z_mod3 = {
    z
    for z in range(3)
    if (pow(2, S, 3) * z - pow(2, A0, 3)) % 3 in good_classes(A0)
}
assert accepted_Z_mod3 == {1, 2}

print("PASS A0 s=1 terminal 28-gate dominance saturation certificate")
print("terminal_gates", L)
print("first_target_exponent", A0)
print("first_good_carry_classes_mod3", sorted(good_classes(A0)))
print("threshold_T0", T[0])
print("minimum_actual_capacity", min(row[3] for row in rows))
print("local_mod6_mod9_checks", local_checks)
print("span2_counterexamples", span2_failures)
print("accepted_zH_mod3", [0, 1])
print("accepted_Z_mod3", [1, 2])
print(
    "exact_acceptance",
    "target-dominance terminal-28 suffix exists iff z_H mod 3 is 0 or 1; equivalently Z is not divisible by 3",
)
print(
    "dsd_audit",
    "this is dominance-suffix existence only; H/L boundary control, exact correction-language membership, and orbit compatibility remain OPEN",
)
