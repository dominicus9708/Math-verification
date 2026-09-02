# Open gates

This register contains unresolved obligations only. Closed/redundant gates belong in the theorem/audit indexes rather than remaining as active search targets.

## G1 — Predicate-driven physical Bellman pruning

**Module:** C4

The forward exact state

`source/control × interval payload × P_min`

remains valid for the directed physical rejection predicate.

Completed finite deep-root executions to `h=72`:

- `f=29`: max 1,080,374 states, final 16, physical closures 0;
- `f=32`: max 419,510, final 16, physical closures 0;
- `f=35`: max 167,507, final 14, physical closures 0;
- `f=37`: max 81,519, final 13, physical closures 0.

These counts are execution evidence only. The `f=27` attempted run timed out and contributes no retained result.

Use `P_min` as a secondary predicate where a source-controlled family is still large. Do not make it the sole principal strategy and do not propagate the merged key beyond ordinary-X exposure for arbitrary later predicates without an exact future-control theorem.

Status: **ACTIVE SECONDARY GATE**.

## G2 — Terminal right-H target-dominance ternary gate

**Module:** C4/C5

This gate is no longer open.

Exact terminal-28 saturation gives

\[
z_H\bmod3\in\{0,1\}
\iff
Z\bmod3\in\{1,2\}.
\]

Every genuine positive-one-count checkpoint already satisfies `3∤Z` by the checkpoint correction identity modulo 3.

Therefore the dominance-only terminal gate removes zero genuine candidates and is **REDUNDANT AS A PRUNING ENGINE**.

Do not restart raw or compressed 28-gate dominance carry enumeration in search of additional pruning.

The full synchronized CRT singleton seam remains exact if another stronger predicate supplies a full `z_H mod 3^28` observation.

Status: **CLOSED / REDUNDANT FOR PRUNING**.

## G3 — Source-controlled exact correction/checkpoint membership

**Module:** C5

This is the **principal active gate**.

For a source state and ordinary checkpoint candidate, the required full pre-bridge correction is

\[
C_{req}=2^{t_0}Z-3^{j_0}X.
\]

At fixed `(t0,j0)`, the correction map is injective. The unresolved task is exact **existence/inversion inside the long formation language**, not uniqueness after a word is found.

Required output:

1. an exact source-controlled state that combines the affine source prefix/control with correction-language information;
2. a legal inverse/join rule using dyadic prefix localization and, only when informative, ternary suffix/projective localization;
3. exact rejection or realization of families without treating an adic mismatch as membership rejection unless the active language predicate actually requires equality;
4. explicit preservation of all boundary/control coordinates needed for continuation;
5. family/root-level counts reported as execution evidence unless separately generalized.

Preferred architecture:

`source prefix/control`
→ `required correction congruence / block state`
→ `exact H/L or equivalent correction-language recursion`
→ `full correction realization or rejection`.

Status: **ACTIVE — principal mathematical bottleneck**.

## G4 — Synchronized ordinary checkpoint/source join when a strong observation exists

**Module:** C5

Closed tools:

- full `Z mod2^27 × z_H mod3^28` CRT singleton exposure;
- exposed `Z` -> exact debit-compatible source fibers.

But dominance-only right-H existence supplies only the automatic condition `3∤Z`, not a full `z_H mod3^28` value.

Therefore use the full CRT singleton seam only if G3 or another independent exact predicate actually produces the full ternary observation.

A weak channel `Z mod2^27` plus `Z mod3 in {1,2}` is non-isolating: for a fixed `X`, each accepted weak CRT class occurs at least 789 times in the ordinary debit interval, at least 1,578 candidates across both accepted classes before other constraints.

Status: **CONDITIONAL / waiting on a stronger G3 observation**.

## G5 — Ordinary checkpoint/debit coherence after membership exposure

**Module:** C5

For every realized or still-possible joined state, verify actual `X`, `Z`, debit `L_-=3X-Z`, and later renewal conditions without circularity.

Status: **OPEN after G3/G4**.

## G6 — Tail first-passage / post-checkpoint compatibility

**Module:** C5

Close the exact tail language and physical first-passage obligations for every pre-bridge survivor.

Status: **OPEN**.

## G7 — C4F / renewal / global formation compatibility

**Module:** C5

Provide an explicit invariant/state theorem if these predicates are needed. Do not assume a local ballot/projective quotient preserves them.

Status: **OPEN**.

## G8 — Route-A completion

**Module:** C6

Complete the independent Route-A obligation.

Status: **OPEN**.

## G9 — All-surplus `s>=2`

**Module:** C6

Generalize or separately close surplus sectors not covered by current `s=1` work.

Status: **OPEN**.

## G10 — Global branch completeness

**Module:** C0/C6

Prove all counterexample classes are covered and that closure of all modules implies ordinary Collatz.

Status: **OPEN**.

---

# Priority order

Current priority:

`G3 -> G4/G5/G6/G7`, with `G1` activated as secondary pruning when useful, then `G8/G9 -> G10`.

Do not reactivate G2 unless a genuinely different predicate, stronger than target-dominance existence, is introduced.