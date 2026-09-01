#!/usr/bin/env python3
"""Exact max-slack quotient for multi-gate backward ternary suffix feasibility.

For equal-count target/candidate one positions a_r,b_r with b_r<=a_r, index
from the right and define

    A_t = a_(q-t),
    B_t = b_(q-t),
    D_t = A_t-(q-t-1),
    s_t = B_t-(q-t-1).

The exact ordering constraints are

    0 <= s_t <= D_t,
    s_(t+1) <= s_t.

At remaining ternary precision m=L-t, a target-relative carry z_t and choice
B_t pass iff

    z_t + 2^A_t - 2^B_t == 0 mod 3,

with successor

    z_(t+1) = (z_t+2^A_t-2^B_t)/3 mod 3^(m-1).

If two histories reach the same projective carry z_t with ordering caps
S1<=S2, every future slack move legal from S1 is also legal from S2.  Taking
the same next slack gives the same exponent, successor carry, and next cap.
Thus S2 dominates S1 for suffix EXISTENCE.

Hence each carry state needs one feasibility label only:

    S_max(z_t) = maximum reachable current slack/cap.

This is not a defect-cost dominance theorem.

For fixed incoming z, target A, precision m, and prescribed successor z', the
existing one-step carry bijection selects one exponent residue modulo

    lambda_m = 2*3^(m-1).

Since B=base+s, the same transition is one slack residue class modulo lambda_m.
Intersecting that class with [0,min(D,S_max)] is exact; its largest member is
the largest successor ordering cap for that specified transition.

The finite code below is a REGRESSION ONLY implementation guard.  The theorem
itself is the nested-future-choice argument above plus the certified one-step
projective carry bijection.
"""

from itertools import combinations

MAX_H = 8
MAX_Z_REP = 20


def cylinder_max(lo: int, hi: int, residue: int, period: int):
    assert period >= 1
    if lo > hi:
        return None
    out = hi - ((hi-residue) % period)
    return out if out >= lo else None


def gate_successor(A: int, B: int, z: int, m: int):
    assert m >= 1
    modulus = 3 ** m
    numer = (z + pow(2, A, modulus) - pow(2, B, modulus)) % modulus
    if numer % 3:
        return None
    return 0 if m == 1 else (numer // 3) % (3 ** (m-1))


def raw_layers(a, L: int, z0: int):
    q = len(a)
    states = {z0 % (3 ** L): [(None, ())]}
    layers = []

    for t in range(L):
        m = L-t
        A = a[q-1-t]
        base = q-t-1
        D = A-base
        nxt = {}

        for z, histories in states.items():
            for previous_slack, history in histories:
                U = D if previous_slack is None else min(D, previous_slack)
                for s in range(U+1):
                    B = base+s
                    zp = gate_successor(A, B, z, m)
                    if zp is None:
                        continue
                    nxt.setdefault(zp, []).append((s, history+(s,)))

        states = nxt
        layers.append(states)

    return layers


def quotient_layers(a, L: int, z0: int):
    q = len(a)
    states = {z0 % (3 ** L): None}
    layers = []

    for t in range(L):
        m = L-t
        A = a[q-1-t]
        base = q-t-1
        D = A-base
        nxt = {}

        for z, previous_max in states.items():
            U = D if previous_max is None else min(D, previous_max)
            for s in range(U+1):
                B = base+s
                zp = gate_successor(A, B, z, m)
                if zp is None:
                    continue
                if zp not in nxt or s > nxt[zp]:
                    nxt[zp] = s

        states = nxt
        layers.append(states)

    return layers


# ---------------------------------------------------------------------------
# 1. Max-slack quotient equals the raw-history projection after every gate.
# ---------------------------------------------------------------------------

layer_checks = 0
strict_merges = 0

for h in range(1, MAX_H+1):
    for q in range(1, h+1):
        for a in combinations(range(h), q):
            for L in range(1, q+1):
                for z0 in range(min(3 ** L, MAX_Z_REP)):
                    raw = raw_layers(a, L, z0)
                    quo = quotient_layers(a, L, z0)
                    assert len(raw) == len(quo) == L

                    for raw_layer, quo_layer in zip(raw, quo):
                        direct = {
                            z: max(s for s, _history in histories)
                            for z, histories in raw_layer.items()
                        }
                        assert quo_layer == direct
                        strict_merges += sum(
                            1 for histories in raw_layer.values()
                            if len(histories) > 1
                        )
                        layer_checks += 1


# ---------------------------------------------------------------------------
# 2. Abstract nested-choice dominance.
# ---------------------------------------------------------------------------

dominance_checks = 0
for D in range(8):
    for S1 in range(D+1):
        for S2 in range(S1, D+1):
            legal1 = set(range(min(D, S1)+1))
            legal2 = set(range(min(D, S2)+1))
            assert legal1 <= legal2
            dominance_checks += 1


# ---------------------------------------------------------------------------
# 3. One-transition slack-cylinder formula.
# ---------------------------------------------------------------------------

cylinder_checks = 0
for m in range(1, 5):
    period = 2 * (3 ** (m-1))
    modulus_next = 3 ** (m-1)
    for A in range(min(12, 2*period)):
        for z in range(3 ** m):
            mapping = {}
            for beta in range(period):
                zp = gate_successor(A, beta, z, m)
                if zp is not None:
                    mapping.setdefault(zp, []).append(beta)

            if not mapping:
                continue

            assert set(mapping) == set(range(modulus_next))
            assert all(len(v) == 1 for v in mapping.values())

            for zp, residues in mapping.items():
                beta = residues[0]
                for base in range(5):
                    gamma = (beta-base) % period
                    for U in range(14):
                        direct = [
                            s for s in range(U+1)
                            if gate_successor(A, base+s, z, m) == zp
                        ]
                        smax = cylinder_max(0, U, gamma, period)
                        if direct:
                            assert smax == max(direct)
                            assert all((s-gamma) % period == 0 for s in direct)
                        else:
                            assert smax is None
                        cylinder_checks += 1


assert layer_checks > 0
assert strict_merges > 0
assert dominance_checks > 0
assert cylinder_checks > 0

print("PASS A0 s=1 Route-B backward max-slack projective quotient certificate")
print("max_h", MAX_H)
print("max_initial_carry_representatives", MAX_Z_REP)
print("layer_checks", layer_checks)
print("strict_merge_states_seen", strict_merges)
print("dominance_checks", dominance_checks)
print("cylinder_checks", cylinder_checks)
print(
    "state",
    "for suffix existence, each projective carry z carries one label S_max, the largest reachable ordering slack",
)
print(
    "dominance",
    "for the same z, larger slack cap contains every future formation choice available from a smaller cap",
)
print(
    "projective_transition",
    "a prescribed z->z' transition is one slack residue class mod 2*3^(m-1), intersected with [0,min(D,S_max)]",
)
print(
    "dsd_audit",
    "formation feasibility is max-slack dominated; no defect-cost dominance or bounded carry-state count is inferred",
)
print(
    "status",
    "multi-gate ordering merge theorem CLOSED; symbolic compression of the set of carry states remains OPEN",
)
