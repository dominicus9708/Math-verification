# A0 gap-only boundary compression: exact covariance rejection

Date: 2026-08-27

Status: **SAFE negative theorem / REJECTED proof shortcut.** This note prevents an over-compression of the newly identified physical two-boundary gap observable. It does not prove the Collatz conjecture.

## 1. Tempting but insufficient compression

The physical Hensel boundaries satisfy

\[
K_R=-Y,
\qquad
K_L=-2^{-A_0}X,
\]

and therefore

\[
\Delta:=2^{A_0}K_L-K_R=Y-X.
\]

In the post-`A0,A0,J0` reset strip, `Delta` is completely exposed by 21 ternary digits.

It is tempting to discard the absolute boundary carries and retain only

\[
\Delta\pmod{3^{21}}.
\]

That compression is too aggressive.

## 2. Two-boundary Hensel covariance

For a full odd-ordinal Hensel word of length `q`, the already-certified affine covariance is

\[
\boxed{
(K_R,K_L)
\longmapsto
(K_R+3^q t,\ K_L+t).
}
\]

The same displacement controls remain admissible and have exactly the same cost.

For the first-resonance block, `q=Q_0`.

Under this transformation the physical-gap functional becomes

\[
\begin{aligned}
\Delta(t)
&=2^{A_0}(K_L+t)-(K_R+3^{Q_0}t)\\
&=\Delta(0)+(2^{A_0}-3^{Q_0})t.
\end{aligned}
\]

Hence

\[
\boxed{
\Delta(t)-\Delta(0)
=(2^{A_0}-3^{Q_0})t.
}
\]

## 3. The shift coefficient is a 3-adic unit

Since `A0` is even,

\[
2^{A_0}\equiv1\pmod3,
\]

while

\[
3^{Q_0}\equiv0\pmod3.
\]

Therefore

\[
\boxed{
2^{A_0}-3^{Q_0}\equiv1\pmod3,
}
\]

so this coefficient is a unit in `Z_3`.

Consequently multiplication by it is a permutation modulo every finite power `3^h`.

For every target residue `r mod 3^h`, there is a unique

\[
t\pmod{3^h}
\]

such that

\[
\Delta(t)\equiv r\pmod{3^h}.
\]

## 4. Zero-cost consequence

A mechanical zero-displacement Hensel path exists for one suitable pair of abstract boundary carries.  Apply the covariance above to that zero-cost pair.

The controls and cost remain unchanged, but the finite residue of `Delta` can be moved to **any** chosen class modulo `3^h`.

Therefore any nonempty constraint that sees only

\[
\Delta\pmod{3^h}
\]

still admits a formal zero-cost boundary pair.

In particular,

\[
\boxed{
\inf_{
\operatorname{cent}_{3^{21}}(\Delta)
\in(-0.478G,0.5023G)
}
\mathcal T_{A_0}
=0
}
\]

when the absolute physical boundary anchors are discarded and the infimum is taken over the ambient Hensel boundary state space.

The displayed equality is a statement about the relaxed abstract boundary operator.  It does **not** assert the existence of a physical zero-defect Collatz trajectory.

## 5. What information is missing

The covariance-shifted pair generally no longer satisfies

\[
K_R=-Y
\]

for the same bounded ordinary endpoint `Y`, nor

\[
K_L=-2^{-A_0}X
\]

for the same bounded ordinary start `X`.

That is exactly the information lost by the gap-only projection.

Hence a positive lower bound must retain at least one **absolute physical anchor**, not merely the relative gap residue.

A useful exact choice is the endpoint anchor.  Every relevant first-resonance/reset endpoint satisfies

\[
0<Y<3^{46},
\]

so the complete ordinary endpoint is exposed by its first 46 ternary digits.  Together with the ordinary gap

\[
\Delta=Y-X,
\]

this determines

\[
X=Y-\Delta
\]

and hence both physical Hensel boundaries.

But the statement `Y<3^46` must be retained as an **ordinary representative condition**.  Merely retaining `K_R mod 3^46` is again insufficient for an unbounded Hensel horizon because covariance shifts by `3^{Q_0}t` are invisible modulo `3^46`.

## 6. Corrected boundary representation

The safe physical boundary descriptor is therefore not

\[
\Delta\pmod{3^{21}}
\]

alone.

It is

\[
\boxed{
(\text{ordinary endpoint }Y,\ \text{ordinary small gap }\Delta)
}
\]

with

\[
K_R=-Y,
\qquad
K_L=-2^{-A_0}(Y-\Delta).
\]

For finite computation the endpoint can be supplied by a digit automaton:

- its first 46 ternary digits encode the complete positive ordinary integer `Y`;
- all higher ordinary ternary digits are zero;
- the gap needs only 21 digits in the reset strip;
- the relation `X=Y-Delta` can be propagated by ordinary base-3 borrow/carry states.

This is qualitatively different from treating `K mod 3^46` as a global Hensel state quotient.

## 7. DSD circularity/compression audit

### SAFE

\[
\text{physical ordinary boundary}
\to
\text{its growing 3-adic residues at each requested depth}
\to
\text{Hensel transfer}.
\]

### REJECTED

\[
\text{physical boundary pair}
\to
\Delta\bmod3^{21}
\to
\text{discard both absolute anchors}
\to
\text{claim positive Hensel cost}.
\]

The covariance theorem proves that this projection loses exactly the degree of freedom needed to restore a zero-cost abstract path.

## 8. Revised next gate

The next boundary compression should be an **ordinary-boundary digit automaton**, not a gap-only carry quotient.

For the reset `s=1` sector it should retain:

1. endpoint `Y` as a bounded ordinary integer (`Y<3^46`);
2. signed local gap `Delta=Y-X` in its certified narrow interval;
3. exact relation `X=Y-Delta`;
4. physical Hensel boundaries `K_R=-Y` and `K_L=-2^{-A_0}X` at whatever 3-adic depth the transfer currently requests;
5. tenth-J0 interface ordering state `p in {0,1}`.

Only after this absolute anchoring is retained is it meaningful to seek a positive long-block min-plus lower bound.

Companion regression:

`collatz/src/A0_gap_only_boundary_covariance_rejection.py`
