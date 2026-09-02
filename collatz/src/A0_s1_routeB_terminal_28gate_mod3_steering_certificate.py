#!/usr/bin/env python3
"""Exact 28-gate normalized-carry steering certificate for A0 s=1 Route-B.

For the final L ranked-one gates write

    base_t = q-t-1,
    A_t = base_t + D_t,
    B_t = base_t + s_t,

with exact target-dominance ordering

    0 <= s_t <= D_t,
    s_(t+1) <= s_t.

Normalize the projective carry by

    w_t = 2^(-base_t) z_t  (mod 3^m),
    m = L-t.

The one-gate recurrence becomes

    w_(t+1) = 2*(w_t + 2^D_t - 2^s_t)/3  (mod 3^(m-1)),

whenever the numerator is divisible by 3.

Modulo 3, a gate is impossible for exactly one carry class:

    w_t == (-1)^(D_t+1) (mod 3).

For either allowed carry class, the parity of s_t is uniquely fixed.  Among
six consecutive slack values there are three representatives of that parity,
one in each residue class modulo 6.  Because 2^s modulo 9 cycles through three
values on a fixed parity class, those three choices produce all three possible
values of w_(t+1) modulo 3.

Therefore if every capacity D_t is at least 5L, one may always choose s_t from
the top six legal values, losing at most five units of ordering cap per gate,
and steer the next normalized carry away from the next forbidden mod-3 class.
This proves:

    completion exists  <=>  w_0 != (-1)^(D_0+1) (mod 3).

For the current right-H terminal window L=28,

    q_H = 397,573,380,
    D_0 = 232,565,517,
    min D_t = 232,565,502 > 5*28.

Since base_0=q_H-1 is odd, w_0 == 2 z_H (mod 3).  Since D_0 is odd, the
forbidden normalized class is w_0==1, hence

    right-H dominance completion exists <=> z_H != 2 (mod 3).

Using the synchronized checkpoint affine observation

    z_H = 2^S Z - C(H_s^*) (mod 3^28),

with 2^S==2 and C(H_s^*)==1 modulo 3, this is exactly

    Z != 0 (mod 3).

Scope: this closes the pure target-dominance + terminal-residue existence
predicate only.  It does not prove full pre-bridge correction-language
membership, same-orbit connectivity, physical closure, or Collatz.
"""

from functools import lru_cache

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


def capacity(t: int) -> int:
    r = QH - t
    A = target_one_position(r)
    base = QH - t - 1
    return A - base


D = tuple(capacity(t) for t in range(L))
assert QH == 397_573_380
assert D[0] == 232_565_517
assert D[-1] == 232_565_502
assert min(D) == 232_565_502
assert min(D) > 5 * L


def forbidden_class(Dt: int) -> int:
    return pow(-1, Dt + 1, 3)


def normalized_successor_mod3(w_mod9: int, Dt: int, s: int):
    numer = (w_mod9 + pow(2, Dt, 9) - pow(2, s, 9)) % 9
    if numer % 3:
        return None
    return (2 * (numer // 3)) % 3


# Exact local steering lemma modulo 9: for every allowed w mod 3, fixing the
# required slack parity and ranging over its three classes mod 6 reaches all
# three successor residues mod 3.
local_checks = 0
for Dt in range(12):
    f = forbidden_class(Dt)
    for w9 in range(9):
        if w9 % 3 == f:
            # No slack parity can satisfy divisibility modulo 3.
            assert all(
                normalized_successor_mod3(w9, Dt, s) is None
                for s in range(6)
            )
            local_checks += 1
            continue

        valid = [s for s in range(6) if normalized_successor_mod3(w9, Dt, s) is not None]
        assert len(valid) == 3
        assert len({s % 2 for s in valid}) == 1
        assert {normalized_successor_mod3(w9, Dt, s) for s in valid} == {0, 1, 2}
        local_checks += 1

assert local_checks == 108

# Small-horizon exhaustive regression for the general 5L steering theorem.
# This is implementation evidence only; the proof is the top-six steering
# argument in the module docstring.
def full_successor(w: int, Dt: int, s: int, m: int):
    mod = 3 ** m
    numer = (w + pow(2, Dt, mod) - pow(2, s, mod)) % mod
    if numer % 3:
        return None
    if m == 1:
        return 0
    return (2 * (numer // 3)) % (3 ** (m - 1))


def brute_accept(Ds):
    LL = len(Ds)

    @lru_cache(None)
    def ok(t: int, w: int, previous_slack: int):
        if t == LL:
            return True
        m = LL - t
        U = Ds[t] if previous_slack < 0 else min(Ds[t], previous_slack)
        for s in range(U + 1):
            wp = full_successor(w, Ds[t], s, m)
            if wp is not None and ok(t + 1, wp, s):
                return True
        return False

    return {w for w in range(3 ** LL) if ok(0, w, -1)}


regression_checks = 0
for LL in range(1, 5):
    # Vary parity/capacity profile while keeping min D >= 5L.
    for offset in range(3):
        Ds = tuple(5 * LL + offset + ((t + offset) & 1) for t in range(LL))
        actual = brute_accept(Ds)
        expected = {
            w for w in range(3 ** LL)
            if w % 3 != forbidden_class(Ds[0])
        }
        assert actual == expected
        regression_checks += 1

assert regression_checks == 12

# Current-coordinate reduction.
BASE0 = QH - 1
assert BASE0 % 2 == 1
assert D[0] % 2 == 1

# mod 3, 2^{-odd} == 2.
for zh in range(3):
    w0 = (2 * zh) % 3
    accepted = w0 != forbidden_class(D[0])
    assert accepted == (zh != 2)

M3 = 3 ** 28
# Recompute the final-28 target correction residue exactly.
CH28 = 0
for r in range(QH - 28 + 1, QH + 1):
    a = target_one_position(r)
    CH28 = (CH28 + pow(3, QH - r, M3) * pow(2, a, M3)) % M3
A28 = pow(2, S, M3)
assert A28 % 3 == 2
assert CH28 % 3 == 1

for Z3 in range(3):
    zh3 = (A28 * Z3 - CH28) % 3
    assert (zh3 != 2) == (Z3 != 0)

print("PASS A0 s=1 Route-B terminal 28-gate mod3 steering certificate")
print("q_H", QH)
print("terminal_precision", L)
print("D0", D[0])
print("Dmin", min(D))
print("steering_margin_Dmin_minus_5L", min(D) - 5 * L)
print("local_mod9_steering_checks", local_checks)
print("small_horizon_regression_checks", regression_checks)
print("normalized_forbidden_w_mod3", forbidden_class(D[0]))
print("accepted_z_H_mod3", (0, 1))
print("rejected_z_H_mod3", (2,))
print("equivalent_checkpoint_condition", "Z mod 3 in {1,2}; equivalently 3 does not divide Z")
print("status", "EXACT target-dominance terminal-residue existence collapse; full membership remains OPEN")
