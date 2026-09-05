# Terminal defect / projective-observation redundancy

Status: **EXACT / CLOSED state-minimization theorem**

## Scope

This theorem identifies the synchronized right-H projective observation with the
`3^L` projection of the exact target-displacement defect carried by the final
`L` ranked one-events.

Its purpose is state minimization.  It does **not** supply right-H formation
membership, source provenance, or a new independent pruning factor.

## 1. Right-indexed terminal defect

Let a target right block `H*` and a candidate right block `W` have the same
length `s` and the same one-count `q_H`, with

\[
q_H\ge L.
\]

Index the final `L` ranked one-events from the right.  Let their local bit
positions inside the right block be

\[
A_0,A_1,\ldots,A_{L-1}
\]

for the target and

\[
B_0,B_1,\ldots,B_{L-1}
\]

for the candidate, where index `0` is the event nearest the terminal boundary.

Define the exact local terminal target-displacement defect

\[
\boxed{
E_L=
\sum_{i=0}^{L-1}3^i\left(2^{A_i}-2^{B_i}\right).
}
\]

Target dominance implies `E_L>=0`, but the congruence identities below do not
require that sign assumption.

## 2. Correction difference modulo `3^L`

For a block with ordered one positions, the correction coefficient of the
`i`-th one-event counted from the right is `3^i`.  Therefore every event lying
strictly to the left of the final `L` one-events has coefficient divisible by
`3^L`.

Hence

\[
C(W)-C(H^*)
\equiv
\sum_{i=0}^{L-1}3^i\left(2^{B_i}-2^{A_i}\right)
\pmod{3^L},
\]

so

\[
\boxed{
C(W)-C(H^*)\equiv-E_L\pmod{3^L}.
}
\]

This is exactly the same terminal-locality mechanism already used by the
terminal carry-extinction theorem, now written in the physical defect
coordinate.

## 3. Right-H observation is the defect projection

Suppose the candidate right block is realized on an ordinary orbit from `Y` to
checkpoint `Z`.  Its affine equation is

\[
2^s Z=3^{q_H}Y+C(W).
\]

Because `q_H>=L`, reduction modulo `3^L` gives

\[
2^sZ\equiv C(W)\pmod{3^L}.
\]

The synchronized target-relative right-H observation is

\[
z_H\equiv2^sZ-C(H^*)\pmod{3^L}.
\]

Consequently

\[
\boxed{
z_H\equiv C(W)-C(H^*)\equiv-E_L\pmod{3^L}.}
\]

Thus `z_H` is not independent of the exact terminal physical defect.  It is
its finite `3`-adic observation.

## 4. Absolute-coordinate defect

Let the right block begin at absolute bit offset `p_R` inside the full word.
The absolute positions of the final events are `p_R+A_i` and `p_R+B_i`.
Define their full-word defect contribution

\[
F_L
=
\sum_{i=0}^{L-1}3^i
\left(2^{p_R+A_i}-2^{p_R+B_i}\right).
\]

Then

\[
\boxed{F_L=2^{p_R}E_L.}
\]

Since `2` is a unit modulo `3^L`, the right-H observation is equivalently

\[
\boxed{
z_H\equiv-2^{-p_R}F_L\pmod{3^L}.}
\]

Therefore the exact absolute terminal defect determines the projective
observation uniquely.

Conversely, `z_H` determines only the residue class

\[
F_L\pmod{3^L}
\]

after multiplication by the fixed unit `-2^{p_R}`.  It does not recover the
exact integer defect.

## 5. Current `A0, s=1, Route-B` checkpoint specialization

For the current synchronized checkpoint window,

\[
L=28,
\qquad
t_0=104{,}398{,}605{,}910,
\qquad
s=630{,}138{,}897.
\]

Hence the right-H block begins at

\[
\boxed{p_R=t_0-s=103{,}768{,}467{,}013.}
\]

Modulo

\[
3^{28}=22{,}876{,}792{,}454{,}961,
\]

one has

\[
2^{-p_R}\equiv1{,}051{,}701{,}240{,}047.
\]

Thus the current final-28 defect and synchronized right-H observation obey

\[
\boxed{
z_H
\equiv
-1{,}051{,}701{,}240{,}047\,F_{28}
\pmod{3^{28}}.}
\]

Here `F_28` is the same absolute final-28 target-displacement defect used by
`DEFECT_COORDINATE_CHECKPOINT_JOIN_EQUIVALENCE.md`.

At the late activation seam, a validated terminal suffix descriptor `(n,C_B)`
with `h=t_0-n` gives

\[
F_{28}=C_{T,tail}^{(28)}-2^hC_B.
\]

Therefore

\[
\boxed{(n,C_B)\quad\Longrightarrow\quad F_{28}\quad\Longrightarrow\quad z_H}
\]

exactly, with the target and right-H offset fixed.

## 6. Export-state consequence

When the source-preserving exporter already retains a validated exact terminal
suffix descriptor `(n,C_B)`, it should not Cartesian-product that record with an
independently generated `z_H` coordinate.

The safe flow is

```text
source activation record
    -> validated (n,C_B)
    -> exact F_28
    -> derived z_H mod 3^28
    -> query right-H formation/acceptance at that prescribed observation
    -> synchronize with the dyadic checkpoint side
    -> expose Z
    -> apply the source/checkpoint provenance join.
```

This removes one redundant observation coordinate.  It does **not** remove the
right-H formation predicate itself.

In particular, a terminal suffix can determine what right-H observation must
be queried without proving that the suffix extends through every required
right-H grammar/boundary condition.

## 7. DSD interpretation

The two coordinates have different information levels:

- **physical coordinate:** exact integer terminal defect `F_L`;
- **projective observation:** `z_H`, the fixed unit-scaled residue of `F_L`
  modulo `3^L`.

Thus the projective observation is a quotient/projection of the physical
coordinate, not an independent channel once the exact physical value is
retained.

### EXACT / CLOSED

- final-`L` correction-difference truncation modulo `3^L`;
- `z_H=-E_L mod 3^L`;
- `F_L=2^{p_R}E_L`;
- `z_H=-2^{-p_R}F_L mod 3^L`;
- current `L=28` unit and offset;
- derivation of `z_H` from a validated `(n,C_B)` terminal descriptor.

### REJECTED

- counting exact `F_28` and its derived `z_H` as independent pruning factors;
- Cartesian pairing of a source-derived exact terminal suffix with an unrelated
  right-H `z_H` marginal;
- replacing right-H formation membership by residue agreement alone;
- recovering the exact integer `F_28` from `z_H` alone.

### OPEN

- compressed source-preserving generation of the admissible `(n,C_B)` terminal
  descriptors;
- exact right-H formation acceptance for the prescribed derived observation;
- synchronization with the dyadic checkpoint side without marginal pairing;
- closure of `A0,s=1,Route-B` and the remaining global branches.

## Certificate

- `../src/A0_s1_routeB_terminal_defect_projective_observation_redundancy_certificate.py`
