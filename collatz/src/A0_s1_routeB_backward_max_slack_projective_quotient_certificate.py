#!/usr/bin/env python3
"""Exact max-slack quotient for multi-gate backward ternary suffix feasibility.

This closes the ordering-composition part left open by the one-gate projective
carry/displacement theorems.

Let equal-count target/candidate one positions be

    a_1<...<a_q,
    b_1<...<b_q,
    b_r<=a_r.

Index the last L ranked ones from the right:

    A_t = a_(q-t),
    B_t = b_(q-t),

and define target capacity and candidate slack

    D_t = A_t-(q-t-1),
    s_t = B_t-(q-t-1).

The exact ordering language is

    0 <= s_t <= D_t,
    s_(t+1) <= s_t.

For a prescribed target-relative terminal ternary residue, use the usual suffix
carry z_t at remaining precision m=L-t.  A candidate slack s_t gives

    B_t = q-t-1+s_t

and passes the one-trit gate iff

    z_t + 2^A_t - 2^B_t == 0 mod3.

If it passes, the successor carry is

    z_(t+1)
      = (z_t + 2^A_t - 2^B_t)/3 mod3^(m-1).

At one layer, suppose two histories reach the SAME projective carry z_t but with
ordering caps S1<=S2, where the next slack is required to satisfy

    s_t <= min(D_t,S_i).

Every move legal from S1 is also legal from S2.  Moreover after choosing the
same s_t both histories have the same B_t, same successor carry, and same next
ordering cap s_t.  Hence S2 dominates S1 for all future suffix EXISTENCE tests.

Therefore one exact feasibility label is sufficient:

    S_max(z_t) = maximum reachable current slack/cap at carry z_t.

After every gate, histories reaching the same successor carry may be merged by
keeping only their maximum emitted slack.

This is a max-plus/upper-cap Bellman quotient for formation feasibility.  It is
NOT a defect-cost dominance theorem: two histories with different earlier
right-suffix defects may still trade off physical cost.  The quotient is used
for the backward residue/formation filter only.

Projective-cylinder transition.  For fixed incoming z, target A, remaining
precision m, and prescribed successor z', the existing carry bijection selects
one candidate exponent residue

    B == beta mod lambda_m,
    lambda_m = 2*3^(m-1).

Since B=base+s, the same transition is one slack cylinder

    s == gamma mod lambda_m.

Intersecting with the current legal interval [0,U] gives either no transition
or an exact arithmetic progression.  Its largest member is the successor's
largest possible ordering cap for that particular (z -> z') transition.
"""

from itertools import combinations

MAX_H = 8
+MAX_Z_REP = 20
+
+
+def correction_positions(pos):
+    q = len(pos)
+    return sum(3 ** (q-r-1) * 2 ** a for r, a in enumerate(pos))
+
+
+def cylinder_max(lo: int, hi: int, residue: int, period: int):
+    assert period >= 1
+    if lo > hi:
+        return None
+    out = hi - ((hi-residue) % period)
+    return out if out >= lo else None
+
+
+def gate_successor(A: int, B: int, z: int, m: int):
+    assert m >= 1
+    modulus = 3 ** m
+    numer = (z + pow(2, A, modulus) - pow(2, B, modulus)) % modulus
+    if numer % 3:
+        return None
+    return 0 if m == 1 else (numer // 3) % (3 ** (m-1))
+
+
+def projective_beta(A: int, z: int, m: int, zp: int):
+    """Unique B residue mod lambda_m for prescribed successor, or None."""
+    period = 2 * (3 ** (m-1))
+    hits = [b for b in range(period) if gate_successor(A, b, z, m) == zp]
+    if not hits:
+        return None
+    assert len(hits) == 1
+    return hits[0]
+
+
+def raw_layers(a, L: int, z0: int):
+    q = len(a)
+    states = {z0 % (3 ** L): [(None, ())]}
+    layers = []
+
+    for t in range(L):
+        m = L-t
+        A = a[q-1-t]
+        base = q-t-1
+        D = A-base
+        nxt = {}
+
+        for z, histories in states.items():
+            for previous_slack, history in histories:
+                U = D if previous_slack is None else min(D, previous_slack)
+                for s in range(U+1):
+                    B = base+s
+                    zp = gate_successor(A, B, z, m)
+                    if zp is None:
+                        continue
+                    nxt.setdefault(zp, []).append((s, history+(s,)))
+
+        states = nxt
+        layers.append(states)
+
+    return layers
+
+
+def quotient_layers(a, L: int, z0: int):
+    q = len(a)
+    # None is the unbounded-by-previous-slack initial cap; D_0 is applied at
+    # the first gate.
+    states = {z0 % (3 ** L): None}
+    layers = []
+
+    for t in range(L):
+        m = L-t
+        A = a[q-1-t]
+        base = q-t-1
+        D = A-base
+        nxt = {}
+
+        for z, previous_max in states.items():
+            U = D if previous_max is None else min(D, previous_max)
+            for s in range(U+1):
+                B = base+s
+                zp = gate_successor(A, B, z, m)
+                if zp is None:
+                    continue
+                if zp not in nxt or s > nxt[zp]:
+                    nxt[zp] = s
+
+        states = nxt
+        layers.append(states)
+
+    return layers
+
+
+# ---------------------------------------------------------------------------
+# 1. Exact finite regression: max-slack quotient equals raw history projection
+#    after EVERY gate, not merely at the terminal layer.
+# ---------------------------------------------------------------------------
+
+layer_checks = 0
+strict_merges = 0
+
+for h in range(1, MAX_H+1):
+    for q in range(1, h+1):
+        for a in combinations(range(h), q):
+            for L in range(1, q+1):
+                for z0 in range(min(3 ** L, MAX_Z_REP)):
+                    raw = raw_layers(a, L, z0)
+                    quo = quotient_layers(a, L, z0)
+                    assert len(raw) == len(quo) == L
+
+                    for raw_layer, quo_layer in zip(raw, quo):
+                        direct = {
+                            z: max(s for s, _history in histories)
+                            for z, histories in raw_layer.items()
+                        }
+                        assert quo_layer == direct
+                        for z, histories in raw_layer.items():
+                            if len(histories) > 1:
+                                strict_merges += 1
+                        layer_checks += 1
+
+
+# ---------------------------------------------------------------------------
+# 2. Abstract dominance preservation.
+# ---------------------------------------------------------------------------
+
+dominance_checks = 0
+for D in range(8):
+    for S1 in range(D+1):
+        for S2 in range(S1, D+1):
+            legal1 = set(range(min(D, S1)+1))
+            legal2 = set(range(min(D, S2)+1))
+            assert legal1 <= legal2
+            dominance_checks += 1
+
+
+# ---------------------------------------------------------------------------
+# 3. Exact one-transition slack-cylinder formula.
+# ---------------------------------------------------------------------------
+
+cylinder_checks = 0
+for m in range(1, 5):
+    period = 2 * (3 ** (m-1))
+    modulus_next = 3 ** (m-1)
+    for A in range(0, min(12, 2*period)):
+        for z in range(3 ** m):
+            # If the mod-3 gate itself is empty, there are no successor states.
+            mapping = {}
+            for beta in range(period):
+                zp = gate_successor(A, beta, z, m)
+                if zp is not None:
+                    mapping.setdefault(zp, []).append(beta)
+
+            if not mapping:
+                continue
+
+            assert set(mapping) == set(range(modulus_next))
+            assert all(len(v) == 1 for v in mapping.values())
+
+            for zp, vals in mapping.items():
+                beta = vals[0]
+                for base in range(0, 5):
+                    gamma = (beta-base) % period
+                    for U in range(0, 14):
+                        direct = [
+                            s for s in range(U+1)
+                            if gate_successor(A, base+s, z, m) == zp
+                        ]
+                        smax = cylinder_max(0, U, gamma, period)
+                        if direct:
+                            assert smax == max(direct)
+                            assert all((s-gamma) % period == 0 for s in direct)
+                        else:
+                            assert smax is None
+                        cylinder_checks += 1
+
+
+assert layer_checks > 0
+assert strict_merges > 0
+assert dominance_checks > 0
+assert cylinder_checks > 0
+
+print("PASS A0 s=1 Route-B backward max-slack projective quotient certificate")
+print("max_h", MAX_H)
+print("max_initial_carry_representatives", MAX_Z_REP)
+print("layer_checks", layer_checks)
+print("strict_merge_histories_seen", strict_merges)
+print("dominance_checks", dominance_checks)
+print("cylinder_checks", cylinder_checks)
+print(
+    "state",
+    "for suffix-existence at one layer, projective carry z carries one label S_max: the largest reachable ordering slack",
+)
+print(
+    "dominance",
+    "for the same z, a larger slack cap weakly contains every future formation choice available from a smaller cap",
+)
+print(
+    "projective_transition",
+    "a prescribed z->z' transition is one slack residue class mod 2*3^(m-1), intersected exactly with [0,min(D,S_max)]",
+)
+print(
+    "dsd_audit",
+    "formation feasibility is max-slack dominated; no defect-cost dominance or bounded carry-state count is inferred",
+)
+print(
+    "status",
+    "multi-gate ordering merge theorem CLOSED; symbolic compression of the set of carry states remains OPEN",
+)
