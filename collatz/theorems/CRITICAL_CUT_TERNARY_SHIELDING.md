# Critical-cut ternary shielding theorem

Status: **EXACT / CLOSED**

This is a direct consequence of correction composition and the existing exact critical-cut product theorem.

## Block identity

Let target and candidate words split at the same position as

\[
T=A B,
\qquad
W=A'B',
\]

with equal lengths within corresponding blocks and equal one-counts within corresponding blocks.

Let

\[
q_B=\#1(B)=\#1(B').
\]

Write the correction difference

\[
\Delta_{AB}=C(T)-C(W),
\]

and corresponding local block differences

\[
\Delta_A=C(A)-C(A'),
\qquad
\Delta_B=C(B)-C(B').
\]

Correction concatenation gives

\[
\boxed{
\Delta_{AB}
=
3^{q_B}\Delta_A
+
2^{|A|}\Delta_B.
}
\]

The same identity is the block form of the integer-defect recurrence

\[
N_{out}=3^{q_B}N_{in}+A_B.
\]

## Ternary shielding

Fix terminal ternary precision `L`.

If

\[
q_B\ge L,
\]

then

\[
3^{q_B}\Delta_A\equiv0\pmod{3^L}.
\]

Therefore

\[
\boxed{
\Delta_{AB}
\equiv
2^{|A|}\Delta_B
\pmod{3^L}.
}
\]

Since `2` is a unit modulo `3^L`, multiplication by `2^|A|` is bijective. A prescribed full-word residue

\[
\Delta_{AB}\equiv\rho\pmod{3^L}
\]

is therefore equivalent to the unique right-block condition

\[
\boxed{
\Delta_B
\equiv
2^{-|A|}\rho
\pmod{3^L}.
}
\]

Thus the left block is completely invisible to this terminal ternary predicate.

## Current exact critical cut

The existing Route-B critical cut has

\[
c=9,809,721,694,
\qquad
s=630,138,897,
\]

with

\[
q_A=6,189,245,290,
\qquad
q_B=397,573,380.
\]

The right factor is the strict-high/H-side factor used by the current critical-cut product decomposition.

Hence for every

\[
L\le397,573,380
\]

the full-word terminal ternary residue is completely shielded from the left block.

In particular this holds for the currently relevant finite resolutions

\[
L=24,
\qquad
L=28,
\qquad
L=47.
\]

The margins are

\[
q_B-24=397,573,356,
\]

\[
q_B-28=397,573,352,
\]

\[
q_B-47=397,573,333.
\]

## Consequence for the active state

The terminal ternary condition should **not** be inserted into the left/forward 14-root state before the critical cut.

Instead:

1. reduce the prescribed full-word terminal residue to its unique right-block residue by multiplication with `2^(-|A|) mod 3^L`;
2. solve/filter that residue entirely inside the right H/projective factor;
3. propagate the surviving right-factor boundary/control information to the cut;
4. join it exactly to the left forward source/interval/physical state.

This turns the current architecture into a genuine two-front product:

\[
\text{left forward source/physical Bellman}
\quad\Join\quad
\text{right backward H/projective residue filter}.
\]

## Relation to lazy ternary observation

`LAZY_TERNARY_OBSERVATION.md` proves that a forward residue coordinate is dormant while at least `L` future one-events remain.

This shielding theorem is the block version of the same information-flow fact.

Because the critical right block contains vastly more than `L` one-events, the terminal ternary predicate can be solved on the right without adding any ternary state dimension to the left factor.

## DSD audit

### EXACT / CLOSED

- correction-difference block identity;
- left-block annihilation modulo `3^L` when `q_B>=L`;
- unique conversion from full-word residue to right-block residue;
- application to the current critical cut for `L=24,28,47`.

### IMPORTANT SCOPE

This theorem localizes a predicate **already expressed as a correction/defect residue modulo `3^L`**.

It does not prove that checkpoint ordinary-value coherence, debit coherence, C4F, or tail first-passage reduce to the same residue predicate.

### REJECTED

Do not infer statistical independence between left and right factors. The decomposition is algebraic and the eventual join must use exact shared boundary/control data.

### OPEN

- construct the compressed right-H backward residue filter;
- determine the exact cut-boundary state exported by that filter;
- join it to the 14-root forward Bellman state;
- execute whole-family closure.

### NOT CLAIMED

No current root is closed by the shielding theorem alone, and no Collatz proof is claimed.
