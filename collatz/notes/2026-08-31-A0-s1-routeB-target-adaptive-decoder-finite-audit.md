# A0 s=1 Route-B target-aware adaptive decoder finite audit

## Purpose

This note validates the operational G4 decoder architecture on an exact finite threshold-prefix regression.

It is **not** a universal Route-B membership proof.

## Target

The target is the exact threshold word of length 18,

\[
TH_i=REQ(i+1)-REQ(i),\qquad 0\le i<18,
\]

with `REQ(n)=floor(n log_3 2)+1` for `n>0`.

Its exact metadata is

\[
(h,q,m,a)=(18,12,0,\varnothing).
\]

Among all `2^18` parity words, exactly 2,652 share the same `(h,q,m,a)` metadata.

## Adaptive target collision rule

For each remaining candidate `W`, define

\[
\Delta_W=C(W)-C(TH).
\]

At bridge resolution `(K,L)`, the candidate collides with the target iff

\[
K\le v_2(\Delta_W),\qquad L\le v_3(\Delta_W).
\]

The decoder evaluates one-step refinement of the dyadic and ternary axes and chooses the axis leaving fewer target-colliding candidates.

## Exact regression path

Starting at `(K,L)=(1,1)`, the greedy path is

```text
(1,1)   1498 other colliders
(1,2)    960
(1,3)    476
(1,4)    180
(1,5)     85
(1,6)     30
(1,7)     12
(1,8)      6
(1,9)      2
(1,10)     1
(1,11)     0
```

Thus this target class is isolated without increasing the dyadic axis beyond `K=1`; ternary refinement alone suffices in this finite example.

This is not assumed to generalize. It demonstrates that independent adaptive axis selection can materially outperform symmetric/global refinement.

## Independent modular check

For every resolution on the path, every one of the 2,651 non-target candidates was checked directly by

\[
C(W)\equiv C(TH)\pmod{2^K3^L}.
\]

Total direct modular comparisons:

```text
29161
```

The direct counts agree exactly with valuation screening at every step.

## Formation-Axiom audit

The decoder does not redefine the candidate when resolution changes. It only increases the precision of an already formed correction coordinate and intersects it with the already formed ballot summary.

Status: ✅.

## Axis-property audit

Dyadic and ternary resolutions remain separate observation axes. The decoder may refine either one based on actual collision information.

Status: ✅.

## DSD audit

✅ target-aware filtering algorithm implemented;

✅ adaptive axis choice implemented;

✅ independent direct-modulus regression passed;

✅ finite candidate isolation achieved;

❌ finite length 18 isolation is not a universal theorem;

❌ no claim that every long Route-B candidate will terminate under the same refinement strategy;

❌ G5 remains open.

## Gate update

G4 now has the following closed components:

- exact channel-block jump;
- exact dual-adic localization;
- finite bridge semigroup;
- valuation-based adaptive refinement;
- correction+ballot finite right-congruence;
- target-aware adaptive decoder algorithm, finite regression.

The remaining G4 task is the **recursive long-word lift**: replace finite enumeration by a hierarchy/channel representation of survivor classes and prove that each undecided class either closes, refines, or descends to a strictly smaller recursive subproblem.

That termination/closure statement is the bridge from G4 to G5.
